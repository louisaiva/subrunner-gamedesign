#system #designing

- [ ] [[Combat_Rework_1]]


---
# description

Le système de **Combat** est l'un des éléments centraux du gameplay du jeu.
Il prend en charge l'attaque, le dodge et les mouvements du joueur afin de créer une expérience de combat immersive.

> Inclut donc le dodge.
> N'inclut **PAS** le hacking, même le hacking in-game. cf [[Hacking Gameplay]]


---
# fonctionnement du système

Ce gameplay de combat est créé grâce à plusieurs élements plus ou moins indépendants. Il émerge à partir de plusieurs systèmes différents, et donc c'est pour ça que ce n'est pas un système à proprement parler. Mais plutôt un point de convergence de plusieurs systèmes. Notamment :

- les **Capacity** de Dodge & d'Attaque (DodgeCapacity, AttackCapacity, CycleAttackCapacity, ...) qui gère les attaques (& dodge) à un bas niveau (lance les animations, vérifie les dégats etc)
- les **Actions** d'attaque des mobs, qui permettent d'éxecuter les capacity avec une maitrise plus haut niveau (permet de créer des patterns plus complexes & réalistes)
	- donc relié au [[MotorSystem]] évidemment
- relié à l'[[InputSystem]] car nécessite une précision particulière au niveau des mouvements du joueur, surtout si on met en place un dodge & attaque time-based


---
# problèmes actuels

- problème de [mouse-integration] :
	- combat au clavier souris pas fou, moins kiffant qu'au gamepad

- problème de [très répétitif] :
	- faut ajouter des nouveaux ennemis plus durs
	- ajouter des attaques en haut et bas
