#rework #done

-  version de création : **1.5.0**
-  version de résolution : **1.5.0s**

---
- ## **objectifs**
	- pooler correctement la [WorldKeyData] des [GoapActionProvider]
	- créer une première version d'un [MotorEngine] qui gère les entitées unloadées
		- BatchActionProvider




---
- ## **TODO**

	- [x] comprendre comment sauvegarder les [WorldKeyData]
		- [x] merge les 2 [CapableTarget] ou renommer le serialized one en [SerializableCapableTarget]
		- [x] faire qu'on puisse sauvegarder des [CapableTarget] plutot que les [TransformTarget] de mes couilles
		- [x] **TakeDamage** doit faire partie intégrante de [IA_Action] et arrêter l'action, peu importe laquelle, lorsqu'on prend des damages
			- > plus tard on pourra stocker dans [IAData] des parametres pour savoir si on veut etre safe -> stopper l'action direct, ou etre en mode "combat" -> pas forcément stopper l'action
		- [x] [AttackActionResult] ne doit plus stocker un [Capable] en tant que target mais un [CapableTarget], comme ça on a pas de problème pour checker le target.capable_id

	- [x] faire un premier jet d'un [BatchActionProvider] qui calcule la bonne action à poursuivre
