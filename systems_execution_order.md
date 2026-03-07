

Certains systèmes / scripts dans ces systems doivent être awaken dans l'ordre pour bien fonctionner. L'idée plus tard serait d'avoir un script spécifique qui déclenche les awake de chaque systeme de manière full organisée et parametrable, mais bon pour le moment j'ai aps ça donc je fais seulement avec les paramètres de "Script Execution Order" dans les Project Settings de Unity.

Pour que ça soit pas le bordel (ça l'est déjà), faut pas hésiter à noter les règles et raisons en dessous :

- le script [[CapacitySystem]] doit être awaken **APRES** [GameManager] **CAR** il utilise la methode **IsKind()** qui donc nécessite que GameManager.Instance soit != null