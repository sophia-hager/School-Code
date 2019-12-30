from AttackClasses import statAttack

# a list of stat moves


#ground
sand_attack = statAttack(1, "ground", "accuracy", "Sand Attack",15, "environment")
#normal
leer = statAttack(1, "normal", "defense", "Leer",30, "self" )
growl = statAttack(1, "normal", "attack", "Growl", 40, "self")
tail_whip = statAttack(1, "normal", "defense", "Tail Whip", 30, "self")
#fire
smokescreen = statAttack(1, "fire", "accuracy", "Smokescreen", 20, "environment")
#water
#grass
#rock
#psychic
#poison
#fighting
#flying
defog = statAttack(200, "flying", "accuracy", "Defog", 15, "environment")
#electric
