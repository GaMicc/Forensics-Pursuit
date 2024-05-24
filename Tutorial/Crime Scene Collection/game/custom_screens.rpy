## Opening screen ###############################################################
screen opening_screen():
    imagemap:
        idle "background_idle"
        hover "background_hover"
        ground "background_idle"
        hotspot (1491, 198, 356, 102) action Jump("enter_splash_screen")

screen splash_screen():
    key "K_SPACE" action Jump("instructions_text")

screen move_on():
    frame:
        xpos 0.80 ypos 0.70
        hbox:
            spacing 3
            text "hit space to continue >>"

screen instructions_text_screen():
    frame:
        xcenter 0.5 ycenter 0.5
        hbox:
            spacing 5
            xsize 800
            text "Before we enter the crime scene, let's make sure you know how to navigate your surroundings.\n\n>>hit space to continue"
    key "K_SPACE" action Jump("instructions_key_arrows")

screen instructions_key_screen():
    if middle:
        key "K_UP" action [ToggleDict(front_directions, 'up'), Jump("jump_directions")]
        key "K_DOWN" action [ToggleDict(front_directions, 'down'), Jump("jump_directions")]
        key "K_RIGHT" action [ToggleDict(front_directions, 'right'), Jump("jump_directions")]
        key "K_LEFT" action [ToggleDict(front_directions, 'left'), Jump("jump_directions")]
    else:
        if curr_directions['up']:
            key "K_DOWN" action Jump("jump_directions")
        elif curr_directions['down']:
            key "K_UP" action Jump("jump_directions")
        if curr_directions['right']:
            key "K_LEFT" action Jump("jump_directions")
        elif curr_directions['left']:
            key "K_RIGHT" action Jump("jump_directions")


screen opening(word):
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "You are at the front door, [word]."
  

screen instructions_move_on_screen():
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            text "Are you ready to move on?"
            textbutton "Yes":
                action Jump("enter_scene")
            textbutton "Keep exploring the keys":
                action Jump("keep_exploring")

### entering scene 
screen entering_screen():
    imagemap:
        idle "instructions_bg"
        hover "front_hover"
        ground "instructions_bg"
        hotspot (768, 209, 346, 656) action Jump("hallway")

screen hallway_screen():
    if middle:
        key "K_UP" action [ToggleDict(hallway_directions, 'up'), Jump("hallway_directions")]
        key "K_DOWN" action [ToggleDict(hallway_directions, 'down'), Jump("hallway_directions")]
        key "K_RIGHT" action [ToggleDict(hallway_directions, 'right'), Jump("hallway_directions")]
        key "K_LEFT" action [ToggleDict(hallway_directions, 'left'), Jump("hallway_directions")]
    else:
        if curr_directions['up']:
            key "K_DOWN" action Jump("hallway_directions")
        elif curr_directions['down']:
            key "K_UP" action Jump("hallway_directions")
        if curr_directions['right']:
            key "K_LEFT" action Jump("hallway_directions")
        elif curr_directions['left']:
            key "K_RIGHT" action Jump("hallway_directions")
    key "K_SPACE" action Jump("examination_kitchen")

### kitchen scene
screen stove_screen():
    key "K_UP" action [ToggleDict(stove_directions, 'up'), Jump("stove_directions")]
    key "K_DOWN" action [ToggleDict(stove_directions, 'down'), Jump("stove_directions")]
    key "K_RIGHT" action [ToggleDict(stove_directions, 'right'), Jump("stove_directions")]
    key "K_LEFT" action [ToggleDict(stove_directions, 'left'), Jump("stove_directions")]

screen kitchen_screen():
    imagemap:
        idle "kitchen_idle"
        hover "kitchen_hover"
        ground "kitchen_idle"
        hotspot (245, 685, 438, 400) action Jump("examination_stove")

screen toolbox():
    hbox:
        xpos 0.03 ypos 0.02
        imagebutton:
            idle "toolbox" at toolbox_smaller
            hover "toolbox_hover"
            action Jump("tool_expand")
 
transform toolbox_smaller():
    zoom 0.1

transform tools_extra_small():
    zoom 0.06
 
