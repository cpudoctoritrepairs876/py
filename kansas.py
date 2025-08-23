from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat,but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it in Kansas City.",
        "A considerable part of Kansas City is in Missouri.",
        "Most Kansans are annoyed by wizard oz references from people outside of Kansas"
    ]
    index = choice("0123")
    
    print(funfacts[int(index)])
    
if __name__ == "__main__":
    randomfunfact()    
    