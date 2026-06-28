#subsystem #designing

---
# description

**SousSystem** est une [engine] de : [[EcoSystem]]

Cette engine a pour but de tendre vers l'équilibre entre les espèces souhaité par le dev. Gère les spawners, les entités, et en gros l'équilibre entre les factions

Permet notamment d'ajuster la [difficulté] du jeu !!

---
# fonctionnement du sous système

l'[Engine] connait à chaque instant tous les [Spawner].
à chaque [Spawner] est affecté UNE SEULE classe [Species].
Cette classe représente une espèce entière lol, et chaque entité de cette espèce est appelée par la suite [individu] :


## 1. Species & Individus

On a une seule engine mais plusieurs sous classes [Species].
Cette sous classe contient une species data qui servent à réguler les comportements du monde :

- nom de l'espèce (ex : cat)
- nom du template (ex : cat)
- int population
	- > nombre max d'individus simultané dans le monde (ex : 20)
- [runtime] nombre actuel d'invidius alive
- [runtime] nombre actuel d'individus morts
	- > différence entre le nombre actuel d'individus alive versus le nombre total

Ensuite à chaque tour de boucle on regarde si on a des individus morts, et si oui on peut en affecter à des spawners qui correspondent à cette espèce. Si tous les spawners sont plein bah on peut pas en affecter, et les individus restent morts.

[Species] contient aussi plusieurs paramètres spécifiques de comportement :

- [bool] **wait_for_corspe_despawn** :
	- > si false, dès qu'un individu meurt, on incrémente le nombre actuel d'individus morts (ex : les npc, qwin, etc)
	- > si true, on incrémente le nombre de morts SEULEMENT lorsque le corpse est despawné (ex : zombo).
		- Permet un meilleur contrôle par le joueur. si c'etait false ça veut dire qu'on vient de détruire 50 zombies, et dès qu'on en tue un y'en a un nouveau qui apparait => pas très satisfaisant




## - calcul de difficulté du Level

le score de difficulté **actuel** de chaque [[Level]] est calculé en comptant les mobs vivants présents dans le niveau MAIS AUSSI on comptant les mobs pas encore spawnés des spawners de la pièce.

- c'est super pratique :
	- si on veut un mode de jeu calculé pile poil, on met les spawners en mode **trigger** comme ça ça attend que le joueur soit là pour spawn pile poil le bon nombre d'ennemis
	- si on veut un jeu plus aléatoire et surprenant, on met les spawners en mode **direct** comme ça ça les spawn directement, ce qui peut provoquer de l'émergence


## .


---
# problèmes actuels

- problème de 




---
# todo
- [ ] 


