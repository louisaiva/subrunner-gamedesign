#rework #todo

-  version actuelle : **1.5.0**n

---
- ## **objectifs**

	- résoudre les fps spike lors des changements de [Room] du perso




---
- ## **TODO**

	- [x] tester en enlevant simplement les [bounds resize] à chaque load (inutile sauf pour le premier chargement)
		- [x] tilemap.ResizeBounds()
		- [x] tilemap.CompressBounds()
		- [x] tilemap.ClearAllTiles()

	- [x] cacher les TileBase<> au lieu de les charger à chaque load comme un bourrin mdr

	- [x] si encore problème de fps spike on peut arrêter de pool les **Tilemaps**. ça signifie qu'on charge une fois chaque tilemap ([lazy load pattern]) et ensuite on les stocke sur un game object qui peut même être complètement séparé des [Room] comme ça pas besoin de SetParent(), et ensuite on a juste à enabled/disable les tilemaps avec le [room_id]