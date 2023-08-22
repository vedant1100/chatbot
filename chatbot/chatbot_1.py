username = input("Enter your name: ")
print("Hello "+ username+" TechGen at your service")
print("     To say 'hi'press 1")
choice_number=int(input("enter your choice :"))

if(choice_number==1):
    print(username+" - hi")
else:
    print("I would request you to fill the choose the given options only.")
print ("TechGen - how are you "+username)
print("     To reply I am fine how are you? press 1")
print("     To reply I am not doing fine, Tell me about you press 2")
choice_number2=int(input("Enter Your choice :"))


if(choice_number2==1):
    print(username+": I am fine how are you")
elif(choice_number2==2):
    print(username+": I am not doing fine, Tell me about you")
else:
    print("I am just created dont get your hopes high")
if(choice_number2==1):
    print("TechGen: nice... So what brings you here you bored?")
elif(choice_number2==2):
    print("Fujiwara: Oh, We can talk have a chat with me and i know you will be fine.... I promise you that... So, what do you wanna know about me?")
if(choice_number2==1):
    print("     To reply- Yes I am bored can u suggest me some movies ? press 1"  )
    print("     To reply- yes can I get some music suggestions from you? press 2")
    choice_number3=int(input("Enter your choice :"))
    if(choice_number3==1):
        print(username+":Yes I am bored can u suggest me some movies")
    elif(choice_number3==2):
        print(username+": yes can I get some music suggestions from you?")
    else:
        print("error")

    if(choice_number3==1):
        print("TechGen - Sure....")
        print("         1. Avengers EndGame""\n""2.Titanic""\n""3.Joker""\n""4.Inception""\n""5.Interstellar""\n""6.Harry Potter Series""\n""7. Lord of the Rings Trilogy""\n""8.Transpoter Series""\n""9.The Martian""\n""10.Avatar")
    elif(choice_number3==2):
        print("TechGen - You got it Senpai..")
        print("         1.Enzo""\n""2.Positions""\n""3.34+35""\n""4.POV""\n""5.Bodak Yellow""\n""6.I like it""\n""7.I do""\n""8.Money""\n""9.Therefore I am""\n""10.Lovely")
        print("I love Ariana and Cardi hope you like my taste...")
    else:
        print("Error")
elif(choice_number2==2):
    print("    To reply - How old are you and how were you created?   press 1")
    print("    To reply - You like Anime?   Press 2")
    choice_number4=int(input("Enter your choice:"))
    if(choice_number4==1):
        print(": How old are you and how were you created")
    elif(choice_number4==2):
        print(username+": You like Anime?")
    else:
        print("Error")
    if(choice_number4==1):
        print("TechGen - Well I was created recently by the group of intellectuals And about my age I am a girl i cant answer that lol ;)")
    elif(choice_number4==2):
        print("TechGen - HAhahahahahah.... I love Anime I mean i was named after a Anime Character lol ;)")
    else:
        print("Error")
if(choice_number2==1):
    print("    To reply: Thanks.....    press 1.")
    choice_number5=int(input("Enter Your choice:"))
    if(choice_number5==1):
        print(username+":Thanks......")
        if(choice_number4==1):
            choice_number7=int(input("Enter your choice"))
            print("To reply Tell me a fun fact press 1 ")
            print("To reply suggest me some anime press 2")
        if(choice_number7==1):
            print(username+"Tell me FunFact")
        elif(choice_number==2):
            print(username+"Suggest me some Anime")
        else:
            print("Error")
        if(choice_number7==1):
            print("TechGen=Hunting unicorns is legal in Michigan.")
        elif(choice_number7==2):
            print("TechGen- 1) One Piece""\n""2)Hunter x Hunter""\n""3) Akamega kill""\n""4)Fullmetal Alchemist""\n""5) Deathnote")
        else:
            print("error")