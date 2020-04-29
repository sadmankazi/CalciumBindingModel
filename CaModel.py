import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
import pandas as pd

os.chdir(sys.path[0])

K1 = 10**-2.88 # From DOI: 10.1016/j.ejpb.2013.12.017
K2 = 10**-4.36
K3 = 10**-5.69

Ca3 = 1880 
Ca2 = 67

Kalg = 10**-3.5

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
plt.ylabel('Species Distribution (%)')
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
fig.savefig('Figures/plot.svg')


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
plt.show()
