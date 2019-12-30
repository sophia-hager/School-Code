from EnemyPokemon import enemyPokemon
from OwnPokemon import ownPokemon
from StatMoves import * 
from DamageMoves import *
from random import choice
from PokeList import chooseFighter
import time
from Animation import Animation


#REFERENCES:
#https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/ - used to figure out how to return multiple values
#Bulbapedia - used to figure out how to calculate damage, health and for move data
#Pokemondb.net - used to find base stats and for sprites
#graphics.py by John Zelle- used for graphics
#Final Pam easter egg referencing the Fallout 4 Monster Factory videos by Polygon.com (sprite taken from one of those videos)
try:
    keep_going = True
    while keep_going != False:
        turn = 0 #sets turn order = 0
        win_checker = 0 #nobody has won
        game_animation = Animation() #creates an animation
        levels_list = game_animation.getLevels() #chooses levels
        your_level = levels_list[0]
        enemy_level = levels_list[1]
        pam_variable = game_animation.getPam() #checks if easter egg was activated
        selection = game_animation.chooseYourFighter() #chooses pokemon
        two_pokemon =chooseFighter(selection, your_level, enemy_level, pam_variable) #gets the pokemon back and defines them
        your_pokemon =two_pokemon[0] 
        enemy_pokemon =two_pokemon[1]
        your_pokemon_name = your_pokemon.getName() #gets pokemon data
        enemy_pokemon_name = enemy_pokemon.getName()
        your_pokemon_type = your_pokemon.getType()
        enemy_pokemon_type = enemy_pokemon.getType()



        game_animation.clearWindow() #clears the window
        game_animation.displayText("Wild {0} appeared!".format(enemy_pokemon_name)) #displays the string
        game_animation.enemyAppear(enemy_pokemon) #sends out enemy pokemon
        game_animation.displayText("Go! {0}!".format(your_pokemon_name)) 
        game_animation.sendOut(your_pokemon) #sends out your pokemon

        while win_checker ==0: #while nobody has won
            if turn%2 ==0: #on your turn:
                opponentdefense = enemy_pokemon.getDefenseStat() #gets opponent defense
                attack_list = your_pokemon.Attack(enemy_pokemon_type, enemy_pokemon_name, opponentdefense, game_animation) #gets data from attack function and separates them
                attack_style = attack_list[0]
                attack_data = attack_list[1]
                attack_type = attack_list[2]
                attack_sort = attack_list[3]
                game_animation.playerAttack(attack_type, attack_sort) #animates the attack
                if attack_style == "attack": #if damage attack:
                    enemy_pokemon.getHitDam(attack_data) #reduces health
                    game_animation.lowerOpponentHealth(enemy_pokemon.getHealth()) #animates health
                else:
                    enemy_pokemon.getHitStat(attack_data, game_animation)#gets hit with stat attack
                win_checker = enemy_pokemon.checkHealth(game_animation) #checks for win
                

            else:
                opponentdefense = your_pokemon.getDefenseStat() #gets your defense
                attack_list = enemy_pokemon.Attack(your_pokemon_type, your_pokemon_name, opponentdefense, game_animation) #gets data from attack function, seaparates them
                attack_style = attack_list[0]
                attack_data = attack_list[1]
                attack_type = attack_list[2]
                attack_sort = attack_list[3]
                game_animation.opponentAttack(attack_type, attack_sort) #animates the attack
                if attack_style == "attack":
                    your_pokemon.getHitDam(attack_data) #reduces heatlh
                    game_animation.lowerPlayerHealth(your_pokemon.getHealth()) #animates health
                else:
                    your_pokemon.getHitStat(attack_data, game_animation) #reduces stats
                win_checker = your_pokemon.checkHealth(game_animation)#checks for win
                

            turn = turn+1 #changes turn
        if win_checker == 1: #if you win:
            game_animation.opponentFaint() #opponent faints
            game_animation.displayText("Congratulations! You won!") 
        if win_checker == -1:
            game_animation.playerFaint()#you faint
            game_animation.displayText("Sorry, you lost.")
        game_animation.displayInstruction ("Press ENTER to replay or any other key to close the window.")
        window = game_animation.getWin() #gets the window
        key = window.getKey() #gets a key press
        if key == "Return": #if it is enter
            keep_going = True #keeps playing
        else: #otherwise ends loop
            keep_going = False 
        game_animation.closeWin()#closes window
except Exception:
    print("Window was closed prematurely!") #if window is closed and an exception is raised, terminates program and gives a message explaining why
        


