import pygame
from pygame.locals import *
import os
import time

# Define the width and height of the square box
width = 1024
height = 1024

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
console_text_surface = console_font.render(">>>Type 'Help' at Any Time For a List of Current Commands!", True, console_text_color)

# Set the opacity (alpha) of the console text
console_text_surface.set_alpha(128)
console_text_rect = console_text_surface.get_rect(left=console_rect.left + 10, bottom=console_rect.bottom - 10)

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
    ["You wake up in a dark forest. Your head is pounding and your memory is blurry."],
    ["You can remember that you must pick up...something. From somewhere..."],
    ["No! Not something. Someone! But you can't remember who."],
    ["You rack your mind searching, but you only draw a blank"],
    ["You have absolutely no recollection of how you ended up here."],
    ["Maybe something in your pockets can give you a clue?"],
]

# Set up SceneA color/font
SceneA_text_font = pygame.font.Font(None, 32)
SceneA_text_color = (255, 255, 255)

# Set the position to display the text
SceneA_text_position = [100, 100]

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
has_car_keys = False
b9mm_ammo = 0
b40_ammo = 0
b22lr_ammo = 0
bbirdshot_ammo = 0
bslug_ammo = 0
deer_present = True
has_flower_knowledge = False
has_tulip = False
area_explored = False

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

        if health == 0:
            print("Game Over!")
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
            "Knife" if has_knife else "",
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
            "Mysterious note" if has_note_from_mom else "",
            "Stick" if has_stick else "",
            "A Sharpened Stick" if has_sharp_stick else "",
            "A Dangerously Sharpened Stick" if has_double_sharp_stick else "",
            "A Mysterious Statue" if has_statue else "",
        ]
        inventory = [item for item in items if item != ""]
        SceneA_commands = [
            "Items - Check your pockets.",
            "Health - Check current health.",
            "Snack - Eat a Snack (if you have one!)",
            "Eat - Have a meal.",
            "Read Note - Read whatever note you may have.",
            "Check Battery - Check your phone battery.",
            "Go North/South/East/West - Head to a new area.",
            'There are also hidden commands, which you get hints to by typing "hint!"'
        ]
        SceneA_hidden_commands = [
            "**ase D***",
            "*ppro*** **er *low**",
            "**p***ch H***e",
            "*xp**** the A***",
            "S**r**n St***",
            "**ck * T***p",
        ]

        # Display SceneA text
        if initialized_state and background_filename == background_main_game_filenames[0]:
            if elapsed_time >= text_fade_delay:
                line_spacing = 45  # Adjust this value to set the desired space between lines
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
                        
                        # All permanent console functions
                        
                        # Return to main (developer)
                        if console_input == "MAIN":
                            print("Returning to main... (developer)")
                            background_filename = background_main_game_filenames[0]
                        # Check morality (developer)
                        elif console_input == "MORAL":
                            print(f"Current morality: {morality}")
                        # "health" Display current health
                        elif console_input.lower() == "health":
                            print(f"Current health: {health}")
                        # "help" - Display current commands
                        elif console_input.lower() == "help" and background_filename == background_main_game_filenames[0]:
                            print(f"Available commands: {SceneA_commands}")
                        # "hint" - Display current hints
                        elif console_input.lower() == "hint" and background_filename == background_main_game_filenames[0]:
                            print(f"ChatGPT would make these easy af, but you're too good for that. Look at the scene for clues! {SceneA_hidden_commands}")
                        # Display inventory
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
                            if has_stick and has_knife and not has_sharp_stick:
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
                            elif not has_stick and not has_sharp_stick:
                                print("You try to sharpen your finger since you have no stick.")
                                health -= 2
                                morality -= 2
                                time.sleep(2)
                                print("It doesn't go well. Your finger hurts.")
                                time.sleep(1)
                                print(f"you have {health} health remaining.")
                            elif not has_knife:
                                print("You have no knife to sharpen the stick. You try to flintknap a point...")
                                time.sleep(5)
                                print("But you can't even remember your mother's name, let alone ancient techniques, so you break your stick and hurt yourself.")
                                health -= 4
                                morality -= 2
                                has_stick = False
                                time.sleep(1)
                                print(f"you have {health} health remaining.")
                            elif not knife_sharp:
                                print("You can't sharpen anything with your butter knife.")
                            elif has_knife and has_sharp_stick:
                                print("How much sharper do you want to make it? Maybe a double-bladed thing? Sure, why not...")
                                time.sleep(5)
                                print("Now you have a double pokey stick. Functionally identical, but now you can stab yourself at the same time!")
                                morality -= 5
                                has_sharp_stick = False
                                has_double_sharp_stick = True
                                time.sleep(2)
                                print("You notice your knife is quite dull now, too.")
                                knife_sharp = False
                        # SceneF events
                        elif background_filename == background_main_game_filenames[5]:
                            if console_input.lower() == "leave house":
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
                            elif console_input.lower() == "search chest":
                                if morality >= 51:
                                    print("You're too morally righteous to go through a stranger's things!")
                                    morality -= 3
                                    time.sleep(1.5)
                                    print("You feel your moral fortitude slipping with your growing curiosity to search the chest...")
                                elif morality < 51:
                                    print("You give in to curiosity and rummage through the chest...")
                                    time.sleep(4)
                                    print("You find what appears to be a strange statue. Since you've already entered uninvited and rummaged through this person's things, you don't think much of putting it in your pocket either.")
                                    has_statue = True
                                    morality -= 10
       
                        # SceneE events

                        # SceneD events

                        # SceneC events

                        # SceneB events
                        
                        # SceneA events
                        elif background_filename == background_main_game_filenames[0]:
                             # "explore the area" - Explore SceneA
                            if console_input.lower() == "explore the area":
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
                                    time.sleep(3)
                                    if has_flower_knowledge:
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
                            elif console_input.lower() == "approach house":
                                if deer_present:
                                    print("The deer scatter as you approach.")
                                    time.sleep(2)
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
                                time.sleep(1.5)
                                print(f"{health} health remaining")
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
                                    print("Either you're curious, or you didn't learn your lesson the first time.")
                                    time.sleep(3)
                                    print("Lose 3 health for trying to chasing Bambi (or trying to chase Bambi again)!")
                                    health -= 3
                                    print(f"You have {health} remaining.")
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
                            elif console_input.lower() == "pick a tulip":
                                if has_flower_knowledge:
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
                                elif not has_flower_knowledge:
                                    print("Either you're good at guessing, or trying to cheat. If the former: You're not there yet. If the latter: No keeping your finger on the last page here!")
                            else:
                                print("Invalid command!")  # Error message for undefined commands
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