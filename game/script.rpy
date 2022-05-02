#Game Script, made by Alette

################################################################################################################################################
#Default variables
init:
    default stress = 100 #Balance
    default actiontimer = 0 #We start counting from 1 cause of how menu works, so count events from 1
    default objectNo = 0 #Object to be added to the list when label is called, 0 means nothing is added.
    default Inventory = []
    default money = 15
    default maxmoney = money
    default preferences.text_cps = 50
    default goto_register = False
    default first_aisle = False
    default temptimer = 0
    #define 5 flags, decide if the player has bought an item in an aisle
    default firstaisle_item = False #Household
    default secondaisle_item = False #Entertainment
    default thirdaisle_item = False #Fresh Food
    default fourthaisle_item = False #Bakery
    default fifthaisle_item = False #Frozen
    default breakdown_reached = False #Nodig voor uit loop breken
    default abort_meat = False #
    default isNotStressed = True #
    default hasmusictriggered = False #
    default needtoplay = False
################################################################################################################################################
transform alette_right: #This is how you'd define new positions
    pos (.700, 1.0)
    anchor (.5, 1.0)
transform alette_left: #This is how you'd define new positions
    pos (.200, 1.0)
    anchor (.5, 1.0)
transform alette_notright:
    pos (.400, 1.0)
    anchor (.5, 1.0)
################################################################################################################################################
#Characters for the actual game
define mc1 = Character("Me", image="Characters/MC1.png")
define mc2 = Character("Me", image="Characters/MC2.png")
define mc3 = Character("Me", image="Characters/MC3.png")
define mc4 = Character("Me", image="Characters/MC4.png")
define cashier1 = Character("Cashier", image="Characters/cashier1.png")
define cashier2 = Character("Cashier", image="Characters/cashier2.png")
define cashier3 = Character("Cashier", image="Characters/cashier3.png")
define deliworker1 = Character("Helpful Person", image="Characters/deliworker1.png")
################################################################################################################################################
#Backgrounds for the game
image storefront = "Background/Storefront.png"
image bakery = "Background/Bakery.png"
image deli_fg = "Background/Deli_FG.png"
image deli_bg = "Background/Deli_BG.png"
image entertainment = "Background/Entertainment.png"
image frozen = "Background/Frozen.png"
image household = "Background/Household.png"
image register_fg = "Background/Register_FG.png"
image register_fg2 = "Background/Register_FG2.png"
image deli1 = "Background/Deli_BG.png"
image deli2 = "Background/Deli_FG.png"
image test = "Background/outside.png"
################################################################################################################################################
#Define Screens
screen Money: #Lists money
    text "{color=#FFD700}Money: [money]{/color}" xalign 1.0 xpos 0.99 ypos 0.01
screen Stress:
    text "{color=#00FF00}Stress: [stress]{/color}" xalign 1.0 xpos 0.99 ypos 0.7
screen InventoryList:
    vbox xpos 0.01 ypos 0.01:
        text "{color=#03a9f4}Inventory:{/color}"
        if 1 in Inventory:
            text "{color=#03a9f4}- Comic Book{/color}"
        if 2 in Inventory:
            text "{color=#03a9f4}- Pastrami{/color}"
        if 3 in Inventory:
            text "{color=#03a9f4}- Phlash{/color}"
        if 4 in Inventory:
            text "{color=#03a9f4}- Mrs Strong{/color}"
        if 5 in Inventory:
            text "{color=#03a9f4}- Thick Cut Fries{/color}"
        if 6 in Inventory:
            text "{color=#03a9f4}- Brown Ice Cream{/color}"
        if 7 in Inventory:
            text "{color=#03a9f4}- Red Box Pizza{/color}"
        if 8 in Inventory:
            text "{color=#03a9f4}- Chocolate Cake{/color}"
        if 9 in Inventory:
            text "{color=#03a9f4}- Carrot Cake{/color}"
        if 10 in Inventory:
            text "{color=#03a9f4}- Fancy Bread{/color}"
        if 11 in Inventory:
            text "{color=#03a9f4}- Celery{/color}"
        if 12 in Inventory:
            text "{color=#03a9f4}- Wrong Salami{/color}"
        if 13 in Inventory:
            text "{color=#03a9f4}- Yellow Box Pizza{/color}"
        if 14 in Inventory:
            text "{color=#03a9f4}- French Fries{/color}"
        if 15 in Inventory:
            text "{color=#03a9f4}- Purple Meal{/color}"
        if 16 in Inventory:
            text "{color=#03a9f4}- Pink Ice Cream{/color}"
        if 17 in Inventory:
            text "{color=#03a9f4}- Cupcake{/color}"
        if 18 in Inventory:
            text "{color=#03a9f4}- Blueberry Muffin{/color}"
        if 19 in Inventory:
            text "{color=#03a9f4}- Chocolate Muffin{/color}"
        if 20 in Inventory:
            text "{color=#03a9f4}- Glazed Donuts{/color}"
        if 21 in Inventory:
            text "{color=#03a9f4}- Baguette{/color}"
        if 22 in Inventory:
            text "{color=#03a9f4}- Corn{/color}"
        if 23 in Inventory:
            text "{color=#03a9f4}- Salami{/color}"
        if 24 in Inventory:
            text "{color=#03a9f4}- Brown Meal{/color}"
        if 25 in Inventory:
            text "{color=#03a9f4}- Sponge Cake{/color}"
        if 26 in Inventory:
            text "{color=#03a9f4}- Jam Donut{/color}"
        if 27 in Inventory:
            text "{color=#03a9f4}- Ringed Donut{/color}"
        if 28 in Inventory:
            text "{color=#03a9f4}- White Bread{/color}"
        if 29 in Inventory:
            text "{color=#29b6f6}- Brown Bread{/color}"
        if 30 in Inventory:
            text "{color=#03a9f4}- Mini Baguette{/color}"
        if 31 in Inventory:
            text "{color=#03a9f4}- Spinach{/color}"
        if 32 in Inventory:
            text "{color=#03a9f4}- Green Box Pizza{/color}"
        if 33 in Inventory:
            text "{color=#03a9f4}- Crinkle Cut Fries{/color}"
        if 34 in Inventory:
            text "{color=#03a9f4}- Blue Meal{/color}"
        if 35 in Inventory:
            text "{color=#03a9f4}- Green Ice Cream{/color}"
################################################################################################################################################
#Updates the list with a number based on the value of objectNo
label updateList:
    #ItemID listed in docs
    if objectNo > 0:
        if objectNo < 36: #adjust this number if there are more item IDs
            $Inventory.append(objectNo)
    else:
        "Error: Could not update updateList" #TEDOEN: Remove or not
    return
################################################################################################################################################
#Deze gebruik je elke keer nadat stress erafgaat
label checkMusic:
    if stress < 51:
        if hasmusictriggered == False:
            stop music fadeout 1.0
            play music "audio/Panic in the Aisles.ogg" fadein 1.0
            $ hasmusictriggered = True
#Plays correct button sound based on stress
label buttonSound:
    if stress < 51:
        play sound "audio/SFX/Alt Mouse Click.ogg"
        #if hasmusictriggered == False:
        #    stop music fadeout 1.0
        #    play music "audio/Panic in the Aisles.ogg" fadein 1.0
        #    $ hasmusictriggered = True
    else:
        play sound "audio/SFX/Mouse Click.ogg"
    return
