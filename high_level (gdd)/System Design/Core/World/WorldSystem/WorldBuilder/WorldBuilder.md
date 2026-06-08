#system #designing

- [x] [[WorldBuilder_Rework_1]]
- [x] [[WorldBuilder_Rework_2]]


---
# description

Le [WorldBuilder] sert à faciliter la création de [Room], de leurs tilemaps et des [Door] qui les relient. Il permet aussi de placer des **Lights**, sans cependant choisir la couleur etc pour le moment

Il est accessible via les options de dev, ce qui active/désactive tout le world builder


---
# fonctionnement du système

Le système est séparé en une unité centrale, [WorldBuilder] et plusieurs sous systèmes. Ces sous systèmes intéragissent entre eux pour amener au fonctionnement macro du système.

[WorldBuilder] sert principalement de point d'entrée et de liens entre :
- d'une part le [LevelBuilder] qui s'occuper des .schematic et de build les tilemaps et
- ensuite le [LevelTranslator] qui s'occupe du [AIO] level load, état des lieu des capables & rooms, puis l'auto chunk, placage des doors, level nav mesh, auto neighbouring, et
- enfin le [[SaveSystem]] qui applique la sauvegarde à ce [AIO] level


## **1. LevelBuilder

Le [LevelBuilder] est le script principal qui fait tourner la machine.
C'est un [Singleton] qui sert de point d'entrée aux systèmes extérieurs, et il sert d'orchestrateur des sous systèmes.

Il possède plusieurs methodes public appelées par le [WorldBuilderCaller], qui sert à faire le lien avec les différents boutons [EventFeedback] de l'UI

Il stocke aussi des données :
- tous les [Visualizers]
- garde des liens vers les [Builders]
- garde un lien vers le [Translator]
Et des methodes importantes dont les sous systèmes nécessitent l'accès.

Il gère un système de [tools] qui permet de placer les différentes nodes sur le graph. Il gère aussi un zoom de la caméra (wip)

Il s'occupe de récupérer les inputs de la souris pour le placement des nodes, et gère la création des [Visualizers] selon le tool séléctionné.

Enfin, le [LevelBuilder] gère aussi un sous-système intégré de sauvegarde de la derniere edition du world




### **1.1. Visuals**

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


### **1.2. Builders**

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

## **2. Translator**

Les [Builders] créent les tilemaps mais c'est tout. En plus c'est créé dans un "univers" fictif du world, sans collisions etc etc.

Le rôle du [Translator] est donc de prendre ces tilemaps et de les transformer en un [Level] ~~fonctionnel~~ sauvegardable. qui ensuite pourra donc être chargé en un [Level] fonctionnel.

Il s'occupe de créer :
- le [Level]
- les [Room] (et les [Light2D] associés)
- les [Door]

Le [Translator] ne peut pas override un level existant parce que :
	- duplique les doors / lights
	- ne garde pas les voisins
	- ne build pas le navmesh
	- ne génère pas les ids


Pour cela on doit ajouter plusieurs petits [subsystem] au Translator qui vont s'occuper de :
- calculer le graph de neighbouring
- buildnavmesh (on l'a déjà le subsystem :)))
- autochunk

### 2.1. [[AIO_Level]] loading
### 2.2. [[AutoChunker]]
- permet de séparer les grandes rooms en plus petits chunks
### **2.3.** [[LevelNavBaker]]

- peut pas générer depuis le build, sauf si on utilise genre reflexion ?

### 2.4. [[AutoNeighbourer]]



## @



---
# problèmes actuels

- [x] problème de [logique éparpillée] :
	- il ne place pas le voisinage de [Room] qui devrait être directement intégré au [WorldBuilder]
	- [RoomGraph] fait ce travail mais est mal utile pcq fait pour s'executer dans l'onglet "Scène"


- [x] problème de [translator] :
	- pour passer d'un **schematic** à un level **all-in-one** (laio ?) on doit replacer des capables, qui peuvent avoir changé de place/été supprimés/créés pour la 1e fois. pour gérer ça, plusieurs options :

		- (1e idée, bruteforce) :
		  on supprime tous les objets (doors, lights) et on les recrée à l'endroit spécifique

		- (2e idée, position-based) :
		  on compare les objets existants avec les nouveaux objets, et, en fonction de leur position, soit on les recréé soit on les supprime soit on les garde
			- > pour l'instant on teste ça (+5)
			- > ça fonctionne ok tier
	
		- (3e idée, id-based) :
		  on stocke une [id] dans les [schematics] pour les lights & doors.
		  au début elle est vide, et une fois que la translation est faite, lorsqu'on assigne les ids aux capables dans le **AIO_Level** bah on assigne l'id aussi aux visus du schematics pour que l'id soit jsoné aussi.
		  prochaine fois qu'on re translate on cherche les paires d'id matchantes et on met juste à jour les positions des objets trouvés grace a celle du visu correspondant.
		  pour les objets qui ont une id mais pas de visu, on les supprime
		  pour les visu qui ont pas d'id, on instancie un objet.
			- > un peu relou ça veut dire faut garder l'id dans les visus aussi, et donc pour retrouver le schematic a modif après id generation ça va etre le zbeul (+2)
				- ça attendra un gros rework avec placement d'objets etc


- [ ] problème de [build / AssetDatabase] :
	- ==solution globale== : soit rebuild les trucs au level loading (comme LevelNavBaker) soit faire une petite engine/bank qui sauvegarde les paths des ressources avec un id quand on est dans l'editeur, qui peut ensuite etre retrouvé et loadé sur demande dans un build vu qu'on a les paths dans les assets 
		- ==+1==
	- BEAUCOUP de choses du [WorldBuilder] ne fonctionnent pas correctement dans le build, notamment :
		- [x] get_material_path() de AnimPlayer / AnimLayer
			- > solution potentielle : sauvegarder les materials path dans un .json des [Assets] qui retient le material path par skin quand on travaille dans l'inspector et ensuite s'en sert comme fallback dans le build
		- [x] load tilebases

		- [ ] nav mesh builder
			- [x] ça pas trop de solution, à part modifier moi même le code du navmesh :///
			- > finalement on a réussi on rebake simplement le navmesh dans [LevelNavBaker] au load du level
			- > MAISSS encore problème zut pcq on override les [NavMeshData]


---
# todo
	
- [x] supprimer l'Editor
- [ ] [mid-term] faire un réel light modifier (color picker + intensity)
- [ ] [mid-term] régler les 2 issues de l'[[AutoChunker]]
- [x] [mid-term] quand on charge le AIO_Level et qu'on regénère les ids et qu'on regrab ça risque de supprimer toutes les refs des movables ? sauf si on les load aussi quand le translator demande la construction du AIO_Level

- [ ] [mid-term] on peut enlever les doors du [LevelBuilder] et à la place mettre une option pour effacer les murs à certains endroits.
	- [ ] ensuite comme ça les doors pourront être placées directement depuis le [[WorldPlacer]] comme les autres capables
		- > nécessite un grab dynamique des rooms ??? ca a l'air compliqué avec le door systeme

- [ ] [mid-term] modifier le [[UI_WorldBuilderPool]] pour avoir :
	- [ ] une fois build le bouton build se transforme en bouton eye pour tester le level si souhaité.

- [ ] intégrer certains worlds aux assets afin de pouvoir load des "worlds templates" qui nous permettent notamment de choisir le type de world à créer lors de la création d'un world
	- [ ] faire un ui_pool stackable de création de world, avec un input field, et le template de monde à créer :
		- [ ] creatif (empty)
		- [ ] demo
		- [ ] aventure
		- [ ] 









