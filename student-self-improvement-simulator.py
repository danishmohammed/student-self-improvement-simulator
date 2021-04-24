import time 
import random
from rich.console import Console #for visual text formatting

console = Console() #console object
prompts = {}
def intro(): #the introduction to the game
    time.sleep(1) #for pauses between messages
    console.print("[red]\n\t\t--------------------------------------------------------------------------------[/red]")
    console.print("[red]================[/red][bold red]|[/bold red]                  [green]Welcome to a day in the life of a student![/green]                  [bold red]|[/bold red][red]===============[/red]")
    console.print("[red]\t\t--------------------------------------------------------------------------------[/red]")
    time.sleep(1)
    print("\n- This decision-based game is meant to give you an insight on some of the important decisions you make, even as a student studying from home!")
    time.sleep(1)
    console.print("- [yellow]Habits[/yellow] are one of the most important aspects of human beings...")
    time.sleep(1)
    console.print("  but the [cyan]COVID-19 pandemic[/cyan] has disrupted our routines and forced us to create new habits, some we may not even realize!")
    time.sleep(1)
    console.print("- [red]Quick disclaimer[/red]: this game is an overgeneralization, and there are obviously many more decisions and factors that occur in your day.") 
    time.sleep(1)
    print("  So don't take this TOO seriously, but try to learn a thing or two about yourself, and have some fun!")
    time.sleep(1)
    console.print("- Try to answer [green]honestly[/green] on the first try, and you will get to simulate another day to try and improve your habits!")
    time.sleep(1)
    

def wake_up():

  console.print("[red]BEEP! BEEP! BEEP![/red] Good morning! You just woke up from bed and your school day alarm is going off. How do you start off your day?\n")
  print("(1) Snooze... and snooze again!", "(2) Check my phone! I have a whole night's worth of texts and posts to check!", "(3) Dismiss my alarm and go to the washroom to brush my teeth.", sep='\n')
  wake_up_reply = input("(Enter 1,2 or 3): ")
  while wake_up_reply != "1" and wake_up_reply != "2" and wake_up_reply != "3":
       wake_up_reply = input("Invalid input. Please enter 1, 2, or 3: ")

  if wake_up_reply == "1":
    print("You decide to snooze. After all, there's still an hour until school...")
    time.sleep(3)

    snooze_random = random.randint(1,2)
    if snooze_random == 1:
      print("In what seems like seconds later, you look up at the clock and you're 15 minutes late for your first  class!")
      time.sleep(2)
      print("You groggily reach towards your phone and tell Siri, your virtual assistant, 'Hey Siri, join my first period class.'")
      time.sleep(2)
      print("You join just as your teacher calls your name for attendance.") 
      print("You are glad that you enabled the Siri shortcut to automatically join your Google Meet call. You wonder if other devices have this feature too...")
      print("You try to regain conciousness while the teacher finishes the rest of the attendance.")
    else:
      print("After you snooze for the second time, you finally force yourself out of bed.")
      time.sleep(3)
      print("You get up, tired, and scan the clock. There are 20 minutes until your first period class starts")
      time.sleep(3)
      print("You really want to go back to sleep, but you end up walking around for a few minutes.")
  
  elif wake_up_reply == "2":
    print("You check your phone. You only have a few message notifications, but you decide to go on every app anyways just to feel productive.")
    time.sleep(3)
    print("You don't really feel the best, and on top of that, it seems like there is too much content from your phone to handle your already tired mind.")
    time.sleep(3)
    print("You look at the time and 30 minutes have passed by! You come back to your senses and realize you were scrolling through Instagram again. You scroll back up and count more than 50 posts you mindlessly looked at.")
    time.sleep(3)
    print("'UGHH', you tell yourself. 'How could this get any worse?!'")
    time.sleep(3)
    print("You put your phone away and look away. Suddenly, you feel dizzy, probably from staring at a screen first thing in the morning.")
    time.sleep(3)
    print("Angry, you flop back into bed and lie there for a few minutes.")
  
  elif wake_up_reply == "3":
    print("You get up and turn off your alarm.")
    time.sleep(3)
    print("You are somewhat tired, and think that you would be better off sleeping for a few more minutes. Nonetheless, you force yourself to the washroom.")
    time.sleep(3)
    print("After you wash your face, you suddenly feel much more awake.")
    time.sleep(3)
    print("You stretch for a bit and take some fresh air from outside.")
    time.sleep(3)
    print("Now that your mind is a bit more clear, you start to plan out your day.")
    time.sleep(3)
    print("You remember some forms you still have to fill out and the rest of the math homework you have to do.")
    print("You boot up your computer and get to work. After you fill out your forms, your mind is a bit more alert and ready for math homework.")
    time.sleep(3)
    print("You do your math homework for about 25 minutes, then take a 5 minutes break (also known as the Pomodoro technique)")
    time.sleep(3)
    print("You can't believe how much you got done!")
    time.sleep(3)
    print("You also note how quiet it is. No distractions, no phone notifications, nothing.")
    time.sleep(2)
    print("You attribute this to your productivity.")

def breakfast():
  time.sleep(3)
  print("Suddenly, you feel a pang of hunger, you need to eat something. What's for breakfast?")
  breakfast_reply = input("(1) My favourite cereal! Although I still haven't checked how much sugar it has", "(2) Anything I can get, a granola bar usually or nothing really, I never have time for breakfast!", "(3) Oatmeal, eggs, and toast! Or something else along the lines of that.", "(Enter 1,2 or 3): ", sep='\n')
  while breakfast_reply != "1" and breakfast_reply != "2" and breakfast_reply != "3":
    wake_up_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  
  if breakfast_reply == "1":
    



def first_class():
  pass

def after_school():
  pass


intro()
new_day = console.input("\nWhen you are ready to play, click the rectangle on the right and type 'yes': ")

while new_day[0] == "y":
  mood = 0
  productivity = 0
  energy = 0
  fitness = 0

  wake_up()
  breakfast()
  print("\nFinal stats for the day:")
  print("Mood: " + str(mood) + "/10")
  print("Energy: " + str(energy) + "/10")
  print("Productivity: " + str(productivity) + "/10")
  print("Fitness: " + str(fitness) + "/10")
  new_day = console.input("\nWould you like to start a another day? ([green]yes[/green]/[red]no[/red]) ")


print("Thank you for playing!") 
print("Again, we would like to remind you that some of these factors that we mentioned can simply just be out of your control.")
print("But there are always things we can improve on, and the key here is constantly improving ourselves!")
print("Hopefully you learned a few healthy habits that you want to implement for yourself. Now, back to the real world! Bye-bye!")
