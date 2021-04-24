import time 
import random
from rich.console import Console #for visual text formatting
console = Console() #console object
snooze_random = 0

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
  wake_up_reply = input("(Enter 1, 2 or 3): ")
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
  breakfast_reply = input("(1) Well I was craving french fries, so I might as well have fries and perhaps some ice cream while I'm at it. Some food is better than nothing!)", "(2) Anything I can get, a granola bar usually or nothing really, I never have time for breakfast!", "(3) Oatmeal, eggs, and toast! Or something else along the lines of that.", "(Enter 1, 2 or 3): ", sep='\n')
  while breakfast_reply != "1" and breakfast_reply != "2" and breakfast_reply != "3":
    breakfast_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  
  if snooze_random == 1:
    print("You go downstairs to grab some food, but your teacher begins a crucial lesson that will be on the test. You manage to grab a granola bar, and run back upstairs.")
  else:
    if breakfast_reply == "1":
      print("You go downstairs and eat french fries and icecream. It tastes amazing!")
      time.sleep(3)
      print("You know you should be eating better, but your tastebuds drown you out of that thought.")
      time.sleep(3)
      print("It's almost time for school, so you grab your phone and tell Siri, your virtual assistant, 'Hey Siri, join my first period class.' ")
      time.sleep(5)
      print("You join the call promptly. You are glad that you enabled the Siri shortcut to automatically join your Google Meet call. You wonder if other devices have this feature too...")
      time.sleep(5)
      print("You slowly start to feel tired, even though it's only the first class.")
      time.sleep(4)
      print("You now feel horrible for starting off your day like this!")
    elif breakfast_reply == "2":
      print("You decide to just skip breakfast. Who needs food anyways?")
      time.sleep(4)
      print("It's almost time for school, so you grab your phone and tell Siri, your virtual assistant, 'Hey Siri, join my first period class.' ")
      time.sleep(5)
      print("You join the call promptly. You are glad that you enabled the Siri shortcut to automatically join your Google Meet call. You wonder if other devices have this feature too...")
      time.sleep(5)
      print("You start getting more hunger pangs, and you can't really concentrate on your work. You consider grabbing food from downstairs but are scared you might miss something important, so you ignore your stomach.")

    elif breakfast_reply == "3":
      print("You make your breakfast. Although it takes more time to make, you can't wait to dig in.")
      time.sleep(5)
      print("It's almost time for school, so you grab your phone and tell Siri, your virtual assistant, 'Hey Siri, join my first period class.' ")
      time.sleep(5)
      print("You join the call promptly. You are glad that you enabled the Siri shortcut to automatically join your Google Meet call. You wonder if other devices have this feature too...")

def first_class():
  time.sleep(5)
  print("You are put into breakout rooms. Some time goes by and nobody is discussing anything. What do you do?")
  first_class_reply = input("(1) Stay quiet. Nobody wants to talk anyways.", "(2) Hop on microphone and try to talk to my classmates!", "(3) Say hi to your classmates in the chat and see what comes out of it.", "(Enter 1, 2 or 3): ", sep='\n')
  while first_class_reply != "1" and first_class_reply != "2" and first_class_reply != "3":
    first_class_reply = input("Invalid input. Please enter 1, 2, or 3: ")

  if first_class_reply == "1":
    print("You stay silent. So does everyone else.")
    time.sleep(5)
    print("You start to feel sad and lonely, and so distant from your classmates even though they're right there.")
    time.sleep(5)
    print("But you still keep silent and return to the main room.")
    time.sleep(5)
    print("You don't like how there is no group participation, and you miss in-person school")
    time.sleep(5)
  elif first_class_reply == "2":
    print("You hop on the microphone and try to start a discussion.")
    time.sleep(4)
    first_class_random = random.randint(1,3)
    if first_class_random == 1:
      print("You get some replies, but mostly brief")
      time.sleep(5)
      print("You try one more time, but no luck. People must be tired today.")
      time.sleep(5)
      print("You return to the main room. You are dissapointed, but still happy that you tried")
      time.sleep(4)
      print("Plus, it was nice to actually talk to someone for once, even if it was brief.")
    else:
      print("Someone responds to you, and then someone else.")
      time.sleep(4)
      print("You start a mini discussion and generate some ideas")
      time.sleep(4)
      print("You also introduce yourselves, and you find out that one person goes to your home school!")
      time.sleep(4)
      print("You continue discussing. You try to get the those who are quiet more involved, and they participate a bit.")
      print("Finally, you say your good-byes and return to the main room")
      time.sleep(4)
      print("You feel happy after socializing, and are proud that you took initiative!")
  elif first_class_reply == "3":
    print("You sent a message in the chat.")
    first_class_text_random = random.randint(1,3)
    if first_class_text_random == 1:
      print("One person responds.")
      time.sleep(5)
      print("You send another message, but only get vague responses back.")
      time.sleep(5)
      print("You stay silent for the rest of the duration.")
      time.sleep(4)
      print("You return to the main room. You are dissapointed, but still happy that you tried")
      time.sleep(4)
      print("Maybe you should've opened your microphone...")
    else:
      print("A few people respond back.")
      time.sleep(4)
      print("You share a few ideas. One person shares back.")
      time.sleep(4)
      print("Now a few more people share. You go back and forth.")
      time.sleep(4)
      print("Finally, you say your good-byes and return to the main room")
      time.sleep(4)
      print("You feel happy after socializing, and are proud that you took initiative!")
      time.sleep(4)
      print("Although you still feel a bit lonely... Maybe you should've opened your microphone?")

