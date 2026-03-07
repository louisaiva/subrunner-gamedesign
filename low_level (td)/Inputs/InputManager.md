- **singleton** qui gère les différents sous systèmes d'inputs

les Inputs sont séparés en plusieurs sous catégories

- [[InputFeedback]]


## rework envisagé :
- faire que l'input manager stocke tous les [[EndlessInput]]
	- ça parait logique lol
	- du coup faut les virer de [[PIC (PersoInputsController)]] & [[UIC (UI_InputsController)]]
- super avantageux parce que ça permet aux [[EventFeedback]] qui le souhaitent de demander non pas une input action, mais potentiellement une endless input action
	- -> ça veut dire que dans les menus on peut afficher des EF qui se colorent seulement quand l'input est hold, ou inversement seulement quand c press !