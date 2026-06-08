#system #designing
- [ ] [[prototype]]


---
# description

[ExpSystem] gère le système d'expérience du jeu. Il permet aux joueurs d'améliorer leurs [[Item]] choisis lorsqu'une barre d'expérience est remplie. Pour se faire, les joueurs doivent se rendre au bon [[Upgrader]].

Tout d'abord le système sert surtout à améliorer :
- le [[Katana]], en lui donnant une meilleure attaque
- les [[Shoes]], en leur donnant plus de vitesse
- La [max_vie] du personnage, remplissant aussi tous les pv
	- cela doit se faire via des objets particuliers donc une classe fille de [[Upgrader]]


---
# fonctionnement du système

[[Upgrader]] est un [[Interactable]] qui est placé à certains endroits stratégiques des [[Level]]. Il récompense le joueur en lui donnant la possibilité de dépenser ses [Exp] dans des upgrades d'[[Item]].

- avantages par rapport à l'ancien système :
	- plus de coupure de gameplay (l'[[UI_LevelUp]] pool s'affiche sur demande de l'utilisateur plutôt qu'en plein combat)
	- fait comprendre au joueur le principe d'**upgrades** qui seront présentess pour améliorer les [[Module]] du [[Laptop]]

Le système repose donc aussi sur le système plus global aussi d'[Exp] et leur emission par le sous système [[ExpEmitter]] :

### 1. Exp

- Les points d'expérience [Exp] sont des particules qui sont émises lors de plusieurs évenements :
	- lors de la mort d'un [[Being]], ses points [Exp] sont relachés
	- lors du succès d'un [[Hack]]
	- lorsqu'un [[Being]] est content il lache des [Exp] aussi ?
		- > [long-term] mais ==+1==
		- > permettrait de donner de la vie aux mobs !


## 2. ExpCapacity

- a un collider pour récupérer les particules [Exp]. stocke et sauvegarde dans sa data les currents points d'exp et les exp restants jusqu'au prochain [ExpLevel] <- petite classe no mono ?
- communique avec l' [[UpgradeStation]]

## 3. CapacityUpgrade

- Sous classe qui peut être reçue par n'importe quelle [[Capacity]] et qui contient des infos d'upgrade de la capacity.

- **NO MONO MAIS SERIALIZABLE**

- Stocke les différents palliers d'une/les variables visées de la capacity et stocke leur level actuel, ainsi que plusieurs informations [[Descriptable]] pour l'[[UI_Descriptor]]

## 4. [[ExpEmitter]]




---
# problèmes actuels

- problème de [road-map] :
	- est-ce qu'on implémente ça pour la démo de [juillet 2026] ?



---
# todo
- [ ] 