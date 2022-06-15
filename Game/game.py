"""
Author: Anastasia Yazvinskaya
Class: CSE 310-04 (Spring 2022)
Assignment: Module #1
"""

from planet import *

# These are Global constants to use throughout the game
# Planet's distances form Sun (km) - will be scaled
MERCURY_DIST = 57900000
VENUS_DIST = 108200000
EARTH_DIST =  149600000
MARS_DIST = 227900000
JUPITER_DIST = 778600000
SATURN_DIST = 1433500000
URANUS_DIST = 2872500000
NEPTUNE_DIST = 4495100000
# Constants for ship
SHIP_TURN_AMOUNT = 3
SHIP_SPEED = 5
# Planet's images for mini games
MERCURY = []
VENUS = []
EARTH = ["Game/images/earth/earthBG.png", "Game/images/earth/rock.png", "Game/images/earth/bush.png", "Game/images/earth/water.png"]
MARS = ["Game/images/mars/marsBG.png", "Game/images/mars/rock.png", "Game/images/mars/crater.png", "Game/images/mars/pit.png"]
JUPITER = []
SATURN = ["Game/images/saturn/saturnBG.png", "Game/images/saturn/bigRock.png", "Game/images/saturn/smallRocks.png", "Game/images/saturn/mediumRock.png"]
URANUS = ["Game/images/uranus/uranusBG.png", "Game/images/uranus/bigRock.png", "Game/images/uranus/smallRocks.png", "Game/images/uranus/mediumRock.png"]
NEPTUNE = []

class Ship(MoovingObjects):
    """
    This class describes all the characteristics and capabilities of the ship in the space.
    """
    def __init__(self):
        """
        Basic stat initialization
        """
        super().__init__() # Copy characteristics from the parent class Point(), Velocity()
        self.img = "Game/images/ship.png" # -> the path to the image
        self.center.x = ((200 + EARTH_DIST/3000000 + 35)**2 - (SCREEN_HEIGHT/2 - 200)**2)**(0.5) # -> x-coordinate changed
        self.center.y = 255 # -> y-coordinate changed
        self.angle = 0 # -> angle for image and mooving
        self.radius = 20 # -> radius of the ship for checking of collision
        
    def draw(self):
        """
        Draw an object. (Image)
        """
        texture = arcade.load_texture(self.img) # -> load an image

        arcade.draw_texture_rectangle(self.center.x, self.center.y, # -> draw image with the center at the point with Point() value
                                      30, 50,                       #    width = 30, height = 50
                                      texture, self.angle, 255)     #    draw loaded image with appropriate angle and full transparency.

    def rotate(self, key):
        """
        If the user presses the left or right key, the ship will turn in the corresponding direction and start moving.
        """
        if key == 'l' and ((self.center.x) < SCREEN_WIDTH-30): # if user press left and the object is less than 30 units away from the right border
            self.angle += SHIP_TURN_AMOUNT # -> the angle for image should be increased
            self.velocity.dx = (-1)*math.sin(math.radians(self.angle)) # -> speed for changing x-coordinate calculated
            self.velocity.dy = math.cos(math.radians(0-self.angle)) # -> speed for changing y-coordinate calculated
        if key == 'r' and ((self.center.x) > 30): # if user press right and the object is more than 30 units away from the left border
            self.angle -= SHIP_TURN_AMOUNT # -> the angle for image should be decreased
            self.velocity.dx = (-1)*math.sin(math.radians(self.angle)) # -> speed for changing x-coordinate calculated
            self.velocity.dy = math.cos(math.radians(0-self.angle)) # -> speed for changing y-coordinate calculated

    def move(self, key):
        """
        If the user presses the up key, then the ship should move in the direction corresponding to its angle, if the down key is pressed, the ship will stop.
        """
        if key == 'u' and (((self.center.y) < SCREEN_HEIGHT-30) or ((self.center.y) < 30)): # if user press up and the object is more than 30 units away from the top border and is less than 30 units away from the bottom border
            self.velocity.dx = (-1)*math.sin(math.radians(self.angle))  # -> speed for changing x-coordinate calculated
            self.velocity.dy = math.cos(math.radians(0-self.angle))  # -> speed for changing y-coordinate calculated
        if key == 'd': # if user press down
            self.velocity.dx = 0 # -> moovement by the x-coordinate stoped
            self.velocity.dy = 0 # -> moovement by the y-coordinate stoped

