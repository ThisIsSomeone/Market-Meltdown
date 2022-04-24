#Game Script, made by Alette

################################################################################################################################################
#Default variables
init:
    default stress = 100
    default actiontimer = 0 #We start counting from 1 cause of how menu works, so count events from 1
    default objectNo = 0 #Object to be added to the list when label is called, 0 means nothing is added.
    default Inventory = []
    default money = 25
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
define mc1 = Character("Protagonist", image="Characters/MC1.png")
define mc2 = Character("Protagonist", image="Characters/MC2.png")
define mc3 = Character("Protagonist", image="Characters/MC3.png")
define cashier1 = Character("Cashier", image="Characters/cashier1.png")
define cashier2 = Character("Cashier", image="Characters/cashier2.png")
define cashier3 = Character("Cashier", image="Characters/cashier3.png")
define deliworker1 = Character("Helpful Person", image="Characters/deliworker1.png") #TEDOEN: CHange name
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
################################################################################################################################################
#Define Screens
screen Money: #Lists money
    text "{color=#FFD700}Money: [money]{/color}" xalign 1.0 xpos 0.99 ypos 0.01
screen Stress: #Temporary screen, TEDOEN: Remove
    text "{color=#00FF00}Stress: [stress]{/color}" xalign 1.0 xpos 0.99 ypos 0.7
screen InventoryList: #List every object in the list plus their value
    vbox xpos 0.01 ypos 0.01:
        text "{color=#000000}Inventory:{/color}"
        if 1 in Inventory:
            text "{color=#000000}- Comic Book{/color}"
        if 2 in Inventory:
            text "{color=#000000}- Pastrami{/color}"
        if 3 in Inventory:
            text "{color=#000000}- Phlash{/color}"
        if 4 in Inventory:
            text "{color=#000000}- Mrs Strong{/color}"
        if 5 in Inventory:
            text "{color=#000000}- Thick Cut Fries{/color}"
        if 6 in Inventory:
            text "{color=#000000}- Brown Ice Cream{/color}"
        if 7 in Inventory:
            text "{color=#000000}- Red Box Pizza{/color}"
        if 8 in Inventory:
            text "{color=#000000}- Chocolate Cake{/color}"
        if 9 in Inventory:
            text "{color=#000000}- Carrot Cake{/color}"
        if 10 in Inventory:
            text "{color=#000000}- Fancy Bread{/color}"
        if 11 in Inventory:
            text "{color=#000000}- Celery{/color}"
        if 12 in Inventory:
            text "{color=#000000}- Wrong Salami{/color}"
        if 13 in Inventory:
            text "{color=#000000}- Yellow Box Pizza{/color}"
        if 14 in Inventory:
            text "{color=#000000}- French Fries{/color}"
        if 15 in Inventory:
            text "{color=#000000}- Purple Meal{/color}"
        if 16 in Inventory:
            text "{color=#000000}- Pink Ice Cream{/color}"
        if 17 in Inventory:
            text "{color=#000000}- Cupcake{/color}"
        if 18 in Inventory:
            text "{color=#000000}- Blueberry Muffin{/color}"
        if 19 in Inventory:
            text "{color=#000000}- Chocolate Muffin{/color}"
        if 20 in Inventory:
            text "{color=#000000}- Glazed Donuts{/color}"
        if 21 in Inventory:
            text "{color=#000000}- Baguette{/color}"
        if 22 in Inventory:
            text "{color=#000000}- Corn{/color}"
        if 23 in Inventory:
            text "{color=#000000}- Salami{/color}"
        if 24 in Inventory:
            text "{color=#000000}- Brown Meal{/color}"
        if 25 in Inventory:
            text "{color=#000000}- Sponge Cake{/color}"
        if 26 in Inventory:
            text "{color=#000000}- Jam Donut{/color}"
        if 27 in Inventory:
            text "{color=#000000}- Ringed Donut{/color}"
        if 28 in Inventory:
            text "{color=#000000}- White Bread{/color}"
        if 29 in Inventory:
            text "{color=#000000}- Brown Bread{/color}"
        if 30 in Inventory:
            text "{color=#000000}- Mini Baguette{/color}"
        if 31 in Inventory:
            text "{color=#000000}- Spinach{/color}"
        if 32 in Inventory:
            text "{color=#000000}- Green Box Pizza{/color}"
        if 33 in Inventory:
            text "{color=#000000}- Crinkle Cut Fries{/color}"
        if 34 in Inventory:
            text "{color=#000000}- Blue Meal{/color}"
        if 35 in Inventory:
            text "{color=#000000}- Green Ice Cream{/color}"
################################################################################################################################################
#Updates the list with a number based on the value of objectNo
label updateList:
    #ItemID listed in docs
    if objectNo > 0:
        if objectNo < 36: #adjust this number if there are more item IDs
            $Inventory.append(objectNo)
    else:
        "Error: Could not update updateList" #TEDOEN: Remove
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
    show screen Stress
    return
