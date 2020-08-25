import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
from itertools import product
from sklearn import linear_model
from sklearn.model_selection import train_test_split

os.chdir(sys.path[0])


K1 = 10**-2.88 # From DOI: 10.1016/j.ejpb.2013.12.017
K2 = 10**-4.36
K3 = 10**-5.69

Ca3 = 1880 
Ca2 = 67

pH = np.linspace(1, 10, 500)
h = 10**-pH 

alphaCA = h**3 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)
alpha1 = h**2*K1 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)
alpha2 = h**1*K1*K2 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)
alpha3 = K1*K2*K3 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)

fig = plt.figure(figsize=(6,5))

plt.plot(pH, alphaCA*100,':', label="H$_3$Cit")
plt.plot(pH, alpha1*100,'-.', label="H$_2$Cit$^{-1}$")
plt.plot(pH, alpha2*100,'--', label="HCit$^{-2}$")
plt.plot(pH, alpha3*100,'-', label="Cit$^{-3}$")

plt.xlabel('pH')
plt.ylabel(r'Species Distribution, $\alpha$ (%)')
plt.legend(frameon=False)
plt.tight_layout()
fig.savefig('Figures/speciation.svg')
plt.show()



# Plot citric acid titration and model validation 
df = pd.read_excel('Citric Acid Titrations.xlsx')

total_ionization = (3*alpha3 + 2*alpha2 + alpha1)/3

f, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))

ax1.plot(df['HClconc'], df['citrate2'], 'ro', label = "20 mM Sodium Citrate", alpha =0.6)
ax1.plot(df['HClconc'], df['Water'],'bx', label = "Water")

ax1.set_xlabel('HCl (M)')
ax1.set_ylabel('pH')
ax1.set_ylim((1, 10.25))
ax1.legend(frameon=False)

ax2.plot(pH, total_ionization*100,'-', label = "Model")
ax2.plot(df['citrate2'], 100-100*df['Alpha2'],'ro', label = "20 mM Sodium Citrate", alpha =0.6)

ax2.set_xlabel('pH')
ax2.set_ylabel('Total Acid Groups Ionized (%)')
ax2.legend(frameon=False)

plt.tight_layout()
f.savefig('Figures/titration.svg')
plt.show()


# dependence of chelation
df = pd.read_excel('readmeplot.xlsx')

plt.figure(figsize=(6,5))

plt.loglog(df['ph7'], df['ph7free'], 'o', label = "pH 7, No Citric Acid")
plt.loglog(df['ph3'], df['ph3free'],'o', label = "pH 3.7, 30mM Citric Acid")
plt.loglog(df['ph41'], df['ph41free'],'o', label = "pH 4.1, 30mM Citric Acid")

plt.xlabel('[Ca$^{2+}$] (ppm)')
plt.ylabel('[Ca$^{2+}_{Free}$] (ppm)')
plt.legend(frameon=False)
plt.savefig('Figures/examplechelation.svg')
plt.show()


# create new data frame
pH = np.linspace(3, 10, 30)
salt = np.linspace(0, 5, 30)
calc = np.linspace(0, 0.5, 30)
CA = np.linspace(0, 0.5, 30)

frame = pd.DataFrame(list(product(pH, salt, calc, CA)), columns=['pH', 'salt', 'calc', 'CA'])

def add(pH, salt): 
    h = 10**-pH 
    alpha2 = h**1*K1*K2 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)
    alpha3 = K1*K2*K3 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)
    
    Kapp = (Ca2*alpha2 + Ca3*alpha3)*(5-salt)/5
    return Kapp

frame['Kapp'] = frame.apply(lambda row : add(row['pH'], row['salt']), axis = 1)

def free_ion(Kapp, tCa, tCit, pH, salt):
    h = 10**-pH 
    alpha2 = h**1*K1*K2 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)
    alpha3 = K1*K2*K3 / (h**3 + h**2*K1 + h*K1*K2 + K1*K2*K3)

    CaFree = tCa/(1 + Ca2*alpha2*tCit*(5-salt)/5 + Ca3*alpha3*tCit*(5-salt)/5)
    return CaFree 

frame['CaFree'] = frame.apply(lambda row : free_ion(row['Kapp'], row['calc'], row['CA'], row['pH'], row['salt']), axis = 1)

frame['Free'] = frame['CaFree']*100/frame['calc']
frame=frame.dropna()


# Learning 
X = frame.drop('Free', axis =1)
y = frame['Free']
reg = linear_model.LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)
print(np.sqrt(np.mean((y_pred-y_test)**2)))
