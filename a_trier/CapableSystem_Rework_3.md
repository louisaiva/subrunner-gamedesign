#rework #todo

-  version de création : **1.5.2f**
-  version de résolution : 

---
- ## **objectifs**

	- permettre de changer des paramètres de template d'une instance déjà spawnée. ce qui résout un énorme problème de [design/workflow] :
	
		- Actuellement, une fois qwin spawnée, toutes ses variables et les variables de ses capacités sont stockées et sauvegardées. si après son spawn on change des variables sur le template "qwin" ou sur les templates de ses capacités, cela n'aura **AUCUN** impact sur les CapableData & CapacityData déjà spawnées, ce qui veut dire que la qwin déjà spawnée ne changera pas d'un poil sa data.
		- C'est super problématique parce que c'est chiant pour prototyper, tester des trucs. on doit soit respawn toutes les entités pour être surs qu'elles soient à jour, soit travailler en sachant que pas mal de paramètres sont deprecated. c horrible


	- solution : séparer template/instance data avec 2 pipelines json et des attributs type [RuntimeOnly] / [InstanceData] / [KindData]

		- améliore les perfs, réduit la taille de la sauvegarde

		- Comment ça marche ? Bonne question jamy
		- les variables possédant l'attribut [KindData] dans [[CapableData]] & [[CapacityData]] sont désignés comme étant des attributs communs à tous les templates. **ILS NE DOIVENT PAS ETRE INSTANCE BASED**. Ils sont constants après l'initialisation.

	- Voici un aperçu des différences avec le LOAD/SAVE flow d'avant !![[JSON LOAD & SAVE FLOW CHARTS.excalidraw]]
---
- ## **TODO**

	- [ ] écrire [KindData] resolver & faire un test avec le [TemplateJsonConverter] data script
		- [ ] check que ça récupère bien son bon type sans rien faire avec **TypeNameHandling = TypeNameHandling.Auto**
			- [ ] faire le test simplement dans [TemplateJsonConverter] en mimiquant un premier load depuis un instance/kind json
		- [ ] clean l'ancien moyen de récupérer la classe précise via le field **data.kind**

	- [ ] marquer tous les fields de soit [KindData] soit [InstanceData], notamment :
		- [ ] dans CapableData
			- [ ] dans tous les descendants de CapableData
		- [ ] dans CapacityData
			- [ ] dans tous les descendants de CapacityData
		- [ ] dans AnimPlayerData ?
			- [ ] dans AnimLayerData ?
		- [ ] dans FeetData ?
		- [ ] dans InventoryData ?

	- [ ] gérer les classes qui peuvent contenir à la fois des fields [KindData] & [InstanceData]
		- [ ] les marquer avec les deux attributs comme ça les 2 contracts resolver les prennent en compte
		- [ ] renseigner à la main ? ou faire une interface [HoldsData] 

	- [ ] réflechir comment doit fonctionner **Duplicate()**
		- [ ]      **deep-copy** les instances based ?
		- [ ] **reference-copy**       les kind based ?
	
	- [ ] écrire une première load pipeline qui :
		- [ ] deserialize les templates :
			- [ ] load les templates dans **Engine.loadTemplatesData()**
			- [ ] cache les [KindData] fields Infos dans un dict par précise class comme on l'a déjà fait autrepart (cached_data_by_kind) pour accélerer le feedage des values de fields kind-based.
				- [ ] attention ici c'est bien un Dict<**Type**, List<**FieldInfo**>> qu'on veut et pas basé par kind-id pcq tous les kind de memes type share les même kindspecific fieldinfo.
				- [ ] uniquement nécessaire pour le premier template de type Type qu'on croise evidemment.

		- [ ] deserialize les instances :
			- [ ] load les instances dans **Engine.LoadWorldData()**
			- [ ] récupère le template correspondant du Kind (pas avec le field .kind mais en récupérant la racine de l'id)
			- [ ] feed les values des fields kind-based cachés précedemment
				- [ ] on vérifie le type du field.
					- [ ] si c un field tout simple, on **SetValue()** direct
					- [ ] si c un **DataHolder**, alors on le parcourt pour feed ses fields justement, on veut pas l'overwrite
				- [ ] doit aussi feed les values des classes mères evidemment (fields de CapableData même quand on travaille sur ItemData)