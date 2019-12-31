from math import sqrt

#Cracks the vigenere cipher using the same method you would use by hand.

#These are the frequencies in the english language.
A = .084
B = .0207
C = .045
D = .034
E = .112
F = .018
G = .025
H = .03
I = .0758
J = .001965
K = .011
L = .055
M = .03
N = .0665
O = .0716
P = .0317
Q = .001962
R = .0758
S = .05735
T = .0695
U = .0363
V = .01007
W = .012899
X = .002902
Y = .017779
Z = .02722

#This is a very repetitive list of caesar shifts
setA = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
setB = [B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A]
setC = [C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B]
setD = [D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C]
setE = [E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D]
setF = [F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E]
setG = [G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F]
setH = [H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G]
setI = [I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H]
setJ = [J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I]
setK = [K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J]
setL = [L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K]
setM = [M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L]
setN = [N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M]
setO = [O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N]
setP = [P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O]
setQ = [Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]
setR = [R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q]
setS = [S, T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R]
setT = [T, U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S]
setU = [U, V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T]
setV = [V, W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U]
setW = [W, X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V]
setX = [X, Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W]
setY = [Y, Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X]
setZ = [Z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y]

#Here's the set of shifts.
setOfSets= [setA, setB, setC, setD, setE, setF, setG, setH, setI, setJ, setK, setL, setM, setN, setO, setP, setQ, setR, setS, setT, setU, setV, setW, setX, setY, setZ]
setBuilder = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
#Find the factors of a number
def findFactors(number):
    factors = []
    for i in range(2, number+1):
        if number%i == 0:
            factors.append(i)
    return factors

#look for repeated patterns in the ciphertext to act as cribs.
def patternSearch(yourString):
    length = len(yourString)
    spaceList = []
    for i in range(2, length-1): #this is how long the phrase should be.
        for n in range(0, length-i):#this is the beginning index of the string
            string = yourString[n:i+n+1]
            for x in range(1+n, length-n-1):
                newString = yourString[x: x+i+1]
                if len(newString)<len(string):
                    newString = 0
                if string == newString:
                    spaces = x-n
                    spaceList.append(spaces)
    return spaceList

#determine what the most likely key length is from a string.
def findKeyLength(yourString):
    spaceList = patternSearch(yourString)
    #if it can't find it, returns no answer
    if spaceList == []:
        return ("No answer")
    else:
        key_list =[]
        for number in spaceList:
            factors = findFactors(number)
            for item in factors:
                key_list.append(item)
        key_list.sort()
        highest = key_list[-1]
        most = spaceList.count(1)
        key1 = 1
        for number in range(2, highest+1):
            amount = key_list.count(number)
            if amount>=most:
                key1 = number
                most = amount
                
            
        return key1

#compare two lists of frequencies.
def compareFreq(l1, l2):
    xy=0
    x2 = 0
    y2 = 0
    allX = 0
    allY = 0
    for i in range(0, 26):
        x = l1[i]
        y = l2[i]
        xy += (x*y)
        x2 +=x*x
        y2 += y*y
        allX+=x
        allY+=y
    r=((26*xy)-(allX*allY))/(sqrt(((26*x2)-(allX*allX))*(((26*y2)-(allY*allY)))))
    return r

