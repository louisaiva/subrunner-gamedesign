#subsystem #designing

---
# description

**SousSystem** est un [subsystem] de : [[StorySystem]]




---
# fonctionnement du sous système


les dialogues et monologues de texte sont séparées en "bulles" de **messages** (aussi appelés msg). ces messages sont activés via [[TalkCapacity]] qui call [MessageBank] pour demander la création et l'affichage d'une bulle de message.

[[TalkCapacity]] gère ensuite la gestion de la hauteur / fade out de ces bulles de texte ?

On peut aussi stacker plusieurs bulles les unes sur les autres

une bulle ressemble à ça pour le moment :
![[image-9.png|452]]![[image-10.png|239]]

détermination de la taille d'un message :

- chaque message a **UNE WIDTH FIXE DETERMINEE A L'AVANCE** : comme ça pas de problème relou avec un mauvais alignement ou que sais je ! chaque "bulle" de message, une fois complètement affichée, sera à la width déterminée et donc pas de soucis

- par contre la **HEIGHT** s'auto scale automatiquement. pour ça on utilise le combo génialissime j'ai nommé : [UI_AutoResizer] + [ContentSizeFilter]
	- le text tmp pro ui gui a un [content size filter] reglé en preferred size comme ça le texte prend toujours la preferred size
	- quant à lui, le slot a un [ui_autoresizer] qui target le text, ce qui applique dans l'update la taille du text.

détermination de la position d'un message :

- chaque perso a une hauteur de "mouth" ce qui détermine la position de la première bulle et celle de l'encoche
- les bulles déjà présentes lors de la création d'un nouveau message voient leurs positions en y **tweenées** vers le haut pour laisser la place au nouveau message en dessous

on peut mettre des smileys en plus : https://www.youtube.com/watch?v=gJt6vSSlG3I

---
# problèmes actuels

- utilise t on un seul canvas pour les messages ?????
	- ça veut dire qu'on doit calculer manuellement et surtout update à chaque frame la position de chaque message
		- beaucoup de maths de conversion d'echelle
		- nécessaire cependant pour mettre des tweens de position en x
		- est-ce qu'on veut pouvoir tweener la position en x ?
			- (en y on est obligé d'en avoir et c'est pas forcément une mauvaise chose)

- est ce faisable de regrouper les msg d'une discussion ?
	- si un seul canvas c assez simple
	- si un canvas par [TalkCapacity] c'est un peu tendu, surtout si on gère les positions en y avec un [VerticalLayoutGroup]
	- faisable mais pas forcément méga utile vu que les persos qui parlent vont souvent être à côté, il vaudrait mieux faire des bulles séparées quand trop proche du coup

- un monologue / dialogue peut il bouger la camera légèrement ?

- lors d'un dialogue plusieurs choses changent dans [[TalkCapacity]] :
	- [x] le rect transform [msg group] doit changer ses pivot pour être au centre en x afin que les messages à gauche & droite soient centrés autour de la lerp local position
		- [ ] changer aussi les encoches
		- [ ] 

	- [x] le rect transform [msg group] peut voir sa width evoluer en fonction de la distance entre les members histoire d'occuper au mieux l'espace entre les différents membres

	- [x] FacingRight doit changer son calcul. au lieu de déterminer en fonction de l'orientation du joueur, on calcule par rapport à la différence en x entre les différents membres de la discussion.
		- [x] si [avg_members_x] > [capable.x] alors on a FacingRight = true peu importe l'orientation du player. et l'inverse si <


---
# todo

- [ ] [UI_Message] doit stocker les couleurs de la font et du slot
- [x] pareil pour l'encoche de [[TalkCapacity]]

- [ ] lors d'un [Monologue], le facing des messages doit être caculé en fonction de la vitesse de déplacement Movable.VelocityVector afin de ne pas géner la course

- [ ] revoir le déclenchement d'un [Dialog], la gestion du dialogue quand on est trop proche, et donner plus d'importance à la classe [TalkMode] (RTO) qui peut stocker les talk members et avoir les methodes low level pour calculer les distances, etc, peut etre même une methode update()
	- > but : désengorger [TalkCapacity], et avoir des méthodes prédefinies pour chaque poste (leader, talk member) leader/slave basically