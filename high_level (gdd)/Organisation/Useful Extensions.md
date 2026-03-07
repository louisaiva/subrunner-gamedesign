#art #qol

la création / utilisation de plusieurs extensions permettent de simplifier ma vie

### Aseprite
- 
- better-color-replacer : remplace des couleurs sur toutes les frames présentes

- emission-generator : permet de créer/update directement une texture d'emission full noire à partir d'un groupe de layers (créé notre layer ...em/em)
	- [ ] à rajouter :
		- [ ] si y'a un layer nommé ".em. x" dans le groupe selectionné (ou x peu etre n'imp) bah ça le copie directement dans le groupe .em. avec le bon nom
		- [ ] si y'a pas de subname ça enlève simplement .em. du nom
		- [ ] si y'a un subname ça remplace em par le subname
		- [ ] supprime le calque précédent s'il existait
		- [ ] et vérifie que ça les met en haut de la liste

- plusieurs autres extensions devraient être implementées :
	- [x] **aseprite** : sprite sheet custom exporter : permet d'exporter directement dans les bons dossiers les 2 sprite sheets mise à jour : machin.png & machin_em.png
	- [ ] **unity** : auto-spriter : custom sprite editor tool qui permettrait de spriter exactement les bons sprites & pivot avec une spritesheet custom avec des blocs rouges et les points de pivot ?
	- [ ] **unity** : item-auto-spriter : pareil custom sprite editor tool qui permet, à partir d'une sprite sheet d'item (donc contenant seulement 4 frames), de créer directement les 10 sprites nécessaires à la création des animations *idle* & *hover*
	- [ ] **unity** : item-animator : permet de créer directement les animations *idle* & *hover* à partir de la spritesheet de 10 sprites