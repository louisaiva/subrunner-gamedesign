#system #designing

- [ ] [[Controller_Rework_1]]


---
# description

Le [Controller] est le système qui détermine quel capable est actuellement contrôlé par le joueur. Fait le lien entre les **Inputs** du [[InputManager]] et le [[Capable]] qu'on controle actuellement
- en gros c'est un peu notre âme quoi, on peut la transférer d'un [[Capable]] à l'autre et c'est ce qui nous permet de nous déplacer etc quand on contrôle le [[Perso]] ou un [[Being]]


> **READ ME PLEASE**
> ne gère **PAS** les UI_Inputs !! Désormais [[UIC (UI_InputsController)]] est situé sur le [[UI_Manager]] directement et géré par lui :D
> c bcp mieux comme ça même si on a pas de controller bah on peut aller dans les options mdr


---
# fonctionnement du système

[Controller] est un enfant du [[Capable]] contrôlé.

contient aussi des sous systèmes

- ## PIC
	- [[PIC (PersoInputsController)]] se charge de faire le pont entre les **Inputs** in-game et les actions qui vont être trigger par ces **Inputs**

- ### Hacking system
	- [[VulnerableNavigator]] permet de selectionner le [[Vulnerable]] qu'on souhaite hack
	- [[ExploitNavigator]] permet de selectionner l' [[Exploit]] qu'on souhaite selectionner (ou selection automatique)

---
# problèmes actuels


- problème d'[edge-cases] : des fois ça fait des trucs chelous, notamment :
	- destruction du controller
	- callbacks inventaire complètement cassés



- problème de [design] :
	- quand on controle un autre capable que le perso, comment gère t on :
	- -> l'inventaire ??? est-ce qu'on affiche celui du perso tjrs ? ou pas ?
	- -> les shortcuts hud renderer ?? est-ce qu'on en affiche ?
	- -> le hacking ?? est-ce qu'on utilise seulement la [[HackCapacity]] du [[Device]] du [[Perso]] ? ou alors est-ce qu'on peut utiliser par exemple les [[Core]] du [[Device]] controllé ???


---
# todo
- [ ] 
