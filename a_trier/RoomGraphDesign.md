#system #designing

---
# description

[RoomGraph] permet de répondre à plusieurs problématiques :
- pouvoir décider des voisins de chaque room rapidement
- permettre aux unloaded [Capable] de naviguer facilement à travers un [Level]




---
# fonctionnement du système

On utilise un système de [node] / [link].

chaque room représente une [node], et des [links] apparaissent entre les rooms voisines.


[link] doit stocker plusieurs trucs :
- données de frontière (edge collider)
- les 2 rooms qui sont voisines
- est-ce qu'on a des doors ou pas
	- > ça ça sert à savoir quel mob peut passer la frontière !! (quand on est pas dans la zone chargée i mean)


on peut générer statiquement ce graph, via les collisions entre colliders de rooms, mais ça parait bancal si les collisions changent etc



---
# problèmes actuels


- problème de [work flow] :
	- est-ce qu'on doit générer automatiquement le graph ?
		- > moins flexible
		- > moins de taf à ajuster à chaque modif de level
	- ou le tracer à la main ? (+1)
		- > on peut update précisément ce qu'on veut
		- > nécessite de créer un editor de node/link 
