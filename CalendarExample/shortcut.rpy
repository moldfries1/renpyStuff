#Function checkcalendar, add this in script.rpy


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


#Add the calendar in screens.rpy 

screen calendar :
    
    #We call the checkcalendar function
    $ checkcalendar()

    
    # Don't stop the user from interacting with other things - this screen is just showing stuff.
    modal False
    
    # The section of screen to which we'll place the rest.
    frame:
        xalign 0.0    # Place in the upper-right corner.
        yalign 0.0    #
        xsize 230     #
        ysize 75      # 
        xmargin .05   # Leave some transparent space around the box.
        ymargin .05   #
        xpadding .15  # Leave some unused space between the box and its contents.
        ypadding .15  # 

        vbox:  
            text "[day_name] (day [daycount])" size 14 xalign 0.5    # The variable must be called in this way for it to be updated
            hbox:  
                text "[hour]" size 15 yalign 1.5 xalign 0.5 ypos 1.9  



#Initialize the calendar in the first label with 

show screen calendar

#You can either increment to go to the next day, or directly write the name of the day

$ daycount += 1

#OR 

$ daycount = "Tuesday"


