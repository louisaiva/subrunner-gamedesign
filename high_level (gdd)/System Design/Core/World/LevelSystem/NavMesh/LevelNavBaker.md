#subsystem #designing

---
# description

**NavMeshBuilder** est un [subsystem] de : [[LevelSystem]]

Il a pour but de générer et stocker les [NavMeshSurfaceData] afin de les transmettre à NavMesh pour que ça marche bieng !


---
# fonctionnement du sous système

Lorsqu'on load un [Level], [LevelEngine] appelle ce sous systeme pour qu'il load le bon nav mesh

Si on a déjà un nav mesh baké, alors on applique celui-là
Sinon :
1. on load un [AIO_Level] avec que les capables
2. on bake les surfaces (et on sauvegarde les data correctement)
3. on déload le [AIO_Level] et on clear le cache, ce qui va pooler les capables, ce qui sauve du temps pour après pcq pas besoin de reinstancer certains capables

---
# problèmes actuels

- [x] problème de [cant-bake-in-build] :
	- on peut pas stocker facilement des navmesh graph dans le monde ou meme les assets depuis le build... Impossible de bake at runtime, que ce soit depuis l'editor ou en build.
	- C'est pcq on peut pas créer d'assets à retenir at runtime

	- solution potentielle : rework le sous système en bakant automatiquement à chaque premier loading de level, puis on garde en cache la navmeshdata pour la remettre la 2e fois que le level est loadé

	- [[2026_05_07]]

- [ ] problème de [réassignement navmesh data] :
	- le bake flow (load aio -> bake -> deload aio) fonctionne parfaitement, MAIS
	- on ne peut pas sauvegarder les [NavMeshSurfaceData] en dehors que dans un NavMeshSurface, dcp ça veut dire que quand on reload le même level bah ça load un nav mesh data vide
	- problème **on peut pas DUPLIQUER un NavMeshSurfaceData pour le stocker sur le téco en attendant ?**

---
# todo

- [x] tester un 1er auto baker basé sur :
	- https://youtu.be/RuoK7w1OIT0?si=x2v_791xA2_wHDv0