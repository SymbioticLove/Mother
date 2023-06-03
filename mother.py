import pygame
from pygame.locals import *
import os
import time

# Define the width and height of the square box
width = 624 # 624
height = 624 # 624

# Define the duration of the fade-in effects
image_fade_duration = 4500  # in milliseconds
title_fade_delay = 4500  # in milliseconds
title_fade_duration = 2000  # in milliseconds
button_fade_delay = 7000  # in milliseconds
button_fade_duration = 2000  # in milliseconds
instructions_fade_duration = 2000  # in milliseconds
line_fade_delay = 3500  # in milliseconds
new_button_fade_delay = 30000  # in milliseconds
new_button_fade_duration = 3000  # in milliseconds
text_fade_duration = 2000 # in milliseconds
text_fade_delay = 5500 # in milliseconds
line2_fade_delay = 100 # in milliseconds

# Define the delay for the array initialization
array_init_delay = 2000  # in milliseconds

# Initialize Pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pick up Your Mother")

# Set up the fonts
font = pygame.font.Font(os.path.join("GreatVibes-Regular.ttf"), 66)
instructions_font = pygame.font.Font(os.path.join("Figtree-Bolditalic.ttf"), 36)
new_button_font = pygame.font.Font("NotoSansTC-Regular.otf", 40)