################################################################################################################################################
#Calls breakdown correctly
label checkBreak:
    if stress < 1:
        jump breakdown
    return
################################################################################################################################################
#Debug menu, activates all screens
label debugger:
    show screen InventoryList
    show screen Money
    #show screen Stress #Zet deze lijn als commentaar als je dit niet in de game wilt
    return
################################################################################################################################################
label start:
    #Label Calls
    call debugger from _call_debugger
    call introduction from _call_introduction
    while goto_register == False:
        call menuloop from _call_menuloop
        if breakdown_reached == True:
            $ goto_register = True
    if breakdown_reached == True:
        $ goto_register = False

    if goto_register == True:
        call register from _call_register

    call outalive from _call_outalive
    # This ends the game.
    return

label introduction:
    stop music fadeout 2.0 #fades out the music
    scene test #TEDOEN: Remove / fix
    show mc1 with dissolve
    "Heehoo! Good to see you."
    call buttonSound from _call_buttonSound
    "Today I'm heading to the supermarket."
    call buttonSound from _call_buttonSound_1
    "It can be a bit of a minefield, but I have managed to build a pretty good routine to help me survive."
    call buttonSound from _call_buttonSound_2
    "You see, I am autistic, which means everyday environments can prove challenging for my senses and cause me to lose control of my abilities and emotions."
    call buttonSound from _call_buttonSound_3
    "I always plan ahead to avoid sensory overload and triggering situations. The store is usually quiet around this time of day, so I can be in and out in fifteen minutes if everything goes well and nothing has changed..."
    hide mc1
    hide text
    with fade
    scene storefront with dissolve
    "{cps=2}...{/cps}Why today?! {w=0.5} What have they changed?! {w=0.5} How will I find the things I need?! {w=0.5}{cps=10}Why is it so busy?!{/cps}"
    call buttonSound from _call_buttonSound_5
    show mc3 with dissolve
    "Ugh, a queue to get in the door. {w=0.5} I hate being in large crowds, the sound of their talking, footsteps, people coughing and sneezing around me. It's a good thing I have my trusty headphones with me! {w=0.5} Let's hope the battery holds up okay..."
    call buttonSound from _call_buttonSound_6
    hide mc3 with dissolve
    play music "audio/Trip to the Market.ogg"
    "Much better. Now, if I could just figure out where to go when I get inside..."
    call buttonSound from _call_buttonSound_20
    show deliworker1 with dissolve
    deliworker1 "“mfmfmfmfmf mfmf mfmf mfmfm….mmf?"
    call buttonSound from _call_buttonSound_7
    hide deliworker1 with dissolve
    mc1 "I can't hear what you're saying to me..."
    "Oh, what's this? {w=0.5} A leaflet about the refurbishment. Wonderful, where's the bin?"
    call buttonSound from _call_buttonSound_8
    "OH! It has a map of the store. That's actually amazing."
    call buttonSound from _call_buttonSound_9
    "Imagine if every store did this when they change their layout. Wouldn't that be nice?"
    call buttonSound from _call_buttonSound_10
    "Bleh, It’s not particularly detailed though. With 5 aisles, I guess they expect us to walk up and down each one like cattle on a conveyor belt! Not today, supermarket. That kind of chaos leads to meltdowns. I’m going to have to wing this and hope I make it out in one piece."
    call buttonSound from _call_buttonSound_27
    "Which aisle first though? They're all pretty treacherous..."
    call buttonSound from _call_buttonSound_34
    "Oh, wonderful. There's no signal in here now. Can't stream my music. It's so noisy in here without it!"
    #TEDOEN: add busy sounds?
    call buttonSound from _call_buttonSound_35
    "10 years ago, this type of situation would've already sent me spiraling into a {color=#FF0000}meltdown{/color}."
    call buttonSound from _call_buttonSound_11
    "In that time I've built up routines through trial and error. I learned to be careful and avoid the triggers that cause me {color=#FF0000}sensory overload{/color}."
    call buttonSound from _call_buttonSound_13
    "Sometimes I still push myself too far, and getting overloaded is not pretty."
    call buttonSound from _call_buttonSound_14
    "That can't happen today. We must avoid a {color=#FF0000}Sensory Overload{/color}."
    call buttonSound from _call_buttonSound_15
    return

label menuloop:
    $ actiontimer = actiontimer + 1
    if stress > 50:
        if hasmusictriggered == True:
            $ hasmusictriggered = False
            $ needtoplay = True
            stop music fadeout 1.0
    $ alltrue = False
    if firstaisle_item == True:
        if secondaisle_item == True:
            if thirdaisle_item == True:
                if fourthaisle_item == True:
                    if fifthaisle_item == True:
                        $ alltrue = True
    menu:
        "Now, where should I go?"
        "Fresh Foods":
            call freshfood from _call_freshfood
        "Frozen Foods":
            call frozen from _call_frozen
        "Baked Goods":
            call bakery from _call_bakery
        "Entertainment":
            call entertainment from _call_entertainment
        "Household":
            call household from _call_household
        "Go to the register" if alltrue:
            $ goto_register = True
    return

label household:
    scene household
    $ temptimer = 0
    if firstaisle_item == True:
        call mchider from _call_mchider_1
        show mc1
        "Hmmmm, I think I don't need anything from this aisle anymore."
        call buttonSound from _call_buttonSound_36
        hide mc1
        return
    if stress > 50:
        play music "audio/Scanning the Store.ogg"
    "I hate this aisle. The chemical smells overwhelm me the moment I go near them. I get so sick that I usually have to hold my breath and grab what I can before the smell becomes too much."
    call buttonSound from _call_buttonSound_16
    show mc2
    "I have to be very careful about what I buy here. If the scent is overpowering, I can't have it in my house, but I also need to keep my place clean and tidy or my friends won't want to visit me!"
    call buttonSound from _call_buttonSound_17
    "I can't see any cleaning products here that I recognize. {color=#FF0000}Jasmine, pine and vanilla scents{/color} make me feel incredibly ill. Whereas smells like {color=#ACD1AF}lavender{/color} have always been fine. How do I figure out which ones are safe?"
    call buttonSound from _call_buttonSound_37
    call householdmenu from _call_householdmenu
    if breakdown_reached == False:
        if temptimer > 4:
            call mchider from _call_mchider_2
            show mc3
            "Oh no... I stayed in this aisle for too long."
            call buttonSound from _call_buttonSound_38
            jump breakdown
    if stress > 0:
        "Right, let's get out of this aisle before I pass out."
        call buttonSound from _call_buttonSound_39
        if stress > 50:
            stop music fadeout 1.0
            play music "audio/Trip to the Market.ogg"
    return

