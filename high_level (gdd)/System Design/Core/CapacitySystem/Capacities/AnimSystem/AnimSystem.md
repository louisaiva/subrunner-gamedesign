#system #designing

- [ ] [[AnimSystem_Capacity_Integration_Rework]]
- [ ] [[AnimSystem_Rework_S_tier (ia)]]

---
# description

[[AnimPlayer]] gère le rendu des [[Capable]]. Il est associé à un [SpriteRenderer] qui va recevoir les bons sprites pour les bonnes animations sous la classe [Anim].
Il possède donc un paramètre [Skin] qui lui permet d'obtenir les bonnes animations.

Relié à une [[AnimBank]] chez qui il va chercher toutes les anims lol ça parait logique en fait...

Il peut aussi gérer des [[AnimLayer]] auxquels il va transmettre les animations

---
# fonctionnement du système

[AnimPlayer] fait le travail d'une hypothétique [AnimEngine]. c'est lui qui gère l'update des sprite renderer frame par frame. sauf que chaque [[Capable]] à son [[AnimPlayer]] donc c'est pas méga opti

[AnimBank] gère la sauvegarde des [Anim] (leur conversion en json) depuis des **AnimationClip** de Unity. Possède aussi un système de variants pour créer des animations avec des spritesheets différentes à partir des mêmes infos d'[AnimationClip].

---
# problems

- [ ] [mid-term] problème d'[integration core] : [[AnimSystem_Capacity_Integration_Rework]]
	- anim player n'est pas intégré au système de [Capacity]. Ce qui est un peu relou et complexifie le debug, mais surtout, peut amener à des [spaghetti] si on tente de faire par exemple des capables qui n'ont **PAS** de sprite !!
	- > notamment relou parce que **Show/Hide()** ne sont pas interfacés, ce qui fait des bugs avec des capacities.
	- > relou avec la [SpriteCapacity]

- [ ] [mid-term] problème de [design] problème de [decoupling code] :
	- en soit on a pas besoin d'un sprite renderer "principal"... parce que c'est un layer en soit, il faudrait donc supprimer tout le code qui affiche les sprites du leader et faire un layer tout simple basique à la place
	- [animplayer] holderait donc seulement la logique de quel layer doit jouer quelle animation, gestion de la pile d'animation etc
	- --> **un skin serait donc un ensemble de skin_layer**, ce qui est une très bonne chose
	- un layer peut aussi ne pas avoir DU TOUT la capacity, par exemple l'animation "talk" n'affecte que le layer "head", et donc le layer "feet" n'a pas besoin même de jouer idle ou quoi, il doit jouer l'animation de la pile d'en dessous, genre "walk" -> on peut parler en marchant, banger


---
# todo

- [ ] 