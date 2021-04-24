<<<<<<< HEAD
import time
import random

def intro():
    time.sleep(1)
    print("\n\t\t\t\t\t\t    ----------------------------------------------------------------------------------------")
    print("===========================|          Welcome to simulating a typical day in a high school students life!           |===========================")
    print("\t\t\t\t\t\t    ----------------------------------------------------------------------------------------")
    time.sleep(5)
    print("- This game is meant to give you an insight on some of the important decisions you make, even as a student studying from home!")
    time.sleep(5)
    print("- Habits are one of the most important aspects of human beings, but the pandemic has disrupted our routines and forced us to create new habits,   some we may not even realize!")
    time.sleep(6)
    print("- Quick disclaimer: this game is an overgeneralization, and there are obviously many more decisions and factors that go on in your day.") 
    time.sleep(5)
    print("  So don't take this TOO seriously, but try to learn a thing or two about yourself!")
    time.sleep(5)
    print("- Try to answer honestly on the first try, you will get to simulate another day to try and improve your habits!")
    time.sleep(5)
    

def wake_up():
    pass





intro()
new_day = input("When you are ready to play, type 'yes': ")

while new_day[0] == "y":
    


    
    new_day = input("Would you like to start a another day? (yes/no)")

print("Thank you for playing!") 
print("Again, we want to remind you that some of these factors that we mentioned can simply just be out of your control.")
print("But there are always things we can improve on, and the key here is constantly improving ourselves!")
print("Hopefully you learned a few healthy habits that you want to implement for yourself. Now, back to the real world! Bye bye!")
=======
import time
import random

def intro():
    time.sleep(1)
    print("\n\t\t\t----------------------------------------------------------------------------------------")
    print("\t\t\t|         Welcome to simulating a typical day in a high school students life!          |")
    print("\t\t\t----------------------------------------------------------------------------------------")
    time.sleep(4)
    print("- This program is meant to give you an insight on some of the important decisions you make, even as a student studying from home!")
    time.sleep(4)
    print("- Habits are one of the most important aspects of human beings, but the pandemic has")
    time.sleep(4)
    print("- Try to answer honestly on the first try, you will get to simulate another day to try and improve your habits!")
    time.sleep(4)

def wake_up():
    pass





intro()

new_day = "yes"
while new_day == "yes" or new_day == "y":
    


    
    new_day = input("Would you like to start a another day? (yes/no)")

print("Thank you for playing!") 
print("Again, we want to remind you that some of these factors that we mentioned can simply just be out of your control.")
print("But there are always things we can improve on, and the key here is constantly improving ourselves!")
print("Hopefully you learned a few healthy habits that you want to implement for yourself. Now, back to the real world! Bye bye!")
>>>>>>> origin/main
