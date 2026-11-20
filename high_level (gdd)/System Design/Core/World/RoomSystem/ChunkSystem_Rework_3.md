#rework #todo

-  version de création : **1.5.3a**
-  version de résolution : 

---
- ## **objectifs**

	- réécrire le loading/unloading des chunks en se basant sur les frontières de l'écran, ce qui va corriger beaucoup de bugs visuels et réduire drastiquement les frames drop

	- quand le perso change de chunk ça charge plus les nouveaux chunks.
	- règler les bugs de sortie de zone chargée.


---
- ## **TODO**

	- [ ] continuer à écrire ce rework.

	- [ ] relire comment les chunks sont spawné 

	- [ ] recuperer quels chunks sont actuellement affichés à l'écran en permanence
		- [ ] agrandir légèrement la zone de chargement comme ça on a le temps de venir et c déjà chargé
	- [ ] mettre en place des events quand un chunk apparait à l'écran ou disparait
	- [ ] link ces events aux vrais chargement d'écran