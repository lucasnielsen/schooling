import random

choices = ["rock", "paper", "scissors"]


while True:
  
  random_choice = random.choice(choices)
  print("please choose; rock, paper, or scissors!")

  choice = input()

  if choice == random_choice:
    print("tie! ai chose", random_choice)
  else:
    if choice == "scissors":
      if random_choice == "paper":
        print("you win! ai chose", random_choice)
      else:
        print("you lose! ai chose", random_choice)
    
    if choice == "rock":
      if random_choice == "scissors":
        print("you win! ai chose", random_choice)
      else:
        print("you lose! ai chose", random_choice)

    if choice == "paper":
      if random_choice == "rock":
        print("you win! ai chose", random_choice)
      else:
        print("you lose! ai chose", random_choice)
