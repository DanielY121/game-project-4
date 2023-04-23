#colour
class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(colour.BOLD + "The game is text-based.")
def WTB():
    return None

def End():
  print(colour.BOLD + colour.GREEN + "End" + colour.END)

def CEnd():
 print(colour.END)

#1
def Ch1():
  global choice1
  print("\033[1mChapter 1: Discovery \033[0m" + colour.BOLD + colour.BLUE)
  print("You are a young scientist called " + name + " who works in a secret laboratory, researching the possibility of time travel. Your boss is a mysterious man who only contacts you by phone and email, and he provides you with an advanced device called a time machine. You don't know his true identity or purpose, but you are curious and passionate about time travel.")
  print("One day, you perform a test in the laboratory and you set the time machine to jump backwards by one hour. You press the button and feel a wave of dizziness. When you open your eyes, you find yourself still in the lab, but everything has changed. You see another " + name + ", dressed in different clothes, operating the time machine. He looks surprised to see you and says to you:")
  print(colour.END + colour.PURPLE + 'Another ' + name + '  said "Who are you? How did you get in here?"' + colour.END + colour.BLUE)
  print("At that moment, you hear an alarm and the door of the laboratory is locked. You realise you may have done something wrong and you try to escape, but it's too late. You are trapped in this parallel universe, face to face with your other self." + colour.END)
  print("What do you do?" + colour.GREEN)
  print("A) Try to work with another " + name + " to find out what's going on.")
  print("B) Try to take over another " + name + "'s time machine and return to the original universe. ")
  print("C) Try to hide your identity and pretend to be a colleague of another " + name + colour.END)
  choice1 = input("Type A, B, C or End: ")

#2
def Ch2():
 print("\033[1mChapter 2:Conspiracy \033[0m" + colour.BOLD + colour.BLUE)
#3
def Ch3():
 print("\033[1mChapter 3: Disaster \033[0m" + colour.BOLD + colour.BLUE)
#4
def Ch4():
 print("\033[1mChapter 4: The Truth \033[0m" + colour.BOLD + colour.BLUE)

#SpIn stands for Special Input
def SpIn1():
  input("Press enter to continue...")
  
#2A
def Ch2A():
  Ch2()
  print("You work with another " + name + " to find out what is going on.")
  print("You discover that the time machine has a hidden function that allows you to switch between different timelines. ")
  print("You also discover that your boss is actually the leader of an evil organisation that uses the time machine to change history and realise his ambitions.")
  print("He has sent some agents after you to stop you from revealing his plans.")
  print("You must find a way to stop his plot and return to the original universe.")
  CEnd()
  SpIn1()
  Ch3A()

#3A
def Ch3A():
 Ch3()
 print("You work with another you to stop the boss's plot and return to the original universe." )
 print("You discover that the boss's goal is to start a global nuclear war and then use the time machine to escape to a safe timeline. ")
 print("You must break into his base, destroy his time machine and arrest him before he activates the nuclear bomb. But it won't be easy, because he has many guards and traps.")
 print("You must risk your lives to complete this mission.")
 CEnd()
 SpIn1()
 Ch4A()

#4A
def Ch4A():
  Ch4()
  print("You and another " + name + " will successfully stop the boss's plot and return to the original universe.")
  print("You find that peace and stability have been restored to the original universe and that there is no nuclear war.")
  print("You also discover that the boss is actually a criminal from the future who has escaped to the past using a time machine in an attempt to change history.")
  print("You have brought his crimes to light and brought him to justice.")
  print("You also discover that you and another " + name + " are actually one person, but that you have been divided by time travel.")
  print("You decided to merge into one person and destroy the time machine to avoid further confusion.")
  CEnd()
  SpIn1()
  Ch5A()

#5
def Ch5():
  print("\033[1mChapter 5: Choices \033[0m" + colour.BOLD + colour.BLUE)

#5A1
def Ch5A1():
  print(colour.BOLD + colour.BLUE + "You married a girl.")
  print("You have a lovely child.")
  print("You live happily together until you die of old age.")
  CEnd()
  End()
  SpIn1()
  Ch1()