################################################################################################################################################
label start:
    #Label Calls
    call debugger from _call_debugger #TEDOEN: REMOVE
    #TEDOEN: Implement important screenshowers
    call introduction from _call_introduction
    #TEDOEN: for loop calling main menu until goto_register = true en deze wordt
    #alleen op true gezet als player dus in die while menu naar register gaan selecteert
    while goto_register == False:
        call menuloop from _call_menuloop
        if breakdown_reached == True:
            $ goto_register = True
    #Okay hier wordt het leuk, dit is je enige manier om uit je loop te breaken, dus nu moet je toch weer je goto_register false zetten als je breakdown hebt
    #En dan pas ga je checken of je naar de register moet gaan
    if breakdown_reached == True:
        $ goto_register = False

    if goto_register == True:
        call register

    call outalive
    # This ends the game.
    return

label introduction:
    #TEDOEN: A checker for money
    #Text bleeps while speaking, renpy?
    stop music fadeout 2.0 #fades out the music
    scene test #TEDOEN: Remove / fix
    show mc1 with dissolve
    "Hey, good to see you."
    call buttonSound from _call_buttonSound
    "Today, I'm heading to the supermarket."
    call buttonSound from _call_buttonSound_1
    "It... can be a bit of a minefield, but I have managed to build a pretty good routine to help me survive."
    call buttonSound from _call_buttonSound_2
    "You see, I have autism. This means I experience the world around me a little differently than most people."
    call buttonSound from _call_buttonSound_3
    "Different environments can prove challenging for my senses, and can cause me to lose control over my abilities and emotions."
    call buttonSound from _call_buttonSound_4
    "I have to be careful to avoid such a sensory overload. The store is usually quiet around this time, so I plan to be in and out within 15 minutes. That's about my usual time, so if nothing's changed..."
    hide mc1
    hide text
    with fade
    scene storefront with dissolve
    #TEDOEN: fix this transition later
    "{cps=2}...{/cps}Why today?! {w=0.5} What have they changed?! {w=0.5} How will I find the things I need?! {w=0.5}{cps=10}Why is it so busy?!{/cps}"
    call buttonSound from _call_buttonSound_5
    show mc3 with dissolve #TEDOEN: fix transition
    "There's even a queue to get in the door. {w=0.5} I hate being in large crowds, the sound of their talking, footsteps, people coughing and sneezing around me... It's a good thing I have my trusty headphones with me. {w=0.5} Let's hope the battery holds up okay."
    call buttonSound from _call_buttonSound_6
    hide mc3 with dissolve
    play music "audio/Trip to the Market.ogg"
    "Much better. Now, if I could just figure out where to go when I get inside..."
    call buttonSound from _call_buttonSound_20
    show deliworker1 with dissolve
    deliworker1 "“mfmfmfmfmf mfmf mfmf mfmfm….mmf?"
    call buttonSound from _call_buttonSound_7
    hide deliworker1 with dissolve
    "I didn't hear them well... What's this? {w=0.5} Oh, a leaflet about the refurbishment."
    call buttonSound from _call_buttonSound_8
    "It seems to have a map of the store. I guess I won't be needing to throw this in the bin after all."
    call buttonSound from _call_buttonSound_9
    "If only every store did this when they changed their layout. Wouldn't that be nice? It'd save me a lot of stress."
    call buttonSound from _call_buttonSound_10
    "Bleh, It’s not particularly detailed. With 5 aisles, I guess they expect us to walk up and down each one like cattle on a conveyor belt! Not today, Supermarket. That kind of chaos leads to meltdowns. I’m going to have to wing this and hope I make it out in one piece."
    call buttonSound
    "Which aisle first though? They're all pretty treacherous..."
    call buttonSound
    #TEDOEN: play noisy sounds
    "Oh, wonderful. There's no signal in here now. Can't stream my music. It's so noisy in here without it!"
    call buttonSound
    "{color=#ADD8E6}The goal of this game is to get to the end of the store having bought weekly necessities.{/color}"
    call buttonSound from _call_buttonSound_11
    "{color=#ADD8E6}You will need to at least buy a single item from every aisle to proceed to the register. Of course, our character can stick around in the store for longer if you so wish.{/color}"
    call buttonSound from _call_buttonSound_12
    "{color=#ADD8E6}You will be presented with certain choices throughout this game. Depending on your choices, the character's stress level might rise or fall. {/color}"
    call buttonSound from _call_buttonSound_13
    "{color=#ADD8E6}But beware, too much stress and the character might get a{/color}{color=#FF0000} Sensory Overload.{/color}"
    call buttonSound from _call_buttonSound_14
    "{color=#ADD8E6}We hope you have a great time with our game. Now, back to our protagonist.{/color}"
    call buttonSound from _call_buttonSound_15
    return

