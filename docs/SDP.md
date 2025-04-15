
# Software Development Plan


## 0. specifications 
ideas and goals of the project

#### Inspirations and Personal Goals
- The goal of this project is to get some practice writing and also to see how these kinds of systems work. 
- I'm drawing inspiration from other turn based games like various games made from RPG maker. Another big part is that I want to include the possibility to create unique builds for the various classes I plan on including. This idea stems from playing league of legends, specifically the arena game mode. I was interested in the way Riot does the scaling for the abilities of the champions and how you could create new ways to play different champions or how you could do certain builds to maximize the scaling potential for some abilities, mathematically correct sett is what comes to mind.

#### System Goals 
- I think the type of system I described above may be out of scope for my own abilities with respect to completing something within a reasonable time.
- With that said the bare minimums for the project I want to do are as follows.
	1. create a simple and effective UI from scratch.
	2. implement a turn system.
	3. multiple abilities or effects for each class.
	4. allow the computer controlled entities their own turns using some game theory to decide which action to take.
	5. Set up builds for classes
	6. Gold or exp system
	7. Items or more abilities 
- we start out getting some user input to select a class and then go to a menu with options, probably kind of like a rogue like with no saves at the moment.
- Maybe give user a party of their own choice 
- If computer AI is set up we might be able to set it up to play the other PCs in the party or just let the user control them.
- After character selection there should be an option to do a fight. After a fight the user is rewarded with something, exp or gold, to improve their character and or party.
- That should be the loop until they exit the game.

## 1. system analysis 
what the project needs to complete the goals

- I’m using pygame to set up the UI and hopefully have a better layout compare to just printing out to console.
- setting up libraries for the character classes and skills
- ive written some of the base systems without considering how pygame will work with this and interact during the loop
- Need to figure out a way to keep track of base line stats of characters should they change during a fight for buffs or debuffs and such.
	- setup nested dictionary for stats. Makes it less complicated but also need to be careful as editing max values like hp will be as easy to edit as current values

## 2. design 
general workflow and design of project

  
- enemies randomly generated 
	- Either completely random with random names and stats
	- Or
	- several enemy types with stats predefined
	- In both cases stats are increased based on enemies defeated.
- abstract classes for character and skill
- Abstract Character class
	- Getter and setter for attributes 
	- Need to write a method to adjust current health for damage or healing
		- Make sure it is capped at the max health and 0
		- Add a check that if the value is zero at the end of the adjustment, they are defeated 

    ```
    Def abstract class():

    Character(self):
        Self.stats = {
            “hp”: {“max”: 500, “current”: 500},
            “PP”: {“max”: 10, “current”: 10},
            }

        def get_all_stats(self):
			return stats						# this is mainly to get the stats to display

		def get_stat(self, stat):
			return stat[stat]       			# returns both current and max values for a stat
		
		def set_current_stat(self, stat, value):
			stats[stat]["current"] = value
			
		def set_max_stat(self, stat, value):
			stats[stat]["max"] = value
    ```

- Skills are objects but in a character object we are keeping two lists. One is of the names of the skills as strings. The second one is a list of the actual skill objects. when a skill is added we grab that string name and run it through the skill registry which then matches it to the object and instantiates it and puts in the second list.
	- having the two lists makes saving the abilities a character has easier and also lets us quickly access the skill names to display when needed.

- I'm going to try quickly going through what I think the whole process of starting and taking the first turn.

- First the user is prompted to choose a character, the corresponding character object is instantiated
	- all characters start with a basic attack active skill and another skill related to their class, these are part of the init of each class. Those skills are then run through the skill loader to create the skill objects for the character to use later.
- user chooses to start a battle
	- a random enemy is generated, enemies will be based on the Character abstract class so the skill loader will be run again for them.
	- user's character and enemy are displayed
		- hp, resource, scaling stats like pp and mp, resistances, accuracy, critical chance and damage.
		- need a UI to separate active, passive skills and inventory
			- in each of those separate sections we can display more information and allow the user to choose to use a active skill, the other two are just to show the user how they work.
		- another section to inspect an enemy, showing more of their stats
		- another section to choose the basic attack of the character that then goes into targetting.
	- if the user choose the active skill section and an ability to use, we then check if the skill targets allies or enemies and display who is targetable.
		- on selection we use the use_skill method in the character passing the string name of the skill and the target
			- it matches the string to an object based on the object's name
			- on a match we then call the skill object's use method and pass the user's character and the target
		- the skill will handle calling the various functions from the combat file
			- we can say that ally targeted abilities always land so no need to check if an skill lands
			- on enemies we get the hit chance based on the user's accuracy minus the target's dodge chance
				- hit chance is capped at 5 and 95 so there is always a chance to hit or miss
				- then we roll a random number between 0 and 100, if the roll is less than or equal to the hit chance we calculated the hit lands otherwise it misses and returns a true or false based ont he result
			- if the skill lands then we calculate the damage the skill does, this part will be specific to each skill.
				- abilities will have their own base damage or value and then a scaling based on a stat or stats
				- maybe a skill has a % health or stat scaling. We get the corresponding stat and multiply it by the scaling value
				- the values are added to the skill's base damage
				- we calculate the enemie's resistance, either physical or magical 
					- this is a percentage, they take 30% reduced physical damage or such
				- we multiply the damage of the skill and the resist percentage giving us a reduced value
				- finally we call combat.damage_target(), we pass the damage and the target
					- in damage_target we are just getting the target's current hp and subtracting the damage value it was passed.
					- we set a cap to prevent negative values of health
					- we then set the current hp of the target, either 0 or a value higher than 0
		- we need to keep track of enemies and user characters. should either side be completely defeated we return to the main menu and add experience or gold to the user's characters.

- character's get more stats based on level. each class will need to have what increases each level, these will be flat values each level

- loading a save we'll only need the string skill lists, the character lvl, class,
	- instanitate a character based on the class
	- figure out what the stat values should be based on the base character class plus the stats based on level
	- skill loader will be run

#### Menu Stuff
- the various screens are going to have to be various states, having different files will make the them more manageable.
- pygame-menu keeps track of menus and the BACK event goes back to whatever the previous menu was
- the actual game loop will have to be different from the menus

## 3. Implementation

 commentary during implementation
Thinking about how the menu and GUI should look like and what information I want to show has been difficult, I'm not great at designing good looking ones. 

It needs to have a way to look at the character and abilities and items.

need to figure out how items are going to work. probably just objects like the skills.

if i try to make it an auto battler then i'd need to multithreading to keep track of attack speeds of the various actors so this is probably out of scope of this project.

I'm working on how the skill objects are going to work and i'm caught in a kind of loop right now, a loop of imports, because i have all the import statements at the top they get run any time the file gets imported, so after a couple hours of hitting my head against the wall, i realized that i'm passing the objects. as long as i only pass the specific object that a method need then it should be fine. I was passing a character object to the use method in a skill and so i had type checking in the arguments so i needed the import before the stub. i removed that type checking and the import statement for character and things running fine because the file doesn't need to know that a method exisits for it to use it.
  

## 4. testing and debugging

 describe tests and the debugging process