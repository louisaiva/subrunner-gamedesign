#system #designing



---
# description

**CapacitySystem** est le système de base qui gère les capacités, notamment leur chargement/déchargement et pooling dans [CapacityBank]




---
# fonctionnement du système









---
# problèmes actuels

- [x] problème de [queue] :
	- est-ce qu'on veut vraiment utiliser une **loading_queue** / unloading queue ?
	- le problème c'est que du coup les capacités sont chargées de manière asynchrone, et on doit attendre dans le chargement du [[Capable]] pour récupérer les [[Capacity]] une fois celles-ci chargées.
		- -> du coup c relou parce que ça fait que **Capable.LoadData()** doit être async, ce qui veut dire qu'au dessus aussi tout doit être async bref relou as fuck
	- si on utilise pas de loading queue, ça charge directement toutes les capacités du Capable qu'on veut charger. c pas mal en vrai mais à voir si c'est pas trop lourd du coup ?
		- ==-> on teste ça, si on a des rpoblèmes de perf on peut aussi décaler le chargement des sous systèmes de capacités genre **MovableEngine** / **BrainEngine** tout ça on décale le gros du travail dans une loading queue plus bas.==
		- -> parce que ce qu'on veut c'est surtout mettre le bon parent à la capacité et l'enregistrer dans les capacities du capables, c tout en vrai y'a pas forcément besoin d'avoir le gros du taf ici




---
# reworks
- [[CapacitySystem_Proto]]