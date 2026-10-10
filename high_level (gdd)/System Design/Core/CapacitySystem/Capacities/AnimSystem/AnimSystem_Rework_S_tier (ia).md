#rework #todo

- version actuelle : **1.5.0**

---

- ## **objectifs**
    
    - fiabiliser totalement le système [[AnimBank]] + [[AnimPlayer]] + [[AnimLayer]]
    - supprimer les bugs subtils liés aux états partagés entre entités

---

- ## **TODO**

- [ ] **Logique parfaite**
    - [ ]  **ST-001 Isoler l’état runtime de lecture d’animation**
        - [ ]  ne plus modifier les données partagées d’une animation globale
        - [ ]  déplacer speed/frame/timer dans un état instance (par AnimPlayer)
        - [ ]  vérifier que 2 entités peuvent jouer la même anim avec des vitesses différentes sans interférence

    - [ ]  **ST-002 Sécuriser Play contre les nulls**
        - [ ]  ajouter les garde-fous quand aucune animation courante n’existe
        - [ ]  couvrir les cas premier Play, changement de skin, interruption
        - [ ]  valider qu’aucune NullReference n’apparaît en logs

    - [ ] **ST-003 Recalculer les priorités après chargement de data**
        - [x]  reindexer automatiquement les priorités après remplacement de la liste chargée
        - [ ]  garantir la stabilité du tri des priorités
        - [ ]  tester avant/après save-load avec pile identique

    - [ ] **ST-004 Rendre le fallback orientation déterministe sans récursion fragile**
        - [ ]  remplacer la récursion par une stratégie de fallback explicite
        - [ ]  définir un ordre de fallback unique et documenté
        - [ ]  tester toutes les directions avec des sets d’orientations incomplets


- [ ] **Intégrité de la Data & Cycle de vie**
    - [ ]  **ST-005 Corriger les copies profondes de Anim**
        - [ ]  copier sprites_paths et sprites_durations en deep copy
        - [ ]  vérifier qu’un variant n’altère jamais l’animation source
        - [ ]  ajouter un test qui détecte toute mutation croisée

	- [ ]  **ST-006 Durcir la génération de variants**
        - [ ]  garantir que la génération ne modifie jamais les datas de base
        - [ ]  valider les correspondances spritesheet base/variant avec erreurs explicites
        - [ ]  ajouter une vérification d’intégrité avant/après génération

	- [ ]  **ST-007 Sécuriser le cycle de vie des subscriptions AnimLayer**
        - [ ]  gérer proprement enable/disable/destroy/reassign/pooling
        - [ ]  empêcher double subscribe et fuite d’event
        - [ ]  tester 1000 cycles assign/unassign sans callback fantôme


- [ ] **Tooling & Editor etc**
	- [ ]  **ST-008 Ajouter un validateur éditeur**
        - [ ]  lister skins/capacités/orientations manquantes
        - [ ]  détecter noms invalides et chemins sprites cassés
        - [ ]  détecter doublons de clés et incohérences de config
        - [ ]  produire un rapport lisible pour correction rapide

	- [ ]  **ST-009 Nettoyer la politique de logs**
        - [ ]  retirer les logs lourds par défaut au démarrage
        - [ ]  garder un mode debug explicite activable
        - [ ]  vérifier que la release n’est pas polluée


- [ ] **Testing & Perfs**
	- [ ]  **ST-010 Ajouter une suite de tests automatiques**
        - [ ]  tests pile/priorités/one-shot/lock orientation
        - [ ]  tests fallback orientation
        - [ ]  tests save-load cohérence des priorités
        - [ ]  tests non-régression sur variants

	- [ ]  **ST-011 Créer une scène benchmark/soak**
        - [ ]  scène de charge avec grand nombre d’entités animées
        - [ ]  exécution soak 30 minutes minimum
        - [ ]  collecte des métriques frame time/GC/exceptions

	- [ ]  **ST-012 Fixer et valider les budgets perf**
        - [ ]  définir budget CPU animation cible
        - [ ]  imposer objectif zéro allocation/frame en régime normal
        - [ ]  valider budgets sur machine cible
        - [ ]  refuser merge en cas de régression mesurée


- [ ] **Validation de la version finale**
	- [ ]  **ST-013 Critères de sortie S-tier**    
        - [ ]  tous les ST-001 à ST-007 validés
        - [ ]  validateur éditeur sans erreur critique
        - [ ]  tests auto verts sur 2 runs consécutifs
        - [ ]  soak test sans exception
        - [ ]  budgets perf respectés