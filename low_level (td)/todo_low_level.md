#todo 

contrairement au [[todo_high_level]], ce document a pour but de détailler le plus possible les différentes étapes dans un futur proche et ou lointain. les briques détaillées peuvent être à la fois sous forme de **Reworks**, mais aussi des random bidules oklm. chaque brique doit être la plus petite possible comme ça ça a pas l'air super dur à faire mdr

# 1.5.1

- ### UI system rework
	- [ ] [[UI_Manager_Rework_2]]
- ### File
	- [ ] faire des [[File]] des [[Item]]
	- [ ] faire des sprites de slots pour les [[File]]
	- [ ] 
- ### Inputs
	- changer les inputs sur 







(la suite c évidemment à retrier)


- [ ] est-ce qu'on peut faire que le bg devient rouge quand on se fait hacker/on prend des dégats

- [ ] implement cinematics system
	- [ ] make 2 start cinematic
	- [ ] make demo completed cinematic
	
- [x] polish the [[Keyboard + Mouse problem]] integration
	- [x] adapt hacking to mouse
		- [x] PIC input : left mouse
	- [x] adapt exploit selection
		- [x] PIC input : mid mouse
	- [x] create a InputFeedbackSwitcher + InputFeedbackManager for updating them all

- [ ] implement enemy wave system for the spawners to not appear
- [ ] implement first computer UI to have a proper way to steal the door' key
- [ ] change [[UI_File]] visuals to have better UX for
	- [ ] [[UI_ExploitSelector]]
	- [ ] [[UI_Device]]
	- [ ] [[UI_HDD]]

- [x] rework and fix the [[UI_Description]]
	- [x] smaller description
	- [x] that can write multiple characters at once ?

- [x] try with [[UI_CancelButton]] which is a [[UI_Button]] that cancels a specific [[UI_Slottable]] / [[UI_Pool]]
	- [x] prototype on [[Oven]] & [[Sink]]
	- [x] on [[Chest]]
	- [x] on [[UI_Window]]

- [x] rework la [[UI_HUD]] pool pour qu'interagir avec un [[Chest]] fasse que le déplacement est désactivé
	- [x] on navigue dans l'ui via **LJoy**
	- [x] on récup les items rapidement via **B**
	- [x] on ferme l'ui via activation d'un [[UI_CancelButton]]

- [x] create a [[SettingsManager]]
- [x] rework title screen