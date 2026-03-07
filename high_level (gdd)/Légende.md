
# 1 - Légende du wiki


*N.B. la légende n'est pas à jour. Encore en transition de milanote vers logseq/obsidian*



Ce docu est truffé de notes plus ou moins bordéliques en apparence.

Pour essayer d'organiser un peu mieux cette masse étrange de lettres de symboles et de croquis plus ou moins bien réalisés, on a quelques règles non-obligatoires mais conseillées :


**scripts :**

_[abstract] class_ **Bidule** -> ceci est le nom de la classe de la note

_interface_ **Blurp** -> pareil mais c une interface quoi

- _float_ **variable** -> cette variable appartient à la classe du dessus. écrit avec son _type_
    
- _void [virtual/override]_ **DoSomething()** -> ceci est une fonction
    



**notes globales :** 

**machin** -> nom de variable, truc un peu important.

**machin : \n** -> début d'un paragraphe qui porte sur machin

**Machin** -> nom d'un script

**MACHIN** -> des trucs importants, le nom de la ville du jeu, le nom d'un perso souhaitant rester discret aussi par extension





**questionnements :**

qqch? -> signifie on a une question sur ce terme précisément

==qqch omg fait ça?== -> questionnement important en cours de réflexion

==qqch omg fais ça== -> equivalent du fluo, c'est important et il faut faire ça. réponse définitive et importante à un questionnement important aussi

==qqch omg fais ça== -> equivalent du fluo aussi !! mais plus funky lesgo

-> euh jsp mais jpropose cette idée -> réponse potentielle à un questionnement. si on est pas sûr on passe à autre chose et on y reviendra. lance un score de 0

-> non il faut pas faire ça -> ancienne (ou nouvelle) réponse votée -> score +1

-> euh avant fallait le faire ça -> ancienne réponse (ou réflexion) votée nul mdr c nul ! -> score -2

-> en vrai ptet faut faire ça mais jpense qd meme pas -> ancienne (ou nouvelle mais mdr souvent ancienne quand même quand c orange) réponse votée -> score -1

quand on revient dessus et qu'une idée est grave majoritaire ça veut souvent dire qu'il est l'heure de déclarer forfait et la proposition jetée passe dans les **deprectated**.

==wha ça c qqch== -> peut-etre faut le mettre à un autre endroit genre dans un autre script/board





# **2 - Légendes des commits (git)**

Sur le github (https://github.com/louisaiva/subrunner) il y a plein de commits (292 à ce jour). Les noms de ces commits nous informent sur leur état de santé et leur contenu.  

**(#14) wsh ceci est un commit** -> commit normal n°14, en cours de développement

**(~15) omg g tout cassé** -> ce commit est cassé, rien ne marche

**(%16) j'ai tout réparé !!** -> ce commit est un build, dernière version à ce jour !! si notre code actuel est cassé c'est une bonne idée de revenir à un commit comme ça. Idéalement à chaque commit % faudrait faire une release mais bon tkt pr le moment j'ai 3 builds de retard mdr

*N.B. : des fois je m'embrouille du coup ces légendes de commit ne sont pas forcément fiables à 100%, je crois j'ai noté des (~XX) en tant que maj stables mais je sais plus*
- [ ] à vérifier







# **3 - Légendes des versions de Build alpha**

les builds viennent avec un numéro de version _idéalement_ unique à ce build.  
les numéros de builds se présentent comme ça:

## - 1.4.1

## - 1.5.2c

ou, plus généralement, sous la forme:
#### itération . grosse_maj . prototype (+ lettre de build)

où :

- **itération** est le nombre de fois que je reprends mon jeu vidéo de la base (la première itération part de 0)
    
- **grosse_maj** est une mise à jour majeure du jeu, ajout d'un ou plusieurs nouveaux systèmes / gros rework de gros systemes
	- (exemple ajouter un world_builder)
    
- **prototype** est une mise à jour d'une fonctionnalité légèrement complexe, soit un rework de systeme, soit développement de plusieurs sous système, soit des fois un système complet si je fais un gros prototype ou quoi
	- (ex : ajout d'un menu avec plusieurs trucs)
    
- enfin la lettre qui suit (ou pas) indique le numéro de build actuel dans le dév de la fonctionnalité en cours de prototypage.
	- pas de **a** parce que quand on fait le 1er build bah c'est la première maj quoi, donc commence à partir de la b (si y'a un a c pas si grave non plus mdr)
	- en fait des fois y'a des **a** j'ai menti oups