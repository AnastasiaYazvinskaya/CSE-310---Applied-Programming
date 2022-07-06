# Space Adventure Game Overview

This is an imitation of the solar system, where the user can see all the planets included in it. For control, the user is provided with a spaceship, which is standard on the ground and from where it can get to any point in our system. Each planet is a playable area that differs only graphically. To get to the planet you need to make a stop on it, and to leave it you need to pass the level in order to get back on the spaceship and fly away to travel further. All game control is carried out through the keyboard, using the arrow keys and the spacebar to resume the game if you fail to complete the level.

The purpose of this app is educational and entertainment. So people can get acquainted with the composition of the solar system, as well as just play and relax while passing through various levels.

[Space Adventure Game (Demo Video)](https://youtu.be/HnvBXryvVO4)

# Development Environment

The tools that I used to develop software are VSCode and the corresponding extensions for working with the python language. I also actively used Git and its version control system.

This programm was written in Python programming language. The following libraries were also required: arcade (because the program is based on it), math (for calculations of complexly moving objects) and random (for unpredictable sequencing).

# Useful Websites

* [Python Arcade 2.6.15 (How-To Example Code)](https://api.arcade.academy/en/stable/examples)
* [GeeksforGeeks (Python Arcade – Playing Audio file)](https://www.geeksforgeeks.org/python-arcade-playing-audio-file/)

# Future Work

* Play zones for Mercury, Venus, Neptune and Jupiter. (The task is to create images of the background and three types of obstacles for each of the planets)

* Fix the player's jumps. (This should respond to a keystroke once and smoothly rise and then fall)

* Fix boundaries when flying in space. (Either create clear boundaries beyond which the ship cannot fly away, or vice versa, the camera should move when flying around the solar system, for which you need to add more objects to the background)

* Improve play areas on planets so you can collect things or get points for actions.