label householdmenu:
    call mchider from _call_mchider
    $ temptimer = temptimer + 1
    menu:
        "So, what should I buy?"
        "Zebreze":
            "Is this some kind of... Zebra based scent? I don't know if I trust this..."
            call buttonSound from _call_buttonSound_18
            menu:
                "What should I do?"
                "Test Smell":
                    show mc3
                    "Ugh, zebras smell really really bad... I don't think I'll buy this."
                    call buttonSound from _call_buttonSound_19
                    $ stress = stress - 10 #Balance
                    call checkMusic from _call_checkMusic
                    if stress < 1:
                        call checkBreak from _call_checkBreak
                        return
                    jump householdmenu
                "Put Back":
                    jump householdmenu
        "Jaspinilla":
            show mc3
            "BLURGH!{w=0.5} This is like a death mix. Jasmine, pine and vanilla in one can?! It seems my enemies have learned greatest weakness... I can even smell it through the can. I need to put this awful thing down!"
            call buttonSound from _call_buttonSound_21
            $ stress = stress - 50 #Balance
            call checkMusic from _call_checkMusic_1
            if stress < 1:
                call checkBreak from _call_checkBreak_1
                return
            jump householdmenu
        "Clade":
            "There are trees on the can. This is probably disgusting pine."
            call buttonSound from _call_buttonSound_22
            menu:
                "What should I do?"
                "Test Smell":
                    show mc3
                    "Yuck, Pine! Why did I think testing this was a good idea?!"
                    call buttonSound from _call_buttonSound_40
                    $ stress = stress - 20 #Balance
                    call checkMusic from _call_checkMusic_2
                    if stress < 1:
                        call checkBreak from _call_checkBreak_2
                        return
                    jump householdmenu
                "Put Back":
                    jump householdmenu
        "Phlash":
            "There is nothing on this name or bottle that helps me figure out what is inside of it. The words on the back are just gibberish... What happened to clear instructions, people?!"
            call buttonSound from _call_buttonSound_23
            menu:
                "What should I do?"
                "Test Smell":
                    show mc1
                    "Oooh, I have no idea what this is... spiced apples, maybe? I love it though, it smells incredible. It costs {color=#FFD700}€1,31{/color}."
                    call buttonSound from _call_buttonSound_24
                    hide mc1
                    $ stress = stress + 5 #Balance
                    menu:
                        "Do I buy this?"
                        "Put in basket":
                            $ firstaisle_item = True
                            if money < 1.31:
                                show mc3
                                "Ah, I can't afford this. Or anything on this shelf... I guess I won't be inviting friends over this week after all."
                                call buttonSound from _call_buttonSound_41
                                hide mc3
                                return
                            $ money = money - 1.31
                            $ objectNo = 3
                            call updateList from _call_updateList
                            $ objectNo = 0
                            return
                        "Put Back":
                            jump householdmenu
                "Put Back":
                    jump householdmenu
        "Mrs Strong":
            show mc1
            "Hmmm, it's a purple can. Could this be{cps=3}...{/cps} {w=0.1} It is Lavender! It costs {color=#FFD700}€2,00{/color}."
            call buttonSound from _call_buttonSound_25
            hide mc1
            menu:
                "Do I buy this?"
                "Put in basket":
                    if money < 2.00:
                        if money > 1.31:
                            show mc2
                            "Hmmm, I don't have enough money for this. Is there something cheaper I can afford?"
                            call buttonSound from _call_buttonSound_42
                            hide mc2
                        else:
                            $ firstaisle_item = True
                            show mc3
                            "Ah, I can't afford this. Or anything else on this shelf... I guess I won't be inviting friends over this week after all."
                            call buttonSound from _call_buttonSound_43
                            hide mc3
                            return
                    $ firstaisle_item = True
                    $ money = money - 2.00
                    $ objectNo = 4
                    call updateList from _call_updateList_1
                    $ objectNo = 0
                    return
                "Put Back":
                    jump householdmenu
    return

label entertainment:
    scene entertainment
    call mchider from _call_mchider_3
    if needtoplay == True:
        play music "audio/Trip to the Market.ogg"
        $ needtoplay = False
    if secondaisle_item == True:
        show mc1
        "Hmmm, I don't think I need anything else from this aisle."
        call buttonSound from _call_buttonSound_44
        hide mc1
        return
    show mc1
    "Oh hey that's right, Sensory: Life on the Spectrum! I've been meaning to buy it. The creators are so cool, I think they have another kickstarter coming out soon too..."
    call buttonSound from _call_buttonSound_26
    hide mc1
    if actiontimer <= 2:
        show mc2
        "Ah, nuts. There are so many people in this aisle I can't get to the shelf. I'll come back later. Crowded spaces are a horrible experience."
        call buttonSound from _call_buttonSound_45
        $ stress = stress - 10 #Balance
        call checkMusic from _call_checkMusic_3
        if stress < 1:
            call checkBreak from _call_checkBreak_3
            return
        hide mc2
    elif actiontimer > 5: #Balance
        show mc3
        "It SOLD OUT?! I knew it was popular, but come on! I have been waiting to read it for a year now. I can't believe I missed it... I'll have to go and order it online."
        call buttonSound from _call_buttonSound_28
        $ secondaisle_item = True
        $ stress = stress - 40#Balance
        call checkMusic from _call_checkMusic_4
        if stress < 1:
            call checkBreak from _call_checkBreak_4
            return
    else:
        show mc1
        "Oooh at last! I have been waiting so long to read this. An anthology of comics written by autistic people, for autistic people. It has rave reviews online!"
        $ peeked_already = False
        call buttonSound from _call_buttonSound_29
        call mchider from _call_mchider_4
        menu bookchoice:
            "What should I do?"
            "Take a quick peek at it now!":
                if peeked_already == True:
                    "I already did this! I need to get going."
                    call buttonSound from _call_buttonSound_30
                    jump bookchoice
                $ actiontimer = actiontimer + 1
                show mc1
                "Ahh, so relatable... what a great book!"
                $ peeked_already = True
                hide mc1
                call buttonSound from _call_buttonSound_31
                jump bookchoice
            "Put in basket.":
                $ secondaisle_item = True
                if money < 8.00:
                    show mc2
                    "I don't think I have enough money left for this. I'll have to order it on Amazon!"
                    call buttonSound from _call_buttonSound_32
                    $ stress = stress - 20 #Balance
                    call checkMusic from _call_checkMusic_5
                    hide mc2
                    if stress < 1:
                        call checkBreak from _call_checkBreak_5
                        return
                    return
                show mc1
                "I can't wait to go home and read this!"
                call buttonSound from _call_buttonSound_33
                hide mc1
                $ stress = stress + 20 #Balance
                $ objectNo = 1
                call updateList from _call_updateList_2
                $ objectNo = 0
                $ money = money - 8
    return

