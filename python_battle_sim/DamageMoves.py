from AttackClasses import damageAttack
from StatMoves import *
import random

#a list of damaging moves
#normal
tackle = damageAttack("normal", 40, 1, "Tackle", 35, "physical")
scratch = damageAttack("normal", 40, 1, "Scratch", 35, "physical")
headbutt = damageAttack("normal" , 70, 1, "Headbutt" , 70, "physical")
facade = damageAttack("normal", 70, 1, "Facade", 20, "physical")
slash = damageAttack("normal", 70, 1, "Slash", 20, "physical")
hyper_voice = damageAttack("normal", 90, 1, "Hyper Voice", 10, "special")
body_slam = damageAttack("normal", 85, 1, "Body Slam", 15, "physical")
struggle = damageAttack("normal", 10, 1, "Struggle", 1000000000000000000, "physical")
#fire
ember = damageAttack("fire", 25, 1, "Ember", 25, "special")
flamethrower = damageAttack("fire", 90, 1, "Flamethrower",15, "special")
fire_punch = damageAttack("fire", 75, 1, "Fire Punch",15, "physical")
fire_blast = damageAttack("fire", 110, .85, "Fire Blast", 5, "special")
fire_fang = damageAttack("fire", 65, .95, "Fire Fang",15, "physical")
flame_burst = damageAttack("fire", 70, 1, "Flame Burst",15, "special")
flame_charge = damageAttack("fire", 50, 1, "Flame Charge", 20, "physical")
#grass
vine_whip = damageAttack("grass", 45, 1, "Vine Whip",25, "physical")
razor_leaf = damageAttack("grass", 55, .95, "Razor Leaf",25, "special")
seed_bomb = damageAttack("grass", 80, 1, "Seed Bomb", 15, "special")
energy_ball = damageAttack("grass", 90, 1, "Energy Ball",10, "special")
#water
water_gun = damageAttack("water", 40, 1, "Water Gun",25, "special")
bubble = damageAttack("water", 40, 1, "Bubble",30, "special")
bubble_beam = damageAttack("water", 65, 1, "Bubble Beam",20, "special")
hydro_pump = damageAttack("water", 110, .8, "Hydro Pump",5, "special")
waterfall = damageAttack("water", 80, 1, "Waterfall",15, "special")
scald = damageAttack("water", 80, 1, "Scald",15, "special")
surf = damageAttack("water", 90, 1, "Surf",15, "special")
water_pulse = damageAttack("water", 60, 1, "Water Pulse",20, "special")
#fighting
mach_punch = damageAttack("fighting", 40, 1, "Mach Punch", 30, "physical")
brick_break = damageAttack("fighting", 75, 1, "Brick Break",15, "physical")
karate_chop= damageAttack("fighting", 50, 1, "Karate Chop",25, "physical")
low_sweep  = damageAttack("fighting", 65, 1, "Low Sweep",20, "physical")
cross_chop = damageAttack("fighting", 100, .8, "Cross Chop",5, "physical")
superpower = damageAttack("fighting", 120, 1, "Superpower", 5, "physical")
#poison
sludge_bomb = damageAttack("poison", 90, 1, "Sludge Bomb",10, "special")
poison_jab = damageAttack("poison", 80, 1, "Poison Jab",20, "physical")
sludge = damageAttack("poison", 65, 1, "Sludge", 20, "special")
sludge_wave = damageAttack("poison", 95, 1, "Sludge Wave",10, "special")
gunk_shot = damageAttack("poison", 120, .8, "Gunk Shot",5, "special")

