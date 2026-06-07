#subsystem #designing

---
# description

**SousSystem** est un [subsystem] de : [[WorldBuilder]] - [LevelTranslator]


[AutoNeighbourer] permet de faciliter le workflow de dessin des voisinages de chunks des rooms.

il ne **PERMET PAS** de dresser un itinéraire de navigation à travers un [Level] car le graph dessiné sert uniquement au [[ChunkSystem]] pour savoir quels chunks doit-on loader.
Pour le graph de navigation il faut plutot se diriger vers [[DoorSystem]]




---
# fonctionnement du sous système


S'applique une fois tous les chunks déterminés. fait une grosse passe sur tous les chunks et regarde s'ils sont voisins comme ça :
- si leurs bounds n'overlappent pas du tout, ça dégage
- si oui, alors on regarde la plus petite distance entre les deux [chunks colliders], si inférieur à un epsilon petit (0.05) bah c super c des voisins bravo les voisins !



---
# problèmes actuels

- problème de [flemme] : pas encore implémenté lol, pour le moment c'est fait à la schalgue en 2 phases :
	- d'abord bien comme on veut dans l'[AutoChunker] (ce qu'on doit etendre à tout les chunks en fait)
	- puis ensuite on ajoute les chunks avec des doors qui se connectent entre eux -> problème si une door est à la frontière de 3 chunks (voire 4 c possible), bah c niqué




---
# todo

- [ ] tout regrouper dans [AutoNeighbourer] avec une seule passe clean
- [ ] suprrimer DEFINITIVEMENT l'ancien obsolete [RoomGraph] system qui est vieux oh mon dieu j'ai 2 semaines (c très vieux pour un système à moi ok dac ???)