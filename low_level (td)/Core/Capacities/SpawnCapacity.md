#capacity
sert de **Data/Component** pour [[Ecosystem]]



# description

Un spawner **STOCKE** et **SPAWN** des entités. il reçoit chaque entité via l'engine [[EcosystemEngine]] qui s'occupe de distribuer les différentes entités et choisit de la temporalité de cette distribution.

Les spawners désactivés par le [[RoomSystem]] ont leur **SpawnCapacity** désactivée. Sauf qu'on veut pouvoir spawn des entités même dans ce cas. Heuresement, chaque capacité est stockée par l'engine [[EcosystemEngine]] qui elle est tout le temps active, et qui va loop à travers toutes les capacities pour déterminer lesquelles doivent recevoir / spawn quelle entité à quel moment.

Le comportement du spawner est définie par son **mode de spawn** (spawn_mode) & son **mode de storage** (store_mode) :

# modes de spawn

- le mode de spawn définit quand et comment le spawner spawn ses entités stored.

- ### **DIRECT**
	- dès qu'une entité est reçue, elle est spawné directement
	- ne s'arrête jamais

- ### **TRIGGER**
	- lorsque le joueur est en dehors d'une zone de trigger, le spawner ne spawn rien jamais
	- lorsque le joueur est dans une zone de trigger, le spawner est comme en mode direct
		- *si le spawner a déjà des entités stored quand le joueur entre, le spawner spawn tout d'un coup*


# modes de storage

- le mode de storage définit comment les entités sont emmagasinées (lol) par le spawner. Cela ne concerne pas le spawnage de ces entités mais juste la logique de comment le spawner souhaite recevoir ses entités.

- un **RESET** est déclenché lorsque le joueur utilise l'ascenceur (change de niveau) ou sauvegarde. Ce reset affecte tous les spawners mais n'a pas d'effet sur le mode de storage **ENDLESS**

- ### **ENDLESS**
	- commence à zéro (aucune entité stored), puis reçoit en continu selon [[EcosystemEngine]]
	- si on atteint *max_entities* stored, alors on peut plus recevoir d'entités

- ### **ONCE**
	- commence à zéro (aucune entité stored), puis reçoit en continu selon [[EcosystemEngine]]
	- une fois *max_entities* reçues, alors on peut plus recevoir d'entités.
		- */!\ attention /!\
		  grosse différence avec le mode endless parce que cela signifie que seulement x entités pourront être spawn. si on tue ces x entités, alors il n'y a plus d'entités du tout dans le niveau. dans le mode endless au contraire dès qu'on tue une entité une autre est spawned donc on peut tuer à l'infini, y'aura toujours des entités qui vont spawn*
	- cette limite se reset lors d'un **RESET** lol eh g pas d'inspi la team ou qwa mdr

- ### **FULL**
	- équivalent du mode endless mais, lors de chaque reset, se remplit directement à *max_entities* stored. cela signifie que ça commence à max_entities direct aussi

- ### **FULL_ONCE**
	- équivalent du mode once mais à chaque reset se remplit directement à *max_entities* stored. en gros c'est comme isaac. t'arrives dans un level, tous les ennemis sont déjà là et spawnent puis ne respawnent jjamais (sauf si tu reviens dans le level)



# variables

- entity_prefab : *skin*
- spawn_mode : *direct / trigger* 
- store_mode : *endless / once / full / full_once*
- max_entities : *int*
- stored_entities : *being?[]*

- plusieurs spawn parameters qui permettent de définir la position du mob spawné ?

















#### --- logs ---



- peut-etre qu'on veut pouvoir spawn des entités même si les spawners sont désactivé ?
	- *+1 sinon c la merde comment qu'on fait si on a une attack breach au -3 et qu'on veut spawn des devs/cyborgs depuis le -1 ?*
	- *+1* encore plus en fait même au sein du même étage un spawner peut être room-disabled mais doit continuer à spawn des entités (même si elles vont spawn disabled)