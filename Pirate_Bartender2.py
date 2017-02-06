import random   

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

answers = {}
drink = []

def Customer_Ask ():
    #Captures y/n answers to customers drink preferences and build the "answers" dictionary
    strongq = input(questions["strong"]).lower()

    if strongq == "y" or strongq == "yes" :
        answers["strong"] = True
    
    else:
        answers["strong"] = False   
        

    saltyq = input(questions["salty"]).lower()

    if saltyq == "y" or saltyq == "yes":
        answers["salty"] = True

    else: 
        answers["salty"] = False
    

    bitterq = input(questions["bitter"]).lower()

    if bitterq == "y" or bitterq == "yes":
        answers["bitter"] = True

    else: 
        answers["bitter"] = False
    

    sweetq = input(questions["sweet"]).lower()

    if sweetq == "y" or sweetq == "yes":
        answers["sweet"] = True

    else: 
        answers["sweet"] = False
    

    fruityq = input(questions["fruity"]).lower()

    if fruityq == "y" or fruityq == "yes":
        answers["fruity"] = True

    else: 
        answers["fruity"] = False

if __name__ == '__main__':
	Customer_Ask()


for choice in answers:
    if answers[choice] != False: 
        drink +=(choice,)
  
if len(drink)>0: 
    print("I'll make Ye drink wit da followin': ")
else:
    print ("Looks like you're not thirsty!")

        
def Customer_Drink(drink):
    for item in drink:
        if len(drink) > 0: 
            drink = (ingredients[item])
            print (random.choice(drink))

if __name__ == '__main__':
	Customer_Drink(drink)

        

