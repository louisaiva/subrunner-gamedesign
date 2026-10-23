#chara-design

première version d'ajout recensée : **1.5.2e**

---

## description :

Le robot [USB] de la faction [[Unit]] est un robot complètement électronique générés en masse pour ~ de base ~ aider les gens dans leur tâche de tous les jours. ils ont été retrouvés par centaines dans les profondeurs de **SUBCITY**, et sont majoritairement endormis. Mais des hackers et/ou des policiers peuvent les controller et leur donner des instructions.

---

## aspect visuel :

![[image-28.png]]![[image-29.png|384x411]]

---

## capacités & attaques :


Ils peuvent utiliser des [[Shield]]s :
- apparaissent lévitant devant eux. (Comme ça pas besoin de faire des sprites galères supplémentaires).
- Empêche de dasher.
- Le layer est contenu directement dans la [[ShieldCapacity]]


Ils attaquent à distance avec leurs bras : 
- leur bras se transforme en lance roquette et un missile nous arrive dessus. 3 missiles ?


Ils ont aussi une grosse attaque chargée :
- quand on reste proche d'eux longtemps, ils peuvent nous attraper s'ils arrivent à charger une animation d'attaque dont la charge est très lente et qui finit par un attrapage par le colbak par le robot. on prend plein de baffes et on retombe au sol
- si on part de la zone d'attaque pendant que ça charge, le robot peut arrêter de charger son attaque.

comment décider si le robot doit faire une grosse attaque ou une attaque à distance ?
- on peut mettre un neurone là ! pile entre les deux. ce neurone fait une formule mathématique influencée par un facteur, et si c'est pile hop attaque lointaine, si c face hop attrapage