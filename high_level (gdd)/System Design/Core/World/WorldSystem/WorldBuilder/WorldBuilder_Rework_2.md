#rework #done

-  version de création : **1.5.0v**
-  version de résolution : **1.5.0z**

---
- ## **objectifs**

	- peaufiner le world builder en implémentant les sous systèmes manquants :
		- Auto Chunker
		- Auto Neighbourer

	- régler le problème du [[LevelNavBaker]] -> en fait non




---
- ## **TODO**


	- [x] créer un [CameraMover] pour le [LevelBuilder]

	- [x] implémenter un [AutoChunker]
	- [x] transférer le code de calcul des neighbours en une seule passe dans [[AutoNeighbourer]]
	
	- [x] voir si on change pas les [DoorData] id stockées en room_id plutot que chunk_id

	- [x] supprimer les fichiers de room & de capables & capacities obsolete après translation