screen expand_tools():
    hbox:
        xpos 0.888 ypos 0.415
        imagebutton:
            insensitive "scalebar_insensitive" at tools_extra_small
            idle "scalebar_idle"
            hover "scalebar_hover"

            hovered Notify("scale bar")
            unhovered Notify('')

            action Jump('scalebar')
            sensitive tools['scalebar']

    hbox:
        xpos 0.890 ypos 0.590
        imagebutton:
            insensitive "lifting_backing_insensitive" at tools_extra_small
            idle "lifting_backing_idle"
            hover "lifting_backing_hover"

            hovered Notify("fingerprint lifting tape")
            unhovered Notify('')

            action Jump('lifting_tape')
            sensitive tools['lifting_tape']

    hbox:
        xpos 0.004 ypos 0.3
        imagebutton:
            insensitive "evident_tape_insensitive" at tools_extra_small
            idle "evident_tape_idle"
            hover "evident_tape_hover"

            hovered Notify("evident tape")
            unhovered Notify('')

            action Jump('tamper_tape')
            sensitive tools['tape']

    hbox:
        xpos 0.038 ypos 0.47
        imagebutton:
            insensitive "evidence_bags_insensitive" at tools_extra_small
            idle "evidence_bags_idle"
            hover "evidence_bags_hover"

            hovered Notify("evidence bags")
            unhovered Notify('')

            action Jump('evidence_bags')
            sensitive tools['bag']

    hbox:
        xpos 0.895 ypos 0.238
        imagebutton:   
            insensitive "magnetic_powder_insensitive" at tools_extra_small
            idle "magnetic_powder"
            hover "hover_magnetic_powder"

            hovered Notify("granular powder")
            unhovered Notify('')

            action Jump('magnetic_powder')
            sensitive tools['powder']

    hbox:
        xpos 0.021 ypos 0.67
        imagebutton:
            insensitive "evidence_markers_insensitive" at tools_extra_small
            idle "evidence_markers"
            hover "evidence_markers_hover"
    
            hovered Notify("evidence markers")
            unhovered Notify('')

            action Jump('evidence_markers')
            sensitive tools['marker']

    hbox:
        xpos 0.89 ypos 0.03
        imagebutton:
            insensitive "uv_light_insensitive"
            idle "uv_light_idle" at tools_extra_small
            hover "uv_light_hover"
    
            hovered Notify("flashlight")
            unhovered Notify('')

            action Jump('uv_light')
            sensitive tools['light']

screen arrow():
    showif tools['light']:
        hbox:
            xpos 0.85 ypos 0.12
            image "arrow" at tools_extra_small
    showif tools['powder']:
        hbox:
            xpos 0.84 ypos 0.30
            image "arrow" at tools_extra_small
    showif tools['scalebar']:
        hbox:
            xpos 0.84 ypos 0.5
            image "arrow" at tools_extra_small
    showif tools['lifting_tape']:
        hbox:
            xpos 0.84 ypos 0.7
            image "arrow" at tools_extra_small
    showif tools['bag']:
        hbox:
            xpos 0.11 ypos 0.53
            image "arrow_flip" at tools_extra_small
    showif tools['tape']:
        hbox:
            xpos 0.11 ypos 0.33
            image "arrow_flip" at tools_extra_small
 
screen uv_light_stove():
    default discover = False
    imagemap:
        idle "stove_fingerprint"
        hover "stove_fingerprint_hover"
        ground "stove_fingerprint"
        hotspot (730,539, 82, 73) action SetLocalVariable('discover', True)

    showif discover:
        image "stove_fingerprint_hover"
        frame:
            xalign 0.6 yalign 0.5
            text "You've discovered a latent fingerprint!"
        hbox:
            xalign 0.95 yalign 0.93
            imagebutton:
                idle "checkmark" at checkmark_small
                hover "checkmark_hover"
                action Jump("finished_uv_light")
                
transform checkmark_small():
    zoom 0.2

transform backing_card():
    zoom 0.31

transform evidence_marker_1():
    zoom 0.07

screen evidence_marker_stove():
    hbox:
        xpos 0.32 yalign 0.48
        image "evidence_marker_1" at evidence_marker_1


screen magnetic_powder_stove():
    default dusted = False
    imagemap:
        idle "stove_fingerprint_persist"
        hover "stove_fingerprint_persist"
        hotspot (730,512, 82, 73) action SetLocalVariable('dusted', True)
    
    showif dusted:
        image "stove_fingerprint_dusted"
        frame:
            xalign 0.54 yalign 0.5
            text "You've dusted the fingerprint!"
        hbox:
            xalign 0.95 yalign 0.93
            imagebutton:
                idle "checkmark" at checkmark_small
                hover "checkmark_hover"
                action Jump("finished_magnetic_powder")

screen scalebar_stove():
    default taped = False
    imagemap:
        idle "stove_fingerprint_zoomed"
        hover "stove_fingerprint_zoomed"
        hotspot (745,420,601,369) action SetLocalVariable('taped', True)
    
    showif taped:
        add "scalebar_taped_zoomed"
        frame:
            xalign 0.6 yalign 0.38
            text "You've added the scalebar!"
        # add "stove_fingerprint_tape"
        hbox:
            xalign 0.95 yalign 0.93
            imagebutton:
                idle "checkmark" at checkmark_small
                hover "checkmark_hover"
                action Jump("finished_scalebar")


screen lifting_tape_stove():
    default taped = False
    imagemap:
        idle "scalebar_lifting"
        hover "scalebar_lifting"
        hotspot (696,510,226,129) action Jump("lifting_to_backing")


