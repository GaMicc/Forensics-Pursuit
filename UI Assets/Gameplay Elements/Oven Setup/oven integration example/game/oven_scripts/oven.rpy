init python:
    class Oven:
        """A custom data type representing the various states of the oven.
        The oven state is one of the following:
            (1) off
            (2) preheating
            (3) preheated
            (4) baking
            (5) baked
            (6) finished
        
        When the oven is in states (2) or (4), in_use is True.
        """
        state: str
        in_use: bool
        
        def __init__(self) -> None:
            self.state = "off"
            self.in_use = False

        def update_state(self) -> None:
            if self.state == "off":
                self.state = "preheating"
                self.in_use = True
            elif self.state == "preheating":
                self.state = "preheated"
                self.in_use = False
            elif self.state == "preheated":
                self.state = "baking"
                self.in_use = True
            elif self.state == "baking":
                self.state = "baked"
                self.in_use = False
            else: # oven.state == baked
                self.state = "finished"
                self.in_use = False
    
    oven = Oven()

screen oven:
    python:
        if oven.state == "off" or oven.state == "finished":
            background = "oven_closed_normal_%s"
        elif oven.state == "preheating" or oven.state == "baking":
            background = "oven_closed_baking_%s"
        elif oven.state == "preheated" or oven.state == "baked":
            background = "oven_closed_complete_%s"

    imagemap:
        auto background

        hotspot (757, 569, 371, 224) action [If(oven.state == "off", Jump("preheat")),
                                            If(oven.state == "preheated", Jump("bake")),
                                            If(oven.state == "baked", Jump("label_baked"))]

label oven:
    show screen back_button_screen('materials_lab') onlayer over_screens
    if oven.in_use:
        scene oven_closed_baking_idle
        "The oven isn't finished [oven.state] yet. Let's come back another time."
        jump oven_demo_end
    elif oven.state == "finished":
        scene oven_closed_normal_idle
        "We have no more business with the oven."
        jump oven_demo_end
    call screen oven

label preheat:
    hide screen back_button_screen onlayer over_screens
    scene oven_closed_normal_idle
    "Let's leave the time at zero and set the temperature between 100 to 200 degrees to preheat."
    hide screen oven
    $ correct_time_start = "000"
    $ correct_time_end = "001"
    $ correct_temp_start = "200"
    $ correct_temp_end = "300"
    $ correct_label = "preheat_confirmed"
    call screen main_interface

label preheat_confirmed:
    scene oven_closed_normal_idle
    $ oven.update_state() # to preheating
    scene baking_in_progress
    s "Excellent!"
    s "Let's wait until it's finished."
    "Some time passes..."
    $ oven.update_state() # to preheated
    jump oven

label bake:
    scene oven_closed_complete_idle
    s "Looks like it's finished preheating! Now we want to start baking."
    s "Let's adjust the time between 1h00 and 2h00 and leave the temperature as is."
    hide screen oven
    $ correct_time_start = "100"
    $ correct_time_end = "200"
    $ correct_label = "bake_confirmed"
    call screen main_interface

label bake_confirmed:
    scene oven_closed_normal_idle
    $ oven.update_state() # to baking
    scene baking_in_progress
    s "Excellent!"
    s "Let's wait until it's finished."
    "Some time passes..."
    $ oven.update_state() # to baked
    s "We're finished with the oven!"
    $ oven.update_state() # to finished
    jump oven

label oven_demo_end:
    return