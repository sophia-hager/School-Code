import random
from TypeChecker import typeCheck
from AttackClasses import statAttack, damageAttack
import Animation

class ownPokemon():
    
    def __init__(self, name, pokemon_type, health, level, move_list, attack_stat, defense_stat, sprite_name):
        self.name = name #initializes name and type
        self.type = pokemon_type
        self.max_health = round((((health+ random.randint(0,31)*2)*level)/100)+level + 10)#initializes max health from the listed formula
        self.health = self.max_health #initializes current health
        self.level = level #initializes level
        self.movelist_length = len(move_list)-1 #finds the movelist length, -1 to compensate for list iteration
        self.attack1_number = random.randint(0, self.movelist_length) # generates a number that corresponds to the first attack
        self.attack2_number = random.randint(0, self.movelist_length) #generates a number that corresponds to the second attack
        while self.attack2_number == self.attack1_number:  #if it is the same as the first, retries until it gets a unique number
            self.attack2_number = random.randint(0, self.movelist_length)
        self.attack3_number = random.randint(0, self.movelist_length)#repeats for the other moves
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
        self.attack = round((((attack_stat+ random.randint(0,31)*2)*level)/100)+5)#these are the formulas for attack and defense, ignoring EVs.
        self.defense = round((((defense_stat+ random.randint(0,31)*2)*level)/100)+5)
        self.accuracy = 100 #starts out the pokemon's inherent accuracy at 100.
        self.attack_reduction_counter = 0 #counts how many times attack/defense have been reduced.
        self.defense_reduction_counter = 0
        self.sprite = sprite_name #initializes the sprite
        
    def getDefenseStat(self): # gets stats
        return self.defense
    def getSprite(self):
        return self.sprite #returns sprite
    
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getHealth(self):
        return self.health #returns health
    def Attack(self, opponent_type, opponent_name, opponent_defense, animation): # a function to attack a pokemon.
        #self.move_counter = 1 #a variable to number a list
        self.pp_list = []
        for move in self.move_list: # for each move, gets the name and prints it with a number
            #move_name = move.getName()
            checker = move.checkPP()
            self.pp_list.append(checker) #adds to a list of if move is possible or not
            #print("{0}. {1}".format(self.move_counter, move_name))
            #self.move_counter = self.move_counter + 1
        if True not in self.pp_list: #if all moves out of pp
            animation.displayText("All moves out of PP!")
            self.used_attack = struggle #uses struggle automatically
        else:
            self.used_attack = animation.animateChoice(self.move_list[0], self.move_list[1],self.move_list[2],self.move_list[3]) #move choice via animation
            self.used_attack_possible =   self.used_attack.checkPP() #checks pp
            while self.used_attack_possible == False: #if out off pp, says so and chooses other ones
                animation.displayText("Out of PP!")
                self.used_attack = animation.animateChoice(self.move_list[0], self.move_list[1],self.move_list[2],self.move_list[3])
                self.used_attack_possible =   self.used_attack.checkPP()
            self.used_attack.reducePP() #reduces move PP
        self.used_attack_name = self.used_attack.getName() #gets attack name
        self.kind = self.used_attack.getKind() #gets information
        self.sort = self.used_attack.getSort()
        if self.kind == "attack": #if the attack causes damage...
            self.attack_accuracy = self.used_attack.getAcc() #finds move accuracy
            animation.displayText("{0} used {1}!".format(self.name, self.used_attack_name)) # prints used attack
            self.attack_chance = 100*(self.attack_accuracy) * (self.accuracy/100) #calculates chance of hitting and randomly decides
            self.attack_chance = round(self.attack_chance)
            self.attack_shot = random.randint(1,100)
            if self.attack_shot in range(1, self.attack_chance+1): # if the attack hits...
                self.attack_type = self.used_attack.getType() #gets remaining stats and finds the move effectiveness
                self.attack_power = self.used_attack.getPower()
                self.move_effectiveness = (typeCheck(self.attack_type, opponent_type))
                if self.move_effectiveness == 0: #if immune, says so
                    animation.displayText("It doesn't affect foe {0}...".format(opponent_name))
                    return["attack", 0, self.attack_type, None]
                elif self.move_effectiveness == 2: #if it's super effective, says so
                    animation.displayText("It's super effective!")
                    self.damage = (((((((2*self.level)/5)+2)*(self.attack/opponent_defense)*self.attack_power)/50)+2)*self.move_effectiveness) #calculates damage
                    self.damage = round(self.damage)
                    return ["attack", self.damage, self.attack_type, self.sort] #returns damage
                elif self.move_effectiveness == .5: #if not effective, says so
                    animation.displayText("It's not very effective...")
                    self.damage = (((((((2*self.level)/5)+2)*(self.attack/opponent_defense)*self.attack_power)/50)+2)*self.move_effectiveness) #calculates damage
                    self.damage = round(self.damage)
                    return ["attack", self.damage, self.attack_type, self.sort] #returns damage
                else:
                    self.damage = (((((((2*self.level)/5)+2)*(self.attack/opponent_defense)*self.attack_power)/50)+2)*self.move_effectiveness) #calculates damage
                    self.damage = round(self.damage)
                    return ["attack", self.damage, self.attack_type, self.sort] #returns damage
            else: #if it misses, returns 0
                animation.displayText("The attack missed!") 
                self.damage = 0
                return ["attack", self.damage, self.used_attack.getType(), None]
        elif self.kind == "stat":                                                       #If it reduces stat....
            self.attack_accuracy = self.used_attack.getAcc() #finds move accuracy
            animation.displayText("{0} used {1}!".format(self.name, self.used_attack_name)) #prints used attack
            self.attack_chance = 100*self.attack_accuracy * self.accuracy #calculates accuracy and randomly decides
            self.attack_shot = random.randint(1,100)
            if self.attack_shot in range(1, self.attack_chance+1): #if the attack hits....
                self.attack_type = self.used_attack.getType()
                self.stat_attacked = self.used_attack.getStat()
                self.move_effectiveness = typeCheck(self.attack_type, opponent_type) #finds if it is immune
                if self.move_effectiveness == 0:                            #if it is....
                    animation.displayText("It doesn't affect foe {0}...".format(opponent_name)) # says so, returns no reduction
                    self.reduction = "none"
                    return ["stat", self.reduction, self.attack_type, None]
                else:
                    if self.stat_attacked == "accuracy": #for each stat, finds accuracy, gets hit, etc.
                        self.reduction = "accuracy"
                        return ["stat", self.reduction, self.attack_type, self.sort]
                    elif self.stat_attacked == "attack":
                        self.reduction = "attack"
                        return ["stat", self.reduction, self.attack_type, self.sort]
                    elif self.stat_attacked == "defense":
                        self.reduction = "defense"
                        return ["stat", self.reduction, self.attack_type, self.sort]
                    
    def getHitDam(self, damage):
        self.health = self.health - damage #takes damage
        
    def getHitStat(self, reduction, animation):

        if reduction == "accuracy": #for each reduction, either lowers it, or does not if below a threshold
            if self.accuracy > 60: 
                self.accuracy = self.accuracy - 5
                animation.displayText("{0}'s accuracy went down!".format(self.name))
            else:
                animation.displayText("{0}'s accuracy won't go any lower!".format(self.name))
        elif reduction == "attack":
            if self.attack_reduction_counter <5:
                self.attack = self.attack - 3
                animation.displayText("{0}'s attack went down!".format(self.name))
                self.attack_reduction_counter = self.attack_reduction_counter + 1
            else:
                animation.displayText("{0}'s attack won't go any lower!".format(self.name))

        elif reduction == "defense":
            if self.attack_reduction_counter <5:
                self.defense = self.defense - 3
                animation.displayText("{0}'s defense went down!".format(self.name))
                self.defense_reduction_counter = self.defense_reduction_counter + 1
            else:
                animation.displayText("{0}'s defense won't go any lower!".format(self.name))
    def checkHealth(self,animation): #checks health, and if fainted, says so
        if self.health > 0:
            self.win_checker = 0
        else:
            animation.displayText("{0} fainted!".format(self.name))
            self.win_checker = -1
        return self.win_checker
            
    
            
            
