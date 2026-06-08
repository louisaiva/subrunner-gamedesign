#rework #done 

-  version actuelle : **1.5.0c**

---

- ## **objectifs**
	- réaliser un premier prototype du [[ChunkSystem]], et l'intégrer avec le proto du [[CapableSystem]] as well
	- load/unload dynamiquement les room
	- afficher/cacher les room en fonction du [[DoorSystem]] ?
	- faire qu'un capable puisse changer de room tout seul sans même etre chargé ni que la room soit chargée

---

- ## **TODO**

	- [x] régler le problème de [logique] dans la methode Tick() de [[ChunkSystem]] qui fait qu'on compare qu'un movable IN et OUT par room ce qui n'a pas de sens vu que 2 movables peuvent sortir en même temps d'une room...

- [x] doit pouvoir gérer les movables loaded qui sortent des **Room** loaded
	- pcq sinon les movables qui sortent n'ont pas d'obstacles et donc peuvent circuler à l'infini, ce qui fait que quand on reload les rooms dans lesquels ils marchent sans savoir, bah ça peut les faire apparaitre dans un mur
	- [x] faire que 2 [Room] voisines aient une frontière délimitée par un [EdgeCollider2D] qui s'active lorsque l'une des deux rooms est loadé et l'autre non ET que y'a pas de door fermée entre les deux.