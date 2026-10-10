#rework #todo

-  version de création : **1.5.0**
-  version de résolution : 

> **README PLEASE**
> this is [mid-term], which means we don't do it before the [[july26demo]]

---
- ## **objectifs**


	- réunifier le système des anims et l'ouvrir sous un système de [Visuel]
		- faire une [AnimCapacity] qui fait le lien entre [[AnimPlayer]] et le [[Capable]]

	- 
	- ainsi on peut avoir une [SpriteCapacity] aussi qui gère un système tout simple d'affichage de [Sprite] statiques.



---
- ## **TODO**

	- [ ] Coder [VisualCapacity] et son interface [Visualizable]
	- [ ] la cacher avec une accession la plus performante possible dans [Capable]
		- [ ] faire que tout redirige vers **Capable.Visual** plutôt que ~~**Capable.AnimPlayer**~~
		- [ ] Show/Hide sont [Visualizable], Skin est sous SkinCapacity?????
			- > hein ? est-ce qu'on aurait vraiment besoin de visual qui ont pas de skin ? lampes ? elles ont un skin aussi j'imagine
				- > (+1)
				- [ ] conclusion : regrouper skin + show() + hide() dans visualizable & [VisualCapacity]

		- [ ] les autres points d'entrées à regrouper sont associé à un [cast] soit dans [Capable] directement soit dans les capacity qui en ont besoin ?
			- [ ] notamment toutes les refs à [AnimPlayer] en fait qui doivent être castées vers if TryCast(AnimPlayer) Capable.Visual.
			- [ ] IsPlaying / Play / StopPlaying / IsShowing
			- [ ] Renderer

		- [ ] 

	- [ ] faire que [Capable] stocke une reference mise a jour de sa visual capacity
		- [ ] le faire dans **Capable.LoadData/UnloadData()**
		- [ ] 

	- [ ] Créer une [AnimCapacity] qui fait le lien entre cette interface [Visualizable] et [AnimPlayer]. on fait rien d'autre que remettre tout en l'état ->>>>>>>
		- [ ] S'ASSURER que [AnimCapacity] reste la plus petite possible !! AnimCapacity transfère tous ces appels de [Visualizable] vers ceux de [AnimPlayer] ? pas sur en fait
	- [ ] on **CORRIGE** **TOUT** les bugs du point d'avant