def second_class():
  time.sleep(4)
  print("That was a quiet first class... time for your next one! During class, you notice your friend sounding very withdrawn and tired when they open their mic to speak. What's up with that?")
  second_class_reply = input("(1) I think they’re just tired, I'd ignore it.", "(2) Text in the chat if they are okay; hey, I am sure my classmates are just as confused as me and someone needs to speak up!", "(3) Text them privately and check up on how they are doing, perhaps they had a rough morning and just need some cheering up.", "(Enter 1, 2 or 3): ", sep='\n')
  while second_class_reply != "1" and second_class_reply != "2" and second_class_reply != "3":
      second_class_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if second_class_reply == "1":
    print("I don't think too much of it")
    time.sleep(5)
    print("But I can't stop thinking that something might be wrong.")
    time.sleep(5)
    print("Anyways, I busy myself with the rest of my work.")
  elif second_class_reply == "2":
    print("I text in the chat 'are you okay?'")
    time.sleep(4)
    print("My friend doesn't respond.")
    time.sleep(4)
    print("Then the teacher asks 'are you okay?'")
    time.sleep(4)
    print("My friend texts 'yea i'm fine")
    time.sleep(4)
    print("You're not sure everything is fine, but you still trust your friend.")
  elif second_class_reply == "3":
    print("You text your friend after class: 'Hey, is everything alright? Im always here if you ever need someone to talk to.'")
    time.sleep(4)
    print("Your friend responds: 'Yea, i'm alright. I just feel really lonely and don't know if I have any friends")
    time.sleep(4)    
    print("You respond: 'Of course you do! You're one of the coolest people I know! In fact, do you want to virtually work out after school?")
    time.sleep(4)
    print("Your friend says: 'Oh, sure! That'd be cool!")
    time.sleep(4)
    print("You say: 'Alright! See you at 4:00!'")
    time.sleep(4)
    print("A bunch of thoughts overfill you. Why does my friend say they're lonely? Why did this happen?")
    time.sleep(4)
    print("You think: 'Hmm... maybe it's because my friend is so social, they got hit really hard by the lockdowns. I should've reached out earlier!'")

