 #system #designing

- [x] [[CapableSystem_Proto]]
- [x] [[CapableSystem_Rework_1]]
- ~~[[CapableSystem_Rework_2]]~~
- [ ] [[CapableSystem_Rework_3]]
- [ ] [[CapableSystem_Rework_4]]


---
# description

le **capable system** est le système qui se charge de gérer toutes les entités et les capabilités.

C'est un système de type [[DOPE Pattern Design]] qui comporte 4 composants :
- Pooler : [CapableBank]
- Engine : [CapableEngine]
- Object : les [[Capable]]. ce sont les gameobjects réels, instanciés et poolés par [[CapableBank]]
- Data : [[CapableData]]. gérés par l'[Engine] et associés à des [Object] pour donner l'individu final loadé
	- data possède une [CapableID] c'est ça qui définit l'individualité du capable en fait


---

# fonctionnement du système

- ## 1. [CapableEngine]

	- le but de ce script est de gérer les capable en batch afin d'améliorer certaines perfs.

	- est la porte d'entrée du système, relie le systeme aux autres systemes adjacents notamment [[CapacitySystem]] & [[ChunkSystem]]

	- stocke les capables data loadées et les capables templates. permet à n'importe qui de récupérer n'importe quel capable & capable data efficacement.

	- est relié à un [Loader] qui gère la pile de chargement/déchargement des capables ainsi qu'un système de **Task** qui permet notamment aux chunks de savoir s'ils sont loadés complètement : [[CapableSystem_Rework_4]]


- ## 2. [CapableBank]

	- stocke les capables efficacement, via différentes pool de capables, en mode object pooler.
		- une pool par **kind** de capable. comme ça dès qu'on a besoin d'un capable d'un kind particulier bah on a juste à piocher dans la bonne pool et logiquement y'a déjà des capables instanciés et prêts à être loadés

	- est appelée par l'Engine lorsqu'on spawn/load un capable pour construire le capable final. appelle Capable.LoadData(data)

- ## 3. [Capable]

	- bon c'est un peu mal codé mais dans la théorie **Capable** doit juste stocké la reference à la data.
	- en réalité **Capable** possède de nombreuses variables RuntimeOnly qui doivent potentiellement être fed depuis la data à chaque Loading/Unloading.
	- on a donc plusieurs méthodes nécessaires et utiles :

		- **GetStaticData()** : utile que dans l'editeur. permet d'extraire une [[CapableData]]	d'un [[Capable]]. C'est comme ça qu'on construit la data de base.
		- **LoadData(data)** : methode principale pour loader la data. permet de feed la data dans le Capable
		- **SaveDynamicData()** : sauvegarde les valeurs runtime de Capable dans la CapableData associée, genre met à jour la position du transform dans la data
		- **UnloadData()** : remove proprement la data après avoir appelé SaveDynamicData(). stop les coroutines

- ## 4. [CapableData]

	- la **Data** de base utile aux **Capables** pour fonctionner correctement.
	- Dérive de l'interface [[DataHolder]], donc tous les fields doivent être attribués sinon ils seront ignorés par le JsonSerializer, et donc pas sauvegardés.


les [[Capacity]] gèrent leur propre **data** ET leur propre **logique** au sein du [[CapacitySystem]] ce qui n'est **PAS** le même systeme que celui des capables.

le [CapableSystem] contient aussi différents sub systèmes :

- ## [SUB SYSTEMS]
	- [[MovableEngine]]
	- [[ColliderBank]]
	- [[AnimLayerBank]]


---
# problèmes actuels

- [ ] problème de [design] : instance/template data [[CapableSystem_Rework_3]]

- [ ] bug de [timing] edge case :
	- [ ] lorsqu'on décharge une room, si un mob quitte cette room au mauvais moment, alors il peut changer de room MAIS quand même être déchargé par le [[CapableSystem]] parce qu'on l'avait mis dans sa liste à décharger.
		- [ ] on doit vérifier que l'entité est bien toujours bien assignée à la room avant de la décharger
			- > du coup c intéressant de garder l'id de la room dans les capabledata comme ça on peut vérifier que la room est bien déchargée avant de deload l'entité
		- [ ] comme on a changé d'algo de RoomEngine, peut etre que ce bug n'existe plus. je peux imaginer qu'il arrive si le mob trigger une autre room [OnRoomEnter] juste avant de se faire unload
			- [ ] dans ce cas là c'est simple suffit de faire un flag dans [Capable]  [_unloading]_ comme on en a déjà un pour [Room] (+2)



---
# todo

- [ ] faire une [RigidBodyData] qui sauvegarde différents trucs :
	- [ ] body type (kinematic etc)
	- [ ] mass ?
	- [ ] la stocker dans la [FeetData]