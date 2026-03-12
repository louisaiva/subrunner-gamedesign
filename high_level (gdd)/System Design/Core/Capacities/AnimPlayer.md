#system #designing



---
# description

**AnimPlayer** gère le rendu des [[Capable]]. Il est associé à un [SpriteRenderer] qui va recevoir les bons sprites pour les bonnes animations sous la classe [Anim].
Il possède donc un paramètre [Skin] qui lui permet d'obtenir les bonnes animations.

Relié à une [[AnimBank]] chez qui il va chercher toutes les anims lol ça parait logique en fait...

Il peut aussi gérer des [[AnimLayer]] auxquels il va transmettre les animations

---
# problèmes actuels

- [ ] problème de [hierarchy] :
	- [ ] on devrait mettre l'AnimPlayer principal d'un [[Capable]] sur un **enfant** du capable pour en faire un réel component au lieu de l'avoir directement sur soi-même




---
# reworks
- 