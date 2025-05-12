"""
This file notably contains the start and corridor labels which provide case background to
the player and checks if the player has collected all evidence.

The top of this file (init python block) contains the mouse cursor configuration, tools,
and evidence variables which are used in other scripts.
"""

init python:
    # Defines all mouse cursors used in the game
    config.mouse = {
        "default": [("images/cursor.png", 0, 0)],
        "pointer": [("images/cursor.png", 0, 0)],
        "magnifying": [("images/default_cursor.png", 0, 0)],
        "hover": [("images/hover_cursor.png", 0, 0)],
        "dropper": [("images/dropper.png", 0, 49)],
        "ethanol": [("images/dropper_filled.png", 0, 49)],
        "reagent": [("images/dropper_filled.png", 0, 49)],
        "hydrogen": [("images/dropper_filled.png", 0, 49)],
        "hand": [("images/default_hand.png", 0, 0)],
        "hand_grab": [("images/grab_hand.png", 0, 0)]
    }
    
    # Used for tool sensitivity in the toolbox screens defined in custom_screens.rpy
    tools = {
        "uv light": False,
        "magnetic powder": False,
        "scalebar": False,
        "gel lifter": False,
        "tape": False,
        "backing": False,
        "packaging": False,
        "tube": False,
        "bag": False,
        "tamper evident tape": False,
        "swab": False
    }

    # Used to keep track of player's progress in the game
    analyzing = {
        "handprint": False,
        "fingerprint": False,
        "splatter": False,
        "footprint": False,
        "gin": False
    }

    # Used to keep track of what evidence has been analyzed
    analyzed = {
        "handprint": False,
        "fingerprint": False,
        "splatter": False,
        "splatter presumptive": False,
        "splatter packaged": False,
        "footprint": False,
        "footprint packaged": False,
        "footprint presumptive": False,
        "footprint enhanced": False,
        "gin": False
    }

    # Used to keep track of what evidence has been encountered
    # This is used to display the evidence markers and enable respective photos
    encountered = {
        "door": False,
        "handprint": False,
        "fingerprint": False,
        "gin": False,
        "splatter": False,
        "footprint": False,
        "footprint enhanced": False 
    }

    # Used to ensure that the player is not asked the "How would you like to collect the sample?" question multiple times
    asked = {
        "splatter_swab": False,
        "footprint_swab": False
    }

    # Used to compare against the player's Kastle-Meyer order in the presumptive test scene
    valid_kastle_meyer_orders = [
        ["e", "r", "h"],
        ["e", "r", "r", "h"],
        ["e", "r", "h", "h"],
        ["e", "r", "r", "h", "h"],
        ["e", "e", "r", "h"],
        ["e", "e", "r", "r", "h"],
        ["e", "e", "r", "h", "h"],
        ["e", "e", "r", "r", "h", "h"]
    ]

    player_kastle_meyer_order = []

    # Used to display the evidence description in the casefile
    evidence_desc = ""

    def item_dragging(drags):
        """Used to set the mouse cursor to the hand_grab cursor when dragging an item.
        """
        global default_mouse
        default_mouse = "hand_grab"
        return

    def item_dragged(drags, drop):
        """Used to set the mouse cursor to the hand_grab cursor when grabbing an item.
        """
        global default_mouse
        default_mouse = "hand_grab"
        
        if not drop:
            default_mouse = "hand"
            return

        store.dragged = drags[0].drag_name
        store.dropped = drop.drag_name

        # Hide all draggable screens
        renpy.hide_screen("sample_to_tube")
        renpy.hide_screen("fingerprint_to_bag")
        renpy.hide_screen("handprint_to_bag")
        renpy.hide_screen("tape_to_bag")
        default_mouse = "default"
        return True
    
    def close_menu():
        """Used to close the casefile menu.
        """
        if renpy.get_screen("casefile_physical"):
            evidence_desc = ""
            renpy.hide_screen("casefile_physical")
        elif renpy.get_screen("casefile_photos"):
            renpy.hide_screen("casefile_photos")
        elif renpy.get_screen("casefile"):
            renpy.hide_screen("casefile")
        else:
            renpy.show_screen("casefile")

# Defines the supervisor character "Nina", image="nina" used to facilitate side-images
# See more information on side-images in our wiki: https://github.com/nina-huangg/Forensics-Pursuit/wiki/UI-Elements-Integration#character-sprites-
define s = Character(name=("Nina"), image="nina")

label start:
    $ default_mouse = "default"
    scene front corridor
    "July 13, 2024 8:17 AM. 1219 Address Road."
    show nina normal1
    s "Officer, glad to see you."
    show nina normal2
    s "It’s been a long, long morning. We were called in pretty early- around 10am."
    s "The victim was found in this very living room."
    s "Witnesses say there was possibly a small gathering here last night. Neighbours reported shouting, but dismissed it as just general party behaviour-"
    s "-until this morning when the victim's friend came over to check in on him and found him dead in the living room."
    show nina normal1
    s "Let me give you a quick rundown of what we know so far."
    s "The victim, Davis Dayid, was a 20-year-old student at the University of Rotonro, Simisaugus."
    show nina write1
    s "According to the friend who found him, Davis was hosting a small get-together with a few close friends."
    show nina thinknote1
    s "We've interviewed a few neighbours, and they reported hearing loud voices and shouting around 1am."
    s "Unfortunately, they didn't think much of it at the time, assuming it was just typical party noise."
    s "It wasn't until Davis' friend came by this morning to check on him that anyone realized something was terribly wrong."
    s "The body has been moved to the morgue, but the room itself remains untouched."
    s "I need you to be thorough."
    s "Look for any relevant evidence, collect fingerprints, and keep an eye out for possible weapons."
    s "Fair warning, there’s quite a bit of blood on this scene. I trust you know the drill by now."
    show nina normal2
    s "Remember, time is of the essence. We need to gather all the evidence we can before it gets contaminated or lost."
    s "You can check your collected evidence at anytime through the casefile on the top left corner"
    show nina normal3
    s "Good luck, Officer. We're counting on you to help us solve this case."
    jump corridor  

label corridor:
    $ default_mouse = "magnifying"

    # This changes the background image depending on whether or not the player has collected the gin bottle
    if analyzed["gin"]:
        scene no gin
    else:
        scene front corridor
    show screen ui

    # This checks if the player has collected all the evidence
    if analyzed["fingerprint"] and analyzed["handprint"] and analyzed["splatter"] and analyzed["footprint"] and analyzed["gin"]:
        hide screen ui
        show nina normal3
        s "Well done. It looks like you've processed quite a lot of evidence!"
        show nina normal1
        s "Tomorrow you can head into the lab to analyze them."
        show nina normal3
        s "But for now, give yourself a pat on the back and rest well. Tomorrow's going to be a busy day!"
        return
    call screen front_corridor



    