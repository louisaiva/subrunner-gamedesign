#planning 

-  version de création : **1.5.2d**
-  version de résolution : 

---
#### objectifs actuels :
- **trouver du taf**
- finaliser et peaufiner l'architecture de systèmes **Core** en réglant les différents problèmes, optimisations possibles présentes dans les dernières démos, et **revoir le système global d'animation 2D**
- diversifier le [[gameplay d'attaque & esquive]]
- ajouter du [[Hacking]]
- avoir une première démo postable sur **Steam**

---


## CORE systems finalisation :

- objectif : optimiser les systemes existants, corriger des erreurs de design en implémentant des solutions à prototyper (le design est globalement fini)

- [ ] **Capables** :
	- [ ] [[CapableSystem_Rework_3]]
	- [ ] [[CapableSystem_Rework_4]]

- [ ] **Chunks** : réécrire le loading/unloading des chunks en se basant sur les frontières de l'écran, ce qui va corriger beaucoup de bugs visuels et réduire drastiquement les frames drop
	- [ ] mettre un gros collider idéalement [LineCollider2D] ? ou alors un énorme polygon collider qui épouse la forme du level afin de renforcer les murs pour pas que des items traversent

## .

## [[AnimSystem_Rework_1]]
## .

## [[gameplay d'attaque & esquive]]
## .

## UI & Cinematics :

- changer les messages :
	- la bulle de text s'étend vers le bas
	- **IL NE FAUT PAS QUE LE MOT QU4ON EST EN TRAIN DE LIRE BOUGE**
	- quand on appuie sur A ça valide et fait monter le message, puis ça passe au message d'après
	- on supprime le changement dynamique de coté

	- Quand une discussion est lancée, ça "split" l'écran en 2 avec une enorme bande noire au milieu qui laisse de la place pour les bulles de messages.
		- 2 caméras ??????????
			- +1
			- on peut même faire descendre le perso à qui on parle comme ça les bulles sont "en face" verticalement & horizontalement
			- une discussion ne peut pas changer de coté
				- quand on discute le temps == 0 ?
					- +1
					- pas de mouvement de rien ?
					- pas de déplacements en tout cas
					- ça veut qu'on veut 2 trucs différents : des réactions rapides avec des émojis / onomatopées qui peuvent être dites n'imp quand et arrête pas le gameplay.
					- on peut répondre à n'importe quel réaction rapide et lancer une discussion ??
		- faire un shader fullscreen pour ça ? comment on déplace tout ?
			- -1
			- pas fullscreen, on veut pouvoir placer les bulles de messages dedans
		- quand la discussion est finie, ça s'arrête et ça redevient normal


## .

## Hacking :

- objectif : réintégrer un premier système fonctionnel de hacking **ui-based**

- [ ] pas de hack through gameplay
- [ ] **faire que les Files sont des Items**, stockables sur un ordi serveur etc
- [ ] remettre le laptop
- [ ] faire un premier jet de [[UI_Laptop]]


## .
## lancement 1e démo steam :

- deadline : 
- [ ] fixer la résolution à 16:9
- [ ] faire un shader pour la cinématique
- [ ] et faire un shader pour les traces de [Fred]