#designing

> README PLEASE
> ce systeme est en réalité un système de substitution ayant pour seul but de proposer une fin du jeu accessible dans la [[july26demo]].
> Le crafting des pates est voué à évoluer, gagner en complexité et surtout n'être qu'UN SEUL moyen parmi tant d'autres de manger des pates à terme, et donc de finir le jeu. Le moyen principal [long-term] est d'atteindre la surface et de manger des pâtes chez M'Pasta le stand de pates de [marco], l'ami de longue date de [bob]. mais bon c'est du [long-term] donc on a besoin d'un moyen facile de manger des pates lors des démo précédentes, et crafter des pâtes semble être le moyen fun le plus facile à faire rn.

---
# description

Manger des [[Pasta]] sont l'objectif principal du jeu. 
Pour arriver jusqu'à cela il y a plusieurs étapes avant de pouvoir finalement crafter les pâtes et finir le jeu.


---
# fonctionnement du système

Les différentes étapes de crafting de pates se fait via plusieurs objects [[Interactable]], ayant pour chacun son [[UI_Pool]] associée.

étape préliminaires :

- récupérer un ou plusieurs items [ingredient:pasta_dry] au [[Distributor]]
- réunir les ingrédients autres ingrédients :
	- onion
	- tomato_sauce
	- lentils
- réunir les autres items ?
	- plate
	- fork ? mdr




---
# todo

- [ ] faire des animations :
	- [x] Distributor idle, hover
	- [x] Orderer hover + open/close
	- [ ] sofa bob eating pasta

- [ ] dessiner des items :
	- [x] fork ?
	- [x] pasta_ticket pour le distrib

- [ ] coder [[Distributor]]
	- [ ] supprimer le ticket
	- [ ] quitter l'ui pool dès qu'on drop
	- [ ] ajuster le drop parameters des pates
	- [ ] ticket ui pool n'arrive pas à récup la PoolID "ticket" lors de la connection d'itempool, à vérifier
		- > ptet pour ça qu'on peut pas drag n drop


- [x] coder [[Orderer]]
	- [ ] le relier à [[Printer]]