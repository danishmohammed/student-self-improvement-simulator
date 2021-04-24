import time
import random
from rich.console import Console

console = Console()
prompts = {}
def intro():
    time.sleep(1)
    print("\n\t\t\t   ---------------------------------------------------------------------------------")
    print("===============|             Welcome to a day in the life of a high school student!            |================")
    print("\t\t\t   ---------------------------------------------------------------------------------")
    time.sleep(5)
    print("- This decision-based game is meant to give you an insight on some of the important decisions you make, even as a student studying from home!")
    time.sleep(5)
    print("- Habits are one of the most important aspects of human beings...")
    time.sleep(3)
    print("  but the pandemic has disrupted our routines and forced us to create new habits, some we may not even realize!")
    time.sleep(5)
    print("- Quick disclaimer: this game is an overgeneralization, and there are obviously many more decisions and factors that go on in your day.") 
    time.sleep(5)
    print("  So don't take this TOO seriously, but try to learn a thing or two about yourself, and have some fun!")
    time.sleep(5)
    print("- Try to answer honestly on the first try, and you will get to simulate another day to try and improve your habits!")
    time.sleep(5)
    

def wake_up():
    print("")

def breakfast():
  pass

def first_class():
  pass



def after_school():
  pass


intro()
new_day = input("\nWhen you are ready to play, click the rectangle on the right and type 'yes': ")

while new_day[0] == "y":
  mood = 7
  productivity = 7
  energy = 7
  fitness = 7

  wake_up()
  print("\nFinal stats for the day:")
  print("Mood: " + str(mood) + "/10")
  print("Energy: " + str(energy) + "/10")
  print("Productivity: " + str(productivity) + "/10")
  print("Fitness: " + str(fitness) + "/10")
  new_day = input("Would you like to start a another day? (yes/no) ")


print("Thank you for playing!") 
print("Again, we want to remind you that some of these factors that we mentioned can simply just be out of your control.")
print("But there are always things we can improve on, and the key here is constantly improving ourselves!")
print("Hopefully you learned a few healthy habits that you want to implement for yourself. Now, back to the real world! Good luck!")