def lunch():
  time.sleep(4)
  print("Anyways, you say bye to your teacher and it’s finally lunchtime! How would you plan out the next hour?")
  lunch_reply = input("(1) Social media! This is my break time and I gotta see what others are up to. Plus, I really don’t want to walk all the way to the kitchen.", "(2) Continue my work. I got a bit distracted when my teacher gave us work time during first period, so I might as well do my work now!", "(3) Break time! I get up and move around for 20 minutes, and then enjoy lunch with my family for the rest of the time.","(Enter 1, 2 or 3): ", sep='\n')
  while lunch_reply != "1" and lunch_reply != "2" and lunch_reply != "3":
      lunch_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if lunch_reply == "1":
    print("I hop on my phone and start to browse. ")
    time.sleep(5)
    print("After a while, I start getting a headache.")
    time.sleep(5)
    print("Coincidentally, I read an article that explains that excessive screen time can cause eye-strain, leading to headaches...")
  elif lunch_reply == "2":
    print("I continue my work.")
    time.sleep(4)
    print("I get some work done, but time seems to be ticking faster.")
    time.sleep(4)
    print("I start to get a bit tired, and its getting close to next period.")
    time.sleep(4)
    print("I get up for the limited time i have left, and go outside for a bit.")
  elif lunch_reply == "3":
    print("I'm up and moving. I go for a walk/jog around the block.")
    time.sleep(4)
    print("Then I sit down to eat lunch with my family.")
    time.sleep(4)    
    print("I talk to them about the breakout room situation I was in today, as well as the situation with my friend.")

def test():
  time.sleep(4) 
  print("Hopefully you got to enjoy a nice meal at some point, who doesn't love a good lunch? Today, you have a test for all of third period and you just re-loaded the screen to see the test posted in your Google Classroom. How do you feel?")
  test_reply = input("(1) Great! I studied a good amount these past days and I’m ready!!!", "(2) Yikes! Test day was quicker than I thought. Why do I always procrastinate on studying??!!?", "(3) Whatever, I don't even care about my marks.", sep = '\n')
  while test_reply != "1" and test_reply != "2" and test_reply != "3":
      test_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if test_reply == "1":
    print("You take your test confidently")
    time.sleep(5)
    print("You stumble across a few problems...")
    time.sleep(5)
    print("But you are thankful that you did the extra work, because you relate the concepts to solve tricky problems.")
    time.sleep(5)
    print("You submit your test, feeling confident and proud of how it turned out.")
  elif test_reply == "2":
    print("You quickly scramble your notes and try to intak eas mcuh as you can!")
    time.sleep(4)
    print("But you can't seem to understand what you're reading. You need time to understand the concepts!")
    time.sleep(4)
    print("Anxious, you open the test and are shocked by the questions.")
    time.sleep(4)
    print("You start panicing! 'Ok, calm down,' you tell yourself.")
    time.sleep(4)
    print("Feeling horrible, you still manage to give the test your best shot.")
    time.sleep(4)
    print("You are very regretful and promise not to procrastinate again, even if you do good on this test. The mental troubles you went through were painful and unneccessary.")
  elif test_reply == "3":
    print("You casually open the test, not caring about it whatsoever")
    time.sleep(4)
    print("'Who cares? It's just online school,' you tell yourself'")
    time.sleep(4)    
    print("You carelessly take the test, but something deep down tells you that you have no future, and that you don't deserve such good education...")

def email():
  time.sleep(4)
  print("Phew! You may now take a 10-minute breather, your test is over! As you slump back in your chair, you get an email from a skeptical and seemingly dangerous sender. That's strange, what do you want to do with it?")
  email_reply = input("(1) No way I am opening that! I will drag that email to the trash right away!","(2) Oohhh, Danger is my middle name! I will open that email, I wonder what will happen!", "(3) Tell an adult, and ask for their opinion on what to do. That's way too strange to deal with myself!", "(Enter 1, 2 or 3): ", sep = '\n')
  while email_reply != "1" and email_reply != "2" and email_reply != "3":
      email_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if email_reply == "1":
    print("You drag the email to the trash.")
    time.sleep(5)
    print("You've seen too many people have their credentials exposed because of emails like this. Delete.")
  elif email_reply == "2":
    print("You open the email.")
    time.sleep(4)
    print("There is an attachment at the bottom of the screen. You click it. 'What's gonna happen, are they gonna punch me?' you tell yourself.")
    time.sleep(4)
    print("Suddenly, your screen freezes. You start to panic. You try to close the tab but nothing works. Finally, you force shut off your laptop.")
    time.sleep(4)
    print("You promise to never do that again.")
  elif email_reply == "3":
    print("You show it to a trusted adult.")
    time.sleep(4)
    print("They tell you to dispose of it right away.")
    time.sleep(4)    
    print("You drag it to the trash, never to see it again.")

