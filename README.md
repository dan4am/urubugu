# Description.
This repository contains the code for URUBUGU (ikibuguzo, Igisoro): a variant of the [Bao game](https://en.wikipedia.org/wiki/Bao_(game)) that is played in Burundi.
URUBUGU is a two player turn-based board game.

## Structure:
- [Getting started.](https://github.com/dan4am/urubugu/blob/master/README.md#1-getting-started)
   - [Prerequisites.](https://github.com/dan4am/urubugu/blob/master/README.md#a-prerequesites)
   - [Run the code.](https://github.com/dan4am/urubugu/blob/master/README.md#b-run-the-code)
   - [The GUI.](https://github.com/dan4am/urubugu/blob/master/README.md#cthe-gui)
   - [Commands.](https://github.com/dan4am/urubugu/blob/master/README.md#d-commands)
- [Rules.](https://github.com/dan4am/urubugu/blob/master/README.md#2-rules)
   - [Setting up the board.](https://github.com/dan4am/urubugu/blob/master/README.md#a-setting-up-the-board)
   - [Playing.](https://github.com/dan4am/urubugu/blob/master/README.md#b-playing)
   - [Winning](https://github.com/dan4am/urubugu/blob/master/README.md#c-winning)
- [Strategies.](https://github.com/dan4am/urubugu/blob/master/README.md#3-strategies)
   - [defensive strategies.](https://github.com/dan4am/urubugu/blob/master/README.md#a-defensive-strategies)
   - [Offensive strategies.](https://github.com/dan4am/urubugu/blob/master/README.md#b-offensive-strategies)
- [Future work.](https://github.com/dan4am/urubugu/blob/master/README.md#4-future-work)
    - [Online version.](https://github.com/dan4am/urubugu/blob/master/README.md#a-online-version)
    - [AI.](https://github.com/dan4am/urubugu/blob/master/README.md#b-artificial-intelligence-ai)
    - [Research topics.](https://github.com/dan4am/urubugu/blob/master/README.md#c-research-topics)
   
## 1. Getting started 
### a. Prerequesites.
- [python 3.9](https://www.python.org/downloads/)
- [pygame 2.0.1](https://www.pygame.org/wiki/GettingStarted)
- [numpy 1.20.3](https://numpy.org/install/)

 
### b. Run the code.
After downloading and installing python and the necessary libraries, the user have to run the 
following command to play the game:


- On Windows, Unix-like systems and Mac OS:
---
```
python3 main.py 
```

- Exclusively on windows:

---
The user can download the following file "Executable Files/urubugu v1.1.zip" and launch the .exe file in it.

### c.The GUI.
When the code is executed, this pygame window will appear.

![initial state](https://user-images.githubusercontent.com/39918471/129624035-34fb3747-79e3-47bd-ae4b-9260fdb60a7c.png)

On the menu screen, the user can switch between the "versus computer mode" or "player versus player"
mode by clicking on the slider button in the top center of the window. The default setting is "player versus player".

![VS CPU](https://user-images.githubusercontent.com/39918471/129625941-8cf297b1-cb4a-441a-9c24-860aef31c22b.png)

The user can also choose his favorite language by clicking on the flag appearing in the top left corner of the window.
The displayed flag is the current language, by default, the language is English.

![changing language](https://user-images.githubusercontent.com/39918471/129625799-a8a3976c-cb28-4b6d-8698-17864068d3ff.png)

To start a game, the user has to click on the play button.

![start playing](https://user-images.githubusercontent.com/39918471/129625572-ef986605-4545-4bf2-a3c6-42fd73acf5d6.png)

According to the rules of "URUBUGU", the players can set up their board as they wish before the start of the game.
Our version gives the possibility to only one of the players to do so, the other one has to use a default setting.

![setting up board](https://user-images.githubusercontent.com/39918471/129626389-99fa0edf-8b33-4f07-9ca1-dd36a6e2e8c2.png)

### d. Commands.

`d` → change design.

![Skin change](https://user-images.githubusercontent.com/39918471/129630271-e699303c-1487-44fe-a9d8-9c7d46cc36d2.png)

## 2. Rules.
The board is divided in two, each player has half of the board as his base. Players play facing each other.
image board divided in two symmetrical parts.
![empty board](https://user-images.githubusercontent.com/39918471/129637005-c293ba46-0743-47b6-9148-138cfa32ba47.png)

In each players base there are two zones, an active zone and a "cemetery".
The active zone is the zone where a player can capture opponent's beads, in the "cemetery", the player can either go around and come back in the active zone or he might end his turn (more details in the [playing] section.

![player 1 half.](https://user-images.githubusercontent.com/39918471/129637485-63ebdecc-105b-4fc7-a721-e10c479f7e6a.png)

### a. Setting up the board.
At the beginning, each player has 32 beads and each player is free as to the disposition of his beads.
There no prohibited settings.

The default setting is a two-beads-by-cell setting.

![image](https://user-images.githubusercontent.com/39918471/129638535-6863c633-cee8-4808-9363-db7131ab1eaa.png)


### b. Playing.
#### Start of turn:
---
To start a turn, the player takes the beads in any non-empty cell and spreads it's content in the direction of the play (counter-clockwise).


#### Capturing beads:
---

If the last bead falls in the active zone, and if the adjacent cells in the opponent's base there are beads, the player will capture those beads and restart to play from the 
origin of his play.
![capturing 1/2](https://user-images.githubusercontent.com/39918471/129642497-4d5f8238-af46-4819-8c3a-820acdad35b3.png)
![capturing 2/2](https://user-images.githubusercontent.com/39918471/129642561-0138541d-5a52-41b4-bf4e-b23b88e94987.png)

If the adjacent cells in the opponent's base are empty, then the player will take the beads of that cell (if the cell was not empty) and spread it's content in the direction of the play (counter-clockwise) until the end of his turn.

![Adjacent empty 1/2](https://user-images.githubusercontent.com/39918471/129643110-bad6834b-d622-4cf0-8354-41a1ad2a254b.png)
![adjacent empty 2/2](https://user-images.githubusercontent.com/39918471/129643151-ff7ae1b1-4327-492e-a723-1183c8ba9a97.png)


#### End of turn :
---
A turn is ended in two cases:
1. When the last bead of a play falls into an empty cell in the cemetery.
 ![end turn 1](https://user-images.githubusercontent.com/39918471/129640197-36219d29-1824-46ed-b1c7-a15ec8f042f6.png)
2. When the last bead of a play falls into an empty cell in the active zone and the adjacent cells in the opponent's base are also empty.
![end turn 2](https://user-images.githubusercontent.com/39918471/129640690-b2760140-5cf8-4381-a966-06305a5f9133.png)

### c. Winning.

TO win, a player must capture all the beads from the opponent, in other world, a player wins, iff all 64 beads are in his base.
![image](https://user-images.githubusercontent.com/39918471/129643735-a0f1cb1f-1d8a-4ccb-9e1d-6006f6c7da6b.png)


## 3. Strategies.
In this section, we give two strategies (among a plethora of other strategies) to give a gist of what can be done in this game.

### a. Defensive strategies.
#### a.1. Spreading.
Spreading is a strategy where the player spreads the content of one cell, so as to fill the most cells. That strategy gives more chances to the player to capture ennemy's beads in two turns.

![spreading 1](https://user-images.githubusercontent.com/39918471/129629986-5cbbb5b5-e62d-47c3-9935-5e114c9f6b16.png)
![Spreading 2](https://user-images.githubusercontent.com/39918471/129630032-4cb6941b-5751-44c2-8baa-b12b975896d4.png)




### b. Offensive strategies.
##### b.1. Decapitation.

The decapitation's main objective is to prohibit the opponent to captuure any of our beads in his turn.
The player will capture the beads from the left corner of the opponents board (the head) .
 
![decapitation](https://user-images.githubusercontent.com/39918471/129628783-69781ef8-8c6e-4f75-871a-7cbd2522b80e.png)


## 4. Future work.

### a. Online version.
The online version of this game is in developpement, a first step has been reached: players can play against one another on a local network, the next step is to launch it over the internet for players to interact from all over the world. But a deployment on internet comes with financial costs, that is why it has been put on hold for now.
### b. Artificial Intelligence (AI).
One of the next steps of this project is to develop an artificial intelligence model capable of playing against a player.
This AI would also facilitate simulations in the context of research.
### c. Research questions.
This game has many opportunities to explore in terms of research, the intuitive questions are:
> " Is there a counter setting for each setting?"
> 
> " If there is a counter-setting, how can we compute it?"

But there are also some non-trivial questions like:
> " How initial settings influence the game? "

In Conclusion, there are many avenues to be explored in this game.

---
We define by counter-setting a setting that insures a "one-play-win" ("IMPAGA") to the player who starts.