class Planet:
    """
    The class describes the main characteristics of the planet and draws it.
    """
    def __init__(self, id, name, p_dist, Y, radius):
        """
        Basic stat initialization.

        It uses:
        id - Determines the planet we will land on when we stop
        name - Used to make a path to the image and to label the planet
        p_dist - planet distance from the Sun
        Y - y-position on the screen. Using the height of the position of the planet on the screen, its distance from the sun and the x-coordinate are calculated.
        radius - planet radius.
        """
        self.id = id # -> planet id
        self.name = name # -> planet name
        self.p_dist = p_dist # -> planet distance from the Sun
        self.img = "Game/images/"+self.name+".png" # -> the path to the image
        self.radius = radius # -> radius of the planet
        self.center = Point() # -> coordinates of the center
        if self.name != "Sun": # -> for all planets except Sun The x-coordinate will be calculated
            if p_dist/2500000 < 600: # -> for planets whose scaled distance from the sun does not exceed 60, the following formula will be used:
                self.center.x = ((200 + p_dist/3000000 + self.radius)**2 - (SCREEN_HEIGHT/2 - Y)**2)**(0.5) # -> x-coordinate changed according to the planet distance
            else: # -> for planets whose scaled distance from the sun greater than 60, the following formula will be used:
                self.center.x = ((200 + p_dist/8000000 + self.radius)**2 - (SCREEN_HEIGHT/2 - Y)**2)**(0.5) # -> x-coordinate changed according to the planet distance
        else:
            self.center.x = -300 # -> x-coordinate for Sun
        self.center.y = Y # -> y-coordinate changed to the default

    def draw(self):
        """
        Draw an object. (Image with text above)
        """
        texture = arcade.load_texture(self.img) # -> load an image

        arcade.draw_texture_rectangle(self.center.x, self.center.y, # -> draw image with the center at the point with Point() value
                                      self.radius*2, self.radius*2, #    width and height the same and equal to the doubled radius
                                      texture, 0, 255)              #    draw loaded image with zero angle and full transparency.
        arcade.draw_text(self.name,                                                           # -> draw a text of planet name
                        start_x=self.center.x-20, start_y=(self.center.y - self.radius - 15), #    in this line I determined the coordinates of the beginning of the text
                        font_size=12, color=arcade.color.BEIGE)                               #    font size is 12, and the color of the text is Beige

