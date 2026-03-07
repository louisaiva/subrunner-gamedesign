#rework #todo

-  version actuelle : **1.5.0**

---

- ## **objectifs**
	- réaliser un premier prototype du [[RoomSystem]], et l'intégrer avec le proto du [[CapableSystem]] as well
	- load/unload dynamiquement les room
	- afficher/cacher les room en fonction du [[DoorSystem]] ?
	- faire qu'un capable puisse changer de room tout seul sans même etre chargé ni que la room soit chargée

---

- ## **TODO**

	- [ ] intégrer hide/show avec le [[DoorSystem]]
		- [ ] les doors, comme n'importe quel capable, sont pop par le [[CapableSystem]] ?
		- [ ] elles retiennent par contre dans leur [DoorData] 2 **room_ids** et elles trigger un event quand elles sont toggled
		- [ ] ou alors [RoomData] stocke directement, à coté de la liste de voisins, la liste des doors et on register cet event
			- -> je crois c mieux ça, la door n'a pas à savoir quoi que ce soit des rooms
		- [ ] [RoomSystem] register cet event et quand la porte s'ouvre ou se ferme, on regarde 
			- si les rooms sont loaded
			- laquelle est la room principale
			- ensuite on applle Room.Hide / Show