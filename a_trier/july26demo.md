
c'est la démo du 4 juillet 2026 !

---

## DERNIER JOUR (vendredi 3/7) :




faire le level design final :
- [x] remettre un bob à jour depuis le template
- [x] placer les tags
- [x] placer les objects
- [x] placer les spawners
- [x] mettre le bon nombre d'entités dans EcoSystem (à tester)

puis :
- [x] despawn frigo à la fin de la cinématique d'intro
- [x] reconnecter la door / qg_sofa de la cinématique d'intro
- [x] reconnecter end_sofa, outro

à corriger
- [x] clock speedrun
- [x] décocher allow_multiple_stack dans UI_Manager.TogglePool()

outro :
- [x] revoir les crédits
- [x] mettre un bouton crédits dans demo completed
- [x] afficher speedrun time


bugs remainings :
- [x] quand on cook des pates finales ça enlève pas les capables proprement de l'inventaire de quelque part
	- [x] vérifier que Despawn() fait d'abord drop les items de l'inventaire s'ils sont grabbed
- [x] [space] IF super moche quand on grab les shoes pour la 1e fois
- [x] quand on sauve dynamiquement ? ça enlève les iic des items



optionels :
- [x] mettre des box qui droppent des items (beans/lentils/apple)
- [ ] faire une LightCapacity
- [x] sound design, ajuster les bruits de pieds























## DONE :


systèmes à rework encore (non-exhaustif, à exhaustiver):
- [x] [[EcoSystem_Proto]]   <------- THIS
- [x] [[Pasta Crafting System]]







FINAL WORLD (Level Design) :
- [x] 4 canapés : 1 QG, 1 au milieu, 1 secret room et 1 à la toute fin
- [x] garder que des vertical door ?.? ou presque
- [x] mettre un [[Distributor]] à pates assez en évidence qq part


objects pas encore implémentés / à rework :
- [x] [[Burner]] (anciennement fan_cube à simplement rework)

éléments d'ui à rework encore (ne,àe) :
- [x] Pasta Orderer ui
- [x] Pasta Distributor ui



goap system, action, goals à implémenter :
- [x] [ReturnToNestAction]
- [x] [mid-term] : [MakeCapableInteract<Capable,Interactable,IGoal>]
	- [x] faire simplement une action [BurnCorpsesAction] pour la démo, plus léger, plus rapide à implémenter et entièrement satisfaisant pour le moment
- [x] npc : revoir le brain pour la distribution des goals :
	- finalement même pas besoin, juste avec les cost ça se fait bien !
	- dans [NPC.cs] directement
	- on veut d'abord récupérer x corpses, puis les burn au burner le plus proche, puis retourner dodo au nest
- [x] [TrashEngine] : avoir que les corpses, on veut pas ramasser d'items autres pour le moment que les corpses (et dead_packages ??)
- [x] npc get stuck in doors -> check wander goal + doors ?


visuals à dessiner :
- [x] post its ?
	- [x] 1 dans le QG qui show "manger des pates"
	- [x] 1 autre un peu plus loin avec un IF show inventory
- ~~item recette de pates~~

capable templates à mettre :
- nesters :
	- [x] cat
	- [x] rat
	- [x] spider


- [x] npc / dev / qwin / noby : [pickup()]

- [x] [[SaveSystem]]
- (avoid ???)
- ~~pasta restaurant~~
- [x] [[UI_Dialog]]
- [x] [[ControllerSystem]]
- [x] tv !
- [x] [[StorySystem]]
- [x] npc / dev / cat / qwin / noby : [open_door()]

- [x] big fan à dodge

- [x] npc [clean()]

- bed

- bin
- [x] transférer tous les SpriteCapacity à des skins avec animplayer 
	- [x] zombo

- [x] oven
- [x] sink
- [x] 2 fridges
- [x] refectory
- [x] little sink
- [x] trash container
- [x] trash bag
- [x] dummy
- [x] tv
- [x] box_fan
- [x] tags
- [x] table
- [x] chair