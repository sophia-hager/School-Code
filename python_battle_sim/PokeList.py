from EnemyPokemon import enemyPokemon
from OwnPokemon import ownPokemon
from StatMoves import * 
from DamageMoves import *
import random

def chooseFighter(selection, your_level, enemy_level, pam_variable):

    #creates a list of pokemon
    your_bulbasaur = ownPokemon("Bulbasaur", "grass", 45, your_level, grass_moveset, 49, 49, "Sprites/bulbasaur_back.png") #creates classes of pokemon at that level
    your_charmander = ownPokemon("Charmander", "fire", 39, your_level, fire_moveset, 43, 52, "Sprites/charmander_back.png")
    your_squirtle = ownPokemon("Squirtle", "water", 44, your_level, water_moveset, 48, 65, "Sprites/squirtle_back.png")
    your_sandshrew = ownPokemon("Sandshrew", "ground", 50, your_level, ground_moveset, 75, 85, "Sprites/sandshrew_back.png")
    your_pidgey = ownPokemon("Pidgey", "flying", 40, your_level, flying_moveset, 45, 40, "Sprites/pidgey_back.png")
    your_pikachu = ownPokemon("Pikachu", "electric", 35, your_level, electric_moveset, 55, 40, "Sprites/pikachu_back.png")
    your_caterpie = ownPokemon("Caterpie", "bug", 45, your_level, bug_moveset, 30, 35, "Sprites/caterpie_back.png")
    your_mankey = ownPokemon("Mankey", "fighting", 40, your_level, fighting_moveset, 80, 35, "Sprites/mankey_back.png")
    your_meowth = ownPokemon("Meowth", "normal", 40, your_level, normal_moveset, 45, 35, "Sprites/meowth_back.png")
    your_ekans = ownPokemon("Ekans", "poison", 35, your_level, poison_moveset, 60, 44, "Sprites/ekans_back.png")
    your_mr_mime = ownPokemon("Mr. Mime", "psychic", 40, your_level, psychic_moveset, 45, 65, "Sprites/mr_mime_back.png")
    your_geodude = ownPokemon("Geodude", "rock", 40, your_level, rock_moveset, 80, 100, "Sprites/geodude_back.png")
    
    allyList = [your_bulbasaur, your_charmander, your_squirtle, your_sandshrew, your_pidgey, your_pikachu, your_caterpie, your_mankey, your_meowth, your_ekans, your_mr_mime, your_geodude] 
    your_pokemon = allyList[selection] #finds the pokemon previously selected

    if pam_variable== False: #if easter egg not activated
        #list of enemy pokemon

        bulbasaur = enemyPokemon("Bulbasaur", "grass", 45, enemy_level, grass_moveset, 49, 49,"Sprites/bulbasaur_front.png") #creates classes of enemy pokemon
        charmander = enemyPokemon("Charmander", "fire", 39, enemy_level, fire_moveset, 43, 52,"Sprites/charmander_front.png")
        squirtle = enemyPokemon("Squirtle", "water", 44, enemy_level, water_moveset, 48, 65,"Sprites/squirtle_front.png")
        sandshrew = enemyPokemon("Sandshrew", "ground", 50, enemy_level, ground_moveset, 75, 85,"Sprites/sandshrew_front.png")
        pidgey = enemyPokemon("Pidgey", "flying", 40, enemy_level, flying_moveset, 45, 40,"Sprites/pidgey_front.png")
        pikachu = enemyPokemon("Pikachu", "electric", 35, enemy_level, electric_moveset, 55, 40,"Sprites/pikachu_front.png")
        caterpie = enemyPokemon("Caterpie", "bug", 45, enemy_level, bug_moveset, 30, 35,"Sprites/caterpie_front.png")
        mankey = enemyPokemon("Mankey", "fighting", 40, enemy_level, fighting_moveset, 80, 35,"Sprites/mankey_front.png")
        meowth = enemyPokemon("Meowth", "normal", 40, enemy_level, normal_moveset, 45, 35,"Sprites/meowth_front.png")
        ekans = enemyPokemon("Ekans", "poison", 35, enemy_level, poison_moveset, 60, 44,"Sprites/ekans_front.png")
        mr_mime = enemyPokemon("Mr. Mime", "psychic", 40, enemy_level, psychic_moveset, 45, 65, "Sprites/mr_mime_front.png")
        geodude = enemyPokemon("Geodude", "rock", 40, enemy_level, rock_moveset, 80, 100, "Sprites/geodude_front.png")
        enemyList = [bulbasaur, charmander, squirtle, sandshrew, pidgey, pikachu, caterpie, mankey, meowth, ekans, mr_mime] #a list of pokemon 
        enemy_pokemon = random.choice(enemyList) #randomly chooses one
    else:
        pam = enemyPokemon("The Final Pam", "pam", 9000, 10000, pam_moveset, 10000, 10000, "Sprites/pam_sprite_front.png")
        enemy_pokemon = pam #if activated, pam is activated

    return[your_pokemon, enemy_pokemon] #returns the pokemon that were chosen

    
    
    







