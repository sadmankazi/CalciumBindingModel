# Description of Citric Acid

Speciation can be calculated according to the methods shown by Professor Stephen Bialkowski, [here](http://ion.chem.usu.edu/~sbialkow/Classes/3600/alpha/alpha1.html). 

![Test Image 1](https://github.com/sadmankazi/CalciumBindingModel/blob/master/Figures/citric.png)

![Test Image 2](https://github.com/sadmankazi/CalciumBindingModel/blob/master/Figures/speciation.svg)

Degree of ionization (α) = (10<sup>-pH, Water</sup> - 10<sup>-pH, Sodium Citrate</sup>)/[Sodium Citrate]

Total Ionization = α<sup>3-</sup>  + α <sup>2-</sup> + α<sup>1-</sup>

![Test Image 3](https://github.com/sadmankazi/CalciumBindingModel/blob/master/Figures/titration.svg)

# Chelation

Since calcium is divalent, we can make the assumption that only the  3- and 2- citric acid forms are the predominant chelating agents. This can be reflected by using an apparent binding constant defined as follows: 

Cit<sup>x-</sup> + Ca<sup>2+</sup>  -->  CaCit   

The above reaction is described by an apparent equilibrium constant: 

K<sub>app</sub> = [CaCit]/[Ca<sup>2+</sup>][Cit<sup>x-</sup>]

K<sub>app</sub> can be interpreted as follows:

K<sub>app</sub> =   α<sup>3-</sup>K<sup>3-</sup>  + α<sup>2-</sup>K<sup>2-</sup>

Here, K<sup>3-</sup> and K<sup>2-</sup> are the individual equilibrium association constants for the α<sup>3-</sup>  and α <sup>2-</sup>  species, respectively.  Therefore, K<sub>app</sub> can be used to calculate the fraction of chelated species if the free Ca<sup>2+</sup> concentration in the system is known, a parameter which is measured using an ion selective electrode. 

Chelation is strongly affected by pH and the ratio of chelates to chelator. These two parameters are already accounted for in the equilibriums described above. However, those equilibriums do not take into account the absolute concentration of species or the salt concentration in the system.  To account for these features we need to form a more empirical model.

![Test Image 4](https://github.com/sadmankazi/CalciumBindingModel/blob/master/Figures/examplechelation)
