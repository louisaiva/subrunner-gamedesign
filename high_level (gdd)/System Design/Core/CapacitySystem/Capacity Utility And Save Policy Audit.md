
## title: Capacity Utility And Save Policy Audit  
date: 2026-03-14  
project: subrunner

## Key Conclusions

1. Yes, your instinct is right: Grab, Drop, Open, Close, and Die are mostly runtime-action capacities.
2. Open/Close and OnOff should not save state inside those capacities. The durable state belongs to the owner entities (Chest/Door/Computer), not the action capacity.
3. GrabCapacity looks close to removable as a capacity (very low coupling in code).
4. The biggest missing save risks today are not Grab/Drop/Open/Close. They are:

- Toggle on/off state
- Device storage contents (StoreCapacity files/keys/exploits)
- AI continuity state (Eat hunger, Sleep asleep/timer) if you unload mobs
- Optional if you want offline hacking continuity: Hack/Process/Connect progress

## Full Capacity Audit

### Mob Capacities

|Capacity|Utility|Save Data?|Keep As Capacity?|Recommendation|
|---|---|---|---|---|
|HealthCapacity|High|Yes|Yes|Keep. Save current health and any mutable runtime health state.|
|WalkCapacity|High|No|Yes|Runtime movement controller only.|
|RunCapacity|Medium|No|Maybe|Could merge into Walk as sprint mode to reduce component count.|
|InteractCapacity|High|No|Yes|Runtime proximity/hover selection state should not persist.|
|GrabCapacity|Low|No|No|Remove capacity and route directly to Inventory.Grab in interaction flow.|
|DropCapacity|Medium-High|No|Yes (for now)|Keep for now due current UI/gameplay coupling; runtime-only.|
|EatCapacity|High for AI|Conditional Yes|Yes|Save hunger only if unloaded AI continuity matters.|
|SleepCapacity|Medium-High for SleepingCat|Conditional Yes|Maybe|Save asleep/timer only if unloaded AI continuity matters. Could move to SleepingCat-specific logic.|
|TalkCapacity|Medium|No|Maybe|Runtime flavor behavior; can stay or move to Dialogue/Bark component.|
|AttackCapacity|High|No|Yes|Runtime combat action and cooldown state only.|
|DodgeCapacity|Medium|No|Yes|Runtime-only.|
|DieCapacity|High but overstuffed|No|Yes (split)|Keep death trigger ability, but split XP/drop/corpse pipeline into dedicated services.|

### Object And Interaction Capacities

|Capacity|Utility|Save Data?|Keep As Capacity?|Recommendation|
|---|---|---|---|---|
|HoverCapacity|High|Yes|Yes|Keep current collider save behavior.|
|OpenCapacity|Medium|No|Maybe|Merge with Close into one OpenState action or owner method.|
|CloseCapacity|Medium|No|Maybe|Same as Open.|
|ToggleCapacity|Medium|Yes|Yes|Save toggled state if it affects world behavior/visuals.|
|SpawnCapacity|High|Yes (config), No (runtime counters)|Yes|Keep. Save config; entity_count/last_use_time optional.|
|OnOffCapacity|Medium|No|Maybe|Similar to Open/Close: action wrapper only; durable state should live in owner.|

### Device And System Capacities

|Capacity|Utility|Save Data?|Keep As Capacity?|Recommendation|
|---|---|---|---|---|
|ConnectCapacity|High|Optional|Yes|Runtime network graph usually no-save. Save only if hacking graph must persist over unloads.|
|HackCapacity|High|Optional|Yes|Save only if running hacks must continue while unloaded.|
|ProcessCapacity|High|Optional|Yes|Save only if process/core occupancy must continue while unloaded.|
|StoreCapacity|High|Yes|Yes|Must save disk contents and mutable capacity to prevent data loss.|
|TempCapacity|Low-Medium|No|Maybe|Runtime derived value; likely not worth persistent data.|

## What Should Definitely Not Be Saved In Capacity Data

- Grab selected item / input callbacks
- Drop selected item / temporary throw force state
- Interact current hover / waiting list
- Open and close in-progress invoke timing
- Die local counters and temporary teardown state
- Attack/Dodge cooldown internals (unless you explicitly want exact frame-continuity after unload)

## What Should Be Saved (Either In CapacityData Or Owner Data)

- Health current value and mutable health params
- Toggle on/off state
- StoreCapacity disk payload: files, keys, exploits, mutable disk size
- Owner open/power state:
    - Chest/Door is_open and is_moving (or just is_open if you normalize transitions)
    - Computer IsOn and IsMoving
- AI continuity state if doing unloaded simulation:
    - Eat hunger
    - Sleep asleep/sleep_timer/licking_to_do
- Optional advanced continuity:
    - Hack running jobs + progress
    - Process core assignments
    - Connect active graph path

## Over-Complex Or Likely Unnecessary As Separate Capacities

1. GrabCapacity

- Very low real integration and can be replaced by direct inventory grabbing flow.
- Candidate to remove first.

2. OpenCapacity + CloseCapacity

- Two capacities managing one state machine.
- Merge into one state-action module or owner method set.

3. OnOffCapacity

- Same pattern as Open/Close, strongly coupled to Computer behavior.
- Candidate to merge into owner or a generic state-transition helper.

4. DieCapacity

- Useful ability, but currently too many responsibilities in one place.
- Split into DeathTrigger, DeathRewards, DeathDropper, CorpseTransition.

5. RunCapacity

- Optional simplification: fold into WalkCapacity to reduce component overhead.

## Practical Refactor Order

1. Remove GrabCapacity first.
2. Merge Open + Close.
3. Move OnOff logic to owner-level state transition.
4. Add durable save paths for Toggle and Store.
5. Add optional AI continuity save for Eat/Sleep.
6. Split DieCapacity into smaller services.

## Notes Specific To Your Questions

- Open/Close: runtime-only action capacities, yes.
- Grab/Drop: runtime-only, yes.
- Die: runtime-only in terms of capacity data, yes. The durable outcome (dead entity/corpse/state) must still be saved elsewhere.
- You are correct that several capacities currently add complexity without strong value, especially where owner class state already exists.