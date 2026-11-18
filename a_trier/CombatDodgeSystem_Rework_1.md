#rework #todo

-  version de création : **1.5.2f**
-  version de résolution : 

---
- ## **objectifs**
	- diversifier le gameplay de combat, jugé trop répétitif par les joueureuses




---
- ## **TODO**


	- [ ] augmenter legerement la vitesse de course de bob


	- [ ] intégrer la souris au combat
		- [ ] réflechir mouse dynamic orientation [[2026_05_03]]
		- [ ] faire que la souris indique la direction d'attaque du perso (le perso se tourne dans la bonne direction juste avant de frapper)
	
	- [ ] diversifier les ennemis :
		- [ ] faire un ennemi à distance : petit drone qui lance des ptits missiles lents qui explosent
		- [ ] faire un ennemi in-dodgable : gros zombie lent qui fait d'autres attaques
		- [ ] faire un ennemi qui combine les deux : [usb]
	
	
	- [ ] faire que le dummy peut mourir (et réapparait direct après un cooldown)
		
	
	- [ ] retravailler les animations :
		- [ ] raccourcir le rangement du katana dans l'attaque LR
		- [ ] dessiner des attaques en haut et en bas, voire même en diagonales
		
	- [ ] faire que l'attaque et le dodge sont **time-based**. c'est à dire qu'elles peuvent être soit des attaques/dodge courts, soit des attaques/dodges chargées, si on maintient suffisament un treshold de time (qui est le même pour les deux touches)
		- [ ] réutiliser le même système d'inputs + callbacks que déjà intégré à l'UI avec les [[EndlessInput]]
		- [ ] l'attaque fait plus de dégat, ou alors on dessine ~~une nouvelle animation d'attaque ?~~
		- [ ] le dodge nous emmene plus loin
		- [ ] faire que le treshold soit suffisamment long pour que lorsqu'on fait un simple appui bah ça fasse tout le temps la même attaque qu'on a ajd
