
# Documentation de l'api Alcolometrix

API basée en Flask pour le lulz

## /  

Ne demande rien en entrée.
Retourne un message d'accueil et de modération

## /api/beverage POST

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
retourne le prix moyen constaté


