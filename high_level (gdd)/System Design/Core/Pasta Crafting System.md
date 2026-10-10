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

- récupérer un ou plusieurs items [food:dry_pastas] au [[Distributor]]
- réunir les ingrédients autres ingrédients :
	- onion
	- tomato_sauce
	- lentils
	- beans
- réunir les autres items ?
	- plate
	- fork ? mdr




---
# todo

- [x] faire des animations :
	- [x] Distributor idle, hover
	- [x] Orderer hover + open/close
	- [x] sofa bob eating pasta

- [x] dessiner des items :
	- [x] fork ?
	- [x] pasta_ticket pour le distrib

- [x] coder [[Distributor]]
	- [x] supprimer le ticket
	- [x] quitter l'ui pool dès qu'on drop
	- [x] ajuster le drop parameters des pates
	- [x] mettre big_item type pool
	- [x] ticket ui pool n'arrive pas à récup la PoolID "ticket" lors de la connection d'itempool, à vérifier
	- [x] drag n drop cassé
		- [x] UI_ItemMover doit pouvoir récup les UI_ItemPool depuis un UI_SlottableMixer, donc changer la pool ticket dans le mixer
		- [x] par contre ça drop pas correctement dans l'inventaire ??? ptet à cause de GrabbedFromLowerInventory
	- [x] drop cassé
		- [x] vérifier que ça marche bien avec Inventory.GetInteractingInventory() qui marche avec les Chestable


- [x] coder [[Orderer]]
	- [x] faire l'ui
	- [x] coder cook meal coroutine
		- [x] le relier à [[Printer]]