#5A2
def Ch5A2():
  print(colour.BOLD + colour.DARKCYAN + "You break up with the girl.")
  print("This is because she found out your secret.")
  print("She thinks you're a monster and calls the police.")
  print("You are arrested and sent to a mental hospital.")
  CEnd()
  End()
  SpIn1()
  Ch1()

#5A
def Ch5A():
 Ch5()
 print("You merge with another " + name + " as a person and destroy the time machine. ")
 print("You return to your normal life and enjoy peace and happiness. ")
 print("You also meet a beautiful girl who falls in love with you at first sight, and you soon fall in love. ")
 print("You feel that this is the right choice for you." + colour.END + colour.GREEN)
 print("A1) You married a girl")
 print("A2) You break up with the girl")
 CEnd()
 choice2a = input("Type A1 or A2: ")
 if choice2a.upper == "A1":
   Ch5A1()
 elif choice2a.upper == "A2":
   Ch5A2()
 elif choice2a.upper == "a1":
   Ch5A1()
 elif choice2a.upper == "a2":
   Ch5A2()

#2B
def Ch2B():
  Ch2()
  print("You try to seize another time machine of your own and return to the original universe.")
  print("However, you discover that the time machine has a combination lock that only another " + name + " knows.")
  print("You must find a way to get the code from him or find another way to escape.")
  print("At the same time, you discover the conspiracy of the boss and the agents he has sent.")
  print("You must be careful to avoid being discovered and caught.")
  CEnd()
  SpIn1()
  Ch3B()

#3B
def Ch3B():
 Ch3()
 print("You try to capture another " + name + "'s time machine and return to the original universe.")
 print("However, you discover that another " + name + " is unwilling to give up the time machine, which he considers to be his property.")
 print("A battle ensues between you, and you attack and deceive each other.")
 print("In the process, you accidentally trigger the Time Machine's self-destruct mechanism, causing it to explode and create a rift in space-time.")
 print("This rift sucks you into an unknown timeline and you find yourselves in the ruins of a nuclear war.")
 CEnd()
 SpIn1()
 Ch4B()

#4B
def Ch4B():
  Ch4()
  print("You are trapped in the ruins of a nuclear war with another " + name + ".")
  print("You discover that this timeline is the result of a nuclear war started by the boss, who has escaped to another timeline.")
  print("You also discover that this timeline is in fact your original universe, but that it has been altered by time travel.")
  print("You regret your choice and try to find a way to go back in time, stop the boss's plot and restore the original history.")
  CEnd()
  SpIn1()
  Ch5B()

#5B
def Ch5B():
  Ch5()
  print("You have found a broken time machine with another " + name + " and tried to fix it.")
  print("You succeed in going back in time, stopping the boss's plot and restoring the original history.")
  print("However, you find yourselves unable to return to your own timeline because the time machine is broken.")
  print("You are trapped in a strange timeline and don't know what will happen.")
  print("You think this is a good choice, but you are also a bit sad." + colour.END + colour.GREEN)
  print("B1) You become good friends with another " + name + ".")
  print("B2) You and another " + name + " have become enemies.")
  CEnd()
  choice2b = input("Type B1 or B2: ")
  if choice2b.upper == "B1":
   Ch5B1()
  elif choice2b.upper == "B2":
   Ch5B2()
#5B1 
def Ch5B1():
  print(colour.BOLD + colour.BLUE + "In this timeline, you find a new job.")
  print("You adapt to the timeline and live happily.")
  End()
  SpIn1()
  Ch1()

#5B2
def Ch5B2():
  print(colour.BOLD + colour.DARKCYAN + "In this timeline, competing and fighting with each other.")
  print("You cannot stand the existence of the other, and want to destroy it.")
  print("You want to destroy each other.")
  End()
  SpIn1()
  Ch1()

