This read-me is a work in progress...

The goal was to study whether it was possible to encode (and maybe compress the amount of memory needed to store a shape) shapes with fourier's mathematical theory.



Ces codes visent a mettre en place l'encodage d'une image (stockée dans data.json pour la clé de sol, stockée dans data2.txt pour les lettre "TIPE" )

avec des coefficients de fourier (on stocke seulement les coeff pour encoder l'image)


inspirée par cette vidéo de 3blue1brown https://www.youtube.com/watch?v=r6sGWTCMz2k&vl=en



on a donc une fonction python qui intègre avec la méthode des trapezes les "fonctions mathématiques" qui correspondent aux dessins



modifier la ligne 62 nb_coeffs = 500 avec une valeur entre 20 et 500 pour plus ou moins de précision, pour avoir des résultats divers
#executer avec pygame et numpy d'installés mathsvifnale.py
