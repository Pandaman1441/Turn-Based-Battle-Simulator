
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

        Def get current hp(self):
            Return self.stats[“hp”][“current”]

        Def adjust current hp(self, change):
            self.stats[“hp”][“current”] += change
    ```

## 3. Implementation

 commentary during implementation

  

## 4. testing and debugging

 describe tests and the debugging process