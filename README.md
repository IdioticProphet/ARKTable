# ARKTabe

Also called the ARK Effort Calculator, is a fairly simple algorithmn I developed to determine the best material to XP ratio throughout the game, the only snag in such system is the simple fact that there is no set amount of effort you need to put fourth to get any one item. 

That's where the user comes in! Currently you go through constants and change the value in mats, which will change the calculations and you can go through it to your liking!

## How to use

You really just run main.py, I could add a precompiled version of it if you really want the output; however, with the data I provided, the best item to make is Cooking Pots.

If you would like to change values yourself mosey on down to constants.py with your favorite text editors and change the values within the dictionary called "mats", read the description in there and only change the numbers!


NOTE: A couple things are considered the same (Metal Ingots, Iron Ingots, Scrap Metal/Iron Ingot) I'm aware of stuff like this, but for the sake of argument I decided that if someone cared enough then I'd fix it, but for now its okay! I'm also aware going from dict to Enum to dict is pretty trash... I didn't bother to fix it.

NOTE2: the table is nexted under main_table.table and it is a list, I might make this into a more viewable model at some point in time


Thanks so much to Akia Vongdara for the data table! I was definitely too lazy to make my own scraper!
