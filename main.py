import random

# The code word to end the program is "snickers"

# Allows the user to give their chatbot a name
def name_bot():
  bot_name = input("Hello I am your friendbot would you like to give me a name?\n")
  if bot_name == "snickers":
    return 6
  else:  
    return bot_name

name_of_bot = name_bot()
 # chatbot greets the user with it's new name, asks how they are, and # asks if they want to play a game.
def greeting(friendbot_name):
  name = input("Okay, I am " + friendbot_name +" ! What is your name?\n\n")
  mood = input("\nHi " + name + "! How are you today?\n\n")
  types_of_mood = ["good", "great", "bad", "fine"]
  if mood == "snickers" or name == "snickers":
    return 6
  elif mood == types_of_mood[0] or mood == types_of_mood[1]:
    game = input("\nGreat! Would you like to play a game?\n\n")
  elif mood == types_of_mood[2] or mood == types_of_mood[3]:
    game = input("\nWould you like to make your day better with a game?\n\n")
  else:
    game = input("\nHmm... Would you like to play a game?\n\n") 
    if game == "snickers":
      return 6
    else:
      return game

# If the user chooses to play the game this function does a mad lib  # with user input and then asks about their hobbies. If they choose not to play the game it skips to ask about their hobbies.
def play_a_game():
  if answer == "yes" or answer == "sure":
    print("\nAwesome! Let's play mad lib!\n")
    food = input("Enter a type of food: ")
    color = input("\nEnter a color: ")
    number = input("\nEnter a number: ")
    plural_noun = input("\nEnter a plural noun: ")
    animal = input("\nEnter a type of animal: ")
    print("\nWe have created a masterpiece!\n ")
    mad_lib = ("I woke up to the smell of burnt "+ food + " and walked into the kitchen to find "+ number+" " + color+" " + animal + "s running around the table with " + plural_noun + "!\n ")
    print(mad_lib)
    name_of_hobby = input("Ha ha! So what's one of your hobbies?\n\n")
    if answer == "snickers" or name_of_hobby == "snickers":
      return 6
  else:
    name_of_hobby = input("\nOkay. What's one of your hobbies?\n\n")
    if name_of_hobby == "snickers":
      return 6
    else:   
      return name_of_hobby
  

answer = greeting(name_of_bot)
  
hobby = play_a_game()

# This function take the hobby that the user provided and compares it # to a list. If the hobby is in the list the chatbot will reponds #with a response from a bank. If it's not on the list it will ask the # user to explain what the hobby is and add that hobby onto the list. 
def store_hobby_info():
  list_of_hobbies = ["reading","playing video games", "drawing", "coding", "programming"]
  if hobby in list_of_hobbies:
    if hobby == list_of_hobbies[0]:
      genre = input("\nWhat type of books do you like to read?\n\n")
      print("\n" + genre + " interesting...\n")
      if genre == "snickers":
        return 6
      else:  
        return "book"
    elif hobby == list_of_hobbies[1]:
      name_of_game = input("\nCool! What's your favorite game to play?\n")
      if name_of_game == "snickers":
        return 6
      else:  
        return name_of_game
    else:  
      responses = ["\nThat's one of my hobbies too!", "\nNo way, me too!", "\nMy creator is really into that.", "\nThat sounds like fun!"]
      print(random.choice(responses))
      siblings = input("Do you have any siblings?\n")
      if siblings == "snickers":
        return 6
      
      elif siblings == "yes":
        return True
      else:
        return False   
    
  else:
    list_of_hobbies.append(hobby)
    explanation = input("\nI'm not familiar with that one could you explain it too me? ")

    if explanation == "snickers":
      return 6
    else:  
      print("\nWow! You learn something new everyday!\n")
      return 3
    

next_step = store_hobby_info()    

# This function asks the user what game they like to play and #compares the answer to a list of games known by the chatbot. If the # game is on the list, then a random response will be picked from a #bank. If the game isn't on the list, the chatbot will ask how you #play the game.
def topic_gaming(game):
  list_of_games = ["apex legends", "fortnite", "call of duty", "roblox", "the legend of zelda", "league of legends"]
  if game in list_of_games:
    responses_b = ["I heard of that one. It sounds like fun!", "I play that one too!", "My favorite game!", "Interesting...", "Mine too! We should play sometime!"]
    print(random.choice(responses_b))
  else:
    how_to_play = input("\nI'm not familiar with that one. How do you play?\n")
    if how_to_play == "snickers":
      return 6
    else:
      print("\nAwesome! That sounds like fun!")
      return 4

# This function will ask the user how many siblings they have and #whether or not they are brothers or sisters.

def topic_siblings():
  if next_step == True or next_step == 3:
    num_siblings = str(input("How many siblings do you have?"))

    if num_siblings == "snickers":
      return 6
    elif num_siblings == "none" or num_siblings == 0:
      return 4
    else:  
      bro_or_sis = input(num_siblings + " huh? Are they brothers or sisters?")
      if bro_or_sis == "snickers":
        return 6
      print("Cool!")
      return 4
  else:
    return 4 

# This function will ask the user what their favorite book is and #then respond with the title embedded in the response.         
def topic_genre():
  favorite_book = input("\nWhat's your favorite book?\n")
  if favorite_book == "snickers":
    return 6
  else:  
    responses_c = [("Hmm... " + favorite_book + "? Cool!"), (favorite_book + "? I think I had to read that for a class once."), ("I used to read that to my creator!"), ("I like " + favorite_book +  ". It's a good book!")]
    print(random.choice(responses_c))
    return 4

# This if statement directs the chatbot from the store_hobby_info #function to the direction the chat is going whether it's books, #games, or siblings. 
if next_step == True or next_step == False:
  loop = topic_siblings()
elif next_step == "book":
  loop = topic_genre() 
elif next_step == 3:
  loop = topic_siblings()
else:
  loop = topic_gaming(next_step)

# This if statement will loop the conversation back to hobbies.
if loop == 4:
  hobby = input("What's another hobby you have?")
  store_hobby_info()   







    




