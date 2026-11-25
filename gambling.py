import random

money = 100
event = 0
event1 = 0
shitting = 0
HOMEEVENT = 0
home4 = 0
vipreds2 = 0

while money > 0:
    howmuch = float(input(f"enter how much: "))
    half = howmuch * 0.5
    double = howmuch * 3
    gamble = random.uniform(half, double)
    if money < howmuch:
        print("enter a real amount")
        gamble = 0
        howmuch = 0
    money -= howmuch
    money += gamble
    print(f"you won: {gamble}")
    print(f"money: {money}")
    if money <= 0:
        print("come back with more money you broke lil shit")
        break

    if event == 0:
        if money >= 25689:
            woman = input("hello lil one wanna come home with me im very hot soo please: 1. yes      2. fuck no: ")
            event = 1
            if woman == "1":
                print("you went home with her and magic happend and when you woke up your money was gone and she was gone to(thats fucking crazy tbh like fucking imagine like bro what just no way you wierdo)")
                break
            if woman == "2":
                print("because your a good boy you said fuck off and went back to playing")
    if money >= 1000000:
        event1 = 1
        win = input("you fucking shit you bankrupted my casino and im hard so give me a milkshake and fuck off you made me broke get out you stupid lil bitch (walter white: its actually a he sir its not a woman) shut up (you won. you got the normal? ending)")
        win2 = input("do you wanna go home.(1 yes. 2 no): ")
        if win2 == "1":
            print("you went home and you felt somethings off like your missing someone and then your annoying FUCKING WIFE COMES IN YOUR ROOM AND STARTS YAPPING ABOUT I GOTTA SHAVE MY HAIRY BALLS")
            break
        if win2 == "2":
            win3 = input("you go to the casino and you buy it and take a huge shit in the toilet like i mean A FUCKING BIGGER ONE THAN GODZILLA LIKE ITS HUGE and then you go home and your wife starts yapping ABOUT HOW AM SOOOOO HOMOSEXUAL TOWARDS MEN LIKE WHAT ARE YOU ON ABOUT")
            break
    if shitting == 0:
        if money >= 100000:
            shitting = 1
            shit = input("you start to shit yourself because you got to excited: ")
            print("you start peeing yourself")
    if HOMEEVENT == 0:
        if money >= 1000:
            HOMEEVENT = 1
            home = input("wanna go home 1. yes 2. no: ")
            if home == "1":
                print("you go home and YOUR FUCKING ANNOYING WIFE STARTS TALKING ABOUT SHOPPING AND THAT IM SOOOOOO ANNOYING LIKE WHAT THE FUCK DO YOU MEAN YOUR THE ONE WHOS ANNOYING (vipeds calling) oh its vipreds (vipreds: i love bread and needles to stick them up my FUCKING ASS) YOU FUCKING PSYCHOPATH STOP CALLING ME (vipreds: calm down bro i love needles and bread to stick up peoples asses no need to worry) LIKE ARE YOU MENTAL OK MAN FUCK THIS IM OUT")
                break
            if home == "2":
                print("im gonna fucking explode AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH I FUCKING DONT WANNA DO THIS PLEASE LIKE BRO WHAT THE FUCK ARE YOU DOING I WANNA G O O N IN PEACE AT HOME I FUCKING HATE YOU LIKE WHAT THE FUCK MAN AND YES IM BREAKING THE 4 WALL ok bro im gay ahhhh im ooo im tired allright oooo")
    if home4 == 0:
        if money >= 10000:
            home4 = 1
            vipreds = input("(VipReds Calling) yoo man its vipreds (VipReds: yooooo man i see you got 10k Congrats uhhh i slept with your wife i hope your okay with it uhhhh ALLRIGHT THIS IS GETTING AKWARD UHHHH BYE) -WAIT WHAT... MAN HE HANG UP ON ME")
            print("awww my life sucks yk what fuck vipreds ima gamble instead")
    if vipreds2 == 0:
        if money >= 20000:
            vipreds2 = 1
            vipredsphone = input("(VipReds Calling) (VipReds: and yeah i frogot to tell you your wife is pregnant congrats we are dads) ---WAIT WHA... and he hanged up on me again")
            print("that lil bastard")