label menuloop:
    $ actiontimer = actiontimer + 1
    if stress > 50:
        if hasmusictriggered == True:
            $ hasmusictriggered = False
            $ needtoplay = True
            stop music fadeout 1.0
    #TEDOEN: if all the aisle items are checked, present an alternate menu where you can select goto register, which simply puts the goto register variable on true
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
        "Hmmmm, I think I don't need anything from this aisle anymore." #TEDOEN: check if this is okay, remove?
        call buttonSound
        hide mc1
        return
    if stress > 50:
        play music "audio/Scanning the Store.ogg"
    #TEDOEN: zodra temptimer 10 boven tien komt teveel tijd besteed
    "I hate this aisle. The chemical smells overwhelm me the moment I go near them. I get so sick that I usually have to hold my breath and grab what I can before the smell becomes too much."
    call buttonSound from _call_buttonSound_16
    show mc2 #TEDOEN: check if this is the stressed emotion
    "I do have to be careful what to buy, though. If the scent is overpowering, I can't have it in my house. But... I also need to keep my place clean and tidy or my friends won't want to visit me!"
    call buttonSound from _call_buttonSound_17
    "{color=#FF0000}Jasmine, Pine and Vanilla scents{/color} make me feel incredibly ill. Whereas smells like {color=#ACD1AF}Lavender{/color} have always been fine. How do I figure out which ones are safe?"
    call buttonSound
    call householdmenu from _call_householdmenu
    if breakdown_reached == False:
        if temptimer > 4:
            call mchider from _call_mchider_2
            show mc3
            "Oh no... I stayed in this aisle for too long."
            call buttonSound
            jump breakdown
    if stress > 0:
        "Right, let's get out of this aisle before I pass out."
        call buttonSound
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
            "Is this some... Zebra based scent? I don't know if I trust this..."
            call buttonSound from _call_buttonSound_18
            menu:
                "What should I do?"
                "Test Smell":
                    show mc3
                    "Ugh, zebras smell really really bad... I don't think I'll buy this."
                    call buttonSound from _call_buttonSound_19
                    $ stress = stress - 5 #TEDOEN: Balance
                    call checkMusic
                    if stress < 1:
                        call checkBreak
                        return
                    jump householdmenu
                "Put Back":
                    jump householdmenu
        "Jaspinilla":
            show mc3
            "BLURGH!{w=0.5} This is like a death potion. Jasmine, Pine and Vanilla in one can?! It seems my enemies have learned my weaknesses. I can even smell it through the can, I need to put this down!"
            call buttonSound from _call_buttonSound_21
            $ stress = stress - 20 #TEDOEN: Balance
            call checkMusic
            if stress < 1:
                call checkBreak
                return
            jump householdmenu
        "Clade":
            "There are trees on the can... This is probably pine."
            call buttonSound from _call_buttonSound_22
            menu:
                "What should I do?"
                "Test Smell":
                    show mc3
                    "Yuck, Pine! Why did I think testing this was a good idea?!"
                    call buttonSound
                    $ stress = stress - 10 #TEDOEN: Balance
                    call checkMusic
                    if stress < 1:
                        call checkBreak
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
                    $ stress = stress + 5 #TEDOEN: Balance
                    menu:
                        "Do I buy this?"
                        "Put in basket":
                            $ firstaisle_item = True
                            if money < 1.31:
                                show mc3
                                "I have no money left to buy this. A quick glance around the aisle tells me that the other products are also outside of my budget. I guess no inviting friends this week."
                                call buttonSound
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
                            "Hmmm, I don't have enough money for this. Maybe I can find something cheaper I can afford?"
                            call buttonSound
                            hide mc2
                        else:
                            $ firstaisle_item = True
                            show mc3
                            "I have no money left to buy this. A quick glance around the aisle tells me that the other products are also outside of my budget. I guess no inviting friends this week."
                            call buttonSound
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
        "Hmmmm, I think I don't need anything from this aisle anymore." #TEDOEN: check if this is okay, remove?
        call buttonSound
        hide mc1
        return
    show mc1
    "Oh hey that's right, books books books. The creators are so cool, I think they have another kickstarter coming out soon as well." #TEDOEN: Sensory on the spectrum
    call buttonSound from _call_buttonSound_26
    hide mc1
    if actiontimer <= 2: #TEDOEN: Balance
        show mc2
        "Ah, nuts. There are so many people in this aisle I can't get to the shelf. I'll come back later. Crowded spaces are a horrible experience."
        call buttonSound
        $ stress = stress - 10 #TEDOEN: Balance
        call checkMusic
        if stress < 1:
            call checkBreak
            return
        hide mc2
    elif actiontimer > 5: #TEDOEN: Balance
        show mc3
        "It SOLD OUT?! I knew it was popular, but come on! I have been waiting to read it for a year now. I can't believe I missed it... I'll have to go and order it online."
        call buttonSound from _call_buttonSound_28
        $ secondaisle_item = True
        $ stress = stress - 50
        call checkMusic
        if stress < 1:
            call checkBreak
            return
    else:
        show mc1
        "At last! I have been waiting so long to read this."
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
                " So relatable. What a great book."
                $ peeked_already = True
                hide mc1
                call buttonSound from _call_buttonSound_31
                jump bookchoice
            "Put in basket.":
                $ secondaisle_item = True
                if money < 14.90:
                    show mc2
                    "I don't think I have enough money for this with me. I'll have to order online."
                    call buttonSound from _call_buttonSound_32
                    $ stress = stress - 10
                    call checkMusic
                    hide mc2
                    if stress < 1:
                        call checkBreak
                        return
                    return
                show mc1
                "I can't wait to go home and read this!"
                call buttonSound from _call_buttonSound_33
                hide mc1
                $ stress = stress + 20
                $ objectNo = 1
                call updateList from _call_updateList_2
                $ objectNo = 0
                $ money = money - 14.90
    return

