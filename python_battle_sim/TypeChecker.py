def typeCheck(attack_type, opponent_type):
    #fire matchups
    if attack_type == "fire" and opponent_type == "water": #for each type combination, gives if its super effective or ineffective
        effectiveness = .5
    elif opponent_type == "pam": #this one is for an easter egg ;)
        effectiveness = 0
    elif attack_type == "fire" and opponent_type == "rock":
        effectiveness = .5
    elif attack_type == "fire" and opponent_type == "bug":
        effectiveness = 2
    elif attack_type == "fire" and opponent_type == "fire":
        effectiveness = .5
    elif attack_type == "fire" and opponent_type == "grass":
        effectiveness = 2
    
    #normal matchups
    elif attack_type == "normal" and opponent_type == "rock":
        effectiveness = .5
    #fighting matchups
    elif attack_type == "fighting" and opponent_type == "normal":
        effectiveness = 2
    elif attack_type == "fighting" and opponent_type == "flying":
        effectiveness = .5
    elif attack_type == "fighting" and opponent_type == "poison":
        effectiveness = .5
    elif attack_type == "fighting" and opponent_type == "rock":
        effectiveness = .5
    elif attack_type == "fighting" and opponent_type == "bug":
        effectiveness = 2
    elif attack_type == "fighting" and opponent_type == "psychic":
        effectiveness = .5
    #flying matchups
    elif attack_type == "flying" and opponent_type == "fighting":
        effectiveness = 2
    elif attack_type == "flying" and opponent_type == "rock":
        effectiveness = .5
    elif attack_type == "flying" and opponent_type == "bug":
        effectiveness = 2
    elif attack_type == "flying" and opponent_type == "grass":
        effectiveness = 2
    elif attack_type == "flying" and opponent_type == "electric":
        effectiveness = .5
    #poison matchups
    elif attack_type == "poison" and opponent_type == "poison":
        effectiveness = .5
    elif attack_type == "poison" and opponent_type == "ground":
        effectiveness = .5
    elif attack_type == "poison" and opponent_type == "rock":
        effectiveness = .5
    elif attack_type == "poison" and opponent_type == "grass":
        effectiveness = 2
    #ground matchups
    elif attack_type == "ground" and opponent_type == "flying":
        effectiveness = 0
    elif attack_type == "ground" and opponent_type == "poison":
        effectiveness = 2
    elif attack_type == "ground" and opponent_type == "rock":
        effectiveness = 2
    elif attack_type == "ground" and opponent_type == "bug":
        effectiveness = .5
    elif attack_type == "ground" and opponent_type == "fire":
        effectiveness = 2
    elif attack_type == "ground" and opponent_type == "grass":
        effectiveness = .5
    elif attack_type == "ground" and opponent_type == "electric":
        effectiveness = 2
    #rock matchups
    elif attack_type == "rock" and opponent_type == "fighting":
        effectiveness = .5
    elif attack_type == "rock" and opponent_type == "flying":
        effectiveness = 2
    elif attack_type == "rock" and opponent_type == "ground":
        effectiveness = .5
    elif attack_type == "rock" and opponent_type == "bug":
        effectiveness = 2
    elif attack_type == "rock" and opponent_type == "fire":
        effectiveness = 2
    #bug matchups
    elif attack_type == "bug" and opponent_type == "fighting":
        effectiveness = .5
    elif attack_type == "bug" and opponent_type == "flying":
        effectiveness = .5
    elif attack_type == "bug" and opponent_type == "poison":
        effectiveness = .5
    elif attack_type == "bug" and opponent_type == "fire":
        effectiveness = .5
    elif attack_type == "bug" and opponent_type == "grass":
        effectiveness = 2
    elif attack_type == "bug" and opponent_type == "psychic":
        effectiveness = 2
    #water matchups
    elif attack_type == "water" and opponent_type == "ground":
        effectiveness = 2
    elif attack_type == "water" and opponent_type == "rock":
        effectiveness = 2
    elif attack_type == "water" and opponent_type == "fire":
        effectiveness = 2
    elif attack_type == "water" and opponent_type == "water":
        effectiveness = .5
    elif attack_type == "water" and opponent_type == "grass":
        effectiveness = .5
    #grass matchups
    elif attack_type == "grass" and opponent_type == "flying":
        effectiveness = .5
    elif attack_type == "grass" and opponent_type == "poison":
        effectiveness = .5
    elif attack_type == "grass" and opponent_type == "ground":
        effectiveness = 2
    elif attack_type == "grass" and opponent_type == "rock":
        effectiveness = 2
    elif attack_type == "grass" and opponent_type == "bug":
        effectiveness = .5
    elif attack_type == "grass" and opponent_type == "fire":
        effectiveness = .5
    elif attack_type == "grass" and opponent_type == "water":
        effectiveness = 2
    elif attack_type == "grass" and opponent_type == "grass":
        effectiveness = .5
    #electric matchups
    elif attack_type == "electric" and opponent_type == "flying":
        effectiveness = 2
    elif attack_type == "electric" and opponent_type == "ground":
        effectiveness = 0
    elif attack_type == "electric" and opponent_type == "water":
        effectiveness = 2
    elif attack_type == "electric" and opponent_type == "grass":
        effectiveness = .5
    elif attack_type == "electric" and opponent_type == "electric":
        effectiveness = .5
    #psychic matchups
    elif attack_type == "psychic" and opponent_type == "fighting":
        effectiveness = 2
    elif attack_type == "psychic" and opponent_type == "poison":
        effectiveness = 2
    elif attack_type == "psychic" and opponent_type == "psychic":
        effectiveness = .5
    else:
        effectiveness = 1
    return effectiveness

    
