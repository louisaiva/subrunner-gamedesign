### UI_Device est un [[UI_Pool]]
**purement graphique**

ce pool permet d'afficher plusieurs informations sur un [[Device]]
il s'affiche de 2 manières différentes :
- soit en interagissant avec un [[Computer]] via **A**
- soit en **trojan** sur un [[Device]]

dans tous les cas, ça change le [[Controller]] de capable sur le device visé, ce qui désactive les **perso_inputs**

composition de l'ui :

- affiche toujours en bas milieu de l'écran un [[UI_Window]] de raccourcis de notre [[Laptop]] (si on en a un) : composé de [[UI_Button]] avec les icons des différents [[File]] stockées sur le laptop et en rapport avec le device (les exploits, les clés qui marchent)

- possède aussi une [[UI_Description]]

- si le device est **locked**, alors affiche un [[UI_LoginWindow]] avec une entry user & une entry password
- si le [[Device]] est **unlocked**, alors affiche au milieu de l'écran un [[UI_Window]] de [[UI_Toggle]], un pour les différents [[Module]] installés sur le device :
	- cpu
	- network
	- hdd

- si les toggles sont activés alors ça affiche d'autres ui_window en fonction de l'element :
	- [[UI_FilePool]] pour le hdd
	- [[UI_CoresViewer]] pour le cpu
	- [[UI_Network]] pour network
- 










#### -- deprecated --

- l'UI_Device affiche différentes informations via plusieurs classes d'UI différentes :
	- [[UI_Window]] : permet de répartir les différents éléments d'ui suivants dans des fenetres qui se resizent automatiquement, pratique ! (et joli ^^)
	- [[UI_Button]] : permet d'intéragir avec le device, par exemple un bouton "disconnect" ou un bouton "scan files"
	- [[UI_Details]] : permet d'afficher des infos texte via 2 [[UI_Description]] spécifiques de couleurs différentes
		- un en blanc calé à gauche pour les catégories d'informations *(ex : "os_name :")*
		- un en jaune calé à droite pour les réponses à ces catégories *(ex : "bug_os")*