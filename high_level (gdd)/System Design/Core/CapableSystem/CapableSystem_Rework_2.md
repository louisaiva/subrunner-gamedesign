#rework #todo

-  version de création : **1.5.0**

---
- # !!! continuer le design avant de faire le dev
	- plusieurs problèmes :
		- devoir séparer la data en deux branches peut être périlleux
		- parce qu'on doit couper beaucoup (preque toutes) les [Data] existantes, de capables, de capacities, et même de sous système de type 

	- autre solution de design : on garde une seule et même classe [Data] mais avec des attributes type [InstanceSpecific] / [KindSpecific] et les instance field sont les seuls à être chargés / sauvegardés pcq sinon on regarde le field du template ?


---
- ## **objectifs**


	- avoir une séparation nette des [templates] data et des [instance] data
	- la sauvegarde dynamique ne concerne que les [instance] data
	- spawn un capable ne duplique pas le [template] data, seulement l'[instance] data ?
	- avoir une save file la plus petite possible



---
# details du rework

- après réflexion, on ne fait **PAS** de séparation de **CLASS** entre des potentielles fictives [CapableTemplateData] & [CapableInstanceData] parce que :
	- 




---
- ## **TODO**


- [x] séparer [CapableData] en 2 sous data :
	- [x] [CapableTemplateData]
		- > cette data est sauvegardée dans les templates Assets/Resources/data/templates/capables
		- 
	- [x] [CapableInstanceData]
		- > on sauvegarde que cette data dans le json du world/capables
		- > dynamique upgrade
	- finalement on fait pas ça, trop de code à rewrite



- [ ] finir le design : séparer la [Data] actuelle en 2
	- [ ] une [TemplateData], qui est une sorte de template en gros, on en a une seule par type d'entité (une pour toutes les apple)
		- anim data
			- ~~> problème certains champs (List[CapacityAnimPrio] doit exister pour chaque instance)~~ (-1)
				- ~~> séparer l'[AnimData] en 2 sous anim data : [AnimTemplateData] & [AnimInstanceData] mdrrrr quel enfer~~
				- > mdr c faux en fait genre oui chaque instance doit avoir une instance de list[cap] différente pour fonctionner mais en soit la data des [cap] est la même pour chaque kind
					- déjà +4
					- et oui genre un coffre a toujours "idle", "hover", "open" "close" peu importe le coffre ça n'a pas de sens
		- feet data
		- body data
		- ~~kind~~ <--- pareil le kind doit faire partie de la save du capable sinon comment on le retrouve ?
		- layer tag
		- ~~capacities ids ?~~ <--- mdrrr t fou les ids de capacities sont littéralement différentes pour chaque instance
	- [ ] une [InstanceData], qui contient par exemple la position, les pv, toutes les données qui peuvent varier d'une entité à l'autre. agit comme un [override] de la type data
		- position
		- orientation
		- inventory
		- effects
		- kind
		- capacities_ids
	
	- [ ] comment on gère l'[override] de la data instance sur la data template ?