label frozen:
    $ actuallygotpizza = False
    $ actuallygotmeal = False
    $ actuallygotice = False
    $ actuallygotfries = False
    scene frozen
    call mchider from _call_mchider_5
    if fifthaisle_item == True:
        show mc1
        "Hmmmm, I think I don't need anything from this aisle anymore."
        call buttonSound from _call_buttonSound_46
        hide mc1
        return
    $ stress = stress - 10 #Balance
    call checkMusic from _call_checkMusic_6
    if stress < 1:
        call checkBreak from _call_checkBreak_6
        return
    $ renpy.music.set_volume(.7,0,channel="sound") #TEDOEN: Audio balancing
    play sound "audio/SFX/Fridge Hum.ogg" loop
    if stress > 50:
        play music "audio/Scanning the Store.ogg"
    "For many, the hardest part of the frozen aisle is the coldness. For me it’s the humming. The monotonous repetitive noise from the freezers, burrowing through my ears and into the center of my skull. "
    "I’d normally drown it out with my music, but today I'm stuck with using my headphones like mufflers."
    "If I rush I can leave the aisle quicker and maybe everything will be ok. It’ll be stressful if I get the wrong items, but at least it’s quick!"
    $ frozenfoodcheck = False
    $ frozenfoodcount = 0 #only increase frozen food count if not "any"picked, so that this increases by 2 at most
    $ iceleft = True
    $ readyleft = True
    $ friesleft = True
    $ pizzaleft = True
    $ prizetotal = 0 #add the prices of the items grabbed together and substract from money in the end.
    while frozenfoodcheck == False:
        menu frozenfoods:
            "What should I get?"
            "Pizza" if pizzaleft:
                $ pizzaleft = False
                menu:
                    "What do I grab?"
                    "Anything's good":
                        $ objectNo = 32
                        $ actuallygotpizza = True
                        #no money specified because this item is gonna get returned either way
                    "Get something specific":
                        $ iceleft = False
                        $ trygreen = True
                        $ frozenfoodcount = frozenfoodcount + 1
                        menu pizzachoice:
                            "What should I grab?"
                            "Yellow Box Pizza - {color=#FFD700}€0,99{/color}": #TEDOEN: prize
                                show mc1
                                "Yum, I like plain cheese pizza. This will do nicely."
                                #call buttonSound from _call_buttonSound_50
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ objectNo = 13
                                        $ prizetotal = prizetotal + 0.99
                                        $ actuallygotpizza = True
                                    "Put back":
                                        if actuallygotice == False:
                                            $ iceleft = True
                                        $ pizzaleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
                            "Red Box Pizza - {color=#FFD700}€1,99{/color}":
                                show mc1
                                "Ohhh, meat. It costs a bit more, but I love a thick meaty pizza!"
                                #call buttonSound from _call_buttonSound_51
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ objectNo = 7
                                        $ prizetotal = prizetotal + 1.99
                                        $ actuallygotpizza = True
                                    "Put back":
                                        if actuallygotice == False:
                                            $ iceleft = True
                                        $ pizzaleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
                            "Green Box Pizza - {color=#FFD700}€1,50{/color}" if trygreen:
                                show mc2
                                $ stress = stress - 5 #Balance
                                call checkMusic from _call_checkMusic_7
                                "Oh, veggie pizza. As much as I love crunchy veggies, soft goopie vegetables on a pizza are disgusting. I don't want this!"
                                #call buttonSound from _call_buttonSound_52
                                if stress < 1:
                                    "...."
                                    call checkBreak from _call_checkBreak_7
                                    return
                                hide mc2
                                $ trygreen = False
                                jump pizzachoice
            "Fries" if friesleft:
                $ friesleft = False
                menu:
                    "What do I grab?"
                    "Anything's good":
                        $ objectNo = 14
                        $ prizetotal = prizetotal + 1.09
                        $ frozenfoodcount = frozenfoodcount + 1
                        $ actuallygotfries = True
                    "Get something specific":
                        $ readyleft = False
                        $ trycrinkle = True
                        $ frozenfoodcount = frozenfoodcount + 1
                        menu frieschoice:
                            "What should I grab?"
                            "Thick Cut Fries - {color=#FFD700}€1,00{/color}":
                                show mc1
                                "These are great! So big and filling."
                                #call buttonSound from _call_buttonSound_53
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ objectNo = 5
                                        $ prizetotal = prizetotal + 1.00
                                        $ actuallygotfries = True
                                    "Put Back":
                                        $ friesleft = True
                                        if actuallygotmeal == False:
                                            $ readyleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
                            "French Fries - {color=#FFD700}€1,09{/color}":
                                show mc1
                                "Oooh french fries are all right if I can cook them properly! If I forget... which I usually do, they can be a bit hard and spiky on my mouth. Not the best option..."
                                #call buttonSound from _call_buttonSound_54
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ objectNo = 14
                                        $ prizetotal = prizetotal + 1.09
                                        $ actuallygotfries = True
                                    "Put back":
                                        $ friesleft = True
                                        if actuallygotmeal == False:
                                            $ readyleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
                            "Crinkle Cut Fries - {color=#FFD700}€1,40{/color}" if trycrinkle:
                                $ trycrinkle = False
                                show mc2
                                $ stress = stress - 5 #Balance
                                call checkMusic from _call_checkMusic_8
                                "Someone had the bright idea to make fries with sharp saw-like edges on them, they're a sensory nightmare for me! My mouth aches just thinking about eating these potato blades… get back in the freezer."
                                #call buttonSound from _call_buttonSound_55
                                if stress < 1:
                                    call checkBreak from _call_checkBreak_8
                                    return
                                hide mc2
                                jump frieschoice
            "Ready meal" if readyleft:
                $ readyleft = False
                menu:
                    "What do I grab?"
                    "Anything's good":
                        $ objectNo = 34
                        $ actuallygotmeal = True
                    "Get something specific":
                        $ frozenfoodcount = frozenfoodcount + 1
                        $ friesleft = False
                        $ trybmeal = True
                        menu readychoice:
                            "What should I take?"
                            "Purple Meal - {color=#FFD700}€1,49{/color}":
                                show mc1
                                "Chicken Curry! Not a healthy option, but an easy one. With my energy being so unpredictable it can be great to have one of these in the freezer for days when I'm just too tired to cook."
                                #call buttonSound from _call_buttonSound_56
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ objectNo = 15
                                        $ prizetotal = prizetotal + 1.49
                                        $ actuallygotmeal = True
                                    "Put back":
                                        $ readyleft = True
                                        if actuallygotfries == False:
                                            $ friesleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
                            "Blue Meal - {color=#FFD700}€1,00{/color}" if trybmeal:
                                $ trybmeal = False
                                show mc3
                                $ stress = stress - 5 #Balance
                                call checkMusic from _call_checkMusic_9
                                "Microwave fish?! Who would think this was a good idea? It'll ruin my house, and upset every person within a ten mile radius. This shouldn't exist, it is inviting trouble!"
                                #call buttonSound from _call_buttonSound_57
                                if stress < 1:
                                    call checkBreak from _call_checkBreak_9
                                    return
                                hide mc3
                                jump readychoice
                            "Brown Meal - {color=#FFD700}3,74{/color}":
                                show mc1
                                "Ooh, Microwave Tomato Pasta Bake. This is an easy laid back meal that I'll always be happy to eat. There's a lot of hidden vegetables in here too, which is a bonus!"
                                #call buttonSound from _call_buttonSound_58
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ prizetotal = prizetotal + 3.74
                                        $ objectNo = 24
                                        $ actuallygotmeal = True
                                    "Put back":
                                        $ readyleft = True
                                        if actuallygotfries == False:
                                            $ friesleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
            "Ice cream" if iceleft:
                $ iceleft = False
                menu:
                    "What do I grab?"
                    "Anything's good":
                        $ objectNo = 16
                        $ prizetotal = prizetotal + 1.67
                        $ frozenfoodcount = frozenfoodcount + 1
                        $ actuallygotice = True
                    "Get something specific":
                        $ frozenfoodcount = frozenfoodcount + 1
                        $ trypistache = True
                        $ pizzaleft = False
                        menu icechoice:
                            "What should I get?"
                            "Green Ice Cream - {color=#FFD700}€1.55{/color}" if trypistache:
                                show mc2
                                $ stress = stress - 5 #Balance
                                call checkMusic from _call_checkMusic_10
                                "Mint? No, wait... Pistacchio?! This is criminal. What kind of dessert is this?! Back it goes!"
                                #call buttonSound from _call_buttonSound_59
                                if stress < 1:
                                    call checkBreak from _call_checkBreak_10
                                    return
                                hide mc2
                                $ trypistache = False
                                jump icechoice
                            "Pink Ice Cream - {color=#FFD700}€1,67{/color}":
                                show mc1
                                $ stress = stress + 5 #Balance
                                "Strawberry! Yes, get in the basket now! No further questions."
                                $ actuallygotice = True
                                #call buttonSound from _call_buttonSound_60
                                hide mc1
                                $ prizetotal = prizetotal + 1.67
                                $ objectNo = 16
                            "Brown Ice Cream - {color=#FFD700}€1,87{/color}":
                                show mc1
                                "Wait, coffee ice cream? I was expecting chocolate... but this sounds like it would be nice. It costs a bit more, but I think this is a flavour I could get hooked on for a bit."
                                #call buttonSound from _call_buttonSound_61
                                hide mc1
                                menu:
                                    "What should I do?"
                                    "Put in basket":
                                        $ prizetotal = prizetotal + 1.87
                                        $ actuallygotice = True
                                        $ objectNo = 6
                                    "Put back":
                                        $ iceleft = True
                                        if actuallygotpizza == False:
                                            $ pizzaleft = True
                                        $ frozenfoodcount = frozenfoodcount - 1
                                        jump frozenfoods
        call updateList from _call_updateList_15
        $ objectNo = 0
        if frozenfoodcount == 2:
            $ frozenfoodcheck = True
    $ fifthaisle_item = True
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1,0,channel="sound")
    "Okay, that's everything. I hope I didn't grab anything awful by mistake. Let's quickly check."
    call buttonSound from _call_buttonSound_62
    if 32 in Inventory:
        $ Inventory.remove(32)
        show mc2
        $ stress = stress - 10
        "Ewww, veggie pizza. No, I can't eat that. I'll just put that back in the freezer and leave without..."
        call buttonSound from _call_buttonSound_63
    if 34 in Inventory:
        $ Inventory.remove(34)
        show mc2
        $ stress = stress - 10
        "Microwave fish?! Disgusting! The smell would end me. That's going back in the freezer!"
        call buttonSound from _call_buttonSound_64
    call mchider from _call_mchider_8
    if money < prizetotal:
        show mc2
        $ stress = stress - 10
        "I don't think I have enough money left for all of this... I'd better put everything back and get out of this aisle."
        call buttonSound from _call_buttonSound_65
        $ prizetotal = 0
        if 13 in Inventory:
            $ Inventory.remove(13)
        if 7 in Inventory:
            $ Inventory.remove(7)
        if 14 in Inventory:
            $ Inventory.remove(14)
        if 5 in Inventory:
            $ Inventory.remove(5)
        if 15 in Inventory:
            $ Inventory.remove(15)
        if 24 in Inventory:
            $ Inventory.remove(24)
        if 16 in Inventory:
            $ Inventory.remove(16)
        if 6 in Inventory:
            $ Inventory.remove(6)
        hide mc2
    $ money = money - prizetotal
    "Okay, finally I can get out of this aisle."
    call buttonSound from _call_buttonSound_66
    if stress > 50:
        play music "audio/Trip to the Market.ogg"
    return

