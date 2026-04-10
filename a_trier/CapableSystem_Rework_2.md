#rework #todo

-  version actuelle : **1.5.0**

---
- # !!! continuer le design avant de faire le dev
	- plusieurs problèmes :
		- devoir séparer la data en deux branches peut être périlleux
		- parce qu'on doit couper beaucoup (preque toutes) les [Data] existantes, de capables, de capacities, et même de sous système de type 


---
- ## **objectifs**


	- avoir une séparation nette des [templates] data et des [instance] data
	- la sauvegarde dynamique ne concerne que les [instance] data
	- spawn un capable ne duplique pas le [template] data, seulement l'[instance] data ?
	- avoir une save file la plus petite possible




---
- ## **TODO**


- [ ] séparer [CapableData] en 2 sous data :
	- [ ] [CapableTemplateData]
		- > cette data est sauvegardée dans les templates Assets/Resources/data/templates/capables
		- 
	- [ ] [CapableInstanceData]
		- > on sauvegarde que cette data dans le json du world/capables
		- > dynamique upgrade



- [ ] finir le design : séparer la [Data] actuelle en 2
	- [ ] une [TemplateData], qui est une sorte de template en gros, on en a une seule par type d'entité (une pour toutes les apple)
		- anim data
			- > problème certains champs (List[CapacityAnimPrio] doit exister pour chaque instance)
				- > séparer l'[AnimData] en 2 sous anim data : [AnimTemplateData] & [AnimInstanceData] mdrrrr quel enfer
		- feet data
		- body data
		- kind
		- layer tag
		- capacities ids ?
			- est-ce qu'une instance peut apprendre des capacities différentes du template ?
	- [ ] une [InstanceData], qui contient par exemple la position, les pv, toutes les données qui peuvent varier d'une entité à l'autre. agit comme un [override] de la type data
		- position
		- orientation
		- inventory
		- effects
		- anim instance data ?
	
	- [ ] comment on gère l'[override] de la data instance sur la data template ?