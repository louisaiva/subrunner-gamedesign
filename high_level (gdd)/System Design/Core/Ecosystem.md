#system #designing



# description

l'**ecosystem** est le système qui se charge de gérer l'équilibre entre les différentes factions du jeu.
C'est un système de type **ECS** qui comporte 3 composants :
- Des Entities : typiquement des [[Spawner]]
- Des Composants : [[SpawnCapacity]]
- Un Système : singleton [[EcosystemEngine]]

ps : **ECS** peut être renommé "EDA" Engine, Data, Agents

le but de ce système est de gérer la **DIFFICULTE** du jeu, ainsi que simuler un **EQUILIBRE** de l'éco système.



# fonctionnement du système

[[EcosystemEngine]] est appelée toutes les x frames, et à chaque fois qu'il est appelé il :

- loop à travers [[Level]]
	- calcule la **difficulté** actuelle
	- si manque de difficulté par rapport à la **target difficulté**, alors calcule combien/quel type d'entité on doit spawn.
	- on retient ce nombre+type d'entité pour chaque level, c'est ce qu'on appelle le compteur.

- ensuite on loop à travers tous les [[SpawnCapacity]] :
	- on regarde quel level c et si on **doit** lui donner une entité pour rééquilibrer (via notre compteur définit avant)
		- si non, on continue
		- si oui, on regarde si on **peut** lui donner une entité, via le **store_mode**
			- si oui, on lui donne et on update le compteur
			- si non on continue
	- ensuite on regarde si on doit spawner des entités en fonction des entités actuellement stored dans le spawner



# problèmes actuels

- problème de design : [[Spawner]] inutile ?????????? on veut une SpawnData plutôt ???

- comment on gère la temporalité ? est-ce que c'est [[EcosystemEngine]] qui gère vraiment tout l'aspect temporel ? on veut pas avoir des [[SpawnCapacity]] qui spawn plus souvent que d'autres ?

- comment on gère la position de spawn ?

- des fois on veut spawn des entités via un event -> il manque des modes ?
		- *exemple* je hack un parefeu. on veut qu'un developper arrive après ? en fait y'a pas de problème mdr le hack déclenche une alarme au -1 où y'a déjà une brigade de flics qui envoient des devs et une équipe enquêter. pas besoin de spawn ici
			- *+1* mais du coup faut que le level -1 soit activé en partie alors qu'on est au -4, compliqué à faire mais certainement nécessaire.