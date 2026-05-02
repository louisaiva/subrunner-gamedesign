

Certains systèmes / scripts dans ces systems doivent être awaken dans l'ordre pour bien fonctionner. L'idée plus tard serait d'avoir un script spécifique qui déclenche les awake de chaque systeme de manière full organisée et parametrable, mais bon pour le moment j'ai aps ça donc je fais seulement avec les paramètres de "Script Execution Order" dans les Project Settings de Unity.

Pour que ça soit pas le bordel (ça l'est déjà), faut pas hésiter à noter les règles et raisons en dessous :


- le script [[AppManager]] doit être awaken **AVANT** n'importe quel [[Capable]] **CAR** les capables appellent AppManager.Instance dans leur **OnEnable** (qui est parfois fait en meme temps qu'awake, donc probleme)
- le script [[WorldManager]] doit être awaken **AVANT** [[GameManager]] pcq game manager lance le load du world dans l'awake, et donc world manager doit avoir vérifié quels world sont déjà existants avant sinon il peut pas select
- le script [[CapacitySystem]] doit être awaken **APRES** [GameManager] **CAR** il utilise la methode **IsKind()** qui donc nécessite que GameManager.Instance soit != null