# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Monokuma")

# We initiate the python function that will be called in the calendar

init python : 

    hour = "Morning" # We choose to start the story in the morning
    daycount = 1   # We start the day counter at 1, which corresponds to Sunday according to our list, visible below. 
    
    def checkcalendar():

        global day_name
        if (daycount%7) == 0:
            day_name = "Saturday"
        elif (daycount%7 == 1):
            day_name = "Sunday"
        elif (daycount%7 == 2):
            day_name = "Monday"
        elif (daycount%7 == 3):
            day_name = "Tuesday"
        elif (daycount%7 == 4):
            day_name = "Wednesday"
        elif (daycount%7 == 5):
            day_name = "Thursday"
        elif (daycount%7 == 6):
            day_name = "Friday"


    
# The game starts here.

label start:

    show screen calendar


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hopeacademy

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show monokuma neutre with dissolve and vpunch 

    # These display lines of dialogue.

    m "Tada! Thanks for downloading me!"

    show monokuma oups

    m "On the top left you can see the calendar."
    
    m "You can manipulate it by incrementing the day_count."

    show monokuma neutre

    $ daycount += 1

    m "Here for example I added 1 to the day_count ! "

    m "You can change the head of the list as you want. "

    show monokuma oups

    m "I hope you like this little script."

    show monokuma cutie

    m "Do not hesitate to send me your comments or improvements !"


    # This ends the game.

    return
