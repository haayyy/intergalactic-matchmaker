# Characters
define h = Character("Zopflam", color="#4e832e") # nb
define a = Character("Audience")

define x = Character("Xel", color="#A013DE") # doomed to mediocrity nb
define v = Character("Viktor", color="#99423f") # vampire m
define s = Character("Space Sheep", color="#90A649") # ??????? f
define c = Character("LCpl. Cody Byrne", color="#3E465D") # space marine m
define o = Character("Odonata", color="#98883B") # bug alien f
define r = Character("Rust", color="b63327") # the AI f presenting

define left = Position(xpos=0.3)
define right = Position(xpos=0.7)
define center = Position(xpos=0.5)

#define bg_music = ''
define fadeinDefault = 5.0
define fadeoutDefault = 2.0

# The game starts here.
label start:

    # Handle achievements/persistent data on game (not playthrough) launch
    init python:
        if persistent.achievements is None:
            persistent.achievements = data.achievements
            #print("Persistent data created")
        #else:
            #print(persistent.achievements)

    # Reset playthrough-specific variables
    python:
        data.matches = {}
        for flag in data.flags:
            flag = False
        #print("Playthrough data reset")

    # background doesn't change for the whole game
    scene bg gameroom

    #play music bg_music fadein fadeinDefault
    call show_intro
    call character_intros

    call interviews_intro
    call screen contestant_menu()

    # from here game continued in matchmake label

    return

# literally the worst thing i've ever written
label hide_all:
    hide xel
    hide cody
    hide odonata
    hide rust
    hide sheep
    hide viktor
    hide host
    call screen contestant_menu()

    return

label show_intro:

    show host with dissolve

    a "WOOOO!!!!"

    a "Woooooooooo!!!"

    show host up

    h "Good evening, everyone!"

    a "WooooO!!"

    h "And welcome to another episode of Intergalactic Matchmaker."

    show host left

    h "As always, I'm your host, Zopflam Hapjuc."

    h "For new viewers, every week we come together to welcome six hopefulls looking for love for an appointment with an expert matchmaker."

    show host 

    h "This week, we welcome a new matchmaker to the show for their first ever appearance. As usual, they will remain anonymous, but let's start by asking them a vital question."

    h "So matchmaker, what's your goal for our contestants tonight?"

    menu:
        extend "" # extra line
        "To make realistic matches":
            show host right
            h "Hm, a pragmatist."

        "For everyone to find true love":
            show host right
            h "How about that, everyone?"

            a "Wooo!!"

        "To wreak havok":
            show host right
            a "Ooooooh!"

            h "How unconventional."

    return

label character_intros:

    show host 

    h "And now, lets introduce our matches to be!"

    h "These singles have come from near and far alike with one persuit in mind..."

    show host up

    h "Love."

    a "WOOOOOOO!!!!!"

    show host 

    h "First up, from the far reaches of the galaxy, introducing Xelphde!"

    show host at left with move
    show xel at right with dissolve

    x "Xel for short. Hi, everyone."

    show host right

    h "Well Xel, tell us about yourself."

    show xel thinking

    x "Not much to say, really. I live outside the core worlds, 700 region. Lived on Ajax before that."

    show xel ugh

    x "I never seem to have much luck, romantically, but I'm hoping to change that."

    a "Awwwww!!!"

    show host up

    h "Isn't that great? Give it up for Xel!"

    a "WOOOO!!!! Yeah!"

    hide xel with dissolve

    h "And for our second contestant...meet Viktor!"

    show viktor nervous side at right with dissolve
    
    h "Tell us a little about yourself."

    show viktor nervous

    v "Um...hi everyone!"

    v "I'm Viktor Cl- wait I forgot I said I wasn't going to use my last name! Sorry I'm a little nervous!"

    show viktor

    v "Pleased to meet you all."

    v "...Um, yeah! So."

    v "Yeah."

    show viktor nervous

    v "......"

    v "......"

    show viktor

    h "Give it up for Viktor, everyone!"

    a "Wooooooooooo!!!"

    h "You can sit down again."

    show viktor nervous side

    v "Oh, right."

    hide viktor with dissolve

    h "And next...a contestant who needs no introduction, because you all know who she is. It's Sheep!"

    show sheep at right with dissolve

    a "WOOOO!!!!"

    show sheep happy

    s "Hello, everyone. Lovely to be here."

    show host left

    a "So glad to have you on the show. So, what brings a famous explorer to our humble studio?"

    show sheep

    s "Well, Xel mentioned they were coming on the show, and I thought it would be fun. I've been spending a lot of time in the 700 region recently, and we're good friends."

    show host

    h "Great, glad to to hear it. Give Sheep a round of applause, everyone."

    hide sheep with dissolve

    h "And for contestant number four...give a warm welcome to Rust!"

    show rust at right with dissolve

    a "Woooo!!"

    r "Sup."

    h "Tell us about yourself."

    show rust finger guns

    r "World's sexist AI, at your service. I'm looking for love, baby."

    h "Well, you've come to the right place."

    r "Fuck yeah."

    show rust

    r "Oh, am I allowed to say that?"

    show host left

    h "Yes, it's fine. But we ask contestants to refrain from any sexually explicit statements."

    show rust smile

    r "What about sexually explicit questions?"

    show host

    h "Please also refrain from that."

    show rust

    r "Aw."

    h "Give her a round of applause!"

    a "Woooo!!"

    hide rust with dissolve

    h "And for contestant number five...give it up for Odonata!"

    show host at Position(xpos=0.25) with move
    show odonata at Position(xpos=0.75) with dissolve

    a "Woooo!!"

    o "Greetings."

    show host right

    h "Well Odonata, our producers tell us you're looking for a very specific kind of special someone."

    show odonata point

    o "Yes, that is correct. We will elaborate later when there is time for such discussions."

    h "Thank you, Odonata."

    hide odonata with dissolve
    show host
    
    h "And finally, for our sixth contestant, we have a military man. Introducing Lance Corporal Cody Byrne!"

    show cody at right with dissolve
    
    c "Hello."

    h "Any words before we start, Cody?"

    c "No."

    show host left

    h "......"

    show host up

    h "A man of few words! Give a round of applause for Cody!"

    a "WOOOO!!!"

    hide cody with dissolve

    return


