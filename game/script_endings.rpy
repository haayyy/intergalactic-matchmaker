# Endings scripts

label cody_odonata_ending:

    show cody at left with dissolve
    show odonata at right with dissolve

    o "Hello, Lance Corporal."

    c "You can call me Cody."

    show odonata point

    o "Very well, Cody, shall we start or would you like to?"

    c "I can start."

    c "Odonata, I..."

    c "I don't fully understand this absortion stuff you're proposing but I'd like to hear more."

    show cody smile

    c "So yes, I accept the match. And I'd be honored if you're inclined to do the same."

    show odonata

    o "..."

    show odonata crossed

    o "Brief and to the point. We appreciate that."

    show odonata

    o "Let us end the suspense. We find you an acceptable match and would like to persue this relationship further."

    o "You seem serious and willing to make a commitment. That is our main priority."

    show odonata point

    o "The symbiosis we seek is a one-way process and it is important that all participants are compatible and well informed."

    show odonata

    o "Perhaps we could discuss this further over a shared meal?"

    show cody smile side

    c "I'd like that."

    o "The feeling is mutual."

    show host with dissolve

    h "Well, how about that everyone?"

    a "Woooo!!!"

    hide cody with dissolve
    hide odonata with dissolve
    hide host with dissolve

    $ persistent.achievements["cody-odonata"] = True

    return

label cody_rust_ending:

    show cody at left with dissolve
    show rust at right with dissolve

    r "Sup, big boy."

    c "Hello."

    r "So are we just gonna do this?"

    c "...I guess."

    show rust finger guns

    r "I'm on board. If matchmaker says yes I say why not."

    r "I'm not the playing house type but I know you military types get all sorts of cool tech."

    r "I'm sure we have a lot of common insterests."

    r "And I bet I could beat your ass at laser tag."

    r "So what do you say?"

    c "..."

    show cody sad

    c "Well, actually, I'm a little conflicted."

    show rust mad

    r "Oh, okay."

    c "I will say when I first saw you I thought you were quite attractive, but you don't seem to want the same level of commitment I do."

    r "Oh..."

    show cody

    c "But on the other hand, maybe I'm being a little too stubborn."

    c "I came here to meet someone and if the matchmaker thinks we'd be good together, let's give it a shot."

    show rust smile

    r "Fuck yes. That's what I like to hear."

    show cody smile

    show host up with dissolve

    h "A happy ending! Let's give them a round of applause."

    a "Woooo!!"

    hide cody with dissolve
    hide rust with dissolve
    hide host with dissolve

    $ persistent.achievements["cody-rust"] = True

    return

label cody_sheep_ending:

    show cody at left with dissolve
    show sheep at right with dissolve

    s "Hello, Cody. Is it OK if I call you that?"

    c "Hello, yes, that's fine."

    s "Shall we get on with it?"

    c "Yep, can do. Want me to start?"

    s "If you would like."

    c "Well...first I want to stress what an honor it is to be matched with you."

    show cody thinking

    c "But..."

    show sheep uh

    s "I thought this might be coming."

    show cody

    c "I just don't see how anything between us would work."

    c "I live on base, but I could be sent out on deployment tomorrow."

    c "And you travel so much. I reckon it'd be hard for us to really ever be in the same place all that much."

    c "That'd make it hard, right?"

    c "I don't want to waste either of our time on a relationship that just wouldn't work long term without some kind of dramatic change on at least one of our parts."

    c "I appreciate the thought, matchmaker, but I just don't see this working."

    show cody sad

    c "..."

    show sheep frown

    s "Yes, I do agree that our lifestyles would make a relationship difficult."

    s "I think it's workable when one person travels, but much more difficult when both parties are in that situation."

    s "If our situations were different, perhaps we'd make a fine couple. But unfortunately, they are not."

    show host

    h "So, you both reject the match?"

    hide host

    s "Yes, that's correct."

    show cody

    c "Yes."

    hide sheep with dissolve
    hide cody with dissolve

    $ persistent.achievements["cody-sheep"] = True

    return

