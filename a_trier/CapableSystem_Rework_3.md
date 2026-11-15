#rework #todo

-  version de création : **1.5.2f**
-  version de résolution : 

---
- ## **objectifs**

	- permettre de changer des paramètres de template d'une instance déjà spawnée. ce qui résout un énorme problème de [design/workflow] :
	
		- Actuellement, une fois qwin spawnée, toutes ses variables et les variables de ses capacités sont stockées et sauvegardées. si après son spawn on change des variables sur le template "qwin" ou sur les templates de ses capacités, cela n'aura **AUCUN** impact sur les CapableData & CapacityData déjà spawnées, ce qui veut dire que la qwin déjà spawnée ne changera pas d'un poil sa data.
		- C'est super problématique parce que c'est chiant pour prototyper, tester des trucs. on doit soit respawn toutes les entités pour être surs qu'elles soient à jour, soit travailler en sachant que pas mal de paramètres sont deprecated. c horrible


	- solution : séparer template/instance data avec 2 pipelines json et des attributs type [RuntimeOnly] / [InstanceSpecific] / [KindSpecific]

		- améliore les perfs, réduit la taille de la sauvegarde

		- Comment ça marche ? Bonne question jamy
		- les variables possédant l'attribut [KindSpecific] dans [[CapableData]] & [[CapacityData]] sont désignés comme étant des attributs communs à tous les templates. **ILS NE DOIVENT PAS ETRE INSTANCE BASED**. Ils sont constants après l'initialisation.

		- Voici un aperçu des différences avec le LOAD/SAVE flow d'avant !![[JSON LOAD & SAVE FLOW CHARTS.excalidraw]]

---
- ## **TODO**

	
	- [ ] 