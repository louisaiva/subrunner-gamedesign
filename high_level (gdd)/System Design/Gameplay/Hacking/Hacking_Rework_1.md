#rework #todo

-  version de création : **1.5.3a**
-  version de résolution : 

---
- ## **objectifs**
	- réintégrer un premier système fonctionnel de hacking **ui-based**
	- pas de hack through gameplay

---
- ## **TODO** 

	- [ ] **faire que les Files sont des Items**, stockables sur un ordi serveur etc
		- [ ] les files ne doivent pas être jetées automatiquement à la mort d'un bail, on jette l'ordi (le faire avec le type d'item virtual)

	- [ ] faire un premier jet de [[UI_Laptop]]
		- [ ] password
		- [ ] laptop programs hotbar
			- [ ] [optionnel] button plug laptop (setting auto-plug)
		- [ ] unlocked : modules s'affichent au milieu. Si un module obligatoire est manquant (cpu, network), alors à la place du module y'a une icone warning en rouge missing module. modules pas obligatoires pas affichés par contre si manquants
		- [ ] un click ouvre la fenetre en grand sur le module clické (en gros on stacke l'ui_pool spécifique à ce module sur le [[UI_Laptop]]). Voici la liste des ui_pool de modules :
			- [ ] UI_Explorer (affiche les disques et les fichiers des disques)
			- [ ] UI_Networker (affiche le réseau, permet de jump d'un pc à l'autre)
			- [ ] [mid-term] UI_TaskManager (cpu ? affiche programmes en cours sur le PC)

	- [ ] remettre le laptop
		- [ ] faire que ça se connecte automatiquement au [[UI_FilePool]] du [[UI_InventoryMenu]] pour afficher les files si on a un device
