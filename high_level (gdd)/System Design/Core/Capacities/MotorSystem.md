#system #designing

- [ ] [[MotorSystem_Proto]]


---
# description

**MotorSystem** s'occupe de gérer la réalisation (musculaire un peu) du plan d'actions des entités, loadées ou non. Il s'occupe aussi de pooler correctement les components **GOAP** des entités loadées, et gère les entités unloadées en batch.

Il fait donc le lien avec le **GOAP** system asset. ([[External Assets & Plugins]])

Il ne gère PAS le planning/switching des goals qui lui est réalisé dans [[BrainSystem]]

---
# fonctionnement du système


[MotorEngine] garde en tête les data qui sont loadées ou non, et décide le mode de **sensorisation / déplacement / réalisation des actions**.
Il a 2 sous systèmes qui sont des Monobehaviours :
- **BatchActionProvider** : équivalent GoapActionProvider mais batch (résout des paquets d'entités)
- **BatchActionAchiever** : équivalent AgentBehaviour mais batch (fait tourner les actions/timers)

Les **Actions** du goap system transmettent leurs callbacks vers une interface **Actionnable** (ou backend) récupérée selon mode loadé/unloadé :
- si loadé : comportement Mono normal
- si unloadé : manip data pure (hp, inventaire, states, timers, etc)

Les **Sensors** idem :
- si loadé : colliders / scene
- si unloadé : queries systèmes (RoomSystem / CapableSystem / index monde)

Le **Déplacement** est splitté en 2 :
- si loadé : [[GoToBehaviour]]
- si unloadé : simulation déplacement (délai + fractionnement + update position data)




[MotorData] gère toute la data d'un seul agent, nécessaire au bon déroulement de ces actions/sensors. inhérite de [CapacityData] et stocke toute la data nécessaire :
- goal request / goal courant
- plan courant / action courante
- runtime action (timers, progression, cooldowns)
- target unifié (target_id + position snapshot, pas seulement Transform)
- suivi movement (distance restante / délai / fractionnement)




Ensuite pour chaque entité **LOADEE** on a une [MotorCapacity] qui remplace le [[Brain]] actuel et qui sert d'[Object]. [MotorCapacity] connecte AgentBehaviour + GoapActionProvider + GoToBehaviour, etc

On a donc deux routes de GOAP distinctes en fonction de si l'entité est loadée ou non. **Règle critique** : 1 seule ownership à la fois (jamais double simulation loaded+unloaded en même temps).

**Transition loaded <-> unloaded** :
- loaded -> unloaded : stop action sans resolve, sync MotorData, convertir targets scene -> target_id/position, désactiver adapter, enqueue resolve unloaded
- unloaded -> loaded : spawn/pool GO, bind MotorCapacity, reset dur Agent/Provider, rehydrate MotorData, request resolve

**Hard Reset conseillé quand [MotorCapacity] se load (ou s'unload)** :
- StopAction(false)
- ActionState.Reset()
- Initialize() agent
- reassign AgentType
- clear WorldData local
- clear disablers/actions disabled
- re-request goals



pas besoin de [MotorBank / MotorPooler] si [MotorCapacity] est une capacity et gérée par [[CapacitySystem]].


---
# problèmes actuels

- validation “arrivée à destination” : en mode loadé c'est basé distance/position (souvent via Transform/target position).
	- en mode unloadé il faut un équivalent virtuel (position data + règle IsInRange) dans l'execution batch.
- risque principal pooling : refs/timers/events/goalrequest stale => hard reset obligatoire au rebind.
- perf : prévoir budget de resolve batch + fairness + logs debug (goal demandé, action choisie, backend utilisé, raison no-plan).



---
# todo
- [ ] 