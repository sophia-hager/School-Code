class statAttack(): # defines a class
    
    def __init__(self, accuracy, move_type, target_stat, name, pp, sort): #takes in data and initializes it
        self.accuracy = accuracy
        self.target_stat = target_stat
        self.type = move_type
        self.name = name
        self.max_pp = pp
        self.current_pp = self.max_pp
        self.move_usable = True #begins as usable
        self.sort = sort
    def reducePP(self):
        self.current_pp -= 1 #reduces pp

    def checkPP(self):
        if self.current_pp ==0:
            self.move_usable = False #if out of pp, move cannot be used
        return self.move_usable

    def getStat(self):
        return self.target_stat #returns target stat
                 
    def getAcc(self):
        return self.accuracy #returns inherent move accuracy

    def getType(self):
        return self.type #returns move type
    
    def getName(self):
        return self.name # returns move name 
    def getKind(self):
        return "stat" #returns that it is a stat move
    def getSort(self):
        return self.sort #returns the animation type


        
class damageAttack():
    
    def __init__(self, move_type, power, accuracy, name, pp, sort): #similar to above
        self.type = move_type #initializes from inputs
        self.power = power
        self.accuracy = accuracy
        self.name = name
        self.max_pp = pp
        self.current_pp = self.max_pp #sets current PP from max PP
        self.move_usable = True #move is usable
        self.sort = sort
    def reducePP(self): #reduces PP
        self.current_pp -= 1

    def checkPP(self):
        if self.current_pp ==0: #if it's equal to 0
            self.move_usable = False #move unusable
        return self.move_usable #returns T or F

    def getType(self): #returns type
        return self.type
    def getPower(self):
        return self.power #returns power
    def getAcc(self):
        return self.accuracy #returns accuracy
    def getName(self):
        return self.name #returns name
    def getKind(self):
        return "attack"#returns that it is a damaging move
    def getSort(self):
        return self.sort #returns the sort of animation
