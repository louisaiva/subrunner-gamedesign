#system #designing

---
# description

[RoomGraph] permet de faciliter le workflow de dessin des voisinages de chunks des rooms. C'est un sous système de [[LevelSystem]]

il ne **PERMET PAS** de dresser un itinéraire de navigation à travers un [Level] car c'est un sous système purement [visuel]. pour cela il faut plutot se diriger vers [[DoorSystem]]


---
# fonctionnement du système

On utilise un système de [node] / [link].

chaque room représente une [node], et des [links] apparaissent entre les rooms voisines.

[link] stocke uniquement les 2 [nodes] voisines.


on peut générer statiquement ce graph, via les collisions entre colliders de rooms, mais ça parait bancal si les collisions changent etc



---
# problèmes actuels


- problème encore plus important de [work flow] :
	- l'intégrer au [WorldBuilder]


- problème de [work flow] :
	- est-ce qu'on doit générer automatiquement le graph ?
		- > moins flexible
		- > moins de taf à ajuster à chaque modif de level
	- ou le tracer à la main ? (+1)
		- > on peut update précisément ce qu'on veut
		- > nécessite de créer un editor de node/link 
	- 