label frozen:
    scene frozen
    call mchider from _call_mchider_5
    if fifthaisle_item == True:
        show mc1
        "Hmmmm, I think I don't need anything from this aisle anymore." #TEDOEN: check if this is okay, remove?
        call buttonSound
        hide mc1
        return
    $ stress = stress - 10
    call checkMusic
    if stress < 1:
        call checkBreak
        return
    $ renpy.music.set_volume(.7,0,channel="sound") #TEDOEN: Audio balancing
    play sound "audio/SFX/Fridge Hum.ogg" loop
    if stress > 50:
        play music "audio/Scanning the Store.ogg"
    "For many, the hardest part of the frozen aisle is the coldness. For me it's that irritating humming. The monotous repetitive noise from the freezers, burrowing through my ears and into the center of my skull."
    call buttonSound
    "I’d normally drown it out with my music, but today I'm stuck with using my headphones like mufflers."
    call buttonSound
    "If I rush I can leave the aisle quicker, and maybe everything will be okay... It'll be stressful to get the wrong items though, but at the very least, it will be quick."
    call buttonSound
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
                        #no money specified because this item is gonna get returned either way
                    "Get something specific":
                        $ iceleft = False
                        $ trygreen = True
                        $ frozenfoodcount = frozenfoodcount + 1
                        menu pizzachoice:
                            "What should I grab?"
                            "Yellow Box Pizza":
                                show mc1
                                "Yum, I like plain cheese pizza. This will do nicely."
                                call buttonSound
                                hide mc1
                                $ objectNo = 13
                                $ prizetotal = prizetotal + 0.99
                                #how much does it cost + which objectNo
                            "Red Box Pizza":
                                show mc1
                                "Ohhh, meat. It costs a bit more, but I love a thick meaty pizza!"
                                call buttonSound
                                hide mc1
                                $ objectNo = 7
                                $ prizetotal = prizetotal + 1.99
                            "Green Box Pizza" if trygreen:
                                show mc2
                                $ stress = stress - 5
                                call checkMusic
                                "Oh, veggie pizza. As much as I love crunchy veggies, soft goopie vegetables on a pizza are disgusting. I don't want this!"
                                call buttonSound
                                if stress < 1:
                                    "...." #TEDOEN: overwhelmed
                                    call checkBreak
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
                    "Get something specific":
                        $ readyleft = False
                        $ trycrinkle = True
                        $ frozenfoodcount = frozenfoodcount + 1
                        menu frieschoice:
                            "What should I grab?"
                            "Thick Cut Fries":
                                show mc1
                                "These are great! So big and filling."
                                call buttonSound
                                hide mc1
                                $ objectNo = 5
                                $ prizetotal = prizetotal + 1.00
                            "French Fries":
                                show mc1
                                "French fries are all right if I can cook them properly! If I forget to do that, which I usually do, they can be a bit hard and spiky on my mouth. Not the best option, but not the worst either."
                                call buttonSound
                                hide mc1
                                $ objectNo = 14
                                $ prizetotal = prizetotal + 1.09
                            "Crinkle Cut Fries" if trycrinkle:
                                $ trycrinkle = False
                                show mc2
                                $ stress = stress - 5
                                call checkMusic
                                "Someone had the bright idea to make fries with sharp saw-like edges on them. They're a sensory nightmare for me! My mouth aches just thinking about these, get back in the freezer!"
                                call buttonSound
                                if stress < 1:
                                    call checkBreak
                                    return
                                hide mc2
                                jump frieschoice
            "Ready meal" if readyleft:
                $ readyleft = False
                menu:
                    "What do I grab?"
                    "Anything's good":
                        $ objectNo = 34
                    "Get something specific":
                        $ frozenfoodcount = frozenfoodcount + 1
                        $ friesleft = False
                        $ trybmeal = True
                        menu readychoice:
                            "What should I take?"
                            "Purple Meal":
                                show mc1
                                "Not the healthiest option, but it's definitely an easy one. With my energy being so unpredictable it can be great to have one of these in the freezer for days when I'm just too tired to cook."
                                call buttonSound
                                hide mc1
                                $ objectNo = 15
                                $ prizetotal = prizetotal + 1.49
                            "Blue Meal" if trybmeal:
                                $ trybmeal = False
                                show mc3
                                $ stress = stress - 5
                                call checkMusic
                                "Microwave fish?! Who would think this was a good idea? It'll ruin my house and upset every person in a ten mile radius. Back in the freezer it goes!"
                                call buttonSound
                                if stress < 1:
                                    call checkBreak
                                    return
                                hide mc3
                                jump readychoice
                            "Brown Meal":
                                show mc1
                                "Ooh, Microwave Tomato Pasta Bake. This is an easy laid back meal that I'll always be happy to eat. There's a lot of hidden vegetables in here too, which is a bonus!"
                                call buttonSound
                                hide mc1
                                $ prizetotal = prizetotal + 3.74
                                $ objectNo = 24
            "Ice cream" if iceleft:
                $ iceleft = False
                menu:
                    "What do I grab?"
                    "Anything's good":
                        $ objectNo = 16
                        $ prizetotal = prizetotal + 1.67
                        $ frozenfoodcount = frozenfoodcount + 1
                    "Get something specific":
                        $ frozenfoodcount = frozenfoodcount + 1
                        $ trypistache = True
                        $ pizzaleft = False
                        menu icechoice:
                            "What should I get?"
                            "Green Ice Cream" if trypistache:
                                show mc2
                                $ stress = stress - 5
                                call checkMusic
                                "Mint? No, wait... Pistacchio?! This is criminal. What kind of dessert is this?! Back it goes!"
                                call buttonSound
                                if stress < 1:
                                    call checkBreak
                                    return
                                hide mc2
                                $ trypistache = False
                                jump icechoice
                            "Pink Ice Cream":
                                show mc1
                                $ stress = stress + 5
                                "Strawberry! Yes, get in the basket now! No further questions."
                                call buttonSound
                                hide mc1
                                $ prizetotal = prizetotal + 1.67
                                $ objectNo = 16
                            "Brown Ice Cream":
                                show mc1
                                "Wait, coffee ice cream? I was expecting chocolate... but this sounds like it would be nice. It costs a bit more, but I think this is a flavour I could get hooked on for a bit."
                                call buttonSound
                                hide mc1
                                $ prizetotal = prizetotal + 1.87
                                $ objectNo = 6
        call updateList
        $ objectNo = 0
        #je moet op een of andere manier uit deze loop breaken in alle gevallen: dat doe je nu joepie
        if frozenfoodcount == 2: #TEDOEN: Nu Zijn dit alle cases :) Great job on solving this!
            $ frozenfoodcheck = True
    $ fifthaisle_item = True
    "Okay, that's everything. I hope I didn't grab anything awful by mistake. Let's quickly check."
    call buttonSound
    if 32 in Inventory:
        $ Inventory.remove(32)
        show mc2
        "Ewww, veggie pizza. No, I can't eat that. I'll just put that back in the freezer and leave without..."
        call buttonSound
    if 34 in Inventory:
        $ Inventory.remove(34)
        show mc2
        "Microwave fish?! Disgusting! The smell would end me. That's going back in the freezer!"
        call buttonSound
    call mchider
    if money < prizetotal:
        show mc2
        "Looking at my budget, I don't have money left for all of this... I better just put everything back and get out of this aisle."
        call buttonSound
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
    stop sound fadeout 1.0
    "Okay, finally I can get out of this aisle."
    call buttonSound
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
        "Hmmmm, I think I don't need anything from this aisle anymore." #TEDOEN: check if this is okay, remove?
        call buttonSound
        hide mc1
        return
    show mc1
    "Everything here is so tasty! The smells are wonderful. I could stay here all day! I'd buy everything if I could."
    call buttonSound
    "Unfortunately, I don't have the millions I'd need to satisfy my pastry addiction. So I'll have to make some decisions."
    call buttonSound
    "I hate having to make choices that I might regret later, or that could impact other things. I like to consider my options. According to studies about autistics, this seems to be a common experience for others like me, too."
    call buttonSound
    "I need food for the week, and my friends are coming over later this week too. So I need to buy some bread and a snack." #TEDOEN: colour code bread and snack to be clear
    call buttonSound
    hide mc1
    $ earlygame = False
    $ middlegame = False
    if actiontimer < 2:
        $ earlygame = True
    if actiontimer < 4:
        $ middlegame = True
    if earlygame == True:
        show mc2
        $ stress = stress - 10
        call checkMusic
        if stress > 50:
            play music "audio/Scanning the Store.ogg"
        "There's so much to choose from here, though. What do I get?"
        call buttonSound
        if stress < 1:
            hide mc2
            show mc3
            "There's too much... I'm getting overwhelmed."
            call buttonSound
            call checkBreak
            return
        hide mc2
    elif middlegame == True:
        show mc1
        $ stress = stress - 5
        call checkMusic
        if stress < 1:
            hide mc1
            show mc3
            "There's too many things... I'm getting overwhelmed."
            call buttonSound
            call checkBreak
            return
        "There's quite a bit of choice... what should I get?"
        call buttonSound
        hide mc1
    else:
        show mc2
        "There's not many things left. At least that makes choosing easier."
        call buttonSound
        hide mc2
    if money < 1.35:
        "I don't have enough money left for bread?! Oh no..."
        call buttonSound
        jump breakdown
    menu breadchoices:
        "What should I get?"
        "Sliced Bread":
            "Ah, the best. I could eat this for breakfast, lunch and dinner. Though, I can't really present my friends with plain bread when they visit. I'll have to grab a snack later."
            call buttonSound
            menu slicedbreads:
                "Which one do I get?"
                "Sliced White Bread - €1,35": #TEDOEN: add colour
                    "White bread tastes good... but they say it's not very good for you. How bad could it be?"
                    call buttonSound
                    menu:
                        "What should I do?"
                        "Put in basket":
                            $ fourthaisle_item = True
                            $ money = money - 1.35
                            $ objectNo = 28
                            call updateList from _call_updateList_3
                            $ objectNo = 0
                            $ stress = stress + 5
                        "Get a different kind of bread":
                            jump breadchoices
                "Sliced Brown Bread - €1,35": #TEDOEN: add colour
                    "Brown bread is not as nice, but definitely healthier. The birds in my garden will probably like the seeds too."
                    call buttonSound
                    menu:
                        "What should I do?"
                        "Put in basket":
                            $ fourthaisle_item = True
                            $ money = money - 1.35
                            $ objectNo = 29
                            call updateList from _call_updateList_4
                            $ objectNo = 0
                        "Get something else":
                            jump breadchoices
        "Fancy Unsliced Bread":
            if money < 2:
                "I don't have the money for fancy bread anymore, let's pick a different type of bread."
                call buttonSound
                jump breadchoices
            "Ohhh, yummy. I could treat myself this way... I bet it's expensive though. Let's see. {w=0.1} €2,00." #TEDOEN: add colour
            call buttonSound
            menu:
                "What should I do?"
                "Put in basket":
                    $ fourthaisle_item = True
                    $ money = money - 2.00
                    $ objectNo = 10
                    call updateList from _call_updateList_5
                    $ objectNo = 0
                    $ stress = stress + 10
                "Get something else":
                    "Oh well, I guess getting something else is better for my wallet. Let's see..."
                    call buttonSound
                    jump breadchoices
        "Baguettes" if middlegame:
            "Une baguette, très bien! It seems to cost €0,79. It would be pretty nice for today, but I fear it'll be hard by tomorrow. I do like baguettes though... I should probably still get some normal bread if I buy this." #TEDOEN: Colour
            call buttonSound
            menu:
                "What should I do?"
                "Buy it":
                    #TEDOEN: hoeft hieer maar een van, zorg dat je er maar een kan kopen
                    if money < 2.14:
                        "Taking a quick look at my wallet, I don't think I have enough money to buy more bread after this. I should get normal bread instead."
                        jump breadchoices
                        call buttonSound
                    $ money = money - 0.79
                    $ objectNo = 21
                    call updateList from _call_updateList_6
                    $ objectNo = 0
                    jump breadchoices
                "Get something else":
                    jump breadchoices
        "Mini Baguette" if earlygame:
            "Ooh! Une petite baguette! Seems to be €0.35. That's better than a massive one just for me! I could have this for lunch, but I'd still need something for the rest of the week." #TEDOEN: colour
            call buttonSound
            #TEDOEN: Hoeft hier maar een van, zorg dat je maar een kan kopen
            menu:
                "What should I do?"
                "Buy it":
                    if money < 1.65:
                        "Taking a quick look at my wallet, I don't think I have enough money to buy more bread after this. I should get normal bread instead."
                        call buttonSound
                        jump breadchoices
                    $ money = money - 0.30
                    $ stress = stress + 10
                    $ objectNo = 30
                    call updateList from _call_updateList_7
                    $ objectNo = 0
                    jump breadchoices
                "Get something else":
                    jump breadchoices
    if money < 1:
        "I don't think I have money left for a snack. It's unfortunate, but I'll have to deal with it."
        call buttonSound
        $ stress = stress - 10
        call checkMusic
        call checkBreak
        return
    "Neat. That covers normal bread. Now, let's see what they have for snacks."
    call buttonSound
    menu snackmenu:
        "Let's see. What should I get?" #TEDOEN: Colour all the prices
        "Sponge Cake - 1,79":
            if money < 1.79:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.79
                    $ objectNo = 25
                "Get something else":
                    jump snackmenu
        "Chocolate Cake - 2,75" if earlygame:
            if money < 2.75:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 2.75
                    $ objectNo = 8
                "Get something else":
                    jump snackmenu
        "Cupcakes - 0,99":
            if money < 0.99:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 0.99
                    $ objectNo = 17
                "Get something else":
                    jump snackmenu
        "Chocolate Muffins - 1,66" if middlegame:
            if money < 1.66:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.66
                    $ objectNo = 19
                "Get something else":
                    jump snackmenu
        "Blueberry Muffins - 1,79":
            if money < 1.79:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.79
                    $ objectNo = 18
                "Get something else":
                    jump snackmenu
        "Jam Donuts - 2,40":
            if money < 2.40:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 2.40
                    $ objectNo = 26
                "Get something else":
                    jump snackmenu
        "Ringed Donuts - 1,69" if earlygame:
            if money < 1.69:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.69
                    $ objectNo = 27
                "Get something else":
                    jump snackmenu
        "Glazed Donuts - 1,40" if middlegame:
            if money < 1.40:
                "I don't have enough money for this. Let's get something else."
                call buttonSound
                jump snackmenu
            menu:
                "What should I do?"
                "Put in basket":
                    $ money = money - 1.40
                    $ objectNo = 20
                "Get something else":
                    jump snackmenu
        "Let's skip the snacks this time around.":
            "Hmmmm. It's probably for the better that I don't get a snack. My wallet will be happy, at the very least."
            call buttonSound
            return
    call updateList from _call_updateList_8
    $ objectNo = 0
    $ stress = stress + 5
    if earlygame == True:
        if stress > 50:
            play music "audio/Trip to the Market.ogg"
    "Yum. Great, I managed to get everything I wanted from this aisle."
    call buttonSound
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
            "Even if I wanted to, I don't have enough money on me to buy salami with anymore."
            call buttonSound
            $ abort_meat = False
            return
    if abort_meat == True:
        #check if money too low for salami
        show deliworker1 behind deli2
        "Luckily there seems to be nobody in line when I come back at the deli. I get to order immideately."
        call buttonSound
        if stress > 50:
            play music "audio/Scanning the Store.ogg"
        "Let's get this over with."
        call buttonSound
        jump pointmeat
        return
    if thirdaisle_item == True:
        show mc1
        "Hmmmm, I think I don't need anything from this aisle anymore." #TEDOEN: check if this is okay, remove?
        call buttonSound
        hide mc1
        return
    show mc1
    "Ah, Fresh Food: healthy, nice and crunchy. Autistic people have a reputation for hating certain food types like vegetables because they can be inconsistent to taste, or have a yucky texture."
    call buttonSound
    "But, preferences go both ways. I can't get enough of veggie food. Almost as much as I love salami..."
    call buttonSound
    "Speaking of which, since I'm here I'll grab a ticket for the newly built deli. I can shop here while I wait for them to call my number."
    call buttonSound
    $ actiontimer = actiontimer + 1
    hide mc1
    if money < 1.39:
        show mc2
        stop music fadeout 1.0 #fades out the music
        "Oh no... I don't have enough money left for anything here. But I'm still in line. What do I do..."
        call buttonSound
        jump breakdown #TEDOEN: does this work?
    menu veggiemenuone:
        "What should I do?"
        "Celery - {color=#FFD700}€1,39{/color}":
            "Yum. Celery. Let's get this."
            call buttonSound
            $ thirdaisle_item = True
            $ money = money - 1.39
            $ objectNo = 11
            call updateList from _call_updateList_9
        "Corn - {color=#FFD700}€1,79{/color}":
            if money < 1.79:
                "I don't have enough money for this... I should save what I have to buy salami."
                call buttonSound
            else:
                "Yum, Corn. That's going in the basket."
                call buttonSound
                $ thirdaisle_item = True
                $ money = money - 1.79
                $ objectNo = 22
                call updateList from _call_updateList_10
        "Spinach - {color=#FFD700}€1,89{/color}":
            if money < 1.89:
                "I don't have enough money for this... I should save what I have to buy salami."
                call buttonSound
            else:
                "It's been a while since I've had spinach. Let's take this."
                call buttonSound
                $ thirdaisle_item = True
                $ money = money - 1.89
                $ objectNo = 31
                call updateList from _call_updateList_11
        "Check number in line.":
            "Oh, I think it's my turn."
            call buttonSound
    $ objectNo = 0
    show mc1
    "They are calling number 12, that's me! Salami time!"
    call buttonSound
    if money < 1.39:
        "Oh no, I just realised I don't have any money left for salami anymore... I guess I'll have to get it another time. Let's leave the line."
        call buttonSound
        $ stress = stress - 10
        call checkMusic
        call checkBreak
        return
    hide mc1
    show deliworker1 behind deli2
    if stress < 50:
        $ isNotStressed = False
    "I wish they still offered their pre-packed options here. I hate having to talk to people. Why must they hide my precious meat behind social interaction?!"
    call buttonSound
    "Are the prices listed per slice, or what? I always just used to pick up the packet and put it in my basket... I have no idea what to do."
    call buttonSound
    deliworker1 "How can I help?"
    call buttonSound
    if stress > 50:
        play music "audio/Scanning the Store.ogg"
    "I guess I better get this over with."
    call buttonSound
    #TEDOEN: Scanning the stores play here?
    menu pointmeat:
        "What should I do?"
        "Abort mission!":
            "I simply cannot do this right now, maybe I'll come back later. I quickly mumble an apology to the deli worker."
            call buttonSound
            $ stress = stress + 5
            $ abort_meat = True
        "Request Salami" if isNotStressed:
            mc1 "Salami please..."
            call buttonSound
            deliworker1 "Of course, how much would you like?"
            call buttonSound
            mc1 "Erm... enough for a couple of lunches, I guess? I usually spent €1,39"
            call buttonSound
            $ objectNo = 23
            call updateList from _call_updateList_12
            $ thirdaisle_item = True
            $ objectNo = 0
            $ abort_meat = False
            deliworker1 "No problem, here you go."
            call buttonSound
            $ money = money - 1.39
            $ stress = stress + 10
            "I quickly thank the deli worker before I leave. That was tedious, but I got my salami."
            call buttonSound
        "Point at salami":
            "Not having the energy to speak, I attempt to point at the salami."
            call buttonSound
            $ stress = stress - 10
            call checkMusic
            if stress < 1:
                "I'm getting overwhelmed..."
                call buttonSound
                call checkBreak
                return
            "{fast} Omygosh, this is so awkward. {w=0.5} They're picking up the pastrami! {w=0.5} I pointed at the salami!" #TEDOEN: Formatting
            call buttonSound
            menu salampastrami:
                "What should I do?"
                "Request salami by speaking out loud":
                    $ stress = stress - 10
                    call checkMusic
                    if stress < 1:
                        "I'm getting overwhelmed..."
                        call buttonSound
                        call checkBreak
                        return
                    mc1 "Sorry, it was salami I wanted." #TEDOEN, wrong expression?
                    deliworker1 "Ah, apologies. You pointed at the meat, so I just guessed... Here you go."
                    call buttonSound
                    $ money = money - 1.39
                    $ objectNo = 23
                    call updateList from _call_updateList_13
                    $ objectNo = 0
                    $ abort_meat = False
                    $ thirdaisle_item = True
                    "I give the employee a friendly nod before leaving. That was stressful, but I did manage to get salami."
                    call buttonSound
                    $ stress = stress + 5
                "Accept Pastrami - €2,29": #TEDOEN: add colour to price
                    if money < 2.29:
                        "Ugh... I can't afford this... What do I do?!"
                        call buttonSound
                        jump breakdown
                    $ money = money - 2.29
                    $ stress = stress - 5
                    call checkMusic
                    if stress < 1:
                        "This is too much..."
                        call buttonSound
                        call checkBreak
                        return
                    $ abort_meat = False
                    $ thirdaisle_item = True
                    $ objectNo = 2
                    call updateList from _call_updateList_14
                    $ objectNo = 0
                    "Ugh... this is so expensive. But I'll take it."
                    call buttonSound
    if stress > 50:
        play music "audio/Trip to the Market.ogg"
    return

