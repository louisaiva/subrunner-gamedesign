#problem

- # DESCRIPTION
	- l'inventaire est pas intuitif, que ce soit le quick inventory avec les chests
	- ou même l'inventaire principal
	- c'est dû à plusieurs problèmes actuels (1.5.0):
	
	- ### BUGS ACTUELS
		- expliqué nulle part
		- controls pas identiques tout le temps
		- gestion des coffres in-game pas intuitive, stressante, brise complètement l'immersion

- # SOLUTIONS POTENTIELLES
	- 
	- ### UI_HUD n'a pas d'UI_Pool concurrentes
		- Plus de chest menu / computer menu ui in-game.
		- Tout est fullscreen ce qui signifie qu'interagir avec un coffre ouvre un [[UI_Pool]] (on est plus sur le HUD)
		- tous les [[UI_Pool]] ouvertes depuis des objets ont la time scale = 0.5f
		
		- #### avantages
			- plus intuitif pour le joueur, le menu s'ouvre en grand et on comprend qu'on ne peut plus se déplacer
			- plus d'espace pour faire une UI chouette (vu qu'on peut utiliser tout l'écran)
		- #### inconvenients
			- on peut pas récup des items pendant qu'on court (à la volée)
	
	- ## Unified Controls
		- on unifie les controls pour que le joueur appuie tout le temps sur les mêmes controls pour la même action
		- 
		- plan de rebind :
			- (A) -> interaction avec objets / -> utilisation & deplacement d'UI_Slot
			- (X) -> rien / rien (drop?)
			- (B) -> dodge / cancel menu
			- (Y) -> attack / drop?
		- 
		- ### avantages
			- (A) pour interagir avec tout
			- (B) est le bouton par défaut pour quitter mdr (dodge ça quitte le combat)
			- (Y) bouton 