
## Contestant menu screen ################################################################
##
## Used to display contestants and names as clickable objects
## Clicking a name/picture leads to the contestant's profile
##

screen contestant_menu():

    frame:
        xalign 0.5
        yalign 0.5
        xysize (1700, 900) # size x,y in pixels
        padding (50, 50)

        vbox:
            xalign 0.5
            spacing 25

            text "Choose a contestant to interview" xalign 0.5

            # Display a grid of 3 cols, 2 rows 
            grid 3 2 xspacing 150 yspacing 45:
                # data.profiles must have exactly six items for this to work
                for character in data.profiles:
                    button hover_background "#a00":
                        action [Hide("contestant_menu"), Show("contestant_profile", character=character)]

                        frame:
                            vbox:
                                add character["images"][0]
                                text character["name"] xalign 0.5

            vbox xalign 0.5:
                textbutton "No more questions (proceed)":
                    action [Hide("contestant_menu"), Call("matchmake")]


## Profile screen ################################################################
##
## Displays contestant name, picture, bio and interview question list
##

define done_flag = ' ✓'

screen contestant_profile(character):

    frame:
        xalign 0.5
        yalign 0.5
        xysize (1700, 900) # size x,y in pixels
        padding (50, 50)

        vbox:
            textbutton "< Back":
                action [Hide("contestant_profile"), Call("hide_all")]

            hbox spacing 100:
                # name, pic and bio
                vbox spacing 50 xsize 700:
                    vbox xalign 0.5 spacing 20:
                        frame:
                            add character["images"][0]
                        text character["name"] xalign 0.5

                    vbox xalign 0.5 xsize 600 spacing 20:
                        for item in character["profile"]:
                            hbox:
                                vbox xsize 200:
                                    text item["title"] + ": " bold True size 22
                                vbox xsize 400:
                                    text item["text"] size 22

                # interview question menu
                vbox spacing 65 xsize 800:
                    text "Interview Questions"

                    for question in character["questions"]:
                        if not data.flags[question["label"]]:
                            textbutton question["question"]:
                                action [Hide("contestant_profile"), Call(question["label"])]
                        else:
                            textbutton question["question"] + done_flag:
                                action [Hide("contestant_profile"), Call(question["label"])]


## Matchmake screen ################################################################
##
## Drop and drop contestants into pairs
##

init python:
    def contestant_dragged(drags, drop):
        if not drop:
            # Clear previously matched droppable if character not currently on a droppable
            data.matches[drags[0].drag_name] = ""
            return

        # Snap dragged object to closest droppable
        drags[0].snap(drop.x, drop.y, 0)

        # Store user input
        data.matches[drags[0].drag_name] = drop.drag_name
        #print(data.matches)

screen matchmake():

    frame:
        xalign 0.5
        yalign 0.5
        xysize (1700, 900)
        padding (50, 50)

        vbox spacing 50 ysize 700:
            draggroup:
                for i in range(0, 6):
                    # Droppables
                    drag:
                        drag_name "drop" + str(i)
                        child "profile_empty.png"
                        draggable False
                        xpos i % 3 * 400 ypos i % 2 * 400 # mod 3 in xpos gives us 3 cols, mod 2 in ypos gives 2 rows

                    # Dragables
                    drag:
                        drag_name data.profiles[i]["shortname"]
                        child data.profiles[i]["images"][0]
                        droppable False
                        dragged contestant_dragged
                        xpos 1250 ypos i * 105

            textbutton "Matchmake!!" xalign 0.5:
                action [Hide("matchmake"), Call("matchmake_results")]

        add "heart.png" xpos 118 ypos 247
        add "heart.png" xpos 520 ypos 247
        add "heart.png" xpos 920 ypos 247

## Achievements screen ################################################################
##
## Display achievements
##

screen achievements():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Achievements"), scroll="viewport"):

        # Display a grid of 5 cols, 6 rows to track achievements
        grid 5 3:
            spacing 40

            for key, achieved in persistent.achievements.items():
                vbox:
                    if achieved:
                        if data.endings[key] == (True, True):
                            add "achievement_yy.png" xalign 0.5
                        elif data.endings[key] == (False, False):
                            add "achievement_nn.png" xalign 0.5
                        elif data.endings[key] == (True, False):
                            add "achievement_yn.png" xalign 0.5
                        else:
                            add "achievement_ny.png" xalign 0.5
                    else:
                        add "achievement.png" xalign 0.5
                    text key.split("-")[0].title() + " & " + key.split("-")[1].title() size 20 xalign 0.5
                    
## Epilogue screen ################################################################
##
## Black screen, white text
##

screen epilogue(matches_labels):

    vbox:
        xalign 0.5
        yalign 0.5

        text "one"
        text "two"
        