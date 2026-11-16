#rework #todo

-  version de création : **1.5.2f**
-  version de résolution : 

---
- ## **objectifs**

	- réécrire une pipeline de load de capable par **Task** sur le modèle déjà existant cf [[ChunkLoader]].
	- permettre de savoir quand un [[Chunk]] est finalement complètement loadé. Permettrait aussi de savoir dcp quand le [[World]] est loadé.
	- Résoudre les problèmes edge cases de timing lors de la fin du loading de capables en boucle.



---
- ## **TODO**


	- [ ] comment on gère les task ?
		- [ ] les tasks ont besoin d'être imbriquées non ? en mode [ChunkLoadTask] a besoin de connaitre ses [CapableLoadTask] et doit attendre qu'elles soient finies pour être réellement finie ?
			- [x] ça signifie que, si on load plusieurs chunks task par task et qu'on attend **task.IsDone** pour passer à la prochaine task bah on perd tout l'interet d'avoir un loader de capable en pile
			- [ ] plusieurs états ? (+1)
				- [ ] waiting
				- [ ] running
				- [ ] waiting sub tasks -> si on est dans cet état, le chunk est déjà loadé mais les capables sont en train d'être loadés, on peut passer à la task suivantes
				- [ ] done -> ici on est sur que le chunk est loadé et tous ses capables aussi

		- [x] pareil imbrication de [CapableLoadTask] avec d'autres [CapableLoadTask] ??
			- [x] en mode on doit loader 3 chests. sauf que en fait on doit loader 7 apples et 1 laptop dans ces chests. sauf que en fait on doit loader 3 modules et 4 files dans ce laptop.

		- [ ] une [CapableLoadTask] peut possèder plusieurs [SubTask] ?
		- [ ] on réunit tous les types de tasks sous une seule classe mère [[LoadTask]] 
			- [x] ChunkLoadTask : LoadTask --> et pareil unload
			- [ ] CapableLoadTask : LoadTask --> et pareil unload
			- [ ] CapacityLoadTask : LoadTask --> et pareil unload

			- [ ] chaque load task possède :
				- [ ] un **state** & **IsDone** & **OnDone**
				- [ ] une liste de string **ids** à charger
				- [ ] une list **sub_tasks** de load tasks.
				- [ ] des methodes Constructor, Done & Clear virtual déjà implémentées
				- [ ] une méthode Run(ChunkLoader loader) abstract

				- [ ] a t on besoin d'une methode/event **Cancel()** / **OnCancel** ???
	
		
	- [ ] faire que les items sont spawnés avec leur feet activé comme le reste
		  > résout les problèmes d'items stackés invisibles les uns sur les autres