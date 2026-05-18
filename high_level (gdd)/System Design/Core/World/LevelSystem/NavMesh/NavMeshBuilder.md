#subsystem #designing

---
# description

**NavMeshBuilder** est un [subsystem] de : [[LevelSystem]]

Il a pour but de générer et stocker les [NavMeshSurfaceData] afin de les transmettre à NavMesh pour que ça marche bieng !


---
# fonctionnement du sous système

Pour le moment le [Baking] des surfaces se fait manuellement

---
# problèmes actuels

- problème de [cant-bake-in-build] :
	- on peut pas stocker facilement des navmesh graph dans le monde ou meme les assets depuis le build... Impossible de bake at runtime, que ce soit depuis l'editor ou en build.
	- C'est pcq on peut pas créer d'assets à retenir at runtime

	- solution potentielle : rework le sous système en bakant automatiquement à chaque premier loading de level, puis on garde en cache la navmeshdata pour la remettre la 2e fois que le level est loadé

	- [[2026_05_07]]


---
# todo

- [ ] tester un 1er auto baker basé sur :
	- https://youtu.be/RuoK7w1OIT0?si=x2v_791xA2_wHDv0