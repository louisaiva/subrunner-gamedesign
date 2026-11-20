
---
# description

le systeme design de **subrunner** doit être pensé pour offrir de bonnes performances in-game. pour ça on essaie de suivre un fonctionnement **ECS** adapté à notre sauce qui s'appelle ~~**BSOD**~~ ==**DOPE** pattern==

> README PLEASE
> **BSOD** peut (et doit) être renommé **DOPE** pattern (data, object pooler engine)



---
# Data Object Pooler Engine (DOPE) pattern :


- ## 1. Data
	- une [Data] est une class C# bête et basique qui contient **PAS** de méthodes, seulement des variables
	- elle est passée de main en main
	- n'a pas conscience de tout ce qui se passe en fait c juste de la data
	- peut être sauvegardée directement en .json pour faire des sauvegarde
	- 
	- Une [Data] d'un certain type peut aussi contenir une liste de [Data]
		- ex : [WorldData] contient une liste de [LevelData] > [RoomData] > [CapableData] > [CapacityData]
		- ex : mais aussi [CapableData] stocke les données de son inventaire, et donc [CapableData] contient une liste de [CapableData] aussi MDR

- ## 2. Object
	- un [Object] est un gameObject instancié qui existe dans la hiérarchie unity.
	- il contient une variable [Data] où elle va etre stockée quand loadée.
	- il contient tous les trucs lourds en performance type:
		- colliders / rigidbody
		- visuels
	- il contient deux méthodes **Load & Unload**, appelées par la [Bank] qui lui permettent de charger une [Data] ou de la décharger et passer en mode dodo
	- il contient aussi une méthode **Update**, appelée par [System] qui lui permet de se mettre à jour

- ## 3. Pooler (anciennement Bank)
	- la [Pooler] gère en gros le **Pooling** des [Object].
	- elle instancie des [Object] vides au chargement du jeu et les inclue dans sa pool.
	- lors du **load** elle choisit un [Object] puis l'initialise avec la [Data] fournie puis l'envoie au [System]
	- lors du **unload** elle recoit des [Object] non-vides du [System], elle s'occupe de les réinitialiser correctement puis les ajoute à sa pool
	- elle destroy tout ce beau monde à la fin

- ## 4. Engine (anciennement System)
	- l'[Engine] stocke toute les [Data].
	- lorsqu'un [Object] doit être loaded, il en fait la demande à la [Bank] en lui envoyant la [Data] à charger
	- lorsqu'un [Object] doit être unloaded, il stocke la [Data] (dans sa propre [Data]) et envoie l'object à la bank
	- 
	- il gère aussi en temps réel (update) les appels à tous les [Object]
	- ainsi que les opérations nécessaires à faire sur la [Data] stockée mais non instanciée




---
# problèmes actuels, details, questionnements


- [x] quand [Data] est chargée dans un [Object], que fait-on de la data ? est-ce qu'on l'enlève des listes ? j'ai peur que sinon ça soit trop lourd à envoyer niveau perf parce que copie de copie de data ?
	- ~~-> ex : on veut update un mob 'developpeur' qui marche. MovableEngine récupère toute la data des [Object] du level. sauf que notre dev a dans son inventaire plein d'objects qui eux même ont des objects qui eux meme ont des objects (laptop > module > file)~~
	- ~~-> ça veut dire que quand on copie la data du dev au MovableEngine on copie toute la data de son inventaire aussi ????~~ 
	- 
	- -> sinon on peut faire que, au lieu de stocker les sous-[Data], on stocke seulement une **DataID** ainsi on sait qui intéragit avec quoi, on garde la hiérarchie sans poser les problèmes de load etc
		- > +2
		- ~~> attention cependant faut que **DataID** soit comparée sous forme de Hash, bien plus rapide à tester/comparer que des string~~
			- > ça dépend surtout en fait de comment sont stocké les data dans l'engine (et les obj dans le pooler). Si c'est tout stocké via des Dict<> bah y'a pas de problème à avoir des id en string vu que le hash est intégré au Dict<>, y'a pas à se casser la tête plus que ça
				- > +4


- [ ] problème d'accès aux différents composants :
	- si [System] a besoin d'accéder aux [Object] et [Bank] à la [Data] on fait comment ?
	- pour le moment c'est plutôt bien séparé donc c'est bien. à voir si on a besoin d'accéder l'un à l'autre souvent et si oui faut voir si on a des problèmes de perf si [System] & [Bank] s'échangent souvent des infos
	- ça peut etre intéressant qu'[Object] stocke ses sous [Object] -> genre le [Capable] stocke ses [Capacity] dans le dur



- [ ] problème de **naming** :
	- [System] peut à la fois désigner tout le système (incluant B,S,O & D) mais aussi juste S System... est-ce que ça serait pas mieux de le renommer [Engine] ?
	- de même [Bank] peut porter à confusion pcq j'ai l'impression qu'une bank process de la data jsp pk, on pourrait la renommer [Pooler] comme ça c'est littéralement dit dans le nom ce que ça fait.
	- Une engine process la data, et le pooler process les objects. Comme ça ça fera [DEPO]
		- > oui en plus ça fait [DOPE] (ou [PEDO]...)
