#system #designing

- [ ] [[prototype]]


---
# description

Ce système implémente le [[Scenario]] en fait un peu et permet surtout d'afficher des in-game cinematics (mouvement, action du joueur prédéfinie et sans que le joueur ne joue réellement)

---
# fonctionnement du système

Ce système doit être designé lol j'ai aucune idée de comment ça fonctionne. par contre je sais déjà qu'il contient plusieurs briques distinctes :
- [[Cinematics]]
- déplacement de joueur
- [[UI_Dialog]]
- 


on peut utiliser un "QuestSystem" un peu comme ça : https://www.youtube.com/watch?v=UyTJLDGcT64
- fonctionne full event & data driven, très modulable
- déjà implémenté sur github
- on peut plugger ça dans le [[GOAP_system]] assez simplement pour que [[Brain]] devienne un [QuestBrain] ce qui nous permet de déterminer le goal souhaité
	- exemple :
		- qwin a une quête principale avec plusieurs sous quete :
			- "wait for player"
			- "fight player"
			- "say game over if killed player"
			- "say good job if defeated"

		- ces sous quetes ont plusieurs QuestStep qui déclenchent différents goals chez qwin :
			- do your life
				- choisi une random action, manger ou dormir ou construire des drones
			- defeat player

		- on a donc aussi besoin d'un sous goal qui serait tout le temps actif genre "survivre" qui permet d'esquiver les zombies, s'arrêter de combattre pour manger un truc, boire de l'eau etc.
			- ce goal est tout le temps actif ? vraiment ? pour do your life oui ça jsuis d'accord, mais defeat player


---
# problèmes actuels

- problème de 




---
# todo

- [ ] implement cinematics system
	- [ ] make 2 start cinematic
	- [ ] make demo completed cinematic