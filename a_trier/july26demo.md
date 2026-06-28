
c'est la démo de juillet 2026 !

---

systèmes à rework encore (non-exhaustif, à exhaustiver):
- [ ] [[EcoSystem_Proto]]   <------- THIS
- [ ] [[Pasta Crafting System]]


FINAL WORLD (Level Design) :
- 4 canapés : 1 QG, 1 au milieu, 1 secret room et 1 à la toute fin
- garder que des vertical door ?.?
- mettre un [[Distributor]] à pates assez en évidence qq part


objects pas encore implémentés / à rework :
- [ ] [[Orderer]] + [[Printer]]
- [ ] [[Distributor]]
- [ ] [[Burner]] (anciennement fan_cube à simplement rework)

éléments d'ui à rework encore (ne,àe) :
- [ ] Pasta Orderer ui
- [ ] Pasta Distributor ui



goap system, action, goals à implémenter :
- [ReturnToNestAction]
- [mid-term] : [MakeCapableInteract<Capable,Interactable,IGoal>]
	- faire simplement une action [BurnCorpsesAction] pour la démo, plus léger, plus rapide à implémenter et entièrement satisfaisant pour le moment
- npc : revoir le brain pour la distribution des goals :
	- dans [NPC.cs] directement
	- on veut d'abord récupérer x corpses, puis les burn au burner le plus proche, puis retourner dodo au nest
- [TrashEngine] : avoir que les corpses, on veut pas ramasser d'items autres pour le moment que les corpses (et dead_packages ??)
- npc get stuck in doors -> check wander goal + doors ?


visuals à dessiner :
- post its ?
- item recette de pates

capable templates à mettre :
- nesters :
	- [x] cat
	- [ ] rat
	- [ ] spider












## DONE :

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