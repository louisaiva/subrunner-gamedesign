#rework #todo

-  version de création : **1.5.1f**
-  version de résolution : **1.5.1g**

> README PLEASE
> - seulement un prototype !! doit être fait le plus rapidement possible pour la [[july26demo]], on verra plus tard les trucs compliqués et chiants

---
- ## **objectifs**

	- tester un premier jet de comportement intelligent macroscopique du monde via l'[[Ecosystem]]



---
- ## **TODO**

	- [x] implémenter une premiere version de [[EcoEngine]]
		- [x] coder la sous classe serializable [Species]
		- [x] coller ça aux callbacks du [[CapableSystem]] dans l'awake
		- [x] on calcule aussi au début combien y'a d'entités "mortes" par species en fonction des data d'entités déjà existantes dans capable engine

	- [x] implémenter un premier [[NestCapacity]] qui sera sur les spawners
		- [x] peut possèder une ColliderData si mode de spawn trigger
		- [x] mettre un collider sur le controller directement qui va permettre d'activer ces triggers

	- [x] ensuite on code la loop le cycle dans [[EcoEngine]] qui permet d'affecter des nouvelles entités aux [[NestCapacity]]
		- [x] important : c'est ici qu'on DuplicateTemplate() !!!
		- [x] eco engine envoie seulement l'ID de l'entité à la burrow capacity

	- [x] intégrer des scripts de gestion de spawn manuel des [[NestCapacity]], notamment pour que le [[NPC]] s'active seulement lorsque > 50 trashs détectés
		- [x] pour ça on doit check à chaque update si y'a plus de 50 corpses, et spawn tous les npc des nest si y'en a
		- [x] [mid-term] on pourra plus tard compter combien y'a de npc déjà spawn en train de ramasser les trash, en comptant la différence entre les entités stored dans les nest et la alive_population globale de la species. comme ça ça permet d'avoir seulement 1 npc en train de nettoyer les corps, et dès qu'il revient au nest, si on a encore 50 corpses alors on en renvoit un random direct. pareil on peut mettre des paliers, si 100 corpses on fait en sorte d'en avoir toujours 2 npc qui sont spawned, les autres peuvent rester au nest s'ils veulent

	- [x] tester des nester en spawn : [Trigger] et store :[Once] pour les zombies de la 1e grosse room