
c'est la démo du 3 octobre 2026 ! (aquarium ciné)

---

## OBJECTIFS PRINCIPAUX

- raccourcir l'intro (texte + skippable)
- changer logo
- mettre des logs ?
- ne rien casser



### 0. General
- [x] changer logo
- [x] changer proto version
- [x] mettre le nom du monde dans le menu pause
- [x] bouton pasta maker controller affiche ce qu'on doit réunir
- [x] speedrun clock afficher hms
- [x] connecter button steam

### 1. Intro
- [x] rework l'intro
	- [x] changer le texte pour plus que ça soit génant
	- [x] mettre des logs qui indiquent la position
	- [x] changer le zoom

- [x] mettre un bouton de skip qui fait timeScale x16 ?

### 2. Logs
- [x] faire un système de log par world
- [x] création/ouverture d'un fichier de log lorsqu'on charge un monde
- [x] 3 types de logs :
	- [x] on ajoute automatiquement le real time sur TOUS les logs

	- logs périodiques rapides (2 sec) :
	
		- [x] fps
		- [x] la position du controller

	- logs périodiques lents (20 sec) :

		- [x] toutes les entités chargées et leur chunk affecté

	- logs manuels :

		- [x] quand une entité est loadé + son chunk de load
		- [x] quand une entité est déloadé + son chunk de deload
		- [x] quand une entité change de chunk
	
		- [x] quand une entité est spawnée
		- [x] quand une entité est déspawnée correctement

### 3. Level Design
- [x] supp la porte qui passe par le haut


## 4. Questionnaire
- [ ] faire un google form avec les questions :

	- [ ] est-ce que vous vous êtes senti perdu ?
		- complètement perdu
		- un petit peu perdu, pas assez guidé
		- ça va
		- aucun soucis
	
	- [ ] est-ce que vous avez eu des problèmes de performances ?
		- énormes lags
		- petits lags
		- ça va
		- aucun soucis

	- [ ] est-ce que l'intro était cool, compréhensible ? (choix multiples)
		- pas drôle
		- buggée
		- incompréhensible
		- super chouette

	- [ ] comment était la difficulté ?
		- trop dur
		- un peu trop dur
		- difficulté parfaite
		- un peu trop facile
		- trop facile

	- [ ] comment était le gameplay ? (choix multiples)
		- trop répétitif
		- frustrant
		- dur à prendre en main
		- agréable

	- [ ] avez vous des suggestions ?