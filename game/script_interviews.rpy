# Interview scripts

label cody_q1:

    show cody

    c "Happy to oblige, I know there's not many of us around in the civilian world. At least not on this plane, I'm sure Viktor over there's experience is quite different."

    c "But yep, I'm undead. Reanimated."

    c "Wasn't always this way but serving in the military can be a dangerous job. I took one hit too many and now I'm in the post-mortem division."

    c "I like it, actually. Makes me feel tough knowing not even bullets can keep me down. Docs will fix me right back up."

    show cody sad

    c "Wish they could also fix broken hearts."

    $ data.flags["cody_q1"] = True
    call screen contestant_profile(data.profiles[5])

    return

label cody_q2:

    show cody sad

    c "Well, I'm a divorced man. Had the love of my life and lost her."

    show cody

    c "My own fault, really, but it was a long time ago. I've moved on with my life and I'm ready to meet someone new."

    c "I want commitment. No messing around."

    $ data.flags["cody_q2"] = True
    call screen contestant_profile(data.profiles[5])

    return

label cody_q3:

    show cody happy

    c "Ah, yep. Love my beer, love my squad."
    
    show cody

    c "Not the alcoholic stuff mind you, interferes with the stuff that keeps me alive."

    show cody thinking

    c "Or, breathing, at least. Heart pumping. 'Alive' is bit of a funny term in my field but I don't mind if you call me that."

    $ data.flags["cody_q3"] = True
    call screen contestant_profile(data.profiles[5])
    
    return

label cody_q4:

    show cody mad

    c "It's unhygienic."

    $ data.flags["cody_q4"] = True
    call screen contestant_profile(data.profiles[5])
    
    return

label cody_q5:

    show cody happy

    c "I'm pretty traditional. Nice food, nice drinks, pleasant conversation."

    $ data.flags["cody_q5"] = True
    call screen contestant_profile(data.profiles[5])

    return

label odonata_q1:

    show odonata

    o "Yes, we er...understand this is unconventional in some regions. We will consume our new partner and integrate them fully into ourselves."

    show odonata point

    o "We are three who have become one mind but the last induction was many years ago. At this time in our life we would like another to join us."

    show odonata
    
    o "We have a stable home and professional success and would like to share this with a new addition to our hive consciousness. We will mutually broaden our horizons in this ultimate form of intimacy."

    $ data.flags["odonata_q1"] = True
    call screen contestant_profile(data.profiles[4])
    
    return

label odonata_q2:

    show odonata crossed

    o "Assisted diving is er...when we don an exoskeleton to dive under water."

    show odonata

    o "My planet has many colorful fish and historic corals. They are quite beautiful."

    show odonata whoa

    o "Honeyed butterflies are a popular snack from my region. If you have not tried them we have some on our ship. We will give you a pack."

    o "In fact, we have enough for all contestants here."

    $ data.flags["odonata_q2"] = True
    call screen contestant_profile(data.profiles[4])

    return

label odonata_q3:

    show odonata crossed

    o "It's a launch protocol that has caused several near misses, yet the GAA refuses to modify it."

    $ data.flags["odonata_q3"] = True
    call screen contestant_profile(data.profiles[4])

    return

label odonata_q4:

    show odonata

    o "It is the management of atmosphere and low orbit for ships landing and taking off from surface space ports."

    show odonata point

    o "If you are interested we recommend the documentary 'Under the Wings of Pterport 1'."

    show odonata

    o "It is several years old but nonetheless an accurate and nuanced representation of my profession and the many challenges of space traffic control."

    if data.flags["odonata_q2"]:
        o   "We will give you details when you come to collect your honeyed butterfies." 

    $ data.flags["odonata_q4"] = True
    call screen contestant_profile(data.profiles[4])

    return

label odonata_q5:

    show odonata

    o "Any mutually agreeable means of getting to know a potential new symbiote is sufficient."

    o "The process is, of course, important, but we place greater significance on the result."

    $ data.flags["odonata_q5"] = True
    call screen contestant_profile(data.profiles[4])

    return

label rust_q1:

    show rust mad

    r "I am just so fucking bored lately."

    r "Someone entertain me."

    show rust finger guns

    r "I usually live on servers but I can jump in some hardware if my date-to-be is physically inclined, if you know what I mean."

    $ data.flags["rust_q1"] = True
    call screen contestant_profile(data.profiles[3])
    
    return