#2C
def Ch2C():
  Ch2()
  print("You try to hide your identity and pretend to be a colleague of your own.")
  print("However, this is not easy, because another " + name + " soon discovers your anomaly. ")
  print("He becomes suspicious of you and tries to find out what you are really up to.")
  print("At the same time, you discover the boss's conspiracy and the agents he has sent.")
  print("You must find a way to convince another " + name + " to trust yourself, or find another way to escape." + colour.END)
  CEnd()
  SpIn1()
  Ch3C()

#3C
def Ch3C():
  Ch3()
  print("You find that another " + name + " is becoming increasingly distrustful of you, and he begins to spy on you and investigate you.")
  print("He finds out who you really are and what you are up to, and decides to report it to his boss.")
  print("He thinks that this will earn him the trust and reward of his boss.")
  print("However, he does not know that the boss is in fact an evil man who will not thank him but will kill him.")
  print("When he takes you to see the boss, he has already activated the nuclear bomb and is ready to escape.")
  print("He shoots both of you and jumps into the time machine.")
  CEnd()
  SpIn1()
  Ch4C()

#4C
def Ch4C():
  Ch4()
  print("You and another " + name + " will be shot by the boss and watch as he jumps into the time machine and escapes.")
  print("You discover that the boss has started a nuclear war and that the whole world has been plunged into chaos and destruction.")
  print("You also discover that the boss is in fact an invader from a parallel universe, using the time machine to destroy different timelines to achieve his plan of conquest.")
  print("You realise you have been tricked and try to find a way to track down the boss, stop his invasion and save the world.")
  CEnd()
  SpIn1()
  Ch5C()

#5C
def Ch5C():
  Ch5()
  print("You and another " + name + " will track down the boss, stop his invasion and save the world.")
  print("You discover that the boss is in fact a being from the fourth dimension, who can travel freely between timelines.")
  print("He wants to destroy all three dimensions and make the fourth dimension the only reality. ")
  print("You must use the time machine to follow him to the fourth dimension and fight him in the final battle.")
  print("You find this a very dangerous and exciting choice, but also a little exciting." + colour.END + colour.GREEN)
  print('C1) You will fight against the boss withanother ' + name)
  print('C2) You will be fighting against your boss with another ' + name)
  print('C3) You will fight the boss with another ' + name)
  CEnd()
  choice2c = input("Type C1 , C2 or C3: ")
  if choice2c.upper == "C1":
   Ch5C1()
  elif choice2c.upper == "C2":
   Ch5C2()
  elif choice2c.upper == "C3":
   Ch5C3()

#5C1
def Ch5C1():
  print(colour.BOLD + colour.BLUE + "Successfully defeating the boss and save all the timelines.")
  print("You become heroes and are admired and thanked by the people.")
  print("You also discover the fourth dimension and it is a beautiful and magical place where you can explore and learn freely.")
  print("You feel that this is a perfect ending.")
  print("You feel very proud and satisfied.")
  CEnd()
  End()
  SpIn1()
  Ch1()
 

#5C2
def Ch5C2():
  print(colour.BOLD + colour.DARKCYAN + "You watch in defeat as he destroys all timelines.")
  print("You will be confronted by another " + name + " and the boss.")
  print("The last thought before you die is regret and fear.")
  print("You feel that this is the worst possible outcome.")
  print("You feel very sad and hopeless.")
  CEnd()
  End()
  SpIn1()
  Ch1()

#5C3
def Ch5C3():
  print(colour.BOLD + colour.DARKCYAN + "You have fought the boss to a draw.")
  print("You are trapped in the fourth dimension.")
  print("You are unable to return to your own timeline.")
  print("There is no way to stop the boss's invasion.")
  print("You are left to languish in the fourth dimension, waiting for death.")
  print("You think it's a bad ending, but there's nothing you can do to change it but there's nothing you can do to change it.")
  CEnd()
  End()
  SpIn1()
  Ch1()

#Main
choice1 = None 
while True:
    if choice1 == None:
        name = input("Please enter you name")  
        Ch1()
    elif choice1.upper() == "A":
        Ch2A()
    elif choice1.upper() == "B":
        Ch2B()
    elif choice1.upper() == "C": 
        Ch2C()
    elif choice1.upper() == "END":
        print(colour.GREEN + "End progress...")
        CEnd()
        break