label interviews_intro:

    show host at center with move

    h "Now that we've had a first glimpse of our contestants, we'll move to the interview phase of the show."

    show host left

    h "This is where our matchmaker will be allowed to ask each contestant up to five unique questions to gain insight into their goals and personality."

    show host
    
    h "Take it away, matchmaker."

    hide host

    return

label matchmake:

    show host with dissolve

    h "Well, that concludes the interview phase of the show."

    show host left

    h "Regular viewers know what comes next. That's right...it's time-"

    a "TIME!"

    show host right

    h "to"

    a "TO!"

    show host up

    h "matchmake!"

    a "MATCHMAKE!!"

    show host

    h "It's all up to you now, matchmaker. Call on your many years of matchmaking experience to give our six contestants the partner of their dreams."

    h "Six singles walked in tonight, and if all goes well, three couples will walk out."

    show host left

    h "Take it away."

    hide host with dissolve
    call screen matchmake()

    # game continues in label matchmake_results

    return

label matchmake_results:
    show host with dissolve

    python:
        data.matches_is_valid = True
        for key, value in data.matches.items():
            if value == '':
                data.matches_is_valid = False

        if len(data.matches) < 6:
            data.matches_is_valid = False

    if not data.matches_is_valid:
        h "Hmm...it doesn't look like the matchmaker has filled out all the matches. We'll give them some more time."

        hide host with dissolve
        call screen matchmake()
    else:
        call matchmake_interviews

    return

label matchmake_interviews:

    h "Well, everyone, the results are in."

    h "Will the matchmaker's pairs bring joy or sorrow?"

    show host left

    h "Let's hear from our contestants to find out."

    # this is where i gave up on nice code in this project
    define matches_labels = [[], [], []]

    # call matches
    python:
        matches_list = [0, 1, 2, 3, 4, 5]

        for key, value in data.matches.items():
            index = int(value.replace("drop", ""))
            matches_list[index] = key.title()

        for i in range(0, 3):
            matches_labels[i] = sorted([matches_list[i], matches_list[i + 3]])

        #print(matches_labels)

    h "Our first couple...is [matches_labels[0][0]] and [matches_labels[0][1]]!"

    show host

    h "So will it be 'yes' or will it be 'no'? Please come down to the front and tell us what you think of the match."

    hide host with dissolve

    call expression matches_labels[0][0].lower() + "_" + matches_labels[0][1].lower() + "_ending"

    show host with dissolve

    h "And now for our second couple...it's [matches_labels[1][0]] and [matches_labels[1][1]]!"

    h "Come on down to the front and tell us what you think of the match."

    hide host with dissolve

    call expression matches_labels[1][0].lower() + "_" + matches_labels[1][1].lower() + "_ending"

    show host with dissolve

    h "For our third and final couple tonight...we know who it is, but give them a round of applause anyway! It's  [matches_labels[2][0]] and [matches_labels[2][1]]!"

    h "Come down to the front and tell us what you think."

    hide host with dissolve

    call expression matches_labels[2][0].lower() + "_" + matches_labels[2][1].lower() + "_ending"

    call host_wrapup

    $ renpy.save_persistent()

    # epilogue
    scene black
    call expression matches_labels[0][0].lower() + "_" + matches_labels[0][1].lower() + "_epilogue"
    call expression matches_labels[1][0].lower() + "_" + matches_labels[1][1].lower() + "_epilogue"
    jump expression matches_labels[2][0].lower() + "_" + matches_labels[2][1].lower() + "_epilogue"

    # game ends here

    return

label host_wrapup:

    show host with dissolve

    h "That concludes our show, folks!"

    show host up

    h "Before we finish, let's give a round of applause for the matchmaker."

    a "Wooooo!!"

    show host left

    h "And some applause for our six contestants!"

    a "Wooooo!!!"

    show host

    h "Until next time, I'm Zopflam Hapjuc, and this is Intergalactic Matchmaker."

    h "Love and peace."

    return