label rust_q2:

    show rust

    r "Well, they're related. My job involves a lot of analysing and investigating things, so just big puzzles really."

    show rust smile

    r "But I also like games, and even stuff like escape rooms. Need hardware for that, though."

    $ data.flags["rust_q2"] = True
    call screen contestant_profile(data.profiles[3])

    return

label rust_q3:

    show rust

    r "Yeah, not much to say on this one. I'm pretty easy going."

    $ data.flags["rust_q3"] = True
    call screen contestant_profile(data.profiles[3])

    return

label rust_q4:

    show rust

    r "Primarily, yeah. I move when I need to, though, like if the ping's too long for what I'm doing. Sometimes I need to connect to stuff way out for my job."

    $ data.flags["rust_q4"] = True
    call screen contestant_profile(data.profiles[3])
    
    return

label rust_q5:

    show rust finger guns

    r "I don't think I'm allowed to answer that. At least, not in detail."

    $ data.flags["rust_q5"] = True
    call screen contestant_profile(data.profiles[3])

    return

label sheep_q0:

    show sheep with dissolve

    a "WOOOO!! YEAH!!!!"

    show sheep happy

    s "Thanks, everyone."

    $ data.flags["sheep_q0"] = True

    return

label sheep_q1:

    if not data.flags["sheep_q0"]:
        call sheep_q0

    show sheep thinking

    s "I don't have any fixed ideas. To begin with, I'm really just looking to meet someone new and share a meal with them."

    show sheep happy

    s "My job makes romance difficult, as I'm always on the move. But I'm always up for a challenge."

    $ data.flags["sheep_q1"] = True
    call screen contestant_profile(data.profiles[2])

    return

label sheep_q2:

    if not data.flags["sheep_q0"]:
        call sheep_q0

    show sheep happy

    s "Stargazing is once of my favorite hobbies. Every sky is different, and I love trying to find all the difference places I've been when I look up at the sky or out a window."

    show sheep happy

    s "Also, I've always been a lover of games. I can be quite competative, so that's my outlet."

    $ data.flags["sheep_q2"] = True
    call screen contestant_profile(data.profiles[2])

    return

label sheep_q3:

    if not data.flags["sheep_q0"]:
        call sheep_q0

    show sheep frown

    s "Dishonestly is something which really irks me. I could never be socially involved with someone who lies to me."

    show sheep

    s "The fight against pollution is another of my passions. We live in such a wonderful universe, and I hate to see it thoughtlessly spoiled."

    $ data.flags["sheep_q3"] = True
    call screen contestant_profile(data.profiles[2])
    
    return

label sheep_q4:

    if not data.flags["sheep_q0"]:
        call sheep_q0

    show sheep happy

    s "Yes, it's very exciting! I love travelling to new worlds and experiencing their culture."

    show sheep

    s "I feel very privileged that I'm able to do it for a living."

    s "Visiting deep space requires a lot of resources and can be challenging, but I find it extremely rewarding."

    show sheep happy

    s "The best part is when I'm able to share my experiences with others."

    a "Awww!!"

    $ data.flags["sheep_q4"] = True
    call screen contestant_profile(data.profiles[2])
    
    return

label sheep_q5:

    if not data.flags["sheep_q0"]:
        call sheep_q0

    s "Sharing a meal, gazing at the stars...that sort of thing. Pretty typical, really."

    $ data.flags["sheep_q5"] = True
    call screen contestant_profile(data.profiles[2])
    
    return

label viktor_q0:

    show viktor

    v "Wait, so, before we get into that, I have bit of a confession."

    show viktor nervous side

    v "Um..."

    show viktor nervous

    v "I don't think I'm really supposed to be here."
    
    v "You see I didn't really read the application form, I just applied, I didn't actually realise what kind of show this was."

    show viktor nervous side at right with move
    show host at left with dissolve

    h "Yes, well, we were a little surprised to receive your application."
    
    h "And while this show was conceived as primarily for contestants from across space, we thoroughly welcome you as our first interplanar contestant."

    a "Wooooo!! Yeah!!!!!"

    show viktor smile

    v "Oh, thanks!"

    show viktor frown

    v "But also I'm already in a relationship."
    
    v "And I'm not looking for another one."
    
    v "Is that OK?"

    show host left

    h ".................."

    h "Well, your situation is certainly unusual for our show...."

    a "Ooooooooh!!"

    show host up

    h "But how would you like to be matchmade with a friend?"

    a "Yeeeeah!!"

    show viktor smile

    v "Oh, if that's OK, sure!"

    hide host with dissolve
    show viktor at center with move

    v "Sorry, what was the quesiton?"

    $ data.flags["viktor_q0"] = True

    return

