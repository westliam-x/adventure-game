import random

movement=0
move=["left","right"]
cloth=["fail","pass"]
clothopt=["suit", "raincoat", "battle"]
luck=["lightning fight","heaven","endless void","blazing sun","giant tanning saloon"]
end=["finish", "witch", "sword","loop"] 

print("This is your last chance to go back")

choice=input("Would you like to go back: ").lower()

if choice=="no":
    name=input("What is your name: ")
    print("Welcome", name ,"to this adventure")
else:
    quit()
    

while True:
    answer=input("You are on a dirty road you can ether go left or right choose wisely: ").lower()
    if answer not in move:
        print("Choose either left or right there is no other way!!!")
        continue
    
    any_L = random.randint(0,4)

    lpossi=luck[any_L]

    if answer=="left" and lpossi=="lightning fight":
        print("You got caught in a", lpossi ,"and died")
        print("Gameover!!!")
        print("You got", movement,"points")
        break
    
    elif answer=="left" and lpossi=="heaven":
        movement+=100
        print("You ended up in", lpossi, "tho it is paradise, you died but got", movement, "points")
        print("Gameover!!!")
        print("You got", movement,"points")
        break
    
    elif answer=="left" and lpossi=="endless void":
        print("You got caught in a", lpossi ,"and died")
        print("Gameover!!!")
        print("You got",movement, "points")
        break
    
    elif answer=="left" and lpossi=="blazing sun":
        print("You got caught in a", lpossi ,"and died")
        print("Gameover!!!")
        print("You got",movement, "points")
        break
    
    elif answer=="left" and lpossi=="giant tanning saloon":
        print("You got caught in a", lpossi ,"and died")
        print("Gameover!!!")
        print("You got",movement, "points")
        break
    
    elif answer=="right":
        print("You choose wisely and you are coming out of the dirty road")
        movement+=1
        clothes=input("Would you like a change of clothes?: ").lower()
        
        if clothes=="yes":
            preference=input("What type of clothing would you like? suit, raincoat, battle cloth(containing battle weapons)").lower()
            
            if preference not in clothopt:
                print("That is not an option")
                continue
            
            Rcloth = random.randint(0,1)
            
            possib = cloth[Rcloth]
            
            if preference=="suit" and possib=="fail":
                print("You stumbled and got stabbed with the poisinous pen and died. Gameover!!!")
                print("You got",movement, "points")
                break
            
            elif preference=="suit" and possib=="pass":
                print("You look dashing, 5 points for good fashion sense")
                movement+=5
                
            elif preference=="raincoat":
                print("Doesn't look too pleasant but at least nothing bad can happen")
                
            elif preference=="battle" and possib=="pass":
                print("You look ready for anything, test your readiness by entering into this portal and get extra 50 points if you come out alive")
                
                enter=input("Type yes to enter and no to continue this strange path: ")
                if enter=="yes" and possib=="fail":
                    print("looks like you were not ready, you died!!!!")
                    print("You got",movement,"points")
                    break
                
                elif enter=="yes" and possib=="pass":
                    movement+=50
                    print("looks like you were ready, you got 50 extra points")
                    
                elif enter=="no" and possib=="pass":
                    print("You did not show much bravery, but you can advance")
                    
                elif enter=="no" and possib=="fail":
                    print("looks like you tripped and got stabbed with a death knife, you died!!!!")
                    print("You got",movement,"points")
                    break
                
        else: print("suit yourself in those dirty clothes")
        
        nextp= input("You are approaching another path,would you go,left or right:").lower()
        if answer not in move:
            print("Choose either left or right there is no other way!!!")
            continue
        
        Rend = random.randint(0,3)
        
        ends = end[Rend]
        
        if nextp=="right" and ends=="finish":
            print("You finally made it out",name,"congratulations your final score is:", movement)
            break
        elif nextp=="right" and ends=="witch":
            print("You made it this far out but died because of a witch",name,"your final score is", movement)
            break
        elif nextp=="right" and ends=="sword":
            print("You finally made it out ",name,"congratulations but with you is the",ends,"of the king would you like to go on a quest to return it?")
            break
        elif nextp=="right" and ends=="loop":
            print("You have been renered into a loop",name,"start again,you have",movement,"points.")
            continue
        elif nextp=="left" and ends=="finish":
            movement+=5
            print("You finally made it out",name,"congratulations your final score is",movement)
            break
        elif nextp=="left" and ends=="witch":
            print("You made it this far out but died because of a witch",name,"your final score is", movement)
            break
        elif nextp=="left" and ends=="sword":
            print("You finally made it out ",name,"congratulations but with you is the",ends,"of the king would you like to go on a quest to return it?")
            break
        elif nextp=="left" and ends=="loop":
            movement-=movement
            print("You have been renered into a loop",name,"start again,you have",movement,"points.")
            continue

        
                    
            
                