label bakery:
    scene bakery
    call mchider from _call_mchider_6
    if needtoplay == True:
        play music "audio/Trip to the Market.ogg"
        $ needtoplay = False
    if fourthaisle_item == True:
        show mc1
        "Hmmm, I think I don't need anything else from this aisle."
        call buttonSound from _call_buttonSound_67
        hide mc1
        return
    show mc1
    "Everything here is so tasty! The smells are wonderful. I could stay here all day! I'd buy everything if I could."
    call buttonSound from _call_buttonSound_68
    "Unfortunately, I don't have the millions I'd need to satisfy my pastry addiction. So I'll have to make some decisions."
    call buttonSound from _call_buttonSound_69
    "Decision making can be tough for autistics. I hate having to make choices that I might regret later, or that impact other things. I like to consider my options. Studies show this is a common experience for others like me, too."
    call buttonSound from _call_buttonSound_70
    "I need food for the week, and my friends are coming over tomorrow!" #TEDOEN: colour code bread and snack to be clear
    call buttonSound from _call_buttonSound_71
    hide mc1
    $ earlygame = False
    $ middlegame = False
    if actiontimer < 2:
        $ earlygame = True
    if actiontimer < 4:
        $ middlegame = True
    if earlygame == True:
        show mc2
        $ stress = stress - 10 #Balance
        call checkMusic from _call_checkMusic_11
        if stress > 50:
            play music "audio/Scanning the Store.ogg"
        "There's so much to choose from here, though. What do I get?"
        call buttonSound from _call_buttonSound_72
        if stress < 1:
            hide mc2
            show mc3
            "There's too much... I'm getting overwhelmed."
            call buttonSound from _call_buttonSound_73
            call checkBreak from _call_checkBreak_11
            return
        hide mc2
    elif middlegame == True:
        show mc1
        $ stress = stress - 5 #Balance
        call checkMusic from _call_checkMusic_12
        if stress < 1:
            hide mc1
            show mc3
            "There's too many things... I'm getting overwhelmed."
            call buttonSound from _call_buttonSound_74
            call checkBreak from _call_checkBreak_12
            return
        "There's quite a bit of choice... what should I get?"
        call buttonSound from _call_buttonSound_75
        hide mc1
    else:
        show mc2
        "There's not many things left. At least that makes choosing easier."
        call buttonSound from _call_buttonSound_76
        hide mc2
    if money < 1.35:
        "I don't have enough money left for bread?! Oh no..."
        call buttonSound from _call_buttonSound_77
        jump breakdown
    $ notwbget = True #Has the player not gotten white bread
    $ notbbget = True #Has the player not gotten brown bread
    $ notbagget = True #Has the player not gotten baguette
    $ notmbaget = True #Has the player not gotten mini baguette
    $ notfancyget = True #Has the player not gotten fancy sliced
    $ slicedleft = True #Becomes false if no more sliced left
    if middlegame == False or notbagget == False:
        $ notbagget = False
    if earlygame == False or notmbaget == False:
        $ notmbaget = False
    menu breadchoices:
        "What should I get?"
        "Sliced Bread - {color=#FFD700}€1,35{/color}" if slicedleft:
            "Ah, the best. I could eat you for breakfast, lunch and dinner. I can't really present my friends with plain bread when they visit though, they're not pigeons. If only they were… maybe I'll throw some in the garden when I get home, then sketch the birds that land and eat it."
            call buttonSound from _call_buttonSound_78
            menu slicedbreads:
                "Which one do I get?"
                "Sliced White Bread - {color=#FFD700}€1,35{/color}" if notwbget: #TEDOEN: Colour
                    "White bread tastes good... but they say it's not very good for you. How bad could it be?"
                    call buttonSound from _call_buttonSound_79
                    menu:
                        "What should I do?"
                        "Put in basket":
                            $ fourthaisle_item = True
                            $ money = money - 1.35
                            $ objectNo = 28
                            call updateList from _call_updateList_3
                            $ objectNo = 0
                            $ stress = stress + 5 #Balance
                            $ notwbget = False
                            if notbbget == False:
                                $ slicedleft = False
                            jump breadchoices
                        "Get a different kind of bread":
                            jump breadchoices
                "Sliced Brown Bread - {color=#FFD700}€1,35{/color}" if notbbget: #TEDOEN: add colour
                    "Brown bread is not as nice, but it’s definitely healthier… the birds in my garden would probably like the seeds too."
                    call buttonSound from _call_buttonSound_80
                    menu:
                        "What should I do?"
                        "Put in basket":
                            $ fourthaisle_item = True
                            $ money = money - 1.35
                            $ objectNo = 29
                            call updateList from _call_updateList_4
                            $ objectNo = 0
                            $ notbbget = False
                            if notwbget == False:
                                $ slicedleft = False
                            jump breadchoices
                        "Get something else":
                            jump breadchoices
        "Fancy Unsliced Bread - {color=#FFD700}€2,00{/color}" if notfancyget:
            if money < 2:
                "I don't have the money for fancy bread, let's pick a different type of bread."
                call buttonSound from _call_buttonSound_81
                jump breadchoices
            "Ohoho, fancy bread eh... I could treat myself, and make some nice food for when me and my friends hang out. It's a bit expensive though."
            call buttonSound from _call_buttonSound_82
            menu:
                "What should I do?"
                "Put in basket":
                    $ fourthaisle_item = True
                    $ money = money - 2.00
                    $ objectNo = 10
                    call updateList from _call_updateList_5
                    $ objectNo = 0
                    $ stress = stress + 10 #Balance
                    $ notfancyget = False
                    jump breadchoices
                "Get something else":
                    "Oh well, I guess getting something else is better for my wallet. Let's see..."
                    call buttonSound from _call_buttonSound_83
                    jump breadchoices
        "Baguettes - {color=#FFD700}€0,79{/color}" if notbagget:
            "Une baguette, très bien! This would be pretty nice for today, but it'll be hard by tomorrow. I do like baguettes though..."
            call buttonSound from _call_buttonSound_84
            menu:
                "What should I do?"
                "Buy it":
                    if money < 2.14:
                        "Actually, I don't think I have enough money to buy more bread after this. I should get normal bread instead."
                        jump breadchoices
                        call buttonSound from _call_buttonSound_85
                    $ money = money - 0.79
                    $ objectNo = 21
                    call updateList from _call_updateList_6
                    $ objectNo = 0
                    $ notbagget = False
                    jump breadchoices
                "Get something else":
                    jump breadchoices
            "Ooh! Une petite baguette! That's better than a massive one just for me! I could have this for lunch, but I'd still need something for the rest of the week." #TEDOEN: colour
        "Mini Baguette - {color=#FFD700}€0,30{/color}" if notmbaget:
            call buttonSound from _call_buttonSound_86
            menu:
                "What should I do?"
                "Buy it":
                    if money < 1.65:
                        "Actually, I don't think I have enough money to buy more bread after this. I should get normal bread instead."
                        call buttonSound from _call_buttonSound_87
                        jump breadchoices
                    $ money = money - 0.30
                    $ stress = stress + 10 #Balance
                    $ objectNo = 30
                    $ notmbaget = False
                    call updateList from _call_updateList_7
                    $ objectNo = 0
                    jump breadchoices
                "Get something else":
                    jump breadchoices
        "Head to snacks":
            "Neat. That covers normal bread. Now, let's see what they have for snacks."
    if money < 1:
        "Ahh I don't have enough money left to buy snacks! Maybe I can suggest my friends meet in town so I don't have to feed them..."
        call buttonSound from _call_buttonSound_88
        $ stress = stress - 10 #Balance
        call checkMusic from _call_checkMusic_13
        call checkBreak from _call_checkBreak_13
        return
    call buttonSound from _call_buttonSound_89
    $ notspongeget = True #Has the player not gotten sponge cake
    $ notchocoget = True #Has the player not gotten Chocolate Cake
    $ noccget = True #Has the player not gotten cupcakes
    $ nocmufget = True #Has the player not gotten chocolate muffins
    $ nobbmget = True #Has the player not gotten blueberry muffins
    $ nojdget = True #Has the player not gotten jam donuts
    $ nordget = True #Has the player not gotten ringed donuts
    $ nogdget = True #Has the player not gotten glazed donuts
    if earlygame == False or notchocoget == False:
        $ notchocoget = False
    if middlegame == False or nocmufget == False:
        $ nocmufget = False
    if middlegame == False or nordget == False:
        $ nordget = False
    if nogdget == False or earlygame == False:
        $ nogdget = False
    menu snackmenu:
        "Let's see. What should I get?" #TEDOEN: Colour all the prices
        "Sponge Cake - {color=#FFD700}€1,79{/color}" if notspongeget:
            "I could eat this for dessert over a few nights, or serve it to my friends. Unless it's a bit plain maybe? They might prefer something smaller."
            if money < 1.79:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_90
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.79
                    $ objectNo = 25
                    $ notspongeget = False
                    call updateList from _call_updateList_8
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Chocolate Cake - {color=#FFD700}€2,75{/color}" if notchocoget:
            "It'll be hard work saving this for my friends, it looks delicious! It's so unhealthy though."
            if money < 2.75:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_91
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 2.75
                    $ objectNo = 8
                    $ notchocoget = False
                    call updateList from _call_updateList_16
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Cupcakes - {color=#FFD700}€0,99{/color}" if noccget:
            "Oh these look so cute and delicious! There's 8 of them here so I could eat a few today and serve the rest up to my friends."
            if money < 0.99:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_92
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 0.99
                    $ objectNo = 17
                    $ noccget = False
                    call updateList from _call_updateList_17
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Chocolate Muffins - {color=#FFD700}€1,66{/color}" if nocmufget:
            "Ah Muffins, the perfect food group! 4 in a pack, my friends love these, I'm not so keen."
            if money < 1.66:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_93
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.66
                    $ objectNo = 19
                    $ nocmufget = False
                    call updateList from _call_updateList_18
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Blueberry Muffins - {color=#FFD700}€1,79{/color}" if nobbmget: #TEDOEN: fix all the prices here and add an euro sign
            "Ah Muffins, the perfect food group! 4 in a pack, I love these, I hope my friends do too!"
            if money < 1.79:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_94
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.79
                    $ objectNo = 18
                    $ nobbmget = False
                    call updateList from _call_updateList_19
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Jam Donuts - {color=#FFD700}€2,40{/color}" if nojdget:
            "Hmm I like these, but I don't know if my friends do."
            if money < 2.40:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_95
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 2.40
                    $ objectNo = 26
                    $ nojdget = False
                    call updateList from _call_updateList_20
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Ringed Donuts - {color=#FFD700}€1,69{/color}" if nordget:
            "A bit plain...but inoffensive too! A cup of tea with these would be nice!"
            if money < 1.69:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_96
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.69
                    $ objectNo = 27
                    $ nordget = False
                    call updateList from _call_updateList_21
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Glazed Donuts - {color=#FFD700}€1,40{/color}" if nogdget:
            "Mmm these are probably my favourite actually. Who doesn't like glazed?!"
            if money < 1.40:
                "I don't have enough money for this. Let's get something else."
                call buttonSound from _call_buttonSound_97
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.40
                    $ objectNo = 20
                    $ nogdget = False
                    call updateList from _call_updateList_22
                    jump snackmenu
                "Get something else":
                    jump snackmenu
        "Let's move on.":
            "Hmmm, I think my wallet would be happier if I gave the snacks a miss..."
            call buttonSound from _call_buttonSound_98
            return
    $ objectNo = 0
    $ stress = stress + 5 #Balance
    if earlygame == True:
        if stress > 50:
            play music "audio/Trip to the Market.ogg"
    "Yum. Great, I managed to get everything I wanted from this aisle."
    call buttonSound from _call_buttonSound_99
    return

label freshfood:
    call mchider from _call_mchider_7
    scene deli1
    show deli2
    if needtoplay == True:
        play music "audio/Scanning the Store.ogg"
        $ needtoplay = False
    if abort_meat == True:
        if money < 1.39:
            "Oh no! I don't have enough money on me to buy salami. No use going into this aisle anymore."
            call buttonSound from _call_buttonSound_100
            $ abort_meat = False
            $ thirdaisle_item = True
            return
    if abort_meat == True:
        #check if money too low for salami
        show deliworker1 behind deli2
        "Oh there's no line at the deli. I can order immediately."
        call buttonSound from _call_buttonSound_101
        if stress > 50:
            play music "audio/Scanning the Store.ogg"
        "Let's get this over with."
        call buttonSound from _call_buttonSound_102
        jump pointmeat
        return
    if thirdaisle_item == True:
        show mc1
        "Hmmmm, I think I don't need anything from this aisle anymore."
        call buttonSound from _call_buttonSound_103
        hide mc1
        return
    show mc1
    "Ah, Fresh Food: healthy, nice and crunchy. Autistic people have a reputation for hating certain food types like vegetables because they can be inconsistent to taste, or have a yucky texture."
    call buttonSound from _call_buttonSound_104
    "But preferences go both ways. I love veggie food! Almost as much as I love Salami…"
    call buttonSound from _call_buttonSound_105
    "Mmm, speaking of which, since I'm here I'll grab a ticket for the new deli, I can shop here while I wait for them to call my number."
    call buttonSound from _call_buttonSound_106
    $ actiontimer = actiontimer + 1
    hide mc1
    if money < 1.39:
        show mc2
        stop music fadeout 1.0 #fades out the music
        "Oh no! I don't have enough money left, but I'm still in line. What do I do?!"
        call buttonSound from _call_buttonSound_107
        jump breakdown
    $ corncheck = True #Becomes false if player bought one
    $ celerycheck = True #Becomes false if player bought one
    $ spinachcheck = True #Becomes false if player bought one
    menu veggiemenuone:
        "What should I get?"
        "Celery - {color=#FFD700}€1,39{/color}" if celerycheck:
            "Yum. Celery. Let's get this."
            call buttonSound from _call_buttonSound_108
            $ thirdaisle_item = True
            $ money = money - 1.39
            $ objectNo = 11
            call updateList from _call_updateList_9
            $ celerycheck = False
            jump veggiemenuone
        "Corn - {color=#FFD700}€1,79{/color}" if corncheck:
            if money < 1.79:
                "I don't have enough money for this... I should save what I have for buying salami."
                call buttonSound from _call_buttonSound_109
            else:
                "Yum, Corn. That's going in the basket."
                call buttonSound from _call_buttonSound_110
                $ thirdaisle_item = True
                $ money = money - 1.79
                $ objectNo = 22
                $ corncheck = False
                call updateList from _call_updateList_10
                jump veggiemenuone
        "Spinach - {color=#FFD700}€1,89{/color}" if spinachcheck:
            if money < 1.89:
                "I don't have enough money for this... I should save what I have for buying salami."
                call buttonSound from _call_buttonSound_111
            else:
                "It's been a while since I've had spinach. Let's take this."
                call buttonSound from _call_buttonSound_112
                $ thirdaisle_item = True
                $ money = money - 1.89
                $ objectNo = 31
                $ spinachcheck = False
                call updateList from _call_updateList_11
                jump veggiemenuone
        "Check number in line.":
            "Oh, I think it's my turn."
            call buttonSound from _call_buttonSound_113
    $ objectNo = 0
    show mc1
    "They are calling number 12, that's me! Salami time!"
    call buttonSound from _call_buttonSound_114
    if money < 1.39:
        "Oh no, I just realised I don't have enough money left for salami! I guess I'll have to get it another time."
        call buttonSound from _call_buttonSound_115
        $ stress = stress - 50 #Balance
        call checkMusic from _call_checkMusic_14
        call checkBreak from _call_checkBreak_14
        return
    hide mc1
    show deliworker1 behind deli2
    if stress < 50:
        $ isNotStressed = False
    "I wish they still offered their pre-packed options here. I hate having to talk to people. Why must they hide my precious meat behind social interaction?!"
    call buttonSound from _call_buttonSound_116
    "Are the prices listed per slice, or what? I used to just pick up the packet and put it in my basket... I have no idea what to do here."
    call buttonSound from _call_buttonSound_117
    deliworker1 "How can I help?"
    call buttonSound from _call_buttonSound_118
    if stress > 50:
        play music "audio/Scanning the Store.ogg"
    "I guess I better get this over with."
    call buttonSound from _call_buttonSound_119
    menu pointmeat:
        "What should I do?"
        "Abort mission!":
            "I simply cannot do this right now, maybe I'll come back later. I quickly mumble an apology to the deli worker."
            call buttonSound from _call_buttonSound_120
            $ stress = stress + 5 #Balance
            $ abort_meat = True
        "Request Salami" if isNotStressed:
            mc1 "Salami please..."
            call buttonSound from _call_buttonSound_121
            deliworker1 "Of course, how much would you like?"
            call buttonSound from _call_buttonSound_122
            mc1 "Erm... enough for a couple of lunches, I guess? I usually spent €1,39"
            call buttonSound from _call_buttonSound_123
            $ objectNo = 23
            call updateList from _call_updateList_12
            $ thirdaisle_item = True
            $ objectNo = 0
            $ abort_meat = False
            deliworker1 "No problem, here you go. That makes {color=#FFD700}€1,39{/color}."
            call buttonSound from _call_buttonSound_124
            $ money = money - 1.39
            $ stress = stress + 10 #Balance
            "I quickly thank the deli worker before I leave. That was tedious, but I got my salami."
            call buttonSound from _call_buttonSound_125
        "Point at salami":
            "Not having the energy to speak, I point at the salami."
            call buttonSound from _call_buttonSound_126
            $ stress = stress - 10 #Balance
            call checkMusic from _call_checkMusic_15
            if stress < 1:
                "I'm getting overwhelmed..."
                call buttonSound from _call_buttonSound_127
                call checkBreak from _call_checkBreak_15
                return
            "{fast} Ahhh, this is so awkward. {w=0.5} They're picking up the pastrami! {w=0.5} I pointed at the salami!"
            call buttonSound from _call_buttonSound_128
            menu salampastrami:
                "What should I do?"
                "Point harder":
                    "Please... don't make me talk."
                    deliworker1 "Ah, you want some salami too? All right, here you go. That would be {color=#FFD700}€3,68{/color} total."
                    $ stress = stress - 10 #Balance
                    call checkMusic from _call_checkMusic_18
                    if money < 3.68:
                        "Ugh... I can't afford this... What do I do?!"
                        call buttonSound from _call_buttonSound_132
                        jump breakdown
                    if stress < 1:
                        "I'm getting overwhelmed"
                        call buttonSound from _call_buttonSound_4
                        call checkBreak from _call_checkBreak_18
                        return
                    $ objectNo = 23
                    call updateList from _call_updateList_23
                    $ objectNo = 2
                    call updateList from _call_updateList_24
                    $ objectNo = 0
                    $ money = money - 3.68
                    "Ugh... I guess I'll have to accept this."
                "Request salami by speaking out loud":
                    $ stress = stress - 15 #Balance
                    call checkMusic from _call_checkMusic_16
                    if stress < 1:
                        "I'm getting overwhelmed..."
                        call buttonSound from _call_buttonSound_129
                        call checkBreak from _call_checkBreak_16
                        return
                    mc2 "Sorry, it was salami I wanted."
                    deliworker1 "Ah, apologies. You pointed at the meat, so I just guessed... Here you go. That makes {color=#FFD700}€1,39{/color}."
                    call buttonSound from _call_buttonSound_130
                    $ money = money - 1.39
                    $ objectNo = 23
                    call updateList from _call_updateList_13
                    $ objectNo = 0
                    $ abort_meat = False
                    $ thirdaisle_item = True
                    "I give the employee a friendly nod before leaving. That was stressful, but I did manage to get salami."
                    call buttonSound from _call_buttonSound_131
                    $ stress = stress + 5 #Balance
                "Accept Pastrami - {color=#FFD700}€2,29{/color}": #TEDOEN: add colour to price
                    if money < 2.29:
                        "Ugh... I can't afford this... What do I do?!"
                        call buttonSound from _call_buttonSound_12
                        jump breakdown
                    $ money = money - 2.29
                    $ stress = stress - 5 #Balance
                    call checkMusic from _call_checkMusic_17
                    if stress < 1:
                        "This is too much..."
                        call buttonSound from _call_buttonSound_133
                        call checkBreak from _call_checkBreak_17
                        return
                    $ abort_meat = False
                    $ thirdaisle_item = True
                    $ objectNo = 2
                    call updateList from _call_updateList_14
                    $ objectNo = 0
                    "Ugh... this is so expensive. But I'll take it."
                    call buttonSound from _call_buttonSound_134
    if stress > 50:
        play music "audio/Trip to the Market.ogg"
    return

label register:
    if needtoplay == True:
        play music "audio/Trip to the Market.ogg"
        $ needtoplay = False
    if hasmusictriggered == True:
        play music "audio/Trip to the Market.ogg"
    call mchider from _call_mchider_9
    show mc1
    "Right then, I think that's everything I needed. I really do have to get out here now. We're cutting it close!"
    call buttonSound from _call_buttonSound_135
    hide mc1
    scene register_fg2
    show register_fg
    show cashier1 behind register_fg
    "I can't believe how hard this was. When I talk to friends and family they think I'm exaggerating! I wish I was. But this turned out to be a relatively normal shopping trip despite the renovations. If it had been Christmas or Black Friday, I wouldn't even make it through the door."
    call buttonSound from _call_buttonSound_136
    "Heck, sometimes if they're playing the wrong music on the radio it can derail me entirely."
    call buttonSound from _call_buttonSound_137
    cashier1 "Hey, I'm sorry about the queue. It's nice to see you here again, I hope you found everything you needed."
    call buttonSound from _call_buttonSound_138
    $ howmuchpaid = 15 - money
    cashier1 "Here's the bill. That makes {color=#FFD700}€[howmuchpaid]{/color} total."
    call buttonSound from _call_buttonSound_139
    mc1 "Thank you. I'll pay by card."
    call buttonSound from _call_buttonSound_140
    if len(Inventory) > 5:
        "Yikes, I only came in here for a few things."
        call buttonSound from _call_buttonSound_141
    #Show end screen
    "Not bad, maybe I could have spent less, but I'm relieved I don't have to think about coming here again... until next week."
    call buttonSound from _call_buttonSound_142
    return

label breakdown:
    #anywhere in the store when exceeding stress limit
    stop music
    play sound "audio/Market Meltdown.ogg"
    $ breakdown_reached = True
    hide mc1
    hide mc2
    hide mc3
    hide deliworker1
    with fade
    show mc3 at alette_notright
    show cashier2 at alette_left
    cashier2 "Weewoo, are you ok? It looks like you're a bit overwhelmed here. Let’s get you outside for some air. My colleague will put all this stuff back for you."
    call buttonSound from _call_buttonSound_143
    hide mc3
    hide cashier2
    scene storefront
    with pixellate
    play music "audio/Trip to the Market.ogg" fadein 1.0
    show cashier1
    cashier1 "When this type of thing happens to me, I move away from the things that triggered me first, and try to breathe slowly to calm myself. Can you breathe in for me?"
    call buttonSound from _call_buttonSound_144
    hide cashier1
    mc1 "...Okay."
    show cashier2
    cashier1 "Once I'm able to, I listen to some music. I close my eyes and focus on the sound until I feel like I'm functioning again."
    call buttonSound from _call_buttonSound_145
    hide cashier2
    show mc2
    "Thank you."
    call buttonSound from _call_buttonSound_146
    return

label outalive:
    #end text, show all characters in front of the store
    #if breakdown ending reached, at the end confirm that you can replay from last save to reach a better ending
    hide cashier1
    hide text
    scene test #TEDOEN : fix scene
    show mc1 at alette_right
    show cashier1 at alette_left
    show deliworker1 at alette_notright
    with fade
    "Shopping is a stressful experience for people with disabilities. While it's easier to shop online or depend on somebody else, many of us simply do not have a support network in place or cannot afford online delivery fees on a regular basis."
    call buttonSound from _call_buttonSound_147
    "So instead, we have to endure the situation as best as we can. Usually our coping mechanisms work. We've learned how to manage, through trial and error during childhood, and now we're able to get through the day treating each task like a challenge we must navigate to survive."
    call buttonSound from _call_buttonSound_148
    "Not all autistic people experience the world in exactly the same way though. Everybody loves or hates certain smells, like Jasmine or Fish and prefers one muffin type over another."
    call buttonSound from _call_buttonSound_149
    "But for autistic people, personal preference isn't a matter of flavour and taste. It's a choice between sensory overload and simply being able to eat. It may seem picky and demanding, but the alternative is not pretty."
    call buttonSound from _call_buttonSound_150
    "Next time you are shopping, if you see a person struggling, or a child who is overwhelmed, consider that they may be autistic and the environment may be causing them a lot of stress. Awareness and Acceptance can alleviate that stress, and hopefully lead to changes that better accommodate us."
    call buttonSound from _call_buttonSound_151
    "Thank you for playing Market Meltdown."
    if breakdown_reached == True:
        "PS: Why not reload and see what happens if you make different choices?"
    return

label mchider:
    hide mc1
    hide mc2
    hide mc3
    return
