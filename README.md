<h1>Pick up Your Mother</h1>

Welcome to our ongoing project to create THE definitive text adventure. With hand-drawn stylings, music composed, played and recorded by us, authentic and deep sound design as well as a brilliant interactive story.

Currently, the only output is to the cmd prompt opened with the game. You will need to type commands into the console in the game, and the results will be printed to the external cmd prompt. This will be changed, obviously, but you've gotta build before you paint.

The background variable "morality" will control many of the available options and branches, as well as myriad other factors. This game should ultimately provide many, many hours of satisfying reveals and twists that you either didn't expect or will not be able to reliably recreate.

Each run through is it's own run, informed only by the knowledge of your previous attempts. To truly find everything this game has to offer should take 10s, if not hundreds, of playthroughs.

If you'd like to run the game for yourself right now, you'll need to install Python and Pygame. Instructions can be found here -> https://chat.openai.com/share/ebf921f5-262c-4eb3-b896-d67c0a6cbeb2

Be sure to create a new folder somewhere to hold everything within the repository. It all must be together. To run this program, open a cmd prompt and navigate to the folder you created using the "cd" (change directory) command:

cd c:\mother

This will place you inside the mother folder. Once inside this folder, type the command "python mother.py"

c:\mother>python mother.py

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
            
This game is posted here as a free test version. It is copyrighted, and may not be re-distributed or used in any capacity other than for testing and critique.
<h2>Developer Console Commands</h2>
If you need others, they can be added! All developer commands are case-sensitive and must be typed in ALL CAPS.
<div>HEALTH = Check health</div>
<div>MORAL = Check morality</div>
<div>M25/M50/M75/M100 = Set morality to 25/50/75/100</div>
<div>+10HP = Add 10 hp</div>
<div>-10HP = Subtract 10 hp</div>
<div>SHARPEN = Sharpen Knife</div>
<div>DEATHWISH = Activate deathwish (hard) mode</div>
<div>SCENEA = Go to opening scene</div>
<div>SCENEF = Go to house inside opening scene</div>
<div>SCENEE = Go to ruins scene (reached by typing "go south" from opening)</div>
<div>9MM = Get 9mm pistol and 25 9mm bullets</div>
<div>STICKS = Get all sticks</div>
