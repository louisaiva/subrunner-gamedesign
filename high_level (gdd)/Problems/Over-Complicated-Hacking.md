#problem 

- # DESCRIPTION

	- les mécaniques de hacking sont pour le moment (**subrunner 1.5.0**) trop complexes à comprendre et donc à proprement utiliser par les nouvelleaux joueureuses
	- notamment à cause des problèmes suivants :

	- ## BUGS ACTUELS
		- [[Inventory]] pas accessible parce que indiqué nulle part
		- gestion des modules trop complexe et donc
		- gestion des exploits/keys incompréhensible

- # SOLUTIONS POTENTIELLES
	- ## Exploits en tant qu'Items
		- on garde le même système de hacking, mais les modules ne sont plus trouvable dans des coffres. Au contraire on trouve dans des [[Computer]] des clés / exploits qui vont être directement intégrés, soit au laptop soit au module adéquat

		- les [[Module]] ne peuvent désormais plus être détachés d'un [[Device]] depuis l'inventaire, si on veut vraiment faire ça on pourra le faire en fin de partie (et donc en fin de developpement) avec par exemple un outil comme [[(LT) Screwdriver]]
		- [[Module_HDD]] a désormais stockage illimité
		- les [[Module]] sont carrément invisibles dans l'inventaire ! ils occupent une place particulière et n'existent qu'au sein du [[LaptopInventory]]
	
		- ### avantages
			- le joueur n'a plus besoin de se préoccuper d'installer des modules, ou même de transférer des files d'un module à l'autre, le joueur n'a plus qu'à se préoccuper des [[File]], ce qui est LE truc important du jeu => le but est de trouver des hacks et des clés, donc c'est parfait
			- on peut drop des files par terre ! => quand une porte est bruteforced, la clé pop par terre et la porte s'ouvre
			
	
	- ## Créer des hack tutos
		- premier tutoriel au [[Level_-4]] pour expliquer comment on hack "statiquement".
			- on récupère le [[Laptop]] puis on va sur le [[Server]] et on voit qu'on peut récupérer la clé
			- 
		- faire un petit tutoriel avec un item simple fait pour l'occasion (une lampe, un haut parleur ?)
		- Remplacer le interact tuto par un **joystick R** quand on est dans le radius de hack
		- puis par un **RT** quand on s'est enfin connecté à l'objet