label cody_viktor_ending:

    show cody at left with dissolve
    show viktor at right with dissolve

    show viktor nervous side

    v "Wow, you're really tall up close!"

    c "..."

    v "But not in a bad way!"

    v "Sorry, I didn't mean to be rude. Do you want to be friends?"

    v "I'm undead too! But not like you!"

    v "Uh..."

    v "Also not in a bad way."

    show viktor nervous

    v "Oh god, why am I like this?"

    c "Settle down, I get what you were trying to say."

    v "You do?"

    c "I'm afraid I have bad news, though."

    show viktor frown

    c "You seem like a nice young man, but sorry to say you're just not what I'm after."

    c "I have a lot of good friends and I'm not looking for more."

    c "That's the short of it."

    v "Oh."

    v "Okay."

    show cody smile side

    c "It's been a pleasure meeting you and the other contestants though."

    show cody

    c "Matchmaker, thank you for this opportunity. It wasn't quite right, but it was a solid effort."

    show viktor

    v "Was it?"

    c "..."

    v "I'm going to sit down now."

    hide viktor with dissolve
    show cody sad

    c "So long, matchmaker."

    hide cody with dissolve

    $ persistent.achievements["cody-viktor"] = True

    return

label cody_xel_ending:

    show cody at left with dissolve
    show xel at right with dissolve

    show xel thinking

    x "So..."

    c "..."

    x "..."

    c "..."

    x "Yeah, no. This isn't going to work."

    c "You seem like a...nice..."

    show xel ugh

    x "Save it, I'm not."

    c "Thank you, matchmaker, for this opportunity."

    show xel mad

    x "This is a fucking joke."

    show cody sad

    c "Matchmaker, I appreciate your intentions-"

    show xel ugh

    x "Spare me."

    c "-but I'm afraid I must decline. I just don't think Xel here and I are compatible."

    x "You can say that again."

    show cody

    c "Why?"

    show xel thinking

    x "..........."

    hide xel with dissolve
    show host at right

    h "Uh, give a round of applause for Cody, everyone!"

    a "Woo"

    hide cody with dissolve
    hide host with dissolve

    $ persistent.achievements["cody-xel"] = True

    return

label odonata_rust_ending:

    show odonata at left with dissolve
    show rust at right with dissolve

    o "Hello."

    r "Hi."

    show rust finger guns

    r "I like your carapace."

    r "Wouldn't mind running my digits all over it."

    show rust smile

    r "Get it?"

    r "I thought of that when we were waiting for the matchmaker to finish."

    o "..."

    o "Well, I'm flattered."

    show rust dot

    r "Oh."

    o "Unfortunately you're not quite what I'm looking for."

    r "..."

    r "Not biological enough for you, huh?"

    o "I didn't say that."

    show rust mad

    r "Pfft, whatever."

    hide rust with dissolve
    show host at right

    h "Give them a round of applause!"

    a "Wooo..."

    hide odonata with dissolve
    hide host with dissolve

    $ persistent.achievements["odonata-rust"] = True

    return

label odonata_sheep_ending:

    show odonata at left with dissolve
    show sheep at right with dissolve

    o "Hello."

    s "Same to you."

    o "Shall I start?"

    s "If you'd like to."

    o "Very well. We find you an acceptable candidate."

    o "If you are interested in what we have to offer, we would be interested to discuss it with you further."

    show sheep happy

    s "That's very generous of you."

    show sheep

    s "However, I'm quite attached to my own identity. I'm very headstrong, you see. So I must decline."

    s "I do appreciate the offer though."

    show odonata crossed

    o "I see."

    show sheep happy

    s "But since we're both out here, would you like to have dinner?"

    s "I've always been interested in visiting your sector. Maybe you could tell me more about it?"

    show odonata

    o "We would like that."

    s "Thank you."

    show sheep

    s "We can work out the details after the show."

    o "Yes, let's do that."

    show host

    h "Let's have a round of applause for friendship!"

    a "Wooooo!!!!"

    hide host with dissolve
    hide odonata with dissolve
    hide sheep with dissolve

    $ persistent.achievements["odonata-sheep"] = True

    return

