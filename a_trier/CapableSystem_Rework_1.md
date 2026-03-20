#rework #doing

-  version actuelle : **1.5.0c**

---
- ## **objectifs**
	- mettre en place des [DataTemplates] qui nous permettent de dupliquer la data depuis une data stable plutôt que depuis une [Data] potentiellement changée




---
- ## **TODO**

	- [x] créer un nouveau Dict<string,CapableData> qui stocke des [Templates]
		- [x] faire que ces templates n'aient pas de "-1" à la fin de l'id
		- [x] faire que lorsqu'on spawn un [[Capable]] bah ça créé une [Data] à partir d'un [Template] plutôt que depuis une data existante