def after_school():
  time.sleep(4)
  print("At last, you attend your final class, math, and upon your last equation, School is finally over! Give yourself a pat on the back for another day of school complete! What now?")
  after_school_reply = input("(1) Take a quick break and then attend a school club meeting.","(2) Partake in one of my hobbies! ", "(3) That was a long day! I might as well Binge Youtube/Netflix. I deserve it, I have like 6 hours to do my homework anyways!", "(Enter 1, 2 or 3): ", sep = '\n')
  while after_school_reply != "1" and after_school_reply != "2" and after_school_reply != "3":
      after_school_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if after_school_reply == "1":
    print("You attend your school club")
    time.sleep(5)
    print("Because of your leadership, you happen to be the president of your club!")
    time.sleep(5)
    print("You chat with your team and work on your next presentation")
    time.sleep(4)
    print("You feel good talking to others.")
  elif after_school_reply == "2":
    print("You do one of your hobbies!")
    time.sleep(4)
    print("You have a great time.")
    time.sleep(4)
    print("You relax your mind, and also get some time off the screen!")
    time.sleep(4)
    print("Now, you feel nice and refreshed!")
  elif after_school_reply == "3":
    print("You watch more netflix and youtube")
    time.sleep(4)
    print("Although the binge was good, you get distracted and end up watching 5 too many episodes.")
    time.sleep(4)    
    print("You get up, and try to deal with the headache you just got.")

def hangout():
  print("You step outside, and you see your friends notice and walk-up to you, about to ask if you are down to hang-out. Are you down or nah?")
  time.sleep(4)
  hangout_reply = input("(1) I would politely reject. Stay home, stay safe! ","(2) Alright I’m joining! Let’s head to the local burger joint!", "(3) I would keep walking and ignore them, I don’t care enough to socialize with others.", "(Enter 1, 2 or 3): ", sep = '\n')
  while hangout_reply != "1" and hangout_reply != "2" and hangout_reply != "3":
      hangout_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if hangout_reply == "1":
    print("You greet them but politely refuse.")
    time.sleep(5)
    print("Not just your health, but the health of others is more important than hanging out.")
    time.sleep(5)
    print("You wonder how many lives you saved by socially isolating for the past year...")
  elif hangout_reply == "2":
    print("You go to join your friends.")
    time.sleep(4)
    print("However, when you reach the intersection, you see a bunch of cop cars!")
    time.sleep(4)
    print("You run away as fast as you can!")
    time.sleep(4)
    print("You promise to stay at home and not to break the law again.")
  elif hangout_reply == "3":
    print("You ignore your friends.")
    time.sleep(4)
    print("You can see them giving you a puzzled look, but you honestly can't be bothered.")
    time.sleep(4)    
    print("You enter inside, not sure of why you feel upset.")

def covid():
  time.sleep(4)
  print("You decide to check your social media for a bit before doing some homework. As you scroll, you notice people from your school posting the most bizarre cures and preventatives for COVID-19, what would you do?")
  covid_reply = input("(1) Join in! It’s a harmless joke anyways, did you know balancing cockroaches on your head and eating chips at the same time prevents you from getting COVID-19? My turn to play some jokes!","(2) Laugh, and keep scrolling.", "(3) Perhaps text them about it or make an awareness post on Instagram Stories, this really isn’t something to joke about.", "(Enter 1, 2 or 3): ", sep = '\n')
  while covid_reply != "1" and covid_reply != "2" and covid_reply != "3":
      covid_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if covid_reply == "1":
    print("You join in on the action.")
    time.sleep(5)
    print("People start believing you at first, and it's really funny!")
    time.sleep(5)
    print("But after a while, you start to get mean messages from people that are even close to you.")
    time.sleep(5)
    print("You drop it, delete any posts you made, and apologize to anyone who saw your story. But the damage was already done...")
  elif covid_reply == "2":
    print("You laugh, and keep scrolling")
    time.sleep(4)
    print("You wonder what will happen to the joke.")
    time.sleep(4)
    print("But deep inside, you feel like you are doing something wrong...")
  elif covid_reply == "3":
    print("You message your friends and tell them it's not okay.")
    time.sleep(4)
    print("They are shocked to hear a response from you, but your words are firm.")
    time.sleep(4)    
    print("They eventually stop, and apologize for spreading misinformation. You feel proud of yourself.")