#rock
rock_slide = damageAttack("rock", 75, .9, "Rock Slide",10,"special")
rock_tomb = damageAttack("rock", 60, .95, "Rock Tomb",15, "special")
rock_throw = damageAttack("rock", 50, .9, "Rock Throw",15, "special")
smack_down = damageAttack("rock", 50, 1, "Smack Down",15, "physical")
stone_edge = damageAttack("rock", 100, .8, "Stone Edge", 5, "physical")
#electric
thunder_punch = damageAttack("electric", 75, 1, "Thunder Punch", 15, "physical")
spark = damageAttack("electric", 65, 1, "Spark", 20, "special")
thunder_shock = damageAttack("electric", 40, 1, "Thunder Shock", 30, "special")
thunderbolt = damageAttack("electric", 90, 1, "Thunderbolt", 15, "special")
thunder = damageAttack("electric", 110, .7, "Thunder", 10, "special")
shock_wave = damageAttack("electric", 60, 200, "Shock Wave",20, "special")
#flying
aerial_ace = damageAttack("flying", 60, 200, "Aerial Ace", 20, "physical")
gust = damageAttack("flying", 40, 1, "Gust",35, "special")
wing_attack = damageAttack("flying", 60, 1, "Wing Attack", 35, "special")
air_slash = damageAttack("flying", 75, .95, "Air Slash", 15, "special")
hurricane = damageAttack("flying", 110, .7, "Hurricane", 10, "special")
# bug
bug_buzz = damageAttack("bug", 90, 1, "Bug Buzz", 10, "special")
u_turn = damageAttack("bug", 70, 1, "U-turn", 20, "special")
silver_wind = damageAttack("bug", 60, 1, "Silver Wind", 5, "special")
signal_beam = damageAttack("bug", 75, 1, "Signal Beam", 15, "special")
bug_bite = damageAttack("bug", 60, 1, "Bug Bite", 20, "physical")
# ground
earthquake = damageAttack("ground", 100, 1, "Earthquake",10, "special")
sand_tomb = damageAttack("ground", 35, .85, "Sand Tomb", 15, "special")
magnitude = damageAttack("ground", random.choice([10, 30,30, 50,50,50,50,70,70,70,70,70,70, 90,90,90,90, 110, 110, 150]), 1, "Magnitude", 30, "special")
bulldoze = damageAttack("ground", 60, 1, "Bulldoze", 20, "physical")
mud_shot = damageAttack("ground", 55, .95, "Mud Shot", 15, "special")
#psychic
psybeam = damageAttack("psychic", 65, 1, "Psybeam", 20, "special")
confusion = damageAttack("psychic", 50, 1, "Confusion", 25, "special")
psychic = damageAttack("psychic", 90, 1, "Psychic", 10, "special")
psycho_cut = damageAttack("psychic", 70, 1, "Psycho Cut", 20, "special")
psyshock = damageAttack("psychic", 80, 1, "Psyshock", 10, "special")
#pam
pam_move = damageAttack("pam", 1000000, 100000, "/killall", 100000, "pam")

normal_moveset = [tackle, scratch, headbutt, facade, slash, hyper_voice, leer, growl, tail_whip, sand_attack, smokescreen, defog]
fire_moveset = [tackle, scratch, ember, flamethrower, fire_punch, fire_blast, fire_fang, flame_burst, flame_charge, tail_whip, growl, leer, smokescreen]
grass_moveset = [tackle, scratch, vine_whip, razor_leaf, seed_bomb, energy_ball, sludge, growl, tail_whip, leer]
water_moveset = [tackle, scratch, water_gun, bubble, bubble_beam, hydro_pump, waterfall, scald, surf, water_pulse, tail_whip, growl, leer]
fighting_moveset = [tackle, scratch, mach_punch, brick_break, karate_chop, low_sweep, cross_chop, superpower, tail_whip, growl, leer]
poison_moveset = [tackle, scratch, sludge_bomb, poison_jab, sludge, sludge_wave, gunk_shot, tail_whip, growl, leer]
rock_moveset = [tackle, scratch, rock_slide, rock_tomb, rock_throw, smack_down, stone_edge, magnitude, tail_whip, growl, leer]
electric_moveset = [tackle, scratch, thunder_punch, spark, thunder_shock, thunderbolt, thunder, shock_wave, tail_whip, growl, leer]
flying_moveset = [tackle, scratch, aerial_ace, gust, wing_attack, air_slash, hurricane, tail_whip, growl, leer, defog]
bug_moveset = [tackle, scratch, bug_buzz, u_turn, silver_wind, signal_beam, bug_bite, razor_leaf, tail_whip, growl, leer]
ground_moveset =[tackle, scratch, earthquake, rock_tomb, sand_tomb, magnitude, bulldoze, mud_shot, tail_whip, growl, leer]
psychic_moveset = [tackle, scratch, psybeam, confusion, psychic, psycho_cut, psyshock, tail_whip, growl, leer]
pam_moveset = [pam_move, pam_move, pam_move, pam_move, pam_move, pam_move, pam_move,]






