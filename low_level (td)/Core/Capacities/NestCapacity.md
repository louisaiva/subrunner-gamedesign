#capacity
sert de **Data/Component** pour [[EcoSystem]]


---
# description

[NestCapacity] est la capacity qui sert à stocker et spawn des mobs à travers le monde. Est principalement liée à l'[[EcoEngine]].

Possède une [NestData] qui tourne même quand la capacity est unloadée
Est pluggé sur des [[Spawner]] principalement qui possèdent aussi une [SpawnCapacity]. NestCapacity gère les calls à cette SpawnCapacity lorsque des entités doivent être spawnées.

---
# fonctionnement


Un spawner **STOCKE** et **SPAWN** des entités. il reçoit chaque entité via l'engine [[EcoEngine]] qui s'occupe de distribuer les différentes entités et choisit de la temporalité de cette distribution.

Les spawners désactivés par le [[ChunkSystem]] ont leur **Capacity** désactivée. Sauf qu'on veut pouvoir spawn des entités même dans ce cas. Heuresement [[EcoEngine]] stocke les [NestData], soit direct soit leur IDs.

EcoEngine peut donc 

Le comportement du spawner est définie par son **mode de spawn** (spawn_mode) & son **mode de storage** (store_mode) :

## 1. modes de spawn

- le mode de spawn définit quand et comment le spawner spawn ses entités stored.

- ### **DIRECT**
	- dès qu'une entité est reçue, elle est spawné directement
	- ne s'arrête jamais

- ### **TRIGGER**
	- lorsque le joueur est en dehors d'une zone de trigger, le spawner ne spawn rien jamais
	- lorsque le joueur est dans une zone de trigger, le spawner est comme en mode direct
		- *si le spawner a déjà des entités stored quand le joueur entre, le spawner spawn tout d'un coup*
			- > facon de parler, chaque entité est spawn une par une par spawner (parce qu'on peut avoir qu'une seule animation en mm temps correc)


## 2. modes de storage

- le mode de storage définit comment les entités sont emmagasinées (lol) par le spawner. Cela ne concerne pas le spawnage de ces entités mais juste la logique de comment le spawner souhaite recevoir ses entités.

- un **RESET** est déclenché lorsque le joueur utilise l'ascenceur (change de niveau) ou sauvegarde. Ce reset affecte tous les spawners mais n'a pas d'effet sur le mode de storage **ENDLESS**

- ### **ENDLESS**
	- commence à zéro (aucune entité stored), puis reçoit en continu selon [[EcoEngine]]
	- si on atteint *max_entities* ==stored==, alors on peut plus recevoir d'entités
	- une fois qu'une entité est spawned, alors on est plus à *max_entities* donc on peut re-recevoir une entité

- ### **ONCE**
	- commence à zéro (aucune entité stored), puis reçoit en continu selon [[EcoEngine]]
	- une fois *max_entities* ==reçues==, alors on peut plus recevoir d'entités.
		- */!\ attention /!\
		  grosse différence avec le mode endless parce que cela signifie que seulement x entités pourront être spawn. si on tue ces x entités, alors il n'y a plus d'entités du tout dans le niveau. dans le mode endless au contraire dès qu'on tue une entité une autre est spawned donc on peut tuer à l'infini, y'aura toujours des entités qui vont spawn*
			- > cpour ça j'ai highlight pcq recues & stored sont pas les mêmes mots !!!!

	- cette limite se reset lors d'un **RESET** lol eh g pas d'inspi la team ou qwa mdr

- ### **FULL**
	- équivalent du mode endless mais, lors de chaque reset, se remplit directement à *max_entities* stored. cela signifie que ça commence à max_entities direct aussi

- ### **FULL_ONCE**
	- équivalent du mode once mais à chaque reset se remplit directement à *max_entities* stored. en gros c'est comme isaac. t'arrives dans un level, tous les ennemis sont déjà là et spawnent puis ne respawnent jjamais (sauf si tu reviens dans le level)



## 3. variables

- entity_prefab : *skin*
- spawn_mode : *direct / trigger* 
- store_mode : *endless / once / full / full_once*
- max_entities : *int*
- stored_entities_ids : *string[]*



