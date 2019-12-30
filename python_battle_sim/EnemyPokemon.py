import random
from TypeChecker import typeCheck
from AttackClasses import damageAttack, statAttack
import Animation

class enemyPokemon():
    
    def __init__(self, name, pokemon_type, health, level, move_list, attack_stat, defense_stat, sprite_name):
        self.name = name #initializes name and type
        self.type = pokemon_type
        self.max_health = round((((health+ random.randint(0,31)*2)*level)/100)+level + 10) #initializes max health from the listed formula
        self.health = self.max_health #initializes current health
        self.level = level #initializes level
        self.movelist_length = len(move_list)-1 #finds the movelist length, -1 to compensate for list iteration
        self.attack1_number = random.randint(0, self.movelist_length) # generates a number that corresponds to the first attack
        self.attack2_number = random.randint(0, self.movelist_length) #generates a number that corresponds to the second attack
        while self.attack2_number == self.attack1_number: # if it is the same as the first, retries until it gets a unique number
            self.attack2_number = random.randint(0, self.movelist_length) 
        self.attack3_number = random.randint(0, self.movelist_length) #repeats for the other moves
        while self.attack3_number == self.attack1_number or self.attack3_number == self.attack2_number:
            self.attack3_number = random.randint(0, self.movelist_length)
        self.attack4_number = random.randint(0, self.movelist_length)
        while self.attack4_number == self.attack1_number or self.attack4_number == self.attack2_number or self.attack4_number == self.attack3_number:
            self.attack4_number = random.randint(0, self.movelist_length)
        self.attack1 = move_list[self.attack1_number] #sets attacks using the random number
        self.attack2 = move_list[self.attack2_number]
        self.attack3 = move_list[self.attack3_number]
        self.attack4 = move_list[self.attack4_number]
        self.move_list = [self.attack1, self.attack2, self.attack3, self.attack4] #creates a list of the pokemon's moves
        self.attack = round((((attack_stat+ random.randint(0,31)*2)*level)/100)+5) #this is the formula for attack, ignoring EVs.
        self.defense = round((((defense_stat+ random.randint(0,31)*2)*level)/100)+5) #this is the formula for defense, ignoring EVs.
        self.accuracy = 100 #starts out the pokemon's inherent accuracy at 100.
        self.attack_reduction_counter = 0 #counts how many times attack/defense have been reduced.
        self.defense_reduction_counter = 0
        self.sprite = sprite_name #gets a sprite
        
    def getHealth(self):
        #print("Foe", self.name, "has", self.health, "HP remaining.") #prints out the amount of health remaining
        return self.health
    
    def getName(self): #returns name, type, defense stat
        return self.name
    def getSprite(self):
        return self.sprite
    
    def getType(self):
        return self.type
                             
    def getDefenseStat(self):
        return self.defense

    def Attack(self, opponent_type, opponent_name, opponent_defense, animation): # a function to attack a pokemon.
        self.pp_list = []
        for move in self.move_list:
            checker = move.checkPP()
            self.pp_list.append(checker)
        if True not in self.pp_list: #if all moves out of pp
            self.used_attack = struggle #uses struggle automatically
        else:
            self.used_attack = random.choice([self.attack1, self.attack2, self.attack3, self.attack4]) #picks an attack
            self.used_attack_possible =   self.used_attack.checkPP() #checks PP
            while self.used_attack_possible == False: #if the move is out of PP:
                self.used_attack = random.choice([self.attack1, self.attack2, self.attack3, self.attack4]) #picks an attack
                self.used_attack_possible =   self.used_attack.checkPP() #checks PP again
            self.used_attack.reducePP() #reduces the PP by one
        self.used_attack_name = self.used_attack.getName() #gets name of attack
        self.kind = self.used_attack.getKind() #looks for the kind of attack
        self.sort = self.used_attack.getSort()
        if self.kind == "attack": #if the attack causes damage...
            self.attack_accuracy = self.used_attack.getAcc() #finds move accuracy
            animation.displayText("Foe {0} used {1}!".format(self.name, self.used_attack_name)) # prints used attack
            self.attack_chance = 100*(self.attack_accuracy) * (self.accuracy/100) #calculates chance of hitting and randomly decides
            self.attack_chance = round(self.attack_chance)
            self.attack_shot = random.randint(1,100)
            if self.attack_shot in range(1, self.attack_chance+1): # if the attack hits...
                self.attack_type = self.used_attack.getType() #gets remaining stats and finds the move effectiveness
                self.attack_power = self.used_attack.getPower()
                self.move_effectiveness = (typeCheck(self.attack_type, opponent_type))
                if self.move_effectiveness == 0: #if immune, says so
                    animation.displayText("It doesn't affect {0}...".format(opponent_name))
                    return ["attack", 0 ,self.attack_type, None] #returns type and damage
                elif self.move_effectiveness == 2: #if it's super effective, says so
                    animation.displayText("It's super effective!")
                    self.damage = (((((((2*self.level)/5)+2)*(self.attack/opponent_defense)*self.attack_power)/50)+2)*self.move_effectiveness) #calculates damage
                    self.damage = round(self.damage)
                    return ["attack", self.damage,self.attack_type, self.sort] #returns type and damage
                elif self.move_effectiveness == .5: #if not effective, says so
                    animation.displayText("It's not very effective...")
                    self.damage = (((((((2*self.level)/5)+2)*(self.attack/opponent_defense)*self.attack_power)/50)+2)*self.move_effectiveness) #calculates damage
                    self.damage = round(self.damage)
                    return ["attack", self.damage,self.attack_type, self.sort] #returns type and damage
                else:
                    self.damage = (((((((2*self.level)/5)+2)*(self.attack/opponent_defense)*self.attack_power)/50)+2)*self.move_effectiveness) #calculates damage
                    self.damage = round(self.damage)
                    return ["attack", self.damage,self.attack_type, self.sort] #returns type and damage
            else: #if it misses, returns 0
                animation.displayText("The attack missed!") 
                self.damage = 0
                return ["attack", self.damage, self.attack_type, None] #returns attack and 0
            
        elif self.kind == "stat":                           #If it reduces stat....
            
            self.attack_accuracy = self.used_attack.getAcc() #finds move accuracy
            animation.displayText("Foe {0} used {1}!".format(self.name, self.used_attack_name)) #prints used attack
            self.attack_chance = 100*self.attack_accuracy * self.accuracy #calculates accuracy and randomly decides
            self.attack_shot = random.randint(1,100)
            if self.attack_shot in range(1, self.attack_chance+1): #if the attack hits....
                self.attack_type = self.used_attack.getType()
                self.stat_attacked = self.used_attack.getStat()
                self.move_effectiveness = typeCheck(self.attack_type, opponent_type) #finds if it is immune
                if self.move_effectiveness == 0:                            #if it is....
                    animation.displayText("It doesn't affect {0}...".format(opponent_name)) # says so, returns no reduction
                    self.reduction = "none"
                    return ["stat", self.reduction, self.attack_type, None] 
                else:
                    if self.stat_attacked == "accuracy": #returns accuracy if that is what it attacks
                        self.reduction = "accuracy"
                        return ["stat", self.reduction,self.attack_type, self.sort]
                    elif self.stat_attacked == "attack": #returns attack
                        self.reduction = "attack"
                        return ["stat", self.reduction,self.attack_type, self.sort]
                    elif self.stat_attacked == "defense": #returns defense
                        self.reduction = "defense"
                        return ["stat", self.reduction, self.attack_type, self.sort]
            else: #if it misses, returns 0
                animation.displayText("The attack missed!") 
                self.reduction = "none"
                return ["stat", self.reduction, self.attack_type, None] #returns none
                    
    def getHitDam(self, damage):
        self.health = self.health - damage #changes health from damage
        
    def getHitStat(self, reduction, animation): #reduces the stat of a pokemon

        if reduction == "accuracy": # if accuracy, reduces accuracy
            if self.accuracy >= 60: #if accuracy is above a threshold, reduces accuracy
                self.accuracy = self.accuracy - 5
                animation.displayText("Foe {0}'s accuracy went down!".format(self.name))
            else:
                animation.displayText("Foe {0}'s accuracy won't go any lower!".format(self.name)) #otherwise, prints the message
        elif reduction == "attack":
            if self.attack_reduction_counter <6: #can only be reduced 5 times successfully
                self.attack = self.attack - 3
                animation.displayText("Foe {0}'s attack went down!".format(self.name))
                self.attack_reduction_counter = self.attack_reduction_counter + 1
            else:
                animation.displayText("Foe {0}'s attack won't go any lower!".format(self.name))
        elif reduction == "defense":
            if self.attack_reduction_counter <6: #can only be reduced 5 times successfully
                self.defense = self.defense - 3
                animation.displayText("Foe {0}'s defense went down!".format(self.name))
                self.defense_reduction_counter = self.defense_reduction_counter + 1
            else:
                animation.displayText("Foe {0}'s defense won't go any lower!".format(self.name))

    def checkHealth(self, animation): #checks health
        if self.health > 0:
            self.win_checker = 0 #if your health is greater than 0, nothing happens
        else:
            animation.displayText("Foe {0} fainted!".format(self.name)) #returns 1 and a fun message
            self.win_checker = 1
        return self.win_checker
            
