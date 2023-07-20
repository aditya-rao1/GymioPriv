import pandas as pd   
import random

#Ask user for user information for the app through the terminal. Not really needed as there is visual 
#represenation in the flet.
def getUserInfo():
    userExperience = input("Are you a beginner or intermediate in the gym? ")
    target_muscle = input("What muscle group would you like to grow most? ")
    return userExperience, target_muscle

#Kind of represents the object that each user registers as. Keep as reference for now.
class userInfo:
    def __init__(self, experience, fav_muscle):
        self.experience = experience
        self.fav_muscle = fav_muscle

#Push, pull, legs, fav lists where we add the items from the csv file from.
pull = []
push = []
legs = []
fav = []

#Read the csv file, generate a random integer, then filter and grab some excercises. 
def getPull(experience):
    df = pd.read_csv(r"C:\Users\raoad\OneDrive\Documents\Sophomore\Datasets\megaGymDataset.csv")
    randomInt = random.randint(0, 9)
    #Bicep:
    filtBi = (df['Level'] == experience) & (df['BodyPart'] == 'Biceps')
    randomBicep = df[filtBi]
    specificBicep = randomBicep.iloc[randomInt]['Title']
    pull.append(specificBicep)
    #Lats: 
    filtLats = (df['Level'] == experience) & (df['BodyPart'] == 'Lats')
    randomLat = df[filtLats]
    specificLat = randomLat.iloc[randomInt]['Title']
    pull.append(specificLat)
    #Middle Back:  
    filtMid = (df['Level'] == experience) & (df['BodyPart'] == 'Middle Back')
    randomMid = df[filtMid]
    specificMid = randomMid.iloc[randomInt]['Title']
    pull.append(specificMid)
    #Forearms:
    filtFore = (df['Level'] == experience) & (df['BodyPart'] == 'Forearms')
    randomFore = df[filtFore]
    specificFore = randomFore.iloc[randomInt]['Title']
    pull.append(specificFore)
    return pull

def getPush(experience):
    df = pd.read_csv(r"C:\Users\raoad\OneDrive\Documents\Sophomore\Datasets\megaGymDataset.csv")
    randomInt = random.randint(0, 5)
    randomInt2 = random.randint(6, 9)
    #Chest:
    filtChest = (df['Level'] == experience) & (df['BodyPart'] == 'Chest')
    randomChest = df[filtChest]
    specificChest = randomChest.iloc[randomInt]['Title']
    specificChest2 = randomChest.iloc[randomInt2]['Title']
    push.append(specificChest)
    push.append(specificChest2)
    #Tri
    filtTri = (df['Level'] == experience) & (df['BodyPart'] == 'Triceps')
    randomTri = df[filtTri]
    specificTri = randomTri.iloc[randomInt]['Title']
    push.append(specificTri)
    #Shoulders
    filtShould = (df['Level'] == experience) & (df['BodyPart'] == 'Shoulders')
    randomShould = df[filtShould]
    specificShould = randomShould.iloc[randomInt]['Title']
    push.append(specificShould)
    return push

def getLegs(experience):  
    df = pd.read_csv(r"C:\Users\raoad\OneDrive\Documents\Sophomore\Datasets\megaGymDataset.csv")
    randomInt = random.randint(0, 5)
    randomInt2 = random.randint(6, 9)
    #Calves
    filtLegs = (df['Level'] == experience) & (df['BodyPart'] == 'Calves')
    randomLeg = df[filtLegs]
    specificLeg = randomLeg.iloc[randomInt]['Title']
    legs.append(specificLeg)
    #Hamstrings
    filtHam = (df['Level'] == experience) & (df['BodyPart'] == 'Hamstrings')
    randomHam = df[filtHam]
    specificHam = randomHam.iloc[randomInt]['Title']
    specificHam2 = randomHam.iloc[randomInt2]['Title']
    legs.append(specificHam)
    legs.append(specificHam2)
    #Quads
    filtQuads = (df['Level'] == experience) & (df['BodyPart'] == 'Quadriceps')
    randomQuad = df[filtQuads]
    specificQuad = randomQuad.iloc[randomInt]['Title']
    specificQuad2 = randomQuad.iloc[randomInt2]['Title']
    legs.append(specificQuad)
    legs.append(specificQuad2)
    return legs

def getFavorite(experience, fav_muscle): 
    df = pd.read_csv(r"C:\Users\raoad\OneDrive\Documents\Sophomore\Datasets\megaGymDataset.csv")
    randomInt = random.randint(0, 9)
    filtFavorite = (df['Level'] == experience) & (df['BodyPart'] == fav_muscle)
    randomFav = df[filtFavorite]
    specificFav = randomFav.iloc[randomInt]['Title']
    fav.append(specificFav)
    return fav