label register:
    if needtoplay == True:
        play music "audio/Trip to the Market.ogg"
        $ needtoplay = False
    if hasmusictriggered == True:
        play music "audio/Trip to the Market.ogg"
    call mchider
    show mc1
    "Right then, I think that's everything I needed. I really do have to get out here now. We're cutting it close!"
    call buttonSound
    hide mc1
    scene register_fg2
    show register_fg
    show cashier1 behind register_fg
    "I can't believe how hard this was. When I talk to friends and family they think I'm exaggerating! I wish I was. But this turned out to be a relatively normal shopping trip despite the renovations. If it had been Christmas or Black Friday, I wouldn't even make it through the door."
    call buttonSound
    "Heck, sometimes if they're playing the wrong music on the radio it can derail me entirely."
    call buttonSound
    cashier1 "Hey, I'm sorry about the queue. It's nice to see you here again, I hope you found everything you needed."
    call buttonSound
    cashier1 "Here's the bill."
    call buttonSound
    mc1 "Thank you. I'll pay by card."
    call buttonSound
    if len(Inventory) > 5:
        "Yikes, I only came in here for a few things."
        call buttonSound
    #Show end screen
    "Not bad, maybe I could have spent less, but I'm relieved I don't have to think about coming here again... until next week."
    call buttonSound
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
    cashier2 "Hey, are you okay? It looks like you got a bit overwhelmed. My colleague will hold on to your shopping basket, let's get you some fresh air for now."
    call buttonSound
    hide mc3
    hide cashier2
    scene storefront
    with pixellate
    play music "audio/Trip to the Market.ogg" fadein 1.0
    show cashier1
    cashier1 "When this type of thing happens to me, I move away from the things that triggered me first, and try to breathe slowly to calm myself. Can you breathe in for me?"
    call buttonSound
    hide cashier1
    mc1 "...Okay."
    show cashier2
    cashier1 "Once I'm able to, I listen to some music. I close my eyes and focus on the sound until I feel like I'm functioning again."
    call buttonSound
    hide cashier2
    show mc2
    "Thank you."
    call buttonSound
    return

