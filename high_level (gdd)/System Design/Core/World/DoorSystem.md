#system #designing

---

# description

- **DoorSystem** est le système qui gère les différentes [[Door]].

---

# fonctionnement du système

2 potentiels fonctionnements :

- soit purement [visuel] : le systeme **Show/Hide** les bonnes [[Room]] quand une Door est toggled.
	- [avantages] plus réaliste, simule les combats dans les pièces adjacentes
	- [inconvenients] rajoute du overhead au room system, demande une gestion des particules, lumières etc

- soit purement [logique] : le système **Load/Unload** les [[Room]]
	- [avantages] moins d'overhead, reutilisation du [[RoomSystem]]
	- [inconvenients] peut-etre plus de travail sur le [[CapableSystem]] pour rendre réaliste les déplacements des movables au sein d'une room, peut-etre problème de lag aussi quand on ouvre une porte

votes :
- [visuel] : +0
- [logique] : +1

---
# problèmes actuels

- problème de [design] : faut tester quelle methode on veut choisir

---

# todo (en attendant rework)

- [ ] **proto**
	- [ ] méthode 1 purement visuelle :
		- [ ] les doors, comme n'importe quel capable, sont pop par le [[CapableSystem]] ?
			- [ ] elles retiennent par contre dans leur [DoorData] 2 **room_ids** et elles trigger un event quand elles sont toggled
			- [ ] ou alors [RoomData] stocke directement, à coté de la liste de voisins, la liste des doors et on register cet event
				- -> je crois c mieux ça, la door n'a pas à savoir quoi que ce soit des rooms
			- [ ] [RoomSystem] register cet event et quand la porte s'ouvre ou se ferme, on regarde 
				- si les rooms sont loaded
				- laquelle est la room principale
				- ensuite on applle Room.Hide / Show
		
	- [ ] méthode 2 (peutetre mieux ?)
		- [ ] pareil les doors stockent 2 rooms data et chargent/déchargent les rooms quand actionnées.
			- [ ] ça fait que c'est pas que visuel et c'est plus simple y'a pas à gérer les différents trucs chiants :
				- cacher/afficher les capables
				- cacher/afficher les dégats/particules
				- 