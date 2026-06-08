 
# 1. fonctionnement avec colliders :

room reçoit les calls du [PolygonCollider2D] lorsque des capables entrent / sortent de la room.

Room doit implémenter la logique des functions suivantes :
- **LoadData()** / **UnloadData()** / **UpdateData()**
- **Show()** / **Hide()**
	- pour quand une Room est loadée mais qu'on veut pas qu'elle s'affiche parce qu'elle n'est pas visible par le joueur (un mur avec une porte fermée sépare la main room de celle ci par exemple)
- enregistre les calls de colliders dans 2 listes **IN** & **OUT**.




Le reste se passe dans [[ChunkSystem]] :


## update 

dans [RoomSystem], à chaque update on voit si on a attendu un x délai, et puis on parcourt toutes les Room :
- on récupère toutes les paires IN et OUT qui concordent : signifie qu'on doit déplacer un [[Movable]] d'une room à une autre
- on parcourt tous ces [Movable] :
	- si c le perso, on recalcule la bonne room principale, puis on lance le chargement / déchargement des rooms adjacentes **ASYNCHRONE**, peut meme être delay de 0.4 secondes genre
	- si c un capable qui sort des room chargées (loaded zone ?), on appelle [[CapableSystem]] pour qu'il décharge ce capable et on le déplace dans la bonne Room
	- si c un capable qui rentre pareil on veut le charger, on appelle directement [[CapableSystem]] pour qu'il nous le file et on l'assigne à la bonne Room.
	- si c un capable qui passe d'une Room à l'autre, toutes 2 chargées, bah on l'assigne juste à la bonne room et on l'enlève de de l'ancienne


## awake

Pour faciliter le developpement on veut aussi que [RoomSystem] ait un temps d'initialisation avant le lancement des **Tick()**. Parce que sinon les capable qui sont déjà à l'intérieur des rooms vont faire apparaitre des **IN** au début qui ne seront jamais matché avec une autre room étant donné que c'est des téléportations en qq sorte. Pour cette raison on définit donc un **frame_number_init** et à chaque update avant de tick() on vérifie si on est encore dans ce créneau d'initialisation, si oui on fait rien on attend, puis une fois ce compteur terminé on lance une méthode qui arrive qu'une fois et qui va :
- parcourir les IN de chaque room
- leur assigner les capables qui ont fait des IN
	- (si un capable est dans plusieurs rooms à la fois on en choisit un au pif)
- puis wipe toutes les données de IN & OUT.
- ensuite ça lance le Tick !!