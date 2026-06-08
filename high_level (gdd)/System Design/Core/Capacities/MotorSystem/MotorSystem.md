#system #designing

- [x] [[MotorSystem_Proto]]
- [x] [[MotorSystem_Rework_1]]


---
# description

**MotorSystem** s'occupe de gérer la réalisation (musculaire un peu) du plan d'actions des entités, loadées ou non. Il s'occupe aussi de pooler correctement les components **GOAP** des entités loadées, et gère les entités unloadées en batch.

Il fait donc le lien avec le **GOAP** system asset. ([[External Assets & Plugins]])

Il ne gère PAS le planning/switching des goals qui lui est réalisé dans [[BrainSystem]]

---
# fonctionnement du système

**MotorSystem** a 3 composants principaux :
- [MotorData] qui est la data utile au système (inhérite de [CapacityData])
- [MotorCapacity] qui inhérite de [Capacity]
- [MotorEngine] qui gère le backend
- (pas besoin de [MotorBank / MotorPooler] car le pooling des capacity et gérée par [[CapacitySystem]])

Chaque entité voit son goap updaté selon 2 routes distinctes QUI NE DOIVENT JAMAIS SE CHEVAUCHER :
- entitée loadée : goap normal
- entitée unloadée : goap custom via [MotorEngine]

### 1. MotorEngine

[MotorEngine] gère les entités unloadées. Elle récupère les entités qui s'unload et les ajoute à sa liste pour bien les gérer. De même, lorsqu'une entité est loadée, elle l'enlève de sa liste. Pour cela elle register les callbacks du [CapableSystem]

Ensuite elle fait tourner le goap system en batch pour toutes les entités unloadées. Pour ça il a 3 sous systèmes qui sont des Monobehaviours :
- **BatchActionProvider** :
	- équivalent GoapActionProvider mais batch
- **BatchActionAchiever** :
	- équivalent AgentBehaviour mais batch
	- fait touner manuellement les **Actions** & **Sensors** pour les entités unloadées
- **BatchGoToBehaviour** :
	- simule les déplacements des entités à un rate défini


### 2. MotorData

[MotorData] gère toute la data d'un seul agent, nécessaire au bon déroulement de ces actions/sensors. inhérite de [CapacityData] et stocke toute la data nécessaire :
- goal request / goal courant
- ~~plan courant / action courante~~
- ~~runtime action (timers, progression, cooldowns)~~
	- > pas besoin de ces trucs finalement étant donné qu'on transforme automatiquement les goals en action
- target unifié (target_id + position snapshot, pas seulement Transform)
- suivi movement (distance restante / délai / fractionnement)
	- > réellement besoin de ça ?
- **AvoidanceData** pour le goto



### 3. MotorCapacity

Ensuite pour chaque entité **LOADEE** on a une [MotorCapacity] qui remplace le [[Brain]] actuel et qui sert d'[Object]. [MotorCapacity] connecte AgentBehaviour + GoapActionProvider + GoToBehaviour, etc

Pour ces entités loadées, les **Actions** & **Sensors** & **Déplacement** sont gérés avec la route normale du **GOAP** system

### 4. Transition loaded <-> unloaded

**Transition loaded <-> unloaded** :
- loaded -> unloaded : stop action sans resolve, sync MotorData, convertir targets scene -> target_id/position, désactiver adapter, enqueue resolve unloaded
- unloaded -> loaded : spawn/pool GO, bind MotorCapacity, hard reset Agent/Provider, rehydrate MotorData, request resolve

**Hard Reset conseillé quand [MotorCapacity] se load (ou s'unload)** :
- [x] StopAction(false)
- [x] ActionState.Reset()
- [x] Initialize() agent
- [x] reassign AgentType
- [x] clear WorldData local
- [ ] clear disablers/actions disabled
- [x] re-request goals


### .

---
# problèmes actuels

- problème [unloadé] : comment on gère la validation “arrivée à destination” pour les entités unloadées ?
	- en mode loadé c'est basé distance/position (souvent via Transform/target position).
	- en mode unloadé il faut un équivalent virtuel (position data + règle IsInRange) dans l'execution batch.
- [x] problème de [pooling] :
	- [x] risque principal pooling : refs/timers/events/goalrequest stale => hard reset obligatoire au rebind.

- [ ] problème de [spawning] :
	- [ ] j'ai l'impression que les mobs, lors du spawn, ont une position égale à 0,0, ce qui fait que leurs sensors font un premier sensing en 0,0, ce qui est illogique à balle



---
# todo

- [ ] faire un 1er jet de [BatchActionAchiever] qui :
	- [ ] BatchGoToBehaviour
	- [ ] reçoit des actions
	- [ ] récupère la target
	- [ ] move jusqu'à la target
	- [ ] quand l'action est terminée, re s'enregistre pour resolve
- [ ] tester avec une action idle de [WanderGoal] qui permet de voir si les entités se déplacent bien sur la map + gérer la transition loadé / unloadé


- [x] bug d'[Avoidance System] : certains mobs gardent leur avoidance enorme longtemps ce qui les empechent d'atteindre leur destination > ce qui les bloque dans une [Action] infinie, relou

- [x] fix null ref exception bug [AttackAction] line 59