#given the key length, try every caesar shift to see which one best matches the frequency.
def freqAnalysis(keyLength, plaintext):
    freqs1 = []
    for i in range (0, keyLength):
        for number in range(0, keyLength): #for each letter multiple...
            letters = [] 
            multiple = number
            while multiple < len(plaintext):
                letters.append(plaintext[multiple])
                multiple += keyLength
            fA = letters.count("A")/len(letters)
            fB = letters.count("B")/len(letters)
            fC = letters.count("C")/len(letters)
            fD = letters.count("D")/len(letters)
            fE = letters.count("E")/len(letters)
            fF = letters.count("F")/len(letters)
            fG = letters.count("G")/len(letters)
            fH = letters.count("H")/len(letters)
            fI = letters.count("I")/len(letters)
            fJ = letters.count("J")/len(letters)
            fK = letters.count("K")/len(letters)
            fL = letters.count("L")/len(letters)
            fM = letters.count("M")/len(letters)
            fN = letters.count("N")/len(letters)
            fO = letters.count("O")/len(letters)
            fP = letters.count("P")/len(letters)
            fQ = letters.count("Q")/len(letters)
            fR = letters.count("R")/len(letters)
            fS = letters.count("S")/len(letters)
            fT = letters.count("T")/len(letters)
            fU = letters.count("U")/len(letters)
            fV = letters.count("V")/len(letters)
            fW = letters.count("W")/len(letters)
            fX = letters.count("X")/len(letters)
            fY = letters.count("Y")/len(letters)
            fZ = letters.count("Z")/len(letters)
            frequencies = [fA, fB, fC, fD, fE, fF, fG, fH, fI, fJ, fK, fL, fM, fN, fO, fP, fQ, fR, fS, fT, fU, fV, fW, fX, fY, fZ]
            correlationList = []
            for eachSet in setOfSets:
                correlation = compareFreq(frequencies, eachSet)
                correlationList.append(correlation)
            bestPredictionNumber = max(correlationList)
            bestPrediction =setBuilder[correlationList.index(bestPredictionNumber)]
            freqs1.append(bestPrediction)
    #return the best prediction for the key
    return freqs1
            
#use the right caesar shift for each letter to convert it to the correct letter.             
def decode(frequencies, plaintext):
    keyLength = len(frequencies)
    counter = 0
    while len(plaintext)%keyLength != 0:
        plaintext += " "
        counter+=1
    decodeLength = len(plaintext)//keyLength
    decodedText = ""
    for i in range(0, decodeLength):
        for n in range(0, keyLength):
            section = plaintext[(0+(i*keyLength)): keyLength+(i*keyLength)]
            shift = frequencies[n]
            letter = section[n]
            newNum = ord(letter)
            if shift == "A":
                newNum += 25
            elif shift == "B":
                newNum += 24
            elif shift == "C":
                newNum += 23
            elif shift == "D":
                newNum += 22
            elif shift == "E":
                newNum += 21
            elif shift == "F":
                newNum += 20
            elif shift == "G":
                newNum += 19
            elif shift == "H":
                newNum += 18
            elif shift == "I":
                newNum += 17
            elif shift == "J":
                newNum += 16
            elif shift == "K":
                newNum += 15
            elif shift == "L":
                newNum += 14
            elif shift == "M":
                newNum += 13
            elif shift == "N":
                newNum += 12
            elif shift == "O":
                newNum += 11
            elif shift == "P":
                newNum += 10
            elif shift == "Q":
                newNum += 9
            elif shift == "R":
                newNum += 8
            elif shift == "S":
                newNum += 7
            elif shift == "T":
                newNum += 6
            elif shift == "U":
                newNum += 5
            elif shift == "V":
                newNum += 4
            elif shift == "W":
                newNum += 3
            elif shift == "X":
                newNum += 2
            elif shift == "Y":
                newNum += 1
            elif shift == "Z":
                newNum += 26
            if newNum >=91:
                newNum = newNum-26
            letter = chr(newNum)
            decodedText += letter
    decodedText = decodedText[0:len(decodedText)-counter]
    return decodedText
#get ciphertext, remove spaces, and attempt to crack the cipher. If you can't, print that.
def crackCipher():
    plaintext = input("What is the ciphertext? ")
    print("Generating plaintext...")
    print("Please be patient.")
    plaintext = plaintext.replace(" ","")
    plaintext = plaintext.upper()
    key = findKeyLength(plaintext)
    keepgoing = True
    freqList = freqAnalysis(key, plaintext)
    print(decode(freqList, plaintext))
try:
    crackCipher()
except Exception:
    print("Sorry, cannot crack this.")
