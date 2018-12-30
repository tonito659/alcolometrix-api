# Documentation de l'api

## / 

Ne demande rien en entrée.
Retourne un message d'accueil

## /api/beverage POST

Prend un json avec :
barcode
price
postcode

Et l'insère dans la base de données

## /api/beverage GET

Ne demande rien en entrée
Retourne la liste de toutes les boissons

## /api/price/\<int:barcode\> GET

Prend un entier représentant le code barre de la boisson
retourne tous les différents prix correspondant

## /api/price/\<int:barcode\>/\<int:postcode\>  GET

Prend un entier représentant le code barre de la boisson et le code postal de l'achat
retourne tous les prix correspondants au code barre et sa localisation

