import numpy as np
from matplotlib import pyplot as plt

#%% Entrées
    
C_hydroxyde =                    # Concentration de la solution d'hydroxyde de sodium [mol/L]
V_0 =                                 # Volume prélevé de vinaigre dilué [mL]
incertitude_V0 =                   # Incertitude estimée sur le volume prélevé de vinaigre dilué (pipette jaugée) [mL]
V_E =                                 # Volume équivalent [mL]
incertitude_VE =                     # Incertitude estimée sur le volume équivalent [mL]
V_fiole =                            # Volume de la fiole jaugée utilisée pour la dilution [mL]
incertitude_fiole =                  # Incertitude de la fiole jaugée [mL]
V_preleve =                           # Volume prélevé de vinaigre commercial [mL]
incertitude_Vpreleve =             # Incertitude sur le colume prélevé de vinaigre commercial (pipette jaugée) [mL]

#%% Calcul de la concentration en acide acétique du vinaigre dilué

c_0 =           # Concentration en acide acétique du vinaigre dilué calculée à partir des entrées [mol/L]

#%% Calcul de la concentration du vinaigre commercial

c_com =        # Concentration en acide acétique du vinaigre commercial (exploitation de la dilution) [mol/L]


#%% Méthode de Monte Carlo pour trouver les incertitudes sur les concentrations 

nombre_essais = 100000
               
tab_dilue = np.zeros(nombre_essais)         # crée un tableau pour stocker les valeurs tirées au hasard de la concentration en acide acétique du vinaigre dilué 
tab_com = np.zeros(nombre_essais)           # # crée un tableau pour stocker les valeurs tirées au hasard de la concentration en acide acétique du vinaigre commercial

for i in range(nombre_essais):                                          # Réitère nombre_essais fois le processus décrit dans la boucle        
    V0_alea =  np.random.normal(V_0,incertitude_V0)                     # Tire au hasard une valeur aléatoire du volume de vinaigre dilué prélevé (loi normale)
    VE_alea =  np.random.normal(V_E,incertitude_VE)                     # Tire au hasard une valeur aléatoire du volume équivalent (loi normale)
    c0_alea =                            # Tire au hasard une valeur de la concentration en acide acétique du vinaigre dilué  
    tab_dilue[i] = c0_alea                                              # Ajoute la valeur aléatoire de la concentration en acide acétique du vinaigre dilué au tableau tab_dilue 
    Vfiole_alea = np.random.normal(V_fiole,incertitude_fiole)           # Tire au hasard une valeur aléatoire du volume de la fiole jaugée
    Vpreleve_alea =  np.random.normal(V_preleve,incertitude_Vpreleve)   # Tire au hasard une valeur aléatoire du volume prélevé de vinaigre commercial lors de la dilution
    ccom_alea =                   # Tire au hasard une valeur de la concentration en acide acétique du vinaigre commercial
    tab_com[i] = ccom_alea                                              # Ajoute la valeur aléatoire de la concentration en acide acétique du vinaigre commercial au tableau tab_dilue 

Moyc0 = np.sum(tab_dilue) / nombre_essais   # Calcule la moyenne des valeurs de la concentration en acide acétique du vinaigre dilué  
Moyccom =  np.sum(tab_com) / nombre_essais  # Calcule la moyenne des valeurs de la concentration en acide acétique du vinaigre commercial 

incertitude_c0 = np.std(tab_dilue)              # Calcule l'écart-type pour la valeur de la concentration en acide acétique du vinaigre dilué calculée à partir des entrées
incertitude_élargie_c0 = 2 * incertitude_c0     # Calcule l'incertitude pour un intervalle de confiance à 95 %

incertitude_ccom = np.std(tab_com)                  # Calcule l'écart-type pour la valeur de la concentration en acide acétique du vinaigre commercial à partir de la dilution
incertitude_élargie_ccom = 2 * incertitude_ccom     # Calcule l'incertitude pour un intervalle de confiance à 95 %


#%% Affichage

print('Concentration en acide acétique du vinaigre dilué à partir des mesures (Entrées):', c_0, 'mol/L')
print('Moyenne des valeurs simulées de la concentration en acide acétique du vinaigre dilué:', Moyc0, 'mol/L')
print('Incertitude élargie sur la valeur de la concentration en acide acétique du vinaigre dilué:',incertitude_élargie_c0, 'mol/L')

print('Concentration en acide acétique du vinaigre commercial à partir des mesures (Dilutions):', c_com, 'mol/L')
print('Moyenne des valeurs simulées de la concentration en acide acétique du vinaigre commercial:', Moyccom, 'mol/L')
print('Incertitude élargie sur la valeur de la concentration en acide acétique du vinaigre commercial:',incertitude_élargie_ccom, 'mol/L')

fig = plt.figure(figsize = (10, 10))                                                        # Crée une zone graphique
plt.gcf().subplots_adjust(left = 0.1, bottom = 0.1,
                       right = 0.9, top = 0.9, wspace = 0, hspace = 0.2)                    # Ajuste les valeurs des marges de la figure
ax1 = fig.add_subplot(2,1,1)                                                                # Crée le premier graphe de la figure
ax1.hist(tab_dilue, range = (, ), bins = 50, color = 'orange', edgecolor = 'black')        # Affiche l'histogramme de répartion des valeurs simulées de la concentration en acide acétique du vinaigre dilué
ax1.set_xlabel('Concentration en acide acétique du vinaigre dilué (mol/L) ')
ax1.set_ylabel('effectif')
ax1.set_title('Pour {} itérations'.format(nombre_essais))

ax2 = fig.add_subplot(2,1,2)                                                                # Crée le deuxième graphe de la figure
ax2.hist(tab_com, range = (, ), bins = 50, color = 'blue', edgecolor = 'black')       # Affiche l'histogramme de répartion des valeurs simulées de la concentration en acide acétique du vinaigre commercial
ax2.set_xlabel("Concentration en acide acétique du vinaigre commercial (mol/L)")
ax2.set_ylabel('effectif')
ax2.set_title('Pour {} itérations'.format(nombre_essais))

plt.show()    

