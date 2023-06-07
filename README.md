<h1>Pick up Your Mother</h1>
<h2>6/6 Update</h2>
<ul>
            <li>Added more actions (as well as 2 possible exits) to the "Ruins" scene (console command SCENEE)</li>
            <li>Debugged more currently available actions</li>
            <li>Slightly modified the console look, as well as the way the "help" and "scenehelp" commands work</li>
            <li>Added a couple of actions to the "go west" clearing scene, but not many</li>
            <div>&nbsp</div>
            <ol>
                        <li>"help" will now display general instructions at all times</li>
                        <li>A new command, "cmds", will now display a list of currently available global commands</li>
                        <li>"scene" will display scene-specific commands</li>
                        <li>"hint" will still display hidden commands, but they will now instead return "Completed!" when they are finished</li>
            </ol>
</ul>
<h2>Alpha Information</h2>
Welcome to our ongoing project to create THE definitive text adventure. With hand-drawn stylings, music composed, played and recorded by us, authentic and deep sound design as well as a brilliant interactive story.

Currently, the only output is to the cmd prompt opened with the game. You will need to type commands into the console in the game, and the results will be printed to the external cmd prompt. This will be changed, obviously, but you've gotta build before you paint.

The background variable "morality" will control many of the available options and branches, as well as myriad other factors. This game should ultimately provide many, many hours of satisfying reveals and twists that you either didn't expect or will not be able to reliably recreate.

Each run through is it's own, informed only by the knowledge of your previous attempts. To truly find everything this game has to offer should take 10s, if not hundreds, of playthroughs.

If you'd like to run the game for yourself right now, you'll need to install Python and Pygame. Instructions can be found here -> https://chat.openai.com/share/ebf921f5-262c-4eb3-b896-d67c0a6cbeb2

Be sure to create a new folder somewhere to hold everything within the repository. It all must be together. To run this program, open a cmd prompt and navigate to the folder you created using the "cd" (change directory) command. In this example, the folder I created is called "mother" and is located directly in my C drive:

            cd c:\mother

This will place you inside the mother folder. Once inside this folder, type the command "python mother.py"

            python mother.py

The game will launch. Please send any feedback to support@symbiotic.love! You can pre-order here -> https://shop.symbiotic.love/collections/our-games

If you would like to create a .bat file to launch the game with a click, you can:

1. Open a text editor, like Note or Wordpad.
2. Copy and paste what is underneath these instructions into the document. Be sure to replace "path to folder" with the file path to the folder containing the game 
3. Click file and save as, and save this item on the desktop. In the dropdown that likely says .txt, select "all files" instead and name the file "Mother.bat" with the quotation marks.
4. If you did everything correctly, your desktop icon should open your cmd terminal, navigate to the folder, and run the program. Message support@symbiotic.love with any questions and we'll try to get you sorted out!

            @echo off
            cd /d [PATH TO FOLDER]
            python mother.py
            pause
<h2>A note on sizing for smaller screens!</h2>
If you are on a screen that is smaller than 1080px in either direction, the current size will be entirely too large. If you open the mother.py file in any text editor and go to lines #7 and #8, you'll see "height" and "width". Change these both to 624. The text and images on the screen will not appear properly in this sizing yet, but the game will be functional and will not be larger than your screen. Technically, you can change these numbers to whatever you want. Not responsible for odd results.

<h2>Available Scenes with coded actions</h2>
SceneA - The opening scene of the game
<div>&nbsp</div>
SceneF - The scene that is inside the house of the main scene
<div>&nbsp</div>
SceneE - Ruins - reached via "go south" from SceneA
<div>&nbsp</div>
SceneC - Clearing - reached via "go west" from SceneA
<h2>Scenes available but without actions</h2>
SceneB - (picture not final) Reached via "go north" from SceneA
<div>&nbsp</div>
SceneD - (picture not final) Reached via "go east" from SceneA
<div>&nbsp</div>
SceneG - Underground Crystal City (possible exit from Ruins Scene)
<div>&nbsp</div>
SceneH - Inner Ruins (possible exit from Ruins scene)
<h2>Trello board</h2>
https://trello.com/b/REYwEncA/gameplay
<div>&nbsp</div>
Anything listed under "testing" is where we need your help the most!
<h2>Developer Console Commands</h2>
If you need others, they can be added! All developer commands are case-sensitive and must be typed in ALL CAPS.
<div>&nbsp</div>
<strong>HEALTH</strong> = <em>Check health</em>
<div>&nbsp</div>
<strong>MORAL</strong> = <em>Check morality</em>
<div>&nbsp</div>
<strong>M25/M50/M75/M100</strong> = <em>Set morality to 25/50/75/100</em>
<div>&nbsp</div>
<strong>+10HP</strong> = <em>Add 10 hp</em>
<div>&nbsp</div>
<strong>-10HP</strong> = <em>Subtract 10 hp</em>
<div>&nbsp</div>
<strong>SHARPEN</strong> = <em>Sharpen Knife</em>
<div>&nbsp</div>
<strong>DEATHWISH</strong> = <em>Activate death wish (hard) mode</em>
<div>&nbsp</div>
<strong>SCENEA</strong> = <em>Go to opening scene</em>
<div>&nbsp</div>
<strong>SCENEF</strong> = <em>Go to house inside opening scene</em>
<div>&nbsp</div>
<strong>SCENEE</strong> = <em>Go to ruins scene (reached by typing "go south" from opening)</em>
<div>&nbsp</div>
<strong>9MM</strong> = <em>Get 9mm pistol and 25 9mm bullets</em>
<div>&nbsp</div>
<strong>STICKS</strong> = <em>Get all sticks</em>
<div>&nbsp</div>
<blockquote>This game is posted here as a free test version. It is copyrighted, and may not be re-distributed or used in any capacity other than for testing and critique.</blockquote>
