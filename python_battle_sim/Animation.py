from graphics import *
import time
import random

class Animation():
    
    def __init__(self): 
        self.win = GraphWin("Pokemon Battle!", 400, 500) #creates a window
        self.text_box = Rectangle(Point(0,300),Point(399, 415)) #draws a text box
        self.text_box.setFill("white")
        self.text_box.draw(self.win)
        self.input_box = Rectangle(Point(0,415), Point(400,500)) #draws an input box
        self.input_box.setFill("white")
        self.input_box.draw(self.win)
        self.pam_awakened = False #initializes easter egg as false
        
        self.background = Rectangle(Point(0,90), Point(400, 300))#draws a green background
        self.background.setFill("light green")
        self.background.setOutline("light green")
        self.background.draw(self.win)
        self.background_sky = Rectangle(Point(-5,-5), Point(405, 95))#draws the sky
        self.background_sky.setFill("light blue")
        self.background_sky.setOutline("dark green")
        self.background_sky.draw(self.win)
        self.opponent_place = Oval(Point(300, 100), Point(390, 120))#draws the opponent's place
        self.opponent_place.setFill("light yellow")
        self.opponent_place.setOutline("tan")
        self.opponent_place.draw(self.win)
        self.player_place = Oval(Point(110, 270), Point(20, 250)) #draws the player's place
        self.player_place.setFill("light yellow")
        self.player_place.setOutline("tan")
        self.player_place.draw(self.win)

        self.text = Text(Point(200, 320), "What level would you like to be?") #draws instructions
        self.text2 = Text(Point (200, 340), "Type a number from 1-100. (Please type slowly!)")
        self.text3 = Text(Point (200, 360), "If you want to clear, hit DELETE.")
        self.text4 = Text(Point(200, 380), "Press ENTER to confirm level.")
        self.text.draw(self.win)
        self.text2.draw(self.win)
        self.text3.draw(self.win)
        self.text4.draw(self.win)
        self.level = "" #initializes a level string
        self.level_text = Text(Point(200, 460), str(self.level)) #an ongoing string showing whathas been typed
        self.level_text.draw(self.win)
        self.keepGoing = "hello" #starts out with a random string
        while self.keepGoing != "Return": #until enter is pressed:
                self.keepGoing = self.win.getKey() #gets a key
                if self.keepGoing == "BackSpace": #if the key is backspace:
                        self.input_box = Rectangle(Point(0,415), Point(400,500)) #clears current input
                        self.input_box.setFill("white")
                        self.input_box.draw(self.win)
                        self.level = "" #starts over with level string
                        self.level_text = Text(Point(200, 460), str(self.level))
                        self.level_text.draw(self.win)
                elif self.keepGoing !="Return": #otherwise:
                        self.input_box = Rectangle(Point(0,415), Point(400,500)) #draws box over last string
                        self.input_box.setFill("white") 
                        self.input_box.draw(self.win)
                        self.level = self.level+str(self.keepGoing) #adds the key pressed to the level string
                        self.level_text = Text(Point(200, 460), str(self.level)) #draws that
                        self.level_text.draw(self.win)
        
        self.input_box = Rectangle(Point(0,415), Point(400,500)) #clears the input box
        self.input_box.setFill("white")
        self.input_box.draw(self.win)
        if self.level == "pam": #if you type in "pam" to activate easter egg:
            self.pam_awakened = True #switches variable to true
            self.text_box = Rectangle(Point(0,300),Point(399, 415)) #clears the text box
            self.text_box.setFill("white")
            self.text_box.draw(self.win)
            self.pam_text = Text(Point(200, 320), "She awakens...") #puts ominous message on screen
            self.pam_text.draw(self.win)
            for i in range (0,20): #moves the ominous message (to make it extra ominous)
                        self.pam_text.move(0,2)
                        self.pam_text.move(0,-2)
        self.text_box = Rectangle(Point(0,300),Point(399, 415)) #clears message
        self.text_box.setFill("white")
        self.text_box.draw(self.win)
        
        try:
                self.level = int(self.level) #try if its an integer
        except ValueError:
                self.level = False #if not, level is False
        while self.level == False or self.level<1 or self.level>100: #while the level is false or out of bounds:
                self.new_text = Text(Point(200, 350), "Invalid input!") #Tells invalid input
                self.new_text.draw(self.win)
                time.sleep(1.5) #waits for comprehension
                self.text_box = Rectangle(Point(0,300),Point(399, 415)) #clears text box
                self.text_box.setFill("white")
                self.text_box.draw(self.win)
                self.text = Text(Point(200, 320), "What level would you like to be?") #asks again using same mechanism as above
                self.text2 = Text(Point (200, 340), "Type a number from 1-100. (Please type slowly!)")
                self.text3 = Text(Point (200, 360), "If you want to clear, hit DELETE.")
                self.text4 = Text(Point(200, 380), "Press ENTER to confirm level.")
                self.text.draw(self.win) 
                self.text2.draw(self.win)
                self.text3.draw(self.win)
                self.text4.draw(self.win)
                self.level = ""
                self.level_text = Text(Point(200, 460), str(self.level))
                self.level_text.draw(self.win)
                self.keepGoing = "hello"
                while self.keepGoing != "Return":
                        self.keepGoing = self.win.getKey()
                        if self.keepGoing == "BackSpace":
                                self.input_box = Rectangle(Point(0,415), Point(400,500))
                                self.input_box.setFill("white")
                                self.input_box.draw(self.win)
                                self.level = ""
                                self.level_text = Text(Point(200, 460), str(self.level))
                                self.level_text.draw(self.win)
                        elif self.keepGoing !="Return":
                                self.input_box = Rectangle(Point(0,415), Point(400,500))
                                self.input_box.setFill("white")
                                self.input_box.draw(self.win)
                                self.level = self.level+str(self.keepGoing)
                                self.level_text = Text(Point(200, 460), str(self.level))
                                self.level_text.draw(self.win)
                
                if self.level == "pam":
                    self.pam_awakened = True
                    self.text_box = Rectangle(Point(0,300),Point(399, 415))
                    self.text_box.setFill("white")
                    self.text_box.draw(self.win)
                    self.pam_text = Text(Point(200, 320), "She awakens...")
                    self.pam_text.draw(self.win)
                    for i in range(0, 20):
                        self.pam_text.move(0,2)
                        self.pam_text.move(0,-2)
                self.text_box = Rectangle(Point(0,300),Point(399, 415))
                self.text_box.setFill("white")
                self.text_box.draw(self.win)
                try:
                        self.level = int(self.level)
                except ValueError:
                        self.level = False
        if self.pam_awakened == True:
            self.opponent_level = "???" #sorry about all the easter egg stuff but anyway if its activated, the level is ???
        else: #if easter egg not activated:
            self.opponent_level = random.randint(self.level-5,self.level+5)#chooses a random opponent level
            while self.opponent_level >100 or self.opponent_level <1:
                self.opponent_level = random.randint(self.level-2, self.level+2) #if the level is over 100 or under 1, narrows the range and tries again until it works
        self.your_level = self.level
        
    def clearWindow(self): #clears boxes of all text
        self.input_box = Rectangle(Point(0,415), Point(400,500))  #clears top box
        self.input_box.setFill("white")
        self.input_box.draw(self.win)
        
        self.text_box = Rectangle(Point(0,300),Point(399, 415)) #clears bottom box
        self.text_box.setFill("white")
        self.text_box.draw(self.win)
        
    def getPam(self): #returns if easter egg has happened
        return self.pam_awakened
    
    def getLevels(self):
        return [self.your_level, self.opponent_level] #returns level

    
    def chooseYourFighter(self): #chooses a pokemon
        self.whole_box = Rectangle(Point(0,300), Point(400, 500))  #turns the input and text boxes into one big box
        self.whole_box.setFill("white")
        self.whole_box.draw(self.win)
        
        self.bulbasaur_text = Text(Point(60, 320), "Bulbasaur") #prints the names of pokemon in a grid
        self.bulbasaur_text.draw(self.win)
        
        self.charmander_text = Text(Point(150, 320), "Charmander")
        self.charmander_text.draw(self.win)
        
        self.squirtle_text = Text(Point(240,320), "Squirtle")
        self.squirtle_text.draw(self.win)
        
        self.sandshrew_text = Text(Point(330, 320), "Sandshrew")
        self.sandshrew_text.draw(self.win)
        
        self.pidgey_text = Text(Point(60, 380), "Pidgey")
        self.pidgey_text.draw(self.win)
        
        self.pikachu_text = Text(Point(150, 380), "Pikachu")
        self.pikachu_text.draw(self.win)
        
        self.caterpie_text = Text(Point(240, 380), "Caterpie")
        self.caterpie_text.draw(self.win)
        
        self.mankey_text = Text(Point(330, 380), "Mankey")
        self.mankey_text.draw(self.win)
        
        self.meowth_text = Text(Point(60, 440),"Meowth")
        self.meowth_text.draw(self.win)
        
        self.ekans_text = Text(Point(150, 440), "Ekans")
        self.ekans_text.draw(self.win)
        
        self.mr_mime_text = Text(Point(240, 440), "Mr. Mime")
        self.mr_mime_text.draw(self.win)
        
        self.geodude_text = Text(Point(330, 440), "Geodude")
        self.geodude_text.draw(self.win)

        self.pointer = Polygon(Point(20,320), Point(15, 325), Point(15, 315)) #creates a triangle that points towards the first name
        self.pointer.setFill("black")
        self.pointer.draw(self.win)
        self.tutorial_text = Text(Point(200, 470),"Choose a Pokemon using arrow keys and ENTER when ready!") #draws instructions
        self.tutorial_text.draw(self.win)
        self.keepGoing = True #sets keepGoing to true
        while self.keepGoing == True: #while enter isn't pressed:
            self.text = self.win.getKey() #looks for key
            self.pointList = self.pointer.getPoints() #gets the points of the triangle
            self.xpoint = self.pointList[0].getX() #gets x of first point
            self.ypoint = self.pointList[0].getY()#gets y of first point
        
            if self.text == "Right" and self.xpoint< 290: #moves pointer right while not on the edge
                self.pointer.move(90, 0)
            
            elif self.text == "Right" and self.xpoint>289: #if on the edge, moves all the way ack to the left
                self.pointer.move(-270,0)
            
            elif self.text =="Left" and self.xpoint< 21: #moves pointer all the way back to the right if on the edge
                self.pointer.move(270,0)
            elif self.text == "Left" and self.xpoint > 20: #moves left if not on edge
                self.pointer.move(-90, 0)

                
            elif self.text =="Up" and self.ypoint >320: #moves up if not at top
                self.pointer.move(0, -60)
            elif self.text =="Up" and self.ypoint <321: #if at top, moves to the bottom
                self.pointer.move(0,120)
            
            elif self.text == "Down" and self.ypoint >439: #moves up if att the bottom
                self.pointer.move(0,-120)
            elif self.text == "Down" and self.ypoint <440: #otherwise, moves down
                self.pointer.move(0,60)
            elif self.text == "Return": #when key is pressed:
                self.xlocation = self.xpoint #gets x location
                self.ylocation = self.ypoint #gets y location
                self.keepGoing = False #sets variable to false, ending the loop
        if self.xlocation == 20 and self.ylocation == 320: #depending on the location of the pointer, returns the list number of a pokemon.
            return 0
        elif self.xlocation == 110 and self.ylocation == 320:
            return 1
        elif self.xlocation == 200 and self.ylocation == 320:
            return 2
        elif self.xlocation == 290 and self.ylocation == 320:
            return 3
        elif self.xlocation == 20 and self.ylocation == 380:
            return 4
        elif self.xlocation == 110 and self.ylocation == 380:
            return 5
        elif self.xlocation == 200 and self.ylocation == 380:
            return 6
        elif self.xlocation == 290 and self.ylocation == 380:
            return 7
        elif self.xlocation == 20 and self.ylocation == 440:
            return 8
        elif self.xlocation == 110 and self.ylocation == 440:
            return 9
        elif self.xlocation == 200 and self.ylocation == 440:
            return 10
        elif self.xlocation == 290 and self.ylocation == 440:
            return 11
    def enemyAppear(self,enemyPokemon): #a pokemon appears (takes in that pokemon)
        self.text_box = Rectangle(Point(0,300),Point(399, 415)) #clears top box
        self.text_box.setFill("white")
        self.text_box.draw(self.win)
        self.input_box = Rectangle(Point(0,415), Point(400,500)) #clears bottom box
        self.input_box.setFill("white")
        self.input_box.draw(self.win)
        self.enemy_pokemon = enemyPokemon #gets the pokemon
        self.opponent_sprite = Image(Point(345, 95),enemyPokemon.getSprite()) #gets pokemon's sprite
        self.enemy_name = enemyPokemon.getName() #gets enemy's name
        self.opponent_sprite.draw(self.win) #draws opponent's sprite 
        self.enemy_max_health = self.enemy_pokemon.getHealth() #finds enemy's max health
        self.o_health_bar_rectangle = Rectangle(Point(1, 1), Point(171, 91)) #a UI box
        self.o_health_bar_rectangle.setFill(color_rgb(255, 255, 230)) 
        self.o_health_bar_rectangle.draw(self.win) #draws UI box
        self.enemy_health_bar = Rectangle(Point(22, 36), Point(152, 56)) #inside it, puts a health bar
        self.enemy_health_bar.setFill(color_rgb(100, 255, 100)) #sets the color to green
        self.enemy_health_bar.draw(self.win)
        self.enemy_counter = self.enemy_pokemon.getHealth()/130 #divides health by length of health bar (will be used later to decrease length of health bar proportional to health)
        self.enemy_info_top = Text(Point(86, 16), "Lvl {0} {1:^10}".format(self.opponent_level, self.enemy_pokemon.getName())) #prints level and name in UI box
        self.enemy_info_top.draw(self.win)
        
    def sendOut(self,yourPokemon): #sends out your pokemon
        self.your_pokemon = yourPokemon #gets pokemon
        self.your_sprite = Image(Point(65,245),yourPokemon.getSprite()) #gets sprite
        self.your_name = self.your_pokemon.getName() #gets name
        self.your_max_health = self.your_pokemon.getHealth() #gets health
        pokeball = Circle(Point(-5, 211), 5) #draws an ultra ball just offscreen
        pokeball.setFill("black")
        pokeball.setOutline("yellow")
        pokeball_line = Line(Point(-10, 211), Point(0, 211))
        pokeball_line.setOutline("yellow")
        pokeball.draw(self.win)
        pokeball_line.draw(self.win)
        self.health_bar_rectangle = Rectangle(Point(229, 200),Point(399, 290)) #draws UI box
        self.own_health_bar = Rectangle(Point(250, 235), Point(380, 255)) #draws your health bar
        self.health_bar_rectangle.setFill(color_rgb(255, 255, 230)) 
        self.own_health_bar.setFill(color_rgb(100, 255, 100))#sets health bar color green
        self.health_bar_rectangle.draw(self.win)
        self.own_health_bar.draw(self.win)
        self.your_counter =self.your_pokemon.getHealth()/130 #finds a varaible proportional to health and health bar
        self.your_info_top = Text(Point(314, 215), "Lvl {0} {1:^10}".format(self.your_level, self.your_pokemon.getName())) #prints level and name in health bar
        self.your_info_top.draw(self.win)
        self.your_info_bottom = Text(Point(314, 284), "HP: {0}/{1}".format(self.your_max_health, self.your_max_health)) #prints health as a fraction in health bar
        self.your_info_bottom.draw(self.win)

        for i in range(0,14): #animates the movement of a pokeball
            pokeball.move(5, 2)
            pokeball_line.move(5,2)
        pokeball.move(800,800) #moves pokeball off screen
        pokeball_line.move(900,900)
        self.your_sprite.draw(self.win) #draws your sprite


        
        
                                                

    def lowerPlayerHealth(self, player_health): #animates lowering health
        self.health_bar_rectangle = Rectangle(Point(229, 200),Point(399, 290)) #draws UI box
        self.health_bar_rectangle.setFill(color_rgb(255, 255, 230))
        self.health_bar_rectangle.draw(self.win)
        self.health_bar_maximum = Rectangle(Point(250, 235), Point(380, 255)) #draws the outline of the max health bar
        self.health_bar_maximum.draw(self.win)
        self.current_health = self.your_pokemon.getHealth() #gets player's current health
        self.remaining_health =round(player_health/self.your_counter) #finds a number proportional to the length of the health bar (as a fraction of the health bar)
        if self.remaining_health < 0: #if fraction of bar health is negative
            self.remaining_health = 0 #sets it to 0
        if self.remaining_health <65 and self.remaining_health>29: #if it's in this range:
            self.color = "yellow" #sets fill color to yellow
        elif self.remaining_health <30: #if in this range:
            self.color = "red" #sets fill color to red
        else:
            self.color = color_rgb(100, 255, 100) #otherwise, it's green
        if self.current_health <0: #if health is negative:
            self.current_health = 0 #sets it to 0
        self.health_bar = Rectangle(Point(250, 235), Point(250+self.remaining_health, 255)) #draws the health bar with length using remaining health
        self.health_bar.setFill(self.color) #sets fill with color
        self.health_bar.draw(self.win)
        self.your_info_top = Text(Point(314, 215), "Lvl {0} {1:^10}".format(self.your_level, self.your_pokemon.getName())) #redraws name, HP, etc.
        self.your_info_top.draw(self.win)
        self.your_info_bottom = Text(Point(314, 284), "HP: {0}/{1}".format(self.current_health,self.your_max_health)) #health as a fraction of max health
        self.your_info_bottom.draw(self.win)

    def lowerOpponentHealth(self, opponent_health): #lowers opponent health
        self.o_health_bar_rectangle = Rectangle(Point(1, 1), Point(171, 91)) #draws UI box
        self.o_health_bar_rectangle.setFill(color_rgb(255, 255, 230))
        self.o_health_bar_rectangle.draw(self.win)
        self.health_bar_maximum = Rectangle(Point(22, 36), Point(152, 56)) #draws max HP
        self.health_bar_maximum.draw(self.win)
        self.remaining_health =round(opponent_health/self.enemy_counter) #finds health proportional to health bar length
        if self.remaining_health < 0: #if below 0, 0
            self.remaining_health = 0
        if self.remaining_health <65 and self.remaining_health>29: #if it's in this range, color = yellow
            self.color = "yellow"
        elif self.remaining_health <30: #if it's in this range, color = red
            self.color = "red"
        else:
            self.color = color_rgb(100, 255, 100) #otherwise, green
        self.health_bar = Rectangle(Point(22, 36), Point(22+self.remaining_health, 56)) #draws proporitonal health bar
        self.health_bar.setFill(self.color)
        self.health_bar.draw(self.win)
        self.enemy_info_top = Text(Point(86, 16), "Lvl {0} {1:^10}".format(self.opponent_level, self.enemy_name)) #reprints name and level
        self.enemy_info_top.draw(self.win)
        
        
        
        
    def playerFaint(self): #animates fainting
        for i in range(0, 10): #flickers sprite
            self.your_sprite.move(900, 900)
            self.your_sprite.move(-900, -900)
        self.your_sprite.move(1000, 1000) #sends offscreen
        
    def opponentFaint(self): #animates fainting
        for i in range(0, 10): #flickers sprite
            self.opponent_sprite.move(900, 900)
            self.opponent_sprite.move(-900, -900)
        self.opponent_sprite.move(1000, 1000) #sends offscreen
        
    def playerAttack(self,attack_type, attack_sort):
        if attack_type == "grass": #depending on attack type, sets color
            self.color = "green"
        elif attack_type == "fire":
            self.color = "red"
        elif attack_type == "water":
            self.color = "dark blue"
        elif attack_type == "bug":
            self.color = "dark green"
        elif attack_type == "normal":
            self.color = "light grey"
        elif attack_type == "fighting":
            self.color = "chocolate"
        elif attack_type == "electric":
            self.color = "yellow"
        elif attack_type == "poison":
            self.color = "magenta"
        elif attack_type == "psychic":
            self.color = "hot pink"
        elif attack_type == "ground":
            self.color = "tan"
        elif attack_type == "rock":
            self.color = "brown"
        elif attack_type == "flying":
            self.color = "white"

        if attack_sort == None: #if attack misses, no animation
            time.sleep(.1)

        if attack_sort == "special": #for one sort of attack (ranged)
            self.attack_orb = Circle(Point(95, 245), 5) #draws a circle with color depending on type
            self.attack_orb.setFill(self.color)
            self.attack_orb.draw(self.win)
            for i in range(0, 231, 5): #moves circle to opponent
                self.attack_orb.move(5, -3)
            self.attack_orb.move(900,900) #when it hits, sends it offscreen
            for i in range(0,4): #flickers opponent to indicate damage taken
                self.opponent_sprite.move(800,800)
                time.sleep(.05)
                self.opponent_sprite.move(-800,-800)
                
        elif attack_sort == "physical": #if attack is physical
            for i in range(0, 231, 10): #moves pokemon sprite to other sprite
                self.your_sprite.move(11,-6)
            p1 = Point(345, 95) #has an origin point
            c1= Circle(p1, 5) #creates 4 circles with color depending on type (represents particles)
            c2 =Circle(p1, 5)
            c3 =Circle(p1, 5)
            c4 =Circle(p1, 5)
            c1.setFill(self.color)
            c2.setFill(self.color)
            c3.setFill(self.color)
            c4.setFill(self.color)
            c1.draw(self.win)
            c2.draw(self.win)
            c3.draw(self.win)
            c4.draw(self.win)
            for i in range(0, 10): #moves quickly offscreen
                c1.move(40, 40)
                c2.move(40, -40)
                c3.move(-40, 40)
                c4.move(-40, -40)
            for i in range(0,4): #flickers opponent
                self.opponent_sprite.move(800,800)
                time.sleep(.05)
                self.opponent_sprite.move(-800,-800)
            for i in range(0, 231, 20): #moves your sprite back
                self.your_sprite.move(-22, 12)
                
        elif attack_sort == "self": #if attack is something done by yourself:
            for i in range(0, 10): #moves to the right
                self.your_sprite.move(1, 0)
            time.sleep(.1)
            for i in range(0, 20): #moves to the left
                self.your_sprite.move(-1,0)
            time.sleep(.1)
            for i in range(0, 10):#moves back to original position
                self.your_sprite.move(1, 0)
            time.sleep(.1)
            for i in range(2): #hops twice
                for i in range(1,6):
                    self.your_sprite.move(0,-3)
                time.sleep(.1)
                for i in range(1, 4):
                    self.your_sprite.move(0,5)
                time.sleep(.15)
                
        elif attack_sort == "environment": #if it affects the environment:
            self.attack_orb = Circle(Point(95, 245), 5) #draws attack circle with fill of type
            self.attack_orb.setFill(self.color)
            self.attack_orb.setOutline(self.color)
            self.attack_orb.draw(self.win)
            for i in range(0, 120, 5): #moves to ~halfway point
                self.attack_orb.move(5, -3)
            self.attack_orb.move(900,900) #moves offscreen
            p1 = Point(215, 173)
            c1= Circle(p1, 5) #sends four particles of same color out quickly
            c2 =Circle(p1, 5)
            c3 =Circle(p1, 5)
            c4 =Circle(p1, 5)
            c1.setFill(self.color)
            c2.setFill(self.color)
            c3.setFill(self.color)
            c4.setFill(self.color)
            c1.draw(self.win)
            c2.draw(self.win)
            c3.draw(self.win)
            c4.draw(self.win)
            for i in range(0, 10):
                c1.move(40, 40)
                c2.move(40, -40)
                c3.move(-40, 40)
                c4.move(-40, -40)
            


    def opponentAttack(self, attack_type, attack_sort): #similar to function above, but reversed direction
        if attack_type == "grass": #picks color depending on type
            self.color = "green"
        elif attack_type == "fire":
            self.color = "red"
        elif attack_type == "water":
            self.color = "dark blue"
        elif attack_type == "bug":
            self.color= "dark green"
        elif attack_type == "normal":
            self.color= "light grey"
        elif attack_type == "fighting":
            self.color = "chocolate"
        elif attack_type == "electric":
            self.color = "yellow"
        elif attack_type == "poison":
            self.color = "magenta"
        elif attack_type == "psychic":
            self.color = "hot pink"
        elif attack_type == "ground":
            self.color = "tan"
        elif attack_type == "rock":
            self.color = "brown"
        elif attack_type == "flying":
            self.color = "white"

        if attack_sort == None:
            time.sleep(.1) #if attack misses, no animation
        elif attack_sort == "special": #if the attack is special animation:
            
            self.attack_orb = Circle(Point(345, 95), 5) #creates circle with color based on type
            self.attack_orb.setFill(self.color)
            self.attack_orb.draw(self.win)
            for i in range(0, 231, 5): #moves to your sprite
                self.attack_orb.move(-5, 3)
            self.attack_orb.move(900,900) #moves offscreen
            for i in range(0,4): #flickers your pokemon
                self.your_sprite.move(800,800)
                time.sleep(.05)
                self.your_sprite.move(-800,-800)
                
        elif attack_sort == "physical": #if it's physical
            for i in range(0, 231, 10):
                self.opponent_sprite.move(-11,6) #moves to your pokemon
            p1 = Point(65, 245) #generates 4 particles and sends them away after collision
            c1= Circle(p1, 5)
            c2 =Circle(p1, 5)
            c3 =Circle(p1, 5)
            c4 =Circle(p1, 5)
            c1.setFill(self.color)
            c2.setFill(self.color)
            c3.setFill(self.color)
            c4.setFill(self.color)
            c1.draw(self.win)
            c2.draw(self.win)
            c3.draw(self.win)
            c4.draw(self.win)
            for i in range(0, 12):
                c1.move(40, 40)
                c2.move(40, -40)
                c3.move(-40, 40)
                c4.move(-40, -40)
            for i in range(0,4): #flickers your pokemon
                self.your_sprite.move(800,800)
                time.sleep(.05)
                self.your_sprite.move(-800,-800)
            for i in range(0, 231, 20): #moves opponent back
                self.opponent_sprite.move(22, -12)
                
        elif attack_sort == "self": #if it is only done by opponent 
            for i in range(0, 10): #moves to the left
                self.opponent_sprite.move(1, 0)
            time.sleep(.1)
            for i in range(0, 20): #moves to the right
                self.opponent_sprite.move(-1,0)
            time.sleep(.1)
            for i in range(0, 10): #moves back
                self.opponent_sprite.move(1, 0)
            time.sleep(.1)
            for i in range(2): #hops twice
                for i in range(1,6):
                    self.opponent_sprite.move(0,-3)
                time.sleep(.1)
                for i in range(1, 4):
                    self.opponent_sprite.move(0,5)
                time.sleep(.15)
                
        elif attack_sort == "environment": #if it affects environment
            self.attack_orb = Circle(Point(345, 95), 5) #draws circle with fill color, moves it halfway, disappears it
            self.attack_orb.setFill(self.color)
            self.attack_orb.setOutline(self.color)
            self.attack_orb.draw(self.win)
            for i in range(0, 120, 5):
                self.attack_orb.move(-5, 3)
            self.attack_orb.move(900,900)
            p1 = Point(225, 167) #generates 4 particles and moves them away
            c1= Circle(p1, 5)
            c2 =Circle(p1, 5)
            c3 =Circle(p1, 5)
            c4 =Circle(p1, 5)
            c1.setFill(self.color)
            c2.setFill(self.color)
            c3.setFill(self.color)
            c4.setFill(self.color)
            c1.draw(self.win)
            c2.draw(self.win)
            c3.draw(self.win)
            c4.draw(self.win)
            for i in range(0, 10):
                c1.move(40, 40)
                c2.move(40, -40)
                c3.move(-40, 40)
                c4.move(-40, -40)
        elif attack_sort == "pam": #if easter egg type:
            new_rectangle = Rectangle(Point(0,0), Point(400,300))
            new_rectangle.setFill("black") #turns off screen
            new_rectangle.draw(self.win)
            text = Text( Point (200, 150), "God forgive me...") #prints text referencing monster factory episode
            text.setFill("white")
            text.draw(self.win)
            
    def animateChoice(self, move1, move2, move3, move4): #animates picking a move
        self.text1 = Text( Point(150, 425), move1.getName()) #prints move names in grid
        self.text2 = Text( Point(250, 425), move2.getName())
        self.text3 = Text(Point(150, 475), move3.getName())
        self.text4 = Text(Point(250, 475), move4.getName())
        self.pointer = Polygon(Point(110, 425), Point(105, 420), Point(105, 430)) #draws a pointer pointing to first move
        self.pointer.setFill("black")
        self.pointer.draw(self.win)
        
        self.text1.draw(self.win)
        self.text2.draw(self.win)
        self.text3.draw(self.win)
        self.text4.draw(self.win)
        self.keepGoing = True
        while self.keepGoing == True:
            self.text = self.win.getKey()
            self.pointList = self.pointer.getPoints()
            self.xpoint = self.pointList[0].getX() #gets X and Y stuff
            self.ypoint = self.pointList[0].getY()
        
            if self.text == "Right" and self.xpoint< 210: #if on left option, moves right
                self.pointer.move(100, 0)
            
            elif self.text == "Right" and self.xpoint>209: #if on right option, moves left
                self.pointer.move(-100,0)
            
            elif self.text =="Left" and self.xpoint< 210: #if on left option, moves right
                self.pointer.move(100,0)
            elif self.text == "Left" and self.xpoint > 209: #if on right option, moves left
                self.pointer.move(-100, 0)
            elif self.text =="Up" and self.ypoint >425: #if at bottom, moves to top
                self.pointer.move(0, -50)
            elif self.text =="Up" and self.ypoint <426: #if at top, moves to bottom
                self.pointer.move(0,50)
            
            elif self.text == "Down" and self.ypoint >425: #if at bottom, moves to top
                self.pointer.move(0,-50)
            elif self.text == "Down" and self.ypoint <426:#if at top, moves to bottom
                self.pointer.move(0,50)
            elif self.text == "Return": #when enter pressed:
                self.xlocation = self.xpoint #gets x
                self.ylocation = self.ypoint #gets y
                self.keepGoing = False #ends loop
        self.input_box = Rectangle(Point(0,415), Point(400,500)) #clears box
        self.input_box.setFill("white")
        self.input_box.draw(self.win)
        if self.xlocation <210 and self.ylocation<426: #returns move depending on location of pointer
            return(move1)
        elif self.xlocation <210 and self.ylocation >425:
            return(move3)
        elif self.xlocation >209 and self.ylocation <426:
            return(move2)
        else:
            return(move4)
    def displayText(self, text): #takes in a string
        self.text = Text(Point(200, 360), text) #displays the string in the text box
        self.text.draw(self.win)
        time.sleep(1.5) #pauses
        self.text_box = Rectangle(Point(0,300),Point(399, 415)) #clears it
        self.text_box.setFill("white")
        self.text_box.draw(self.win)

    def displayInstruction(self, text):
        self.text = Text(Point(200, 360), text) #displays the string in the text box
        self.text.draw(self.win)


    def closeWin(self): #closes the window
        self.win.close()

    def getWin(self):
        return self.win #returns window
        
        