label outalive:
    #end text, show all characters in front of the store
    #if breakdown ending reached, at the end confirm that you can replay from last save to reach a better ending
    hide cashier1
    hide text #TEDOEN: fix transition
    scene test #TEDOEN: alter to neutral scene
    show mc1 at alette_right
    show cashier1 at alette_left
    show deliworker1 at alette_notright
    with fade #TEDOEN: make fade longer
    "Shopping is a stressful experience for people with disabilities. While it's easier to shop online or depend on somebody lse, many of us simply do not have a support network in place, and online deliveries include delivery fees which many of us cannot afford on a regular basis."
    call buttonSound
    "So instead, we have to endure the situation as best as we can. Usually our coping mechanisms work. We've learned how to manage, through trial and error during childhood, and now we're able to get through the day treating each task like a challenge we must navigate to survive."
    call buttonSound
    "Not all autistic people experience the world in exactly the same way though, much like non-autistics will love or hate certain smells, like Jasmine or Fish and prefer chocolate muffins over blueberries."
    call buttonSound
    "But sometimes for autistic people, personal preference isn't a matter of flavour and taste, but a choice between sensory overload or simply being able to eat. It may seem picky and demanding, but the alternative is not pretty."
    call buttonSound
    "Next time you are shopping, if you see a person struggling, or a child who is overloaded. Consider that the environment might be causing them great stress. Awareness and Acceptance can alleviate that stress, and hopefully lead to changes that better accomodate everyone."
    call buttonSound
    "Thank you for playing Market Meltdown."
    if breakdown_reached == True:
        "PS: You can reload a save to try and get a different ending, or start over from the beginning! Good luck."
    return

label mchider:
    hide mc1
    hide mc2
    hide mc3
    return