class SpaceRoom():
    """
    The class describes the main characteristics of the space (main) room and draws it.
    """
    def __init__(self):
        """
        Basic stat initialization.
        """
        self.audio = arcade.load_sound('Game/sounds/GameSound.mp3', False) # -> load an audio for a space (main) room
        self.vol = 0.5 # -> declare a volume value for audio

        self.ship = Ship() # -> ship created

        self.planets = [ # -> planets created [Planet(id, name, dist, Y, radius) - (-1) id tells that you can not play on this planet]
            Planet(-1, "Sun", 0, SCREEN_HEIGHT/2, 400),
            Planet(-1, "Mercury", MERCURY_DIST, 100, 15),
            Planet(-1, "Venus", VENUS_DIST, 400, 20),
            Planet(1, "Earth", EARTH_DIST, 200, 35),
            Planet(2, "Mars", MARS_DIST, 500, 15),
            Planet(-1, "Jupiter", JUPITER_DIST, 450, 60),
            Planet(3, "Saturn", SATURN_DIST, 150, 40),
            Planet(4, "Uranus", URANUS_DIST, 300, 45),
            Planet(-1, "Neptune", NEPTUNE_DIST, 450, 30)
        ]

    def draw(self):
        """
        Draw an object. (All planets and ship)
        """
        for planet in self.planets:
            planet.draw() # -> each planet is drawn
        
        self.ship.draw() # -> the ship is drawn

    def advance(self):
        """
        Change of position of all mooving objects in this room. By this method an object will move through the update() method in the Game class. Next it will be redraw.
        """
        self.ship.advance() # -> ship position changed if needed

    def next_room(self):
        """
        Here it is determined if it is necessary to move to another 
        (planet) room and which one. This is determined by the fact that the 
        ship must be close enough to the planet and make a complete stop. 
        The planet must also be accessible.
        """
        next = -1 # -> this value meen that we can not move to another room
        for planet in self.planets: # Checking every planet
            if self.ship.velocity.dx == 0 and self.ship.velocity.dy == 0: # If the ship is standing
                too_close = self.ship.radius + planet.radius # -> calculate the value at which objects are considered close to each other

                if (abs(self.ship.center.x - planet.center.x) < too_close and abs(self.ship.center.y - planet.center.y) < too_close): # If the difference between x and y coordinates is close enough
                    # Reset the parameters for the ship so that when it returns, it has the correct position (it stood on the planet)
                    self.ship.center.x = planet.center.x # -> x-coordinate corresponds to the x-coordinate of the planet
                    self.ship.center.y = planet.center.y + planet.radius + 20 # -> the y-coordinate is higher than the y-coordinate of the planet by the value of its radius and 20 more units so that it is not too close to the planet.
                    self.ship.angle = 0 # -> The angle is zero to make the planet stand vertically on top of the planet
                    next = planet.id # -> Determine the number of the planet to which we will move
        return next # -> Passing the value where to go

    def check_keys(self, held_keys):
        """
        Key processing. This function checks for keys that are being held down.

        It uses:
        held_keys - The value of the key that was activated
        """
        if arcade.key.LEFT in held_keys: # if user press left
            self.ship.rotate('l') # call the rotate method and turn the ship and start to move

        if arcade.key.RIGHT in held_keys: # if user press right
            self.ship.rotate('r') # call the rotate method and turn the ship and start to move

        if arcade.key.UP in held_keys: # if user press up
            self.ship.move('u') # call the move method and start to move

        if arcade.key.DOWN in held_keys: # if user press down
            self.ship.move('d') # call the move method and stop mooving

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    """
    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK) # -> set the default background for a game

        self.held_keys = set()

        # Create each object
        self.rooms = [SpaceRoom(), # -> the main room
                      PlanetRoom(EARTH), 
                      PlanetRoom(MARS), 
                      PlanetRoom(SATURN), 
                      PlanetRoom(URANUS)] # -> list of availiable rooms
        self.current_room = 0 # -> default (main) room id
        
        self.player = arcade.play_sound(self.rooms[self.current_room].audio, # -> play the room's audio loaded
                                        0.5, -1, True)                       #    volume = 0.5, play at the begging and repeate after ending

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        # Clear the screen to begin drawing
        arcade.start_render()

        # Draw each object
        self.rooms[self.current_room].draw() # Call the draw method of the current room and draw each object in it

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys() # -> Check the pressed keys

        self.rooms[self.current_room].advance() # Call the advance method of the current room and change the position for all mooving objects if needed

        next = self.rooms[self.current_room].next_room() # Detecting a transition to another room

        if next != -1: # if next room id 0 and higher
            arcade.stop_sound(self.player) # stop sound for current room

            self.current_room = next # -> change the current room id
            
            self.player = arcade.play_sound(self.rooms[self.current_room].audio,         # -> play the current (new) room's loaded audio
                                            self.rooms[self.current_room].vol, -1, True) #    set the chosen volume, plat at the begging and repeate if ending

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        self.rooms[self.current_room].check_keys(self.held_keys) # Call the check_keys method for the current room and call the appropriate methods for each key

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        """
        self.held_keys.add(key)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()