#system #designing

- [ ] [[WorldSystem_Proto]]


---
# description

[WorldSystem] se charge de gérer les différents mondes directement depuis le bon dossier de data pour éviter d'avoir notamments des [capable_id] ou [room_id] qui se chevauchent, ou encore des [capacities_data] qui ont plusieurs owners différents (ce qui créé des duplicates et donc brise les chaines d'ownership)

il gère par la même occasion la [WorldData] qui peut comme ça être saved facilement.


---
# fonctionnement du système


chaque monde a un dossier de save associé localisé dans

ce dossier se présente sous la forme suivante :

- world_name/
	- world_name.json
	- levels/
	- rooms/
	- capables/
	- capacities/

les templates sont internes à **subrunner** et sont donc situés dans [Assets/Resources/data/templates/]





---
# problèmes actuels

- problème de 




---
# todo
- [ ] 