# Set up the title text
title_text = font.render("Pick up Your Mother", True, (255, 255, 255))
title_text_rect = title_text.get_rect(center=(width // 2, 255))

# Set up the instruction begin button text
new_button_text = new_button_font.render("⇒", True, (255, 255, 255))
new_button_rect = new_button_text.get_rect(bottomright=(width - 30, height - 10))

# Set up button properties
button_width = 200
button_height = 60
button_color = (100, 100, 100)
button_text_color = (255, 255, 255)
button_font = pygame.font.Font(None, 32)

# Set initial alpha values for the image, title, and buttons
image_alpha = 0
text_alpha = 0
begin_button_alpha = 0
instructions_button_alpha = 0
begin_button_rect_alpha = 0
instructions_button_rect_alpha = 0
new_button_alpha = 0
new_button_rect_alpha = 0
SceneA_background_alpha = 0
SceneB_background_alpha = 0
SceneC_background_alpha = 0
SceneD_background_alpha = 0
SceneE_background_alpha = 0
SceneF_background_alpha = 0

# Set up console properties
console_height = height // 24
console_color = (0, 0, 0,)
console_text_color = (255, 255, 255,)
console_font = pygame.font.Font(None, 24)

# Create the console rectangle
console_rect = pygame.Rect(0, height - console_height, width, console_height)

# Set up the console text properties
console_text_surface = console_font.render(">>> Type 'Help' For Instructions!", True, console_text_color)

# Set the opacity (alpha) of the console text
console_text_surface.set_alpha(128)
console_text_rect = console_text_surface.get_rect(left=console_rect.left + 10, bottom=console_rect.bottom - 5)

# Variable to store console input
console_input = ""

# Get the current time
start_time = pygame.time.get_ticks()

# Variable to track whether the instructions button has been clicked
instructions_clicked = False

# Main game loop
running = True
state = "menu"  # Initial state
instructions_state_alpha = 0  # Alpha value for instructions state
line_index = 0  # Index of the current line
line_elapsed_time = 0  # Elapsed time for each line fade-in effect

# Define the filenames for the background images
background_menu_filename = "Background.png"
background_instructions_filename = "Background2.png"
background_main_game_filenames = ["SceneA.png", "SceneB.png", "SceneC.png", "SceneD.png", "SceneE.png", "SceneF.png",]

# Prevent repeated commands
initialized_state = False
initialized_state2 = True

# Set up SceneA text
SceneA_text = [
    ["You wake up in a dark forest. Your head is pounding."],
    ["You can remember that you must pick up...something. From somewhere..."],
    ["No! Not something. Someone! But you can't remember who."],
    ["You rack your mind searching, but you only draw a blank"],
    ["You have absolutely no recollection of how you ended up here."],
    ["Maybe something in your pockets can give you a clue?"],
]
# "help" text
help_block = [
"We encourage you to get used to typing 'explore' in each new area.",
"You should also get in the habit of typing 'Cmds', 'Scene', or 'Hint' any time you are stuck.",
"These help and hint lists will update as you play, and as new actions become available.",
'Once you successfully guess one of the hidden commands, it will be marked "Completed!"',
"You should carefully consider each and every one of your actions, as they are not as straightforward as they seem.",
"Each one has the potential to change the outcome of even the scene you are in dramatically.",
"They may lock you out of items or choices, or may lead to entirely new ones, like a hidden hard-mode. Good luck and have fun!"
]

# Set up SceneA color/font
SceneA_text_font = pygame.font.Font(None, 24)
SceneA_text_color = (255, 255, 255)

# Set the position to display the text
SceneA_text_position = [20, 35]

# Define health and morality starting values
health = 15
morality = 50

# Define gameplay variables
has_note_from_mom = True
note_from_mom_read = False
has_snack = True
has_stick = False
has_sharp_stick = False
has_double_sharp_stick = False
has_food = False
has_knife = True
knife_sharp = True
has_hand_axe = False
has_fire_axe = False
has_lighter = True
has_phone = True
has_charging_cable = False
has_electricity = False
phone_battery_charged = False
has_credit_card = True
has_9mm_pistol = False
has_40_pistol = False
has_rifle = False
has_shotgun = False
has_statue = False
has_key1 = False
has_car_keys = False
deer_present = True
has_flower_knowledge = False
has_tulip = False
area_explored = False
book1_read = False
house1_explored = False
can_shoot1 = False
can_throw_stick = False
stick_thrown_once = False
stick_thrown_twice = False
stick_thrown_thrice = False
has_hair_knowledge = False
rock1_looked_under = False
poisoned = False
deathwish = False
deathwish_on = False
has_rock = False
has_geode = False
item_in_SceneE_tree = True
can_enter_ruins = False
b9mm_ammo = 0
b40_ammo = 0
b22lr_ammo = 0
bbirdshot_ammo = 0
bslug_ammo = 0

while running:
    # Menu event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if state == "menu":
                if begin_button_alpha > 0 and begin_button_rect.collidepoint(mouse_pos):
                    print("Begin Button Clicked")
                    state = "mainGame"
                    start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                elif instructions_button_alpha > 0 and instructions_button_rect.collidepoint(mouse_pos):
                    print("Instructions Button Clicked")
                    state = "instructions"
                    start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
            if state == "instructions":
                if new_button_alpha > 0 and new_button_rect.collidepoint(mouse_pos):
                    print("Instructions Begin Button Clicked")
                    state = "mainGame"
                    start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
    if state == "mainGame" and not initialized_state:
        background_filename = background_main_game_filenames [0]
        initialized_state = True

    # Calculate the elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time

    # Calculate the current alpha values based on the elapsed time
    if elapsed_time <= image_fade_duration:
        image_alpha = min(elapsed_time / image_fade_duration * 255, 255)
    if elapsed_time >= title_fade_delay and state == "menu":
        text_alpha = min((elapsed_time - title_fade_delay) / title_fade_duration * 255, 255)
    if elapsed_time >= button_fade_delay and state == "menu":
        fade_elapsed_time = elapsed_time - button_fade_delay
        if begin_button_alpha < 255:
            begin_button_alpha = min(fade_elapsed_time / button_fade_duration * 255, 255)
            instructions_button_alpha = min(fade_elapsed_time / button_fade_duration * 255, 255)

            # Calculate the corresponding alpha values for the rounded rects
            begin_button_rect_alpha = min((fade_elapsed_time - title_fade_duration) / button_fade_duration * 255, 255)
            instructions_button_rect_alpha = min((fade_elapsed_time - title_fade_duration) / button_fade_duration * 255, 255)

    # Clear the window
    window.fill((0, 0, 0))

    # Load the background image based on the state
    if state == "menu":
        background_filename = background_menu_filename
    elif state == "instructions":
        background_filename = background_instructions_filename

    background_image = pygame.image.load(background_filename)
    background_image = pygame.transform.scale(background_image, (width, height))

    # Draw the background image onto the window surface with the current alpha value
    background_image.set_alpha(image_alpha)
    window.blit(background_image, (0, 0))

    # Draw the title text onto the window surface with the current alpha value
    if state == "menu":
        title_text_with_alpha = title_text.copy()
        title_text_with_alpha.set_alpha(text_alpha)
        window.blit(title_text_with_alpha, title_text_rect)

    # Draw buttons onto the window surface
    if begin_button_alpha > 0 and state == "menu":
        begin_button_rect = pygame.Rect((width // 2) - (button_width // 2), 450, button_width, button_height)
        begin_button_rect_alpha = min(begin_button_alpha, 255)
        pygame.draw.rect(window, button_color, begin_button_rect, width=0, border_radius=8)
        pygame.draw.rect(window, button_color + (begin_button_rect_alpha,), begin_button_rect.inflate(4, 4), width=4, border_radius=12)

        begin_button_text = button_font.render("Begin", True, button_text_color)
        begin_button_text_with_alpha = begin_button_text.copy()
        begin_button_text_with_alpha.set_alpha(begin_button_alpha)
        begin_button_text_rect = begin_button_text_with_alpha.get_rect(center=begin_button_rect.center)
        window.blit(begin_button_text_with_alpha, begin_button_text_rect)

    if instructions_button_alpha > 0 and state == "menu":
        instructions_button_rect = pygame.Rect((width // 2) - (button_width // 2), 525, button_width, button_height)
        instructions_button_rect_alpha = min(instructions_button_alpha, 255)
        pygame.draw.rect(window, button_color, instructions_button_rect, width=0, border_radius=8)
        pygame.draw.rect(window, button_color + (instructions_button_rect_alpha,), instructions_button_rect.inflate(4, 4), width=4, border_radius=12)

        instructions_button_text = button_font.render("Instructions", True, button_text_color)
        instructions_button_text_with_alpha = instructions_button_text.copy()
        instructions_button_text_with_alpha.set_alpha(instructions_button_alpha)
        instructions_button_text_rect = instructions_button_text_with_alpha.get_rect(center=instructions_button_rect.center)
        window.blit(instructions_button_text_with_alpha, instructions_button_text_rect)

    # Render instructions if the state is "instructions"
    if state == "instructions":
        if elapsed_time >= new_button_fade_delay and state == "instructions":
            fade_elapsed_time = elapsed_time - new_button_fade_delay
            new_button_alpha = min(fade_elapsed_time / new_button_fade_duration * 255, 255)
            new_button_rect_alpha = min((fade_elapsed_time - title_fade_duration) / new_button_fade_duration * 255, 255)

        else:
            instructions_state_alpha = 255

        # Set up instructions text
        instructions = [
            ["You are in a forest.", "Your mother awaits your arrival.", "The rest is for you to figure out.", "This is not a game you should play to win."],
            ["Like the experience of developing and engineering...",
            "It should be played to break it in new and exciting ways.", "New losses ARE wins here. Good luck and have fun!"]
        ]

        # Calculate the elapsed time for each line fade-in effect
        line_elapsed_time_1 = max(elapsed_time - instructions_fade_duration - 3200, 0)  # Delayed by an additional 3200ms
        line_elapsed_time_2 = max(elapsed_time - instructions_fade_duration - 18000, 0)  # Delayed by an additional 18000ms for the second sub-array

        for i in range(len(instructions)):
            for j in range(len(instructions[i])):
                line_alpha = 0  # Set initial alpha value to 0

                # Determine which sub-array the line belongs to and calculate the alpha value accordingly
                if i == 0:
                    line_alpha = min((line_elapsed_time_1 - j * line_fade_delay) / instructions_fade_duration * 255, 255)
                elif i == 1:
                    line_alpha = min((line_elapsed_time_2 - j * line_fade_delay) / instructions_fade_duration * 255, 255)

                # Set text color to white for the second sub-array instructions
                if i == 1:
                    line_surface = instructions_font.render(instructions[i][j], True, (255, 255, 255))
                else:
                    line_surface = instructions_font.render(instructions[i][j], True, (0, 0, 0))

                line_surface.set_alpha(line_alpha)

                # Position the sub-array instructions at the top of the screen and around 75% down the page
                if i == 0:
                    line_rect = line_surface.get_rect(center=(width // 2, 50 + j * int(80 * 0.77)))  # Adjusted y-position for the top of the screen
                else:
                    line_rect = line_surface.get_rect(center=(width // 2, 810 + j * int(80 * 0.77)))  # Adjusted y-position for further down the page

                window.blit(line_surface, line_rect)

                if new_button_alpha > 0 and state == "instructions":
                    new_button_text_with_alpha = new_button_text.copy()
                    new_button_text_with_alpha.set_alpha(new_button_alpha)
                    window.blit(new_button_text_with_alpha, new_button_rect)
    
    #Render mainGame state
    if state == "mainGame":

        if health <= 0:
            time.sleep(2)
            print("Game Over!")
            time.sleep(2)
            running = False

        # Draw the console rectangle
        pygame.draw.rect(window, console_color, console_rect)

        # Draw the console text onto the console rectangle
        window.blit(console_text_surface, console_text_rect,)

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time

        # Create inventory and refresh each iteration
        items = [
            "Snack" if has_snack else "",
            "Food" if has_food else "",
            "Knife" if has_knife and knife_sharp else "",
            "Dull Knife" if has_knife and not knife_sharp else "",
            "Hand Axe" if has_hand_axe else "",
            "Fire Axe" if has_fire_axe else "",
            "Lighter" if has_lighter else "",
            "Phone" if has_phone else "",
            "Charging Cord" if has_charging_cable else "",
            "Credit Card" if has_credit_card else "",
            "9mm Pistol" if has_9mm_pistol else "",
            ".40 Pistol" if has_40_pistol else "",
            "Rifle" if has_rifle else "",
            "Shotgun" if has_shotgun else "",
            "Keys" if has_car_keys else "",
            "Mysterious Note" if has_note_from_mom else "",
            "Stick" if has_stick else "",
            "Sharpened Stick" if has_sharp_stick else "",
            "Dangerously Sharp Stick" if has_double_sharp_stick else "",
            "Mysterious Statue" if has_statue else "",
            "Odd Key" if has_key1 else "",
            "A DEATHWISH" if deathwish_on else "",
            "A Rock" if has_rock else "",
            "A Brilliant Geode" if has_geode else "",
        ]
        
        if b9mm_ammo > 0:
            items.append(f"9mm Bullet: {b9mm_ammo}")
        if b40_ammo > 0:
            items.append(f".40 Bullet: {b40_ammo}")
        if b22lr_ammo > 0:
            items.append(f".22LR Bullet: {b22lr_ammo}")
        if bbirdshot_ammo > 0:
            items.append(f"Birdshot: {bbirdshot_ammo}")
        if bslug_ammo > 0:
            items.append(f"Slugs: {bslug_ammo}")
        else:
            ""
        inventory = [item for item in items if item != ""]

        # Universal commands
        universal_commands = [
        "Explore" if not area_explored or house1_explored else "",
        "Items",
        "Snack" if has_snack else "",
        "Eat" if has_food else "",
        "Read Note" if has_note else "",
        "Check Battery" if has_phone else "",
        "Sharpen Stick" if has_stick else "",
        "Sharpen Stick" if has_sharp_stick else "",
        "Fire 9mm" if has_9mm_pistol and b9mm_ammo > 0 else "",
        "View Geode" if has_geode else ""
        ]
        universal_commands = [command for command in universal_commands if command != ""]

        # SceneA Commands (opening)
        SceneA_commands = [
        "Chase Deer" if deer_present else "",
        "Enter House",
        "Go North/South/East/West"
        ]
        SceneA_commands = [command for command in SceneA_commands if command != ""]
        SceneA_hidden_commands = [
        "_ppro___ __er _low__" if not has_flower_knowledge else "Completed!",
        "__ck _ T___p" if not has_tulip else "Completed!",
        ]

        # SceneE Commands (Ruins - "go south")
        SceneE_commands = [
        "Throw Stick" if can_throw_stick and not deathwish_on else "",
        "Shoot Object" if can_shoot1 and b9mm_ammo > 0 else "",
        "Look Under Rock" if not rock1_looked_under and area_explored else "",
        ]
        SceneE_commands = [command for command in SceneE_commands if command != ""]
        SceneE_hidden_commands = [
        "__as_ _o_k" if not has_geode else "Completed!",
        ]

        # SceneF Commands (inside opening house)
        SceneF_commands = [
        "Leave",
        "Rest"
        ]
        SceneF_commands = [command for command in SceneF_commands if command != ""]
        SceneF_hidden_commands = [
        "__ad" if not has_9mm_pistol else "Completed!"
        ]

        # Display SceneA text
        if initialized_state and background_filename == background_main_game_filenames[0]:
            if elapsed_time >= text_fade_delay:
                line_spacing = 25  # Adjust this value to set the desired space between lines
                delay_between_subarrays = 4000  # Delay between rendering each sub-array in milliseconds
                subarray_index = min(int((elapsed_time - text_fade_delay) / delay_between_subarrays), len(SceneA_text) - 1)

                alpha_values = []  # Store alpha values for each subarray
                fade_duration = 2000  # Duration for fading in milliseconds

                for i, line in enumerate(SceneA_text):
                    fade_progress = min(max(elapsed_time - text_fade_delay - i * delay_between_subarrays, 0), fade_duration)
                    alpha_value = int(fade_progress / fade_duration * 255)
                    alpha_values.append(alpha_value)

                for i, line in enumerate(SceneA_text[:subarray_index + 1]):
                    line_text = " ".join(line)
                    text_surface = SceneA_text_font.render(line_text, True, (SceneA_text_color[0], SceneA_text_color[1], SceneA_text_color[2]))
                    text_surface.set_alpha(alpha_values[i])  # Retrieve the appropriate alpha value for each subarray

                    line_position = (SceneA_text_position[0], SceneA_text_position[1] + i * line_spacing)
                    window.blit(text_surface, line_position)

                # Check if all subarrays have been displayed
                if subarray_index >= len(SceneA_text) - 1:
                    pass

        # mainGame state console event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if console_input != ">>> Enter a Command <<<":
                        console_input = console_input[:-1]
                elif event.key == pygame.K_RETURN:
                    # Process the console input here
                    if console_input != ">>> Enter a Command <<<":  # Skip processing if the input is the placeholder text
                        
                        # Developer console functions

                        # Sharpen knife
                        if console_input == "SHARPEN":
                            knife_sharp = True
                            print("Knife sharpened.")
                        elif console_input == "DEATHWISH":
                            deathwish_on = True
                            print("Deathwish mode activated")
                        # Go to SceneA
                        elif console_input == "SCENEA":
                            print("Going to SceneA... ")
                            background_filename = background_main_game_filenames[0]
                        # Go to SceneE
                        elif console_input == "SCENEE":
                            print("Going to SceneE")
                            background_filename = background_main_game_filenames[4]
                        # Go to SceneC
                        elif console_input == "SCENEC":
                            print("Going to SceneC")
                            background_filename = background_main_game_filenames[2]
                        # Display current morality
                        elif console_input == "MORAL":
                            print(f"Current morality: {morality}")
                        # Set morality
                        elif console_input == "M25":
                            morality = 25
                            print(f"Morality: {morality}")
                        elif console_input == "M50":
                            morality = 50
                            print(f"Morality: {morality}")
                        elif console_input == "M75":
                            morality = 75
                            print(f"Morality: {morality}")
                        elif console_input == "M100":
                            morality = 100
                            print(f"Morality: {morality}")
                        # Display current health
                        elif console_input == "HEALTH":
                            print(f"Current health: {health}")
                        # +10 health
                        elif console_input == "+10HP":
                            health += 10
                            print(f"Health: {health}")
                        # -10 health
                        elif console_input == "-10HP":
                            health -= 10
                            print(f"Health: {health}")
                        elif console_input == "9MM":
                            has_9mm_pistol = True
                            b9mm_ammo += 25
                            print("Gun and 25 9mm bullets added.")
                        elif console_input == "STICKS":
                            has_stick = True
                            has_sharp_stick = True
                            has_double_sharp_stick = True
                            print("All sticks added.")

                        # Permanent console commands

                        # "help" - Display universal commands
                        elif console_input.lower() == "help":
                            print(f"Help -> {help_block}")
                        elif console_input.lower() == "cmds":
                            print(f"Universal Commands -> {universal_commands}")
                        # "items" - Display inventory
                        elif console_input.lower() == "items":
                            print(f"The items you are carrying are: {inventory}")
                        # "snack" and "eat" - Control eating
                        elif console_input.lower() == "snack":
                            if has_snack:
                                has_snack = False
                                print(f"Your health has increased from {health} to {health + 5}!")
                                health += 5
                            elif not has_snack:
                                print("You have no snacks left!")
                        elif console_input.lower() == "eat":
                            if has_food:
                                has_food = False
                                print(f"Your health has increased from {health} to {health + 10}!")
                                health += 10
                            elif not has_food:
                                print("You have no food left!")
                        # "read note" - Read notes
                        elif console_input.lower() == "read note":
                            if has_note_from_mom:
                                print("Have fun on your trip sweetie! Make sure you're back in time to pick me up from the airport and I'll make you cookies when I get home. -Love, Mom")
                                note_from_mom_read = True
                                time.sleep(5)
                                print("The note suddenly disentigrates to ash! What is going on here?")
                                has_note_from_mom = False
                                has_note = False
                            elif not has_note:
                                print("You don't have any notes!")
                        # "check battery" - Check phone battery
                        elif console_input.lower() == "check battery":
                            if phone_battery_charged:
                                print("Your phone is charged and ready to use!")
                            elif not phone_battery_charged:
                                print("Your phone is dead!")
                        # "sharpen stick" - Sharpen stick
                        elif console_input.lower() == "sharpen stick":
                            if has_knife:
                                if knife_sharp:
                                    if has_double_sharp_stick:
                                            print("You're truly a psychopath. What are you going to sharpen?")
                                    elif has_sharp_stick:
                                        print("How much sharper do you want to make it? Maybe a double-bladed thing? Sure, why not...")
                                        time.sleep(5)
                                        print("Now you have a double pokey stick. Functionally identical, but now you can stab yourself at the same time!")
                                        morality -= 5
                                        has_sharp_stick = False
                                        has_double_sharp_stick = True
                                        time.sleep(2)
                                        print("You notice your knife is quite dull now, too.")
                                        knife_sharp = False
                                    elif not has_sharp_stick:
                                        if has_stick:
                                            print('You apperantly think it"s "that" type of game, so you pull out your knife and have a seat...')
                                            time.sleep(5)
                                            print("And you successfully sharpen your stick. For the really aggressive deer. You try to put it in your pocket...")
                                            has_sharp_stick = True
                                            has_stick = False
                                            time.sleep(2)
                                            print("And you poke your leg. It's not bad, but you feel silly and will carry the stick instead.")
                                            health -= 1
                                            morality -= 2
                                            time.sleep(1)
                                            print(f"you have {health} health remaining.")
                                        elif not has_stick:
                                            print("You try to sharpen your finger since you have no stick.")
                                            health -= 2
                                            morality -= 2
                                            time.sleep(2)
                                            print("It doesn't go well. Your finger hurts.")
                                            time.sleep(1)
                                            print(f"you have {health} health remaining.")
                                elif not knife_sharp:
                                    print("You can't sharpen anything with your butter knife.")
                            elif not has_knife:
                                print("You have no knife to sharpen the stick. You try to flintknap a point...")
                                time.sleep(5)
                                print("But you can't even remember your mother's name, let alone ancient techniques, so you break your stick and hurt yourself.")
                                health -= 4
                                morality -= 2
                                has_stick = False
                                time.sleep(1)
                                print(f"you have {health} health remaining.")
                        # "fire 9mm"
                        elif console_input.lower() == "fire 9mm":
                            if background_filename == background_main_game_filenames[5]:
                                if b9mm_ammo > 0:
                                    print ("You'll deafen yourself firing that in here.")
                                elif b9mm_ammo == 0:
                                    print ("Even if you had bullets, you'd be dumb to fire them inside. Your ears.")
                            elif b9mm_ammo > 0:
                                print("You fire the pistol into the air. Birds scatter. You feel powerful.")
                                b9mm_ammo -= 1
                            elif b9mm_ammo == 0:
                                print("You have no bullets.")

                        # SceneF events (Inside SceneA house)

                        elif background_filename == background_main_game_filenames[5]:
                            # "scene/hint" - SceneF help/hints
                            if console_input.lower() == "scene":
                                print(f"Scene Specific Commands -> {SceneF_commands}")
                            elif console_input.lower() == "hint":
                                print(f"Hidden scene commands -> {SceneF_hidden_commands} Play/look at the scene for clues!")
                            # "leave" - Exit the house
                            elif console_input.lower() == "leave":
                                print("Heading back outside...")
                                time.sleep(1.5)
                                # Change the background image to background_image_filenames[0]
                                background_filename = background_main_game_filenames[0]
                                start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                                # Fade-in effect for the new background image
                                if elapsed_time >= image_fade_duration:
                                    SceneA_background_alpha = min((elapsed_time - image_fade_duration) / image_fade_duration * 255, 255)
                                # Clear the window
                                window.fill((0, 0, 0))
                                # Draw the background image onto the window surface with the current alpha value
                                background_image.set_alpha(SceneA_background_alpha)
                                window.blit(background_image, (0, 0))
                            # "explore" - Search the house
                            elif console_input.lower() == "explore":
                                if not house1_explored:
                                    if morality >= 50:
                                        print("You're too morally righteous to go through a stranger's things!")
                                        morality -= 4
                                        time.sleep(1.5)
                                        print("You feel your moral fortitude slipping with your growing curiosity to search the room, though...")
                                    elif morality < 50:
                                        print("You give in to curiosity and rummage around the room...")
                                        time.sleep(4)
                                        print("You find a strange statue that calls to you as well as a tasty lunch and a thick book. Since you've already entered uninvited and rummaged through this person's things, you don't think much of taking these, either.")
                                        has_statue = True
                                        has_food = True
                                        house1_explored = True
                                        morality -= 10
                                elif house1_explored:
                                    print("You've already searched the house!")
                            # "rest" - Rest in bed
                            elif console_input.lower() == "rest":
                                print("Strangely, you feel the need to take a load off in this stranger's bed.")
                                time.sleep(2)
                                print("You drift off to sleep, strangely comfortable.")
                                time.sleep(4)
                                print("You awaken some time later to an irate woodsman and the police, who are arresting you for breaking and entering and invasion of privacy. You are facing 3-5 years in prison.")
                                time.sleep(4)
                                print("Game over!")
                                running = False
                            # "read" - read book
                            elif console_input.lower() == "read":
                                if has_9mm_pistol:
                                    print("The only book had a gun in it and you already took it, remember?")
                                elif not has_9mm_pistol:
                                    if not book1_read:
                                        print("Seeking enlightenment, you pick up the book.")
                                        time.sleep(2)
                                        print("It's dusty and has no title.")
                                        time.sleep(1)
                                        print("You open the book to read...")
                                        time.sleep(1)
                                        print("And you find that the book is hollowed out and contains a handgun!")
                                        if morality <= 35:
                                            time.sleep(2)
                                            print("You take gun. For 'protection.' From what, you aren't sure.")
                                            has_9mm_pistol = True
                                            b9mm_ammo += 1
                                            book1_read = True
                                        elif morality >= 35:
                                            book1_read = True
                                            time.sleep(2)
                                            print("You feel no need to take the gun, especially since it's not yours. You replace it in the book.")
                                    elif book1_read:
                                        print("You pick up the book again.")
                                        if morality <= 35:
                                            time.sleep(2)
                                            print("And you retrieve the gun inside. The magazine is empty, but there is one bullet in the chamber.")
                                            has_9mm_pistol = True
                                            b9mm_ammo += 1
                                            morality -= 10
                                        elif morality >= 35:
                                            time.sleep(2)
                                            print("And then you put it right back down. Lunch is one thing, but you don't feel comfortable taking the gun.")
                            else:
                                print("Invalid Command")
                        
       
                        # SceneE events (Ruins)
                        elif background_filename == background_main_game_filenames[4]:
                            # "scene"/"hint" - SceneE help/hints
                            if console_input.lower() == "scene":
                                print(f"Scene-specific commands -> {SceneE_commands}")
                            elif console_input.lower() == "hint":
                                print(f"Hidden scene commands -> {SceneE_hidden_commands} Play/look at the scene for clues!")
                            # "explore" - Explore SceneE
                            elif console_input.lower() == "explore":
                                if not area_explored:
                                    print("You search around the ruins...")
                                    time.sleep(3)
                                    print("You find some sort of key, and you notice a giant rock. You tuck the key away. Your pockets are really big.")
                                    time.sleep(2)
                                    print("Look, suspend your disbelief here. It's my first project.")
                                    has_key1 = True
                                    area_explored = True
                                    if has_double_sharp_stick:
                                        time.sleep(2)
                                        print("Your dangerously sharp stick continues to be a poor decision.")
                                        time.sleep(2)
                                        print("You accidently poke your arm. It hurts.")
                                        health -= 2
                                        time.sleep(2)
                                        print(f"You have {health} health remaining.")
                                    elif not has_double_sharp_stick:
                                        pass
                                    if has_9mm_pistol:
                                        time.sleep(2)
                                        print("You see something hanging from a nearby tree. You walk over to get a better look.")
                                        time.sleep(2)
                                        print("It's very high. Whatever it is, the only way you could get to it is to shoot it down.")
                                        can_shoot1 = True
                                        if has_stick or has_sharp_stick or has_double_sharp_stick:
                                            time.sleep(1)
                                            print("Or you could try throwing your stick... It's very far.")
                                            can_throw_stick = True
                                    elif not has_9mm_pistol:
                                        if has_stick or has_sharp_stick or has_double_sharp_stick:
                                            time.sleep(2)
                                            print("You see something hanging from a nearby tree. You walk over to get a better look.")
                                            time.sleep(2)
                                            print("Whatever it is, it's very high. You could try throwing your stick at it!")
                                            can_throw_stick = True
                                        elif not has_stick or has_sharp_stick or has_double_sharp_stick:
                                            time.sleep(1)
                                            print("Whatever it is, it's way too high to get to.")
                                elif area_explored:
                                    print("You've already looked around the ruins.")
                            # "throw stick" - Throw your stick at the object
                            elif console_input.lower() == "throw stick" and can_throw_stick and item_in_SceneE_tree and not deathwish_on:
                                if deathwish:
                                    print("You must have a deathwish. Fine, you're now in 'deathwish' mode. Good luck.")
                                    deathwish_on = True
                                elif stick_thrown_thrice:
                                    print(f"You're struck by lightning. Lose 6 health. How about that, funny guy?")
                                    health -= 6
                                    time.sleep(2)
                                    print(f"you have {health} health remaining.")
                                    deathwish = True
                                elif stick_thrown_twice:
                                    print("No. I told you we were going to stop you. You're welcome. Type it again and I'll take 3 health out of spite.")
                                    stick_thrown_thrice = True
                                elif not stick_thrown_once:
                                    print("You throw your stick at the item...")
                                    time.sleep(3)
                                    print("It falls back down on your head.")
                                    time.sleep(1)
                                    health -= 3
                                    print("It makes you regret your hubis. It wasn't even close.")
                                    time.sleep(2)
                                    print("...but you DO think you could get closer the next time.")
                                    time.sleep(2)
                                    print(f"You have {health} health remaining.")
                                    stick_thrown_once = True
                                elif stick_thrown_once:
                                    print("You feel like you'll have a better shot the second time. You wind up again...")
                                    time.sleep(3)
                                    print("Not even close! Must've been the hubris again. And it hit your head again. We're gonna stop you from doing that a 3rd time.")
                                    health -= 3
                                    time.sleep(2)
                                    print(f"You have {health} health remaining.")
                                    stick_thrown_twice = True
                            # "shoot object" - Shoot the object out of the tree
                            elif console_input.lower() == "shoot object" and can_shoot1 and item_in_SceneE_tree and has_9mm_pistol: 
                                if b9mm_ammo > 0:
                                    if deathwish_on:
                                        print("(dw) Your gun backfires and the hot brass goes down your shirt.")
                                        time.sleep(1)
                                        print("You dance and struggle to remove it.")
                                        time.sleep(2)
                                        print("You're not seriously injured, but the gun is damaged beyond your skills of repair.")
                                        health -= 1
                                        has_9mm_pistol = False
                                        b9mm_ammo -= 1
                                        time.sleep(2)
                                        print(f"You have {health} health remaining.")
                                    elif morality <= 35:
                                        print("You take aim...")
                                        time.sleep(2)
                                        print("And fire. And miss. To be fair, it was a long shot.")
                                        b9mm_ammo -= 1
                                        morality += 5
                                    elif morality > 35:
                                        print("You take aim...")
                                        time.sleep(2)
                                        print("And you nail the cord supporting the object!")
                                        time.sleep(1)
                                        print("It falls...")
                                        b9mm_ammo -= 1
                                        morality -= 3
                                        item_in_SceneE_tree = False
                                        if morality > 35:
                                            print("You catch the item. Which turns out to be a rock. Hooray!")
                                            time.sleep(2)
                                            print("You put it in your pock...you find a backpack nearby and put it on. There.")
                                            morality += 20
                                            time.sleep(2)
                                            has_rock = True
                                        elif morality <= 35:
                                            print("The item turns out to be a rock. Which you leave on the ground.")
                                elif b9mm_ammo == 0:
                                    print("You have no bullets.")
                            # "approach ruins" - Approach the ruins
                            elif console_input.lower() == "approach ruins" and not can_enter_ruins:
                                if not has_key1:
                                    print("You approach the ruins...")
                                    time.sleep(2)
                                    print("You look along the walls and notice a keyhole in a crevice.")
                                if has_key1:
                                    print("You approach the ruins...")
                                    time.sleep(2)
                                    print("You find a place that your key fits!")
                                    time.sleep(2)
                                    print("Your key works and the doors crack ajar. Enter if you dare.")
                                    can_enter_ruins = True
                            # "smash rock" - Smash the rock open
                            elif console_input.lower() == "smash rock" and has_rock:
                                print("You look around for some way to smash open the rock...")
                                time.sleep(2)
                                print("You decide to smash it against the walls of the ruins.")
                                time.sleep(2)
                                print("The rock splits open quite easily, and inside is revealed to be a beautiful violet geode!")
                                has_geode = True
                                has_rock = False
                            # "view geode" - View the geode
                            elif console_input.lower() == "view geode" and has_geode:
                                if not has_hair_knowledge:
                                    print("As you look at the geode, you suddenly remember a flash of your mother's deep, violet hair.")
                                    morality += 5
                                    time.sleep(2)
                                    print("You feel a rush of self-assurance.")
                                    has_hair_knowledge = True
                                elif has_hair_knowledge:
                                    print("You contemplate the geode once again.")
                                    morality += 2
                                    time.sleep(3)
                                    print("You feel assured and confident.")
                            # "look under rock" - Look under the rock
                            elif console_input.lower() == "look under rock" and not rock1_looked_under and area_explored:
                                if deathwish_on:
                                    print("(dw) You lift up the rock to look under it...")
                                    time.sleep(2)
                                    print("And out hops a black scorpion the size of a small dog!")
                                    time.sleep(2)
                                    print("You try to avoid it, but it's much faster than you and manages to sting your hand.")
                                    time.sleep(2)
                                    print("You're not sure what kind of scorpion it was, but your vision begins to go dark and you fall over.")
                                    time.sleep(2)
                                    print("Your death comes quite soon after.")
                                    health = 0
                                elif not deathwish_on:
                                    print("You lift up the rock to look under it...")
                                    time.sleep(2)
                                    print("And out hops a small scorpion!")
                                    time.sleep(2)
                                    print("You try to avoid it, but it's much faster than you and manages to land a sting on your hand.")
                                    time.sleep(2)
                                    print("Your hand is numb, but you're pretty sure that you'll be fine.")
                                    health -= 3
                                    time.sleep(1)
                                    print(f"You have {health} remaining.")
                                    poisoned = True
                                    rock1_looked_under = True

                        # SceneD events

                        # SceneC events

                        # SceneB events
                        
                        # SceneA events (Opening)

                        elif background_filename == background_main_game_filenames[0]:
                            # "scene"/"hint" - SceneA help/hints
                            if console_input.lower() == "scene":
                                print(f"Scene-specific commands -> {SceneA_commands}")
                            elif console_input.lower() == "hint":
                                print(f"Hidden scene commands -> {SceneA_hidden_commands} Play/look at the scene for clues!")
                             # "explore" - Explore SceneA
                            elif console_input.lower() == "explore":
                                if not area_explored:
                                    if deer_present:
                                        print("The deer scatter as you look around the area...")
                                        deer_present = False
                                    elif not deer_present:
                                        print("You look around...")
                                    time.sleep(4)
                                    print("You pick up a stick and put it in your pocket, in case of more deer.")
                                    has_stick = True
                                    area_explored = True
                                    if has_flower_knowledge:
                                        time.sleep(2)
                                        print("As you look around, you see some tulips nearby...")
                                elif area_explored:
                                    print("You're a thorough explorer, you needn't look twice.")
                            # "go north"
                            elif console_input.lower() == "go north":
                                print("Heading north...")
                                health -= 1
                                time.sleep(3)
                                # Change the background image to background_image_filenames[1]
                                background_filename = background_main_game_filenames[1]
                                start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                                # Fade-in effect for the new background image
                                if elapsed_time >= image_fade_duration:
                                    SceneB_background_alpha = min((elapsed_time - image_fade_duration) / image_fade_duration * 255, 255)
                                # Clear the window
                                window.fill((0, 0, 0))
                                # Draw the background image onto the window surface with the current alpha value
                                background_image.set_alpha(SceneB_background_alpha)
                                window.blit(background_image, (0, 0))
                                time.sleep(1.5)
                                print(f"{health} health remaining")
                                area_explored = False
                                if has_stick:
                                    morality += 4
                            # "go south"
                            elif console_input.lower() == "go south":
                                print("Heading south...")
                                health -= 1
                                time.sleep(3)
                                # Change the background image to background_image_filenames[4]
                                background_filename = background_main_game_filenames[4]
                                start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                                # Fade-in effect for the new background image
                                if elapsed_time >= image_fade_duration:
                                    SceneE_background_alpha = min((elapsed_time - image_fade_duration) / image_fade_duration * 255, 255)
                                # Clear the window
                                window.fill((0, 0, 0))
                                # Draw the background image onto the window surface with the current alpha value
                                background_image.set_alpha(SceneE_background_alpha)
                                window.blit(background_image, (0, 0))
                                time.sleep(1.5)
                                print(f"{health} health remaining")
                                area_explored = False
                                if has_stick:
                                    morality += 4
                            # "go west"
                            elif console_input.lower() == "go west":
                                print("Heading west...")
                                health -= 1
                                time.sleep(3)
                                # Change the background image to background_image_filenames[2]
                                background_filename = background_main_game_filenames[2]
                                start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                                # Fade-in effect for the new background image
                                if elapsed_time >= image_fade_duration:
                                    SceneC_background_alpha = min((elapsed_time - image_fade_duration) / image_fade_duration * 255, 255)
                                # Clear the window
                                window.fill((0, 0, 0))
                                # Draw the background image onto the window surface with the current alpha value
                                background_image.set_alpha(SceneC_background_alpha)
                                window.blit(background_image, (0, 0))
                                time.sleep(1.5)
                                print(f"{health} health remaining")
                                area_explored = False
                                if has_stick:
                                    morality += 4
                            # "go east"
                            elif console_input.lower() == "go east":
                                print("Heading east...")
                                health -= 1
                                time.sleep(3)
                                # Change the background image to background_image_filenames[3]
                                background_filename = background_main_game_filenames[3]
                                start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                                # Fade-in effect for the new background image
                                if elapsed_time >= image_fade_duration:
                                    SceneD_background_alpha = min((elapsed_time - image_fade_duration) / image_fade_duration * 255, 255)
                                # Clear the window
                                window.fill((0, 0, 0))
                                # Draw the background image onto the window surface with the current alpha value
                                background_image.set_alpha(SceneD_background_alpha)
                                window.blit(background_image, (0, 0))
                                time.sleep(1.5)
                                print(f"{health} health remaining")
                                area_explored = False
                                if has_stick:
                                    morality += 4
                            # "approach house"
                            elif console_input.lower() == "enter house":
                                if deer_present:
                                    print("The deer scatter as you approach.")
                                    time.sleep(1)
                                    deer_present = False
                                print("Heading to the house...")
                                time.sleep(3)
                                # Change the background image to background_image_filenames[5]
                                background_filename = background_main_game_filenames[5]
                                start_time = pygame.time.get_ticks()  # Reset start time for fade-in effect
                                # Fade-in effect for the new background image
                                if elapsed_time >= image_fade_duration:
                                    SceneF_background_alpha = min((elapsed_time - image_fade_duration) / image_fade_duration * 255, 255)
                                # Clear the window
                                window.fill((0, 0, 0))
                                # Draw the background image onto the window surface with the current alpha value
                                background_image.set_alpha(SceneF_background_alpha)
                                window.blit(background_image, (0, 0))
                                area_explored = False
                            # "chase deer" - Chase the deer
                            elif console_input.lower() == "chase deer":
                                if deer_present:
                                    print("You try to chase the deer...")
                                    time.sleep(3)
                                    print("You fall down and hurt yourself.")
                                    health -= 3
                                    morality -= 5
                                    time.sleep(1.5)
                                    print(f"Your ankle is throbbing. You have {health} health remaining.")
                                    deer_present = False
                                elif not deer_present:
                                    print("Deer prefer it when you approach slowly. And they've already left anyway.")
                                    time.sleep(3)
                                    print("Lose 3 health for trying to chasing Bambi (or trying to chase Bambi again)!")
                                    health -= 3
                                    print(f"You have {health} health remaining.")
                            # "approach deer slowly" - Approach the deer slowly
                            elif console_input.lower() == "approach deer slowly":
                                if deer_present:
                                    print("You attempt to carefully approach the deer...")
                                    time.sleep(5)
                                    print("The deer allow you to approach and pet them!")
                                    health += 3
                                    morality += 2
                                    time.sleep(3)
                                    print(f"You feel a connection with nature, and you remember how much your mother loves tulips!")
                                    time.sleep(1.5)
                                    print(f"You feel refreshed! You have gained 3 health and have {health} health remaining!")
                                    deer_present = False
                                    has_flower_knowledge = True
                                elif not deer_present:
                                    print("The deer are all gone!")
                            # "pick a tulip" - Pick a tulip
                            elif console_input.lower() == "pick a tulip" and has_flower_knowledge:
                                    if not has_tulip:
                                        print("You walk over to the tulips...")
                                        time.sleep(3)
                                        print("And bend down...")
                                        time.sleep(2)
                                        print("And pick a tulip! You put it in your shirt pocket to keep it safe for your mom.")
                                        has_tulip = True
                                        morality += 5
                                    elif has_tulip:
                                        print("You're going to have a hard time keeping even 1 tulip safe!")
                            else:
                                print("Invalid command")  # Error message for undefined commands
                        console_input = ""  # Clear the console input after processing
                    console_input = ""  # Clear the console input after processing
                else:
                    if console_input == ">>> Enter a Command <<<":
                        console_input = ""  # Clear the placeholder text when typing begins
                    console_input += event.unicode

                # Update the console text surface
                if console_input == "":
                    console_input = ">>> Enter a Command <<<"  # Restore the placeholder text if no text entered
                console_text_surface = console_font.render(console_input, True, console_text_color)
                # Set the opacity (alpha) of the console text
                console_text_surface.set_alpha(128)
                console_text_rect = console_text_surface.get_rect(left=console_rect.left + 10, centery=console_rect.centery)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()








































