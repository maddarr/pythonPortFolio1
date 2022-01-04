import random

title = "Crazy Ways to Die Quiz"
print(title)
questions = [["Robert Taylor died in the grave he was digging at work?", True], ["Wolfgang Amadeus Mozart died of Strep Throat?", True], ["Tennessee Williams choked to death after inhaling a small plastic bottle cap", True], ["Gordon L Harwell, aka Unckle Ben fell into a silo of his own rice and suffocated?", False]]
def random_question():
    questions.random()
    
print(random_question())   
