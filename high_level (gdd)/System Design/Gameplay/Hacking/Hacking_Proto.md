

les mécaniques de hacking apparaissent dans le jeu au **-3** après la rencontre avec **[[qwin]]** et l'arrivée du [[Laptop]]. Tout d'abord
# **[[Module]]**

- hdd : [[Module_HDD]]
- cpu : [[Module_CPU]]
- network : [[Module_Network]]

# **Exploits**

- password bypasser :        
	- [x] bruteforce
	- [x] dictionary_attack
	- [x] rainbow_table

- damage exploits :
	- [x] cpu_overheat
	- [x] cpu_melt

- network exploits :
    - [ ] ddos

- control exploits :
	- [ ] trojan
	- [ ] cyborg_puppet
	- [ ] backdoor


















#### -- ideas --


1) early game

bruteforce – simple key guessing
dictionary_attack – optimized brute force using common patterns
buffer_overflow – memory corruption attack
cpu_overflow – saturates processor with useless operations
port_flood – floods a network port
ddos – distributed attack overload
keylogger – captures input remotely

backdoor – hidden access point (place un tunnel caché qui fait en sorte que les prochains trojan sont instantannés)
keylogger – captures input remotely (récupère automatiquement les mots de passe tapés)
trojan - takes over (prend le contrôle de la machine -> permet de lancer des hacks depuis cette machine)

2) mid game (more technical)

rowhammer – RAM bit-flipping attack
cache_poison – corrupts CPU cache entries
heap_spray – fills memory to manipulate execution flow
side_channel – extracts data from timing/power behavior
syn_flood – network handshake overload


3) late game (famous world ones)

spectre – speculative execution vulnerability
meltdown – privileged memory reading
stuxnet – sabotage-oriented worm
eternalblue – SMB protocol exploit
heartbleed – SSL data leak
wannacry – ransomware propagation