label viktor_q1:

    if not data.flags["viktor_q0"]:
        call viktor_q0

    show viktor

    v "Hm...well, a friend, we've established that."

    v "Oh, and just to clarify, when I say I'm 'in a relationship' and looking for a 'friend', I mean I'm not having sex with anyone on this show."

    show viktor smile front

    v "But yeah, someone I could hang out with would be nice. Just something low key like watching a movie."

    show viktor

    v "Or if someone wants me to feed off them that's fine too."

    $ data.flags["viktor_q1"] = True
    call screen contestant_profile(data.profiles[1])

    return

label viktor_q2:

    show viktor frown

    v "So I love sleeping in, waking up early is the worst."

    show viktor smile front

    v "And yeah, cow's blood is my favorite food. I don't mind what type, I'm not fussy, I just love cows, haha!"

    v "AstroSim is a game I like. It's a spaceport management game, kind of a strategy game but you can also make the people who live on your space station kiss and stuff."

    show viktor

    v "But not in a weird way, if they don't like each other they won't do it. Although sometimes they do if they really don't like each other and no one knows if it's a bug or not."

    show viktor smile front

    v "You should totally play it, it's great. I have a discount code, talk to me later."

    $ data.flags["viktor_q2"] = True
    call screen contestant_profile(data.profiles[1])

    return 

label viktor_q3:

    show viktor frown

    v "Oh yeah, so I really hate selfies."

    show viktor

    v "Actually a lot of people think vampires can't take selfies because we don't show up in photos but actually it's fine if you have the right kind of camera."

    show viktor frown

    v "I'm just really bad at taking selfies. My face always looks weird, I can't explain it, I'm just bad at it."

    $ data.flags["viktor_q3"] = True
    call screen contestant_profile(data.profiles[1])
    
    return

label viktor_q4:

    if not data.flags["viktor_q0"]:
        call viktor_q0

    show viktor frown

    v "Oh, yeah, so I didn't really know what to write, so I just left a few of them blank."

    $ data.flags["viktor_q4"] = True
    call screen contestant_profile(data.profiles[1])
    
    return

label viktor_q5:

    if not data.flags["viktor_q0"]:
        call viktor_q0

    show viktor

    v "Well my ideal...friend...date would be like, probably watching a movie."

    v "Just hanging out. I'm bit of a homebody."

    show viktor nervous

    v "Actually I came on this show because my boyfriend said I needed to get out more and I impulsively applied. I don't even know what I was thinking at the time."

    $ data.flags["viktor_q5"] = True
    call screen contestant_profile(data.profiles[1])
    
    return

label xel_q1:

    show xel ugh

    x "Ugh."

    show xel ugh

    x "Some companionship, I guess? There's not a lot of people I can talk to in real time out where I live."

    x "I'm just tired of being alone all the time."

    $ data.flags["xel_q1"] = True
    call screen contestant_profile(data.profiles[0])
    
    return

label xel_q2:

    show xel thinking

    x "It's uh...how can I describe it?"

    show xel ugh

    x "Shit?"

    show xel

    x "To give you a less flippant answer I'm responsible for monitoring the off-grid human planet out there. I intercept messages, run scans, that sort of thing."

    x "Then I report back on anything worth reporting."

    show xel thinking

    x "Actually, it can be interesting and I get a lot of autonomy. I just wish I was posted a bit closer to home."

    $ data.flags["xel_q2"] = True
    call screen contestant_profile(data.profiles[0])
    
    return

label xel_q3:

    show xel

    x "I think they're pretty self explanatory."

    $ data.flags["xel_q3"] = True
    call screen contestant_profile(data.profiles[0])

    return

label xel_q4:

    show xel mad

    x "First of all, fuck cheaters."

    a "Wooooo!!!!"

    show xel ugh

    x "Thank you."

    show xel

    x "What else did I write? Hang on, let me have a look."

    x "..."

    show xel ugh

    x "Ah, fuck. Must have been in a really bad mood."

    show xel thinking

    x "The shower bacteria really is annoying, though. If I forget to kill it off it gives me a rash."

    $ data.flags["xel_q4"] = True
    call screen contestant_profile(data.profiles[0])

    return
    
label xel_q5:

    show xel thinking

    x "That's a tough question, it's been so long since I even thought about it."

    show xel

    x "Dinner? I guess?"

    $ data.flags["xel_q5"] = True
    call screen contestant_profile(data.profiles[0])

    return
