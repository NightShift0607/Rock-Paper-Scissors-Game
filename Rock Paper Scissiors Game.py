import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

while True:
    Assets = [rock, paper, scissors]
    pchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if pchoice>2 or pchoice<0:
        print('Invalid choice')
    else:
        cchoice = random.randint(0,2)
        if pchoice == cchoice:
            result = "It's a Draw"
        elif pchoice == 1 and cchoice == 0:
            result = "You Won!"
        elif pchoice == 2 and cchoice == 1:
            result = "You Won!"
        elif pchoice == 0 and cchoice == 2:
            result = "You Won!"
        else:
            result = "Computer Won!"
        print(Assets[pchoice])
        print("\nComputer chose:\n")
        print(Assets[cchoice])
        print(result)
    r = input("Do you want to play again? Y/N: ")
    if r.upper() == 'N':
        break
    if r.upper() == 'Y':
        continue
    if r.upper != 'N' or 'Y':
        print("Write 'Y' or 'N' only")
        r = input("Do you want to play again? Y/N: ")
