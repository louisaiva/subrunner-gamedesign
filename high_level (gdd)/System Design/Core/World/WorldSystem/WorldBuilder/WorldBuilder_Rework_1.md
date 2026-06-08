#rework #todo

-  version de création : **1.5.0r**
-  version de résolution : **1.5.0v**

---
- ## **objectifs**
	- améliorer le [Translator] pour réduire le + possible les retouches obligatoires après translation
	- auto save du monde construit
	- sauvegarde de plusieurs schematics de world !
	- ouverture d'une schematic spécifique

![[image-3.png]]


---
- ## **TODO**

	- [x] sauvegarder un [LevelSchematic] par level par world
		- [x] inclure dans la LevelData ?
		- [x] -> non plutot c mieux de l'enregistrer en mode .schematic
		

	- [x] modifier le [[UI_WorldBuilderPool]] pour avoir :
		- [x] un ui world builder pool où on voit toutes les infos du world, on peut changer l'image le nom etc, et surtout on peut sélectionner le level à éditer
		- [x] l'ancien ui wolrd builder pool devient ui level builder pool pour éditer un seul level à la fois
		- [x] déplacer le bouton "build" level dans le world builder plutôt que dans le level builder.
		- [x] faire un bouton save à côté pour sauvegarder le level. 

		- [x] stack le world builder pool sur pause menu
		- [x] ouvrir un popup pour unload le world

	- [x] améliorer le [LevelBuilder] :
		- [x] faire que les [RoomVisu] grabbent automatiquement les différentes cell lors de leur création (lights & doors)
		- [x] remettre une tile de ground en dessous des doors

	- [x] améliorer le [Translator] :
		- [x] load le level spécifique en mode "all-in-one"
		- [x] applique les tilemaps aux rooms
		- [x] applique les polycolliders
		- [x] reinstancie toutes les doors ?
			- [x] > l'ideal serait de ne pas les re instancier :
				- [x] methode 3 "id-based"
		- [x] supprime les old lights qui ne sont pas dans les new light du schematics
		- [x] auto neighbour chunk
		- [x] auto générate buildnavmesh
		- [x] auto regenerate ids
		- [x] make rooms grab capables 
		- [x] level regrab all rooms

	- [x] id generation bug generate new ids for capables that should keep their ids

	- [x] anim player & layers material not getting the right one

	- [x] navmesh build can't work in build ?
		- [x] > yeah no it can't work in build but lots of things in the world builder can't work in build

	- [x] sometimes SaveEngine can't save some capables