def dinner():
  time.sleep(4)
  print("You have now completed all your school-based work for the day. It’s time to get some dinner! Where are you eating?") 
  time.sleep(4)
  dinner_reply = input("(1) With my family. We have the best discussions at the dinner table!","(2) In my room alone, who needs family when you got yourself?", "(3) Dinner? I am still doing my homework and I got no time to eat! Perhaps in an hour or so, I can have a snack.", "(Enter 1, 2 or 3): ", sep = '\n')
  while dinner_reply != "1" and dinner_reply != "2" and dinner_reply != "3":
      dinner_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if dinner_reply == "1":
    print("You sit down to eat with your family.")
    time.sleep(5)
    print("You have a great time.")
    time.sleep(5)
    print("You tell them all about your day, and the meal was great!")
  elif dinner_reply == "2":
    print("You eat dinner alone.")
    time.sleep(4)
    print("For some reason, it feels like dinner is taking forever to finish")
    time.sleep(4)
    print("It also doesn't taste that good...")
    time.sleep(4)
    print("You shrug it off and finish up.")
  elif dinner_reply == "3":
    print("You continue your homework.")
    time.sleep(4)
    print("You finish just as its almost bedtime.")
    time.sleep(4)    
    print("You quickly stuff yourself with whatever leftovers you can find. You don't feel so good...")
def sleep():
  print("Its bedtime! Any last things you want to do once you're in bed ready to sleep?")
  time.sleep(4)
  sleep_reply = input("(1) Check my phone again and again, you never know how many texts you can get at night.","(2) Shout goodnight to my family, make a quick agenda of things to do tomorrow and fall asleep.", "(3) Set my morning alarm, take some deep breaths, and count the sheep leading me into my dream.", "(Enter 1, 2 or 3): ", sep = '\n')
  while sleep_reply != "1" and sleep_reply != "2" and sleep_reply != "3":
      sleep_reply = input("Invalid input. Please enter 1, 2, or 3: ")
  if sleep_reply == "1":
    print("You check your phone.")
    time.sleep(5)
    print("You answer a few texts, and it feels late by the time you are done")
    time.sleep(5)
    print("You try to sleep quickly, but you can't fall asleep. You remeber reading somewhere that blue light from cell phones at night can cause problems sleeping...")
  elif sleep_reply == "2":
    print("You say your bye-byes, and plan your day for tomorrow.")
    time.sleep(4)
    print("You want to be sure that you are prepared for tomorrow.")
    time.sleep(4)
    print("You fall asleep soon after.")
  elif sleep_reply == "3":
    print("You set your alarm, take deep breaths, and lay down")
    time.sleep(4)
    print("You refelct over your day today.")
    time.sleep(4)    
    print("You try to focus on how you can make tomorrow even better as you fall asleep with the counting sheep.")

intro()

new_day = console.input("\nWhen you are ready to play, click the rectangle on the right and type 'yes': ")

while new_day[0] == "y":
  mood = 0
  productivity = 0
  energy = 0
  fitness = 0
  fulfillment = 0

  wake_up()
  breakfast()
  print("\nFinal stats for today:")
  print("Mood: " + str(mood) + "/10")
  print("Energy: " + str(energy) + "/10")
  print("Productivity: " + str(productivity) + "/10")
  print("Fitness: " + str(fitness) + "/10")
  new_day = console.input("\nWould you like to start a another day? ([green]yes[/green]/[red]no[/red]) ")


print("Thank you for playing!") 
print("Again, we would like to remind you that some of these factors that we mentioned can simply just be out of your control.")
print("But there are always things we can improve on, and the key here is constantly improving ourselves!")
print("Hopefully you learned a few healthy habits that you want to implement for yourself. Now, back to the real world! Bye-bye!")
print("-----------------------------------------------------------------------")