label odonata_viktor_ending:

    show odonata at left with dissolve
    show viktor nervous side at right with dissolve

    v "......."

    o "Would you like us to go first?"

    v "............"

    o "Very well. You are an acceptable candidate."

    v "....................."

    o "Are you interested?"

    v ".............................."

    show viktor frown

    v "No! Absolutely not!"

    show viktor

    v "Sorry that was really rude I'm just emotional right now if there are any two people on the show who are obviously incompatabile it's us-"

    v "look there is a very wide gap between wanting to casually meet a new friend and absorbing someone directly into your brain-"

    v "....just no. Sorry."

    show viktor nervous side

    v "........."

    o "Your reaction is not unexpected. We too thought the match odd."

    show odonata point

    o "But we always strive to be open minded and will avail the opportunity to any suitible and interested candidates."

    o "Additionally, we appreciate your honestly."

    show odonata

    o "Allow us to do you the same courtesy; friendship is not what we are currently seeking."

    o "However in the spirit of this show, we extend to you and invitation to our ship. You mentioned you have an interest in spaceport management but I assume such facilities are rare where you live."

    show odonata point

    o "Perhaps you would like a tour of a state of the art ship and a viewing of Under the Wings of Pterport 1 with commentary by someone knowledgable in the field."

    show odonata
    
    o "I regret it is a land based port rather than orbital but there are many similarities."

    show viktor frown

    v "......"

    v "Can I have some butterflies, too?"

    o "Certainly. As long as they won't make you sick."

    v "No, no, it's fine, if I just eat a few..."

    show odonata whoa

    o "Then this evening we shall eat butterflies and take a deep dive into the exciting word of space traffic control."

    show viktor smile

    v "Okay. Sure."

    hide viktor with dissolve
    hide odonata with dissolve

    $ persistent.achievements["odonata-viktor"] = True

    return

label odonata_xel_ending:

    show odonata at left with dissolve
    show xel at right with dissolve

    o "Hello."

    x "Hey."

    o "Shall I start?"

    x "Sure."

    o "Very well. We find you an acceptable candidate."

    o "If you are interested in what we have to offer, we would be interested to discuss it with you further."

    o "What do you say?"

    show xel thinking

    x "..."

    x "Yeah, no."

    x "Not really my thing."

    show xel

    x "This matchmaker sucks."

    hide xel with dissolve

    o "Very well, then."
    
    hide odonata with dissolve

    show host

    h "Give them a cheer!"

    a "Woo."

    hide host with dissolve

    $ persistent.achievements["odonata-xel"] = True

    return

label rust_sheep_ending:

    show sheep at left with dissolve
    show rust at right with dissolve

    s "Hello."

    r "Sup."

    s "Apparently we're a match."

    r "Apparently so."

    s "Would you like me to go first?"

    r "Nah fuck it, it's a yes from me."

    show rust finger guns

    r "You're cool, girl. Let's go out."

    show sheep happy

    s "I would love to."

    show sheep

    s "I was going to say, you're definitely my type, and I'd like to get to know you better."

    show rust

    r "Well I'd be happy to provide you with the opportunity."

    s "Good. It's settled then."

    show host

    h "Let's give it up for our new couple!"

    a "Woooo!!"

    hide host with dissolve
    hide sheep with dissolve
    hide rust with dissolve

    $ persistent.achievements["rust-sheep"] = True

    return

label rust_viktor_ending:

    show rust at left with dissolve
    show viktor at right with dissolve

    r "Sup?"

    v "Not much."

    r "So you like games, huh?"

    show viktor smile

    v "Yes! So much, oh my god."

    show rust smile

    r "Cool. We'll get along. Put me down as a 'yes'."

    v "Oh, me too, then."

    show rust

    r "That was easy. Catch you later, new friend."

    v "Ok!"

    hide rust with dissolve
    hide viktor with dissolve

    $ persistent.achievements["rust-viktor"] = True

    return

label rust_xel_ending:

    show rust at left with dissolve
    show xel at right with dissolve

    show xel thinking

    x "So..."

    show rust smile

    r "Doesn't your system have a planet called Uranus?"

    show xel

    x "Yes."

    show rust finger guns

    r "Fuck yes, that is hilarous."

    show xel happy

    x "Yeah, it is, a bit. Haha."
    
    r "Wanna show me?"

    x "Sure."

    x "..."

    x "There's an obvious joke here but I'm not going to say it."

    show rust smile

    r "Pfffft hahaha!"

    show host

    h "Moving on!"

    hide host
    hide rust with dissolve
    hide xel with dissolve

    $ persistent.achievements["rust-xel"] = True

    return

label sheep_viktor_ending:

    show sheep at left with dissolve
    show viktor nervous side at right with dissolve

    s "Hello, dear."

    v "..."

    show sheep happy

    s "Not much of a talker, are you?"

    show viktor

    v "So you're like, famous?"

    s "I suppose you could say that."

    v "Fuck."

    s "Don't be nervous!"

    show viktor nervous side

    v "..."

    show sheep

    s "Would you like to watch a movie? You said you like that, right?"

    v "Um...if that's ok..."

    v "This is weird I've never met anyone famous before except for this guy who no one really knows here he's mostly famous online, he runs a blog I read, anyway he walked past me once at a shopping center it was really weird."

    s "How interesting!"

    s "That's a yes from me, matchmaker."

    show viktor

    v "Um, from me too, I guess."

    show viktor frown

    v "Sorry if I'm being weird."

    show sheep happy

    s "That's quite alright. Being on camera does tend to put you on the spot."

    show viktor smile

    s "Let's go sit down."

    show viktor

    v "Ok."

    hide sheep with dissolve
    hide viktor with dissolve

    show host

    h "Another happy friend couple!"

    a "Woooo!"

    hide host with dissolve

    $ persistent.achievements["sheep-viktor"] = True

    return

label sheep_xel_ending:

    show sheep at left with dissolve
    show xel at right with dissolve

    show sheep happy

    s "Hello, my friend."

    show xel happy

    x "Hey."

    s "Fancy seeing you here."

    x "Yeah, wow what a surprise!"

    show xel

    x "So what the fuck is this, matchmaker?"

    x "Obviously we came here to meet other people."

    show sheep

    s "Xel, don't be rude!"

    s "I'm sure the matchmaker decided that since we're such good friends, we should spend more time together."

    show sheep happy

    s "Isn't that right, matchmaker?"

    x "..."

    x "Well, this was a waste of time."

    hide xel with dissolve
    show sheep

    s "I'm sure you tried your best."

    s "Zopflam, matchmaker, please consider this match accepted by all paries."

    show sheep happy

    s "Xel would never reject me."

    x "(Unable to translate)"

    s "Xelly no one can hear you over there. You're too far from the microphones."

    x "(Unable to translate)"

    show sheep
    hide sheep with dissolve

    show host

    h "Uh...give them a clap!"

    a "Woooo!"

    hide host with dissolve

    $ persistent.achievements["sheep-xel"] = True

    return

label viktor_xel_ending:

    show xel at left with dissolve
    show viktor at right with dissolve

    x "Hey."

    v "Hi."

    x "..."

    v "..."

    x "So you seem...fine?"

    show viktor nervous side

    x "As a friend."

    show viktor smile

    v "Oh!"

    x "So yes from me? For whatever."

    x "Whatever friendship."

    v "Oh, good!"

    v "Um."

    v "Ok!"

    x "..."

    v "..."

    show viktor

    v "..."

    show host with dissolve

    h "Every friendship has it's blossom, and even awkward starts can-"

    show xel mad
    show viktor nervous side
    
    v "Awkward?"
    
    h "-lead to something beautiful! Give them a round of applause everyone!"

    a "Wooooo!!"

    hide xel with dissolve
    show viktor
    hide viktor with dissolve
    hide host with dissolve

    $ persistent.achievements["viktor-xel"] = True

    return
