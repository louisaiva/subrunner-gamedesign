#system #designing

- [ ] [[WorldBuilder_Rework_1]]


---
# description

Le [WorldBuilder] sert à faciliter la création de [Room], de leurs tilemaps et des [Door] qui les relient. Il permet aussi de placer des **Lights**, sans cependant choisir la couleur etc pour le moment

Il est accessible via les options de dev, ce qui active/désactive tout le world builder


---
# fonctionnement du système

Le système est séparé en une unité centrale, [WorldBuilder] et plusieurs sous systèmes. Ces sous systèmes intéragissent entre eux pour amener au fonctionnement macro du système.


## **1. WorldBuilder**

Le [WorldBuilder] est le script principal qui fait tourner la machine.
C'est un [Singleton] qui sert de point d'entrée aux systèmes extérieurs, et il sert d'orchestrateur des sous systèmes.

Il possède plusieurs methodes public appelées par le [WorldBuilderCaller], qui sert à faire le lien avec les différents boutons [EventFeedback] de l'UI

Il stocke aussi des données :
- tous les [Visualizers]
- garde des liens vers les [Builders]
- garde un lien vers le [Translator]
Et des methodes importantes dont les sous systèmes nécessitent l'accès.

Il gère un système de [tools] qui permet de placer les différentes nodes sur le graph. Il gère aussi un zoom de la caméra (wip)

Il s'occupe de récupérer les inputs de la souris pour le placement des nodes, et gère la création des [Visualizers] selon le tool séléctionné.

Enfin, le [WorldBuilder] gère aussi un sous-système intégré de sauvegarde de la derniere edition du world




## **2. Visuals**

Les différents [Visuals] sont donc créés par le WorldBuilder et sont de différents types :
- [WorldCellVisualizer]
	- ce type de visual représente une cellule (ou deux pour les doors) placé sur la grid du WorldBuilder. Il a une cellule associée, ce qui permet de savoir où est positionné la Cell

	- [WorldNodeVisualizer]
		- ces [Node] représentent les angles des rooms à dessiner. ils sont reliés par des [Link] et définissent les contours des rooms
		- tool de base
	- [WorldDoorVisualizer]
		- comme son nom l'indique, s'occupe du placement des [Door]. 2 tools différents pour placer une verticale ou horizontale.
	- [WorldLightVisualizer]
		- de même pour placer des [Light]

- [WorldLinkVisualizer] 
	- ces links servent à dessiner des liens entre deux [WorldNodeVisualizer]
	- lorsqu'ils forment une boucle, [WorldBuilder] lance la création d'une [WorldRoomVisualizer]

- [WorldRoomVisualizer]
	- représente des [Room] lol mais nan jure ?


## **3. Builders**

Les [Builders] servent à créer des tilemaps à partir des [WorldRoomVisualizer] et des différentes [Cell] placée sur la grid

Ils sont appelés par le [WorldBuilder] et fonctionnent room par room.
- peut-etre on pourrait faire qq passes sur un foncionnement level par level pour retirer du bruit (faire du mastering après le mix mdr)

Ils sont chacun responsables du build d'une tilemap :
- [CarpetBuilder] : crée le carpet, sauf sur les doors
- [GroundBuilder] : crée le ground, attention les tiles sont d'une taille différente donc on a fait une petite manip cheloue pour bypass ce problème
- [WallsBuilder] : crée les walls, gestion presque manuelle des [RuleTile] à placer, evite les doors, paramètre pour placer que les murs intérieurs (à améliorer ?)
- [CeilingBuilder] : équivalent du carpet builder limite
- [MaskBuilder] :
	- crée le ceiling mask, carpet rempli en gros
	- ?? vraiment utile ??
		- > nope plus maintenant qu'on cache les rooms via shaders pour les capables

## **4. Translator**

Les [Builders] créent les tilemaps mais c'est tout. En plus c'est créé dans un "univers" fictif du world, sans collisions etc etc.

Le rôle du [Translator] est donc de prendre ces tilemaps et de les transformer en un [Level] ~~fonctionnel~~ sauvegardable. qui ensuite pourra donc être chargé en un [Level] fonctionnel.

Il s'occupe de créer :
- le [Level]
- les [Room] (et les [Light2D] associés)
- les [Door]

ce translator possède plusieurs limites ce qui nous empêchent de créer sur le champ un level fonctionnel et testable instantanément:
- pas de gestion de voisinage des [Room], donc on est obligé d'ouvrir le [RoomGraph] editor (paouf)
- ne sauvegarde pas immédiatement
- ne peut pas charger directement le monde ?
- ne peut pas override un level existant parce que :
	- duplique les doors
	- ne garde pas les voisins
	- override les lights





## 5. AutoChunker (mid-term ?)

- l'auto chunker a 2 buts :
	- auto draw le [RoomGraphNeighbourhood] pour le chargement réaliste des chunks
	- pouvoir "chunk" des grosses [Room] en plusieurs sous parties (chunks lol)


- pour l'auto neighbourhood calculation :
	- on calcule les 2 tiles les plus proche entre chaque paire de [Chunk]
	- cela nous donne le plus petit vecteur séparant les deux chunks
		- > si inférieur à un treshold, les chunks sont voisins
		- ! si le treshold est trop large cela peut poser des soucis de perf (spike lags) pcq ça voudra dire qu'on charge bcp de chunks d'un coup

- pour l'auto chunkage des grosses rooms :
	- le faire au niveau du translator
	- 
## .


---
# problèmes actuels

- problème de [logique éparpillée] :
	- il ne place pas le voisinage de [Room] qui devrait être directement intégré au [WorldBuilder]
	- [RoomGraph] fait ce travail mais est mal utile pcq fait pour s'executer dans l'onglet "Scène"
	- pas d'appel vers [NavMeshBuilder] pour build le navmesh
		- > plutôt sur le [WorldManager] all-in-one method ???



---
# todo
	
- [x] supprimer l'Editor
- [ ] [long-term] faire un réel light modifier (color picker + intensity)

- [ ] intégrer certains worlds aux assets afin de pouvoir load des "worlds templates" qui nous permettent notamment de choisir le type de world à créer lors de la création d'un world
	- [ ] faire un ui_pool stackable de création de world, avec un input field, et le template de monde à créer :
		- [ ] creatif (empty)
		- [ ] demo
		- [ ] aventure
		- [ ] 
















