#subsystem #designing

---
# description

**SousSystem** est un [subsystem] de :  [[WorldBuilder]] - [LevelTranslator]

sert à faire des pti chunks depuis des grosses Room !




---
# fonctionnement du sous système








---
# problèmes actuels



> **read me please :**
> Ces problèmes sont du [long-term], et donc à retravailler **APRES** la [[july26demo]]




## probème de [génération] :


La génération des chunks peut produire des polygons chelous, à répertorier en prenant des photos ici en dessous.


**solutions potentielles** :

- vu que c'est quand les chunks sont trop petits, on peut tester en élargissant la [max_chunk_area]

- ou alors aussi en détectant une ligne de polygon cheloue et en disant à l'auto chunker de garder le chunk du dessus

- [compliqué ++] ou encore (plus compliqué), en détectant le problème et en créant d'encore plus petits polygons, **MAIS** ça risque de créer des trop petits polygons donc en vrai vaut mieux garder des plus larges ?
	- faire une taille minimum ???

- [compliqué +] ou alors faire un meilleur algorithme d'auto chunk basé sur une sorte de fill tiles ? comme ça on a presque toujours exactement des chunks de la taille de [max area]
	- > sorte de voronoid chunk ?
		- nonn c'est mieux de rester avec des full carrés



**photos** :

 ![[image-5.png|321]]![[image-7.png|321]]
 
- pareil mais en diagonale chelou avec polygon collider inversés limite


---
# todo
- [ ] 