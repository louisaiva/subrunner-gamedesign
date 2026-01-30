[[Ecosystem]]


# description

cette engine a pour but de tendre vers l'équilibre de difficulté souhaité par le dev.
elle calcule la difficulté actuelle de chaque niveau et génère des entités si on doit renforcer la difficulté du niveau. elle s'occupe aussi des [[SpawnCapacity]] en leur donnant des entités et en les faisant spawn au bon moment etc


# calcul de difficulté du Level

le score de difficulté **actuel** de chaque [[Level]] est calculé en comptant les mobs vivants présents dans le niveau MAIS AUSSI on comptant les mobs pas encore spawnés des spawners de la pièce.

- c'est super pratique :
	- si on veut un mode de jeu calculé pile poil, on met les spawners en mode **trigger** comme ça ça attend que le joueur soit là pour spawn pile poil le bon nombre d'ennemis
	- si on veut un jeu plus aléatoire et surprenant, on met les spawners en mode **direct** comme ça ça les spawn directement, ce qui peut provoquer de l'émergence

# variables

- une variable de delai pour combien de fois par frame on est appelé ????