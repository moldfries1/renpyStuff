# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