screen backing_card_stove(action):
    image "lifting_to_backing"
    if action=='lift':
        hbox:
            xpos 0.0003 yalign 0.8
            imagebutton:
                idle "tape_print_scalebar"
                hover "tape_print_scalebar_hover"
                action Jump("drag_tape")
        hbox:
            xpos 0.5 yalign 0.8
            image "backing_card" at backing_card
    elif action=='drag':
        hbox:
            xpos 0.5 yalign 0.8
            imagebutton:
                idle "backing_card" at backing_card
                hover "backing_card"
                action Jump("stick_backing")
    elif action=='stick':
        hbox:
            xpos 0.5 yalign 0.8
            image "complete_backing_card" at backing_card
    else:
        hbox:
            xpos 0.5 yalign 0.8
            image "complete_backing_card_r" at backing_card
        hbox:
            xpos 0.1 yalign 0.8
            image "complete_backing_card_front" at backing_card
        
        hbox:
            xalign 0.95 yalign 0.93
            imagebutton:
                idle "checkmark" at checkmark_small
                hover "checkmark_hover"
                action Jump("finish_lifting_tape")

screen scalebar_stove_tape():
    default collected = False
    imagemap:
        idle "stove_fingerprint_dusted"
        hover "stove_fingerprint_dusted"
        hotspot (717,529, 132, 106) action SetLocalVariable('collected', True)
    
    showif collected:
        add "stove_fingerprint_persist_after"
        frame:
            xalign 0.6 yalign 0.5
            text "You've collected the fingerprint!"
        # add "stove_fingerprint_tape"
        hbox:
            xalign 0.95 yalign 0.93
            imagebutton:
                idle "checkmark" at checkmark_small
                hover "checkmark_hover"
                action Jump("finished_scalebar")


transform resize_current_evidence():
    zoom .2

transform resize_evidence_bags():
    zoom .1

transform resize_evidence_bags_seal():
    zoom .15


screen current_evidence(action):
    hbox:
        xalign 0.5 yalign 0.30
        text "current evidence collected":
            size 28

    if action=='insensitive':
        hbox:
            xpos 0.33 ypos 0.02
            image "complete_backing_card" at resize_current_evidence
        hbox:
            xpos 0.75 ypos 0.50
            image "stove_evidence_bags_light" at resize_evidence_bags
    else:
        hbox:
            xpos 0.75 ypos 0.50
            imagebutton:
                idle "stove_evidence_bags_light" at resize_evidence_bags
                hover "stove_evidence_bags_light_hover"
                action Jump('put_card_into_bag')

        if action =='show':
            hbox:
                xpos 0.33 ypos 0.02
                imagebutton:
                    idle "complete_backing_card" at resize_current_evidence
                    hover "complete_backing_card_hover"
                    action Jump("drag_card_into_bag")
        
        if action=='put_in':
            image "stove_evidence_bags"
            frame:
                xalign 0.65 yalign 0.6
                text "You've packaged your evidence!"
            hbox:
                xalign 0.5 yalign 0.30
                text "current evidence collected":
                    size 28
            hbox:
                xpos 0.75 ypos 0.50
                image "stove_evidence_bags_light" at resize_evidence_bags
        
            hbox:
                xalign 0.95 yalign 0.93
                imagebutton:
                    idle "checkmark" at checkmark_small
                    hover "checkmark_hover"
                    action Jump("evidence_bags_finished")
        
  

    

screen evidence_bags_stove():
    hbox:
        xpos 0.45 ypos 0.30
        image "stove_evidence_bags_light" at resize_evidence_bags


screen tamper_evident_tape_stove(sensitive):
    default taped = False
    if not sensitive:
        hbox:
            xpos 0.42 ypos 0.30
            image 'evidence_bags_idle' at resize_evidence_bags_seal
    else:
        hbox:
            xpos 0.42 ypos 0.30
            imagebutton:
                idle "evidence_bags_idle" at resize_evidence_bags_seal
                hover "evidence_bags_hover"
                action SetLocalVariable('taped', True)
    
    if taped:
        hbox:
            xpos 0.39 ypos 0.28
            image "evidence_bags_packed" at resize_evidence_bags_seal
            
        frame:
            xalign 0.6 yalign 0.5
            text "You've sealed the bag!"
        hbox:
            xalign 0.95 yalign 0.93
            imagebutton:
                idle "checkmark" at checkmark_small
                hover "checkmark_hover"
                action Jump("tutorial_finished")





screen evidence_to_lab():
    frame:
        xalign 0.5 ypos 0.5
        vbox:
            text "Are you ready to to ship your evidence to the lab for examination?"
            textbutton "Yes":
                action Jump("enter_lab")
            textbutton "Keep examining":
                action Jump("tool_expand")

screen move_on_lab():
    key "K_m" action Jump('tutorial_finished')
    frame:
        xpos 0.80 ypos 0.95
        hbox:
            spacing 3
            text "hit m to head to lab >>"

screen temporary_pause:
    key "K_SPACE" action NullAction()
