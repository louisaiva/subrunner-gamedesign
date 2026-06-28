

---
# TODO


- [x] tester avec netwonsoft json
- [x] écrire une methode dans SaveEngine qui permet de load un WorldDataSave depuis un json directement (comme ça on peut load depuis un world template)



- [x] Continuer le small rework de la [SaveEngine] pour pouvoir charger des world templates lors de la création d'un monde
		- > stick with **folder save** until [mid-term]
		- > on répertorie dans data/world_templates/templates_list.json la liste (et donc les paths) des world templates actuels
			- [ ] se met à jour si on est dans l'editor, et sinon charge simplement les templates path dans le build
		- > une fois qu'on a le nom du dossier on peut ensuite charger le world direct (pas besoin de copier) depuis le template en chargeant une [WorldSaveData] qui contient les bons trucs
			- [ ] vu qu'on peut pas naviguer dans l'arborescence des assets peut etre c'est nécessaire de renommer les extensions de fichiers :
				- .world / .level / .room / .chunk / .controller / .capable / .capacity
					- ! marche pas attention pcq resources . load fonctionne sans extension
					- ptet on récup tous les text asset et ensuite on les retrie correctement ?
					- sinon utiliser asset bundle / adressables
