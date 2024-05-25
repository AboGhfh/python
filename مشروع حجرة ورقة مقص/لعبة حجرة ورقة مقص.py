import random
print('Welcome to the Rock🧱, Paper📜, Scissors✂ game:','\n ----------------------------------------------')
user_Help = input('Prees Enter Continun or type (Help) forthe rules: ')
if user_Help.lower() == 'help':
    print('---------------------------------------'
    ,'\n        ******** RULES ********        '
    ,'\n        1) You choose and the computer choose'
    ,'\n        2) Rock smashis Scissors -> Rock wins'
    ,'\n        3) Scissors cut Paper -> Scissors win'
    ,'\n        4) Paper covers Rock -> Paper wins'
    ,'\n------------------------------------------')
user = input("Choose Rock🧱 or Paper📜 or scissors✂ ").capitalize()
Paper = """
                _ _ _ _ _ _ _ _ _
    _ _ _ _ _ _'    _ _ _ _ _ _ _)_ _ _ _ _ _
                            _ _ _ _ _ _ _ _ _)_
                                _ _ _ _ _ _ _ _)
    _ _ _ _ _ _             _ _ _ _ _ _ _ _ _)
               '_ _ _ _ _ _ _ _ _ _ _ _ _ _)    
    """
Rock = """
                _ _ _ _ _ _
    _ _ _ _ _ _'   (_ _ _ _)_ _ _ _ _ _
                           (_ _ _ _ _ _)
                           (_ _ _ _ _ _ _)
    _ _ _ _ _ _            (_ _ _ _ _ _ )
               '_ _ _ _ _ _(_ _ _ _ _ )    
    """
Scissors ="""
                _ _ _ _ _ _ _ _ _
    _ _ _ _ _ _'    _ _ _ _ _ _ _)_ _ _ _ _ _
                            _ _ _ _ _ _ _ _ _)_
                        _ _ _ _ _ _ _ _ _ _ _ _)
    _ _ _ _ _ _        (_ _ _ _ _ _ _)
               '_ _ _(_ _ _ _ _ _ _)    
    """
if user == "Paper":
    user = Paper
elif user == "Rock":
    user = Rock
elif user == "Scissors":
    user = Scissors
else:
    if user:
        print("Error:❌")
    else:
        print("Error:❌")
game = [Paper,Rock,Scissors]
pc = random.choice(game)
if user == pc:
     print('user:😎'
        ,'\n-------------------------------------------------------'
        ,f"\n{user}"
        ,'\n-------------------------------------------------------'
        ,'\nPC:💻'
        ,'\n--------------------------------------------------------'
        ,f'\n{pc}'
        ,'\n------------------------------------------------------'
    ,'\nDraw:🤝')
elif user == Paper and pc == Rock or user == Rock and pc == Scissors or user == Scissors and pc == Paper:
    print('user:😎'
        ,'\n-------------------------------------------------------'
        ,f"\n{user}"
        ,'\n-------------------------------------------------------'
        ,'\nPC:💻'
        ,'\n--------------------------------------------------------'
        ,f'\n{pc}'
        ,'\n------------------------------------------------------'
    ,'\nthe winner is:user😎')
else:
     print('user:😎'
        ,'\n-------------------------------------------------------'
        ,f"\n{user}"
        ,'\n-------------------------------------------------------'
        ,'\nPC:💻'
        ,'\n--------------------------------------------------------'
        ,f'\n{pc}'
        ,'\n------------------------------------------------------'
    ,'\nthe winner is:PC💻')