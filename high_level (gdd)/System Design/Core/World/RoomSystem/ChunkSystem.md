#system #designing

- [x] [[ChunkSystem_Proto]]
- [x] [[ChunkSystem_Rework_1]]
- [x] [[ChunkSystem_Rework_2]]
- [ ] [[ChunkSystem_Rework_3]]

---
# description

**ChunkSystem** est le système qui gère les Chunks et donc les entités qui y sont situés actuellement
C'est un peu un système de chunk


---

# fonctionnement du système

### 1. Colliders

les [[Chunk]] ont une délimitation précise et hébergent les entités en temps réel. Ces [Chunk] storent les [[Capable]] qui sont dans cette délimitation.
- on fait comment pour définir la délimitation ? via collider2D ?
	- -> pour l'instant j'ai fait en [Polygon2D] pcq c plus simple à storer mais si on a des problèmes de perf tester avec [CompositeCollider2D] + box2D ou encore [EdgeCollider2D]

### 2. Zone chargée

Le script [[ChunkSystem]] s'occupe d'activer seulement les bons Chunk, qui sont :
- le Chunk où le perso controllé est situé
- les Chunk adjactenes à cette Chunk principale

Ces Chunks loadées forment ce qu'on appelle la "**Zone Chargée**"

Ces Chunk sont donc les seules à avoir des [Capable] dans des [GameObject] avec leurs Capacities chargées et tout
Tous les autres Chunks sont contrôlées en backend par [ChunkSystem] pour garantir une optimisation opée

Le **ChunkSystem** se charge donc de charger / décharger les différentes Chunks en fonction de la position du perso, et donc il doit aussi appeler [[CapableSystem]].**LoadCapable / UnloadCapable** afin d'afficher seulement les bons mobs dans les bonnes Chunks.

### 3. Update de la zone chargée

à chaque changement de Chunk du Perso, on doit redefinir la zone chargée

dans l'update :
- on traque la position du perso
	- on vérifie qu'on a pas changé de Chunk
	- **si on a changé de Chunk** :
		- on met à jour les Chunks voisines
		- on charge petit à petit les nouvelles et déchargent les anciennes ?
- 
- sinon on parcourt toutes les Chunks :
	- **si elle est active (Chunk principale + voisines):**
		- on update le movableengine pour les mobs de la Chunk
		- 
	- **si elle est inactive (les autres)** :
		- on cycle à travers tous les mobs contenus dans la Chunk
		- on update leur action virtuellement :
			- au lieu de faire des checks de collisions et des déplacements,
			- la Chunk contient toute la data nécessaire à la réalisation d'une action (position de machin, inventaire de machin, skin de bidule)
			- on skip donc tous les déplacements qu'on retient virtuellement au sein d'une [GoalData]?
			- puis toutes les x frames on fait une update, et si on est arrivé au lieu de l'action, alors on l'effectue, mais pareil on a pas de capacité ni de collider, en fait on demande juste à [[LevelEngine]] ? la donnée dont on a besoin, on change un item d'inventaire
			- une action pareil, prend un certain temps virtuel à s'effectuer comme ça ça donne une impression réelle et ça désengorge le cpu





### 4. [mid-term] Meilleur algorithme d'update de zone chargée

- Plutot que de se faire chier à calculer les neighbours pour pouvoir calculer quelle zone faut-il charger, créant des problèmes edges cases de capables à l'écran déloadés, il vaudrait peutetre mieux avoir un big rectangle collider de dimensions de l'écran + légèrement plus grand;
- puis stocker dans un cache quels chunks sont présents à l'écran
- et les chunks qui disparaissent de l'écran se déchargent automatiquement en continu
- comme ça pas besoin de calculer constamment les voisins de chunks, en plus ça calcule les voisins et les ajoute à charger lorsqu'on change de room donc évidemment ça fait des drops de fps
- là ça serait mieux pcq ça décharge une room par une room un peu tout le temps -> plus fluider
- ET avantage on a exactement le bon nombre de chunks optimal chargé en continu (celui qui est à l'écran)



**plusieurs problèmes cependant à cette approche** (qui sont potentiellement aussi dans l'approche actuellement implémentée) :

- seuls les chunks chargés (et résidus de chunks) ont leur chunk collider chargé, ce qui veut dire que les capables peuvent echapper au systeme
	- l'idéal serait d'avoir tous les chunks colliders chargés au chargement du level ?
	- > + on pourrait faire pareil avec les colliders des tilemaps [carpet] afin de s'assurer qu'**AUCUN** capable n'échappe **JAMAIS** au level. niark niark

- ah ben y'a qu'un seul probleme en fait

### .

---


# problèmes actuels

- [x] loading bourrin des [tilemaps] : [[ChunkSystem_Rework_3]]
	- > pas de problème en fait c'est réglé avec le [[TilemapSystem]]