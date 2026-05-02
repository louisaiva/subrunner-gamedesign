#rework #todo

-  version de création : **1.5.0r**
-  version de résolution : 

---
- ## **objectifs**
	- améliorer le [Translator] pour réduire le + possible les retouches obligatoires après translation
	- auto save du monde construit
	- sauvegarde de plusieurs schematics de world !
	- ouverture d'une schematic spécifique

![[image-3.png]]


---
- ## **TODO**

	- [ ] sauvegarder un [LevelSchematic] par level par world
		- [x] inclure dans la LevelData ?
		- [x] -> non plutot c mieux de l'enregistrer en mode .schematic
		

	- [ ] modifier le [[UI_WorldBuilderPool]] pour avoir :
		- [x] un ui world builder pool où on voit toutes les infos du world, on peut changer l'image le nom etc, et surtout on peut sélectionner le level à éditer
		- [x] l'ancien ui wolrd builder pool devient ui level builder pool pour éditer un seul level à la fois
		- [x] déplacer le bouton "build" level dans le world builder plutôt que dans le level builder.
		- [ ] une fois build le bouton build se transforme en bouton eye pour tester le level si souhaité.
		- [x] faire un bouton save à côté pour sauvegarder le level. 

		- [ ] stack le world builder pool sur pause menu
		- [ ] ouvrir un popup pour unload le world

	- [ ] améliorer le [LevelBuilder] :
		- [ ] faire que les [RoomVisu] grabbent automatiquement les différentes cell lors de leur création (lights & doors)
		- [ ] 

	- [ ] améliorer le [Translator] :
		- [ ] target le level spécifique
		- [ ] supprimer les doors/lights OU MIEUX ne pas les recréer