import random

title = "Crazy Ways to Die Quiz"
print(title)

TorF = "True or False"
print (TorF)
questions = {"Robert Taylor died in the grave he was digging at work?": True, "Wolfgang Amadeus Mozart died of Strep Throat?": True, "Tennessee Williams choked to death after inhaling a small plastic bottle cap": True, "Gordon L Harwell, aka Unckle Ben fell into a silo of his own rice and suffocated?": False, "Maria Connor died after a camel bit her on the face and its saliva entered the wound making it deadly toxic": False, "Jasper Vinall died by being struck in the forehead by a cricket bat being swung by the batsman trying to hit the ball a second time": True, "Alex Josey died by taking a drink servers tray as a snow sled and sliding off a 200ft cliff": False, "Adam Ricket died by choking on ramen noodles he stole from another in-mate, after his death penalty was commuted to life in prison": False, "Arius, died in 336AD after suffering from intense diarrhea, hemoraging and then expulsion of his lower intestines": True, "Cristopher Cole, a UK pop singer died by lighting stike on a golf coarse": False, "Sylvester Paul was a fruit and veggie vendor that died by being pummeled to death by a veggie pyramid display": False, "Catherine Macnamara died in after asking , Wonder who will be next, at a funeral. And was then overcome with a fatal seizure": True} 

def random_questions():
    for key in questions:
       print(key)
           
    
random_questions()
  
