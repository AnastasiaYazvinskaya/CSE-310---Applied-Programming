"""
Author: Anastasia Yazvinskaya
Class: CSE 310-04 (Spring 2022)
Assignment: Module #1
"""

import arcade # -> import arcade library (the program based on it)
import math # -> import math library (for calculations of complexly moving objects)
import random # -> for unpredictable sequencing

# These are Global constants to use throughout the game
# Screen parameters
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
# Runner parameters
RUN_SPEED = 5

class Point:
    """
    This class is a coordinates of a central point of objects
    """
    def __init__(self):
        """
        Basic stat initialization.
        By default, the object is located at a point with coordinates (0,0)
        """
        self.x = 0 # -> x-coordinate (horizontal)
        self.y = 0 # -> y-coordinate (vertical)

class Velocity:
    """
    This class tells how the coordinates will change while moving.
    (It is necessary for moving elements. For example: a ship, player)
    """
    def __init__(self):
        """
        Basic stat initialization.
        By default, the coordinates do not change, so the coefficients are specified as 0.
        """
        self.dx = 0 # -> horizontal movement (x-coordinate)
        self.dy = 0 # -> vertical movement (y-coordinate)

class MoovingObjects:
    """
    This class describes all general characteristics and capabilities of the mooving objects.
    """
    def __init__(self):
        """
        Basic stat initialization
        """
        self.center = Point() # -> coordinates of the center
        self.velocity = Velocity() # -> values for changing coordinates
        self.speed = 1 # -> speed if needed (will be used for player)

    def advance(self):
        """
        Change of position. By this method an object will move through the update() method in the Game class. Next it will be redraw.
        By default, the object does not move.
        """
        self.center.x += self.velocity.dx # -> change the x-center position
        self.center.y += self.velocity.dy # -> change the y-center position

class Player(MoovingObjects):
    """
    This class describes all the characteristics and capabilities of the player.
    """
    def __init__(self):
        """
        Basic stat initialization
        """
        super().__init__() # Copy characteristics from the parent class Point(), Velocity() and speed
        self.center.x = 143 # -> x-coordinate changed
        self.center.y = 250 # -> y-coordinate changed
        self.img = "Game/images/player.png" # -> the path to the image
        self.radius = 72.5 # -> radius of the player for checking of collision
        self.alive = True # -> The life of the player, if he loses a life, then you will need to start the game again
    
    def advance(self):
        """
        Change of position. By this method an object will move through the update() method in the Game class. Next it will be redraw.
        By default, the object does not move.
        """
        super().advance() # Copy mooving capabilities from the parent class
        if self.velocity.dx > 0: # if player moves right
            self.img = "Game/images/playerRunRight.png" # -> change img for player running right
        elif self.velocity.dx < 0: # if player moves right
            self.img = "Game/images/playerRunLeft.png" # -> change img for player running left
        else: # in all other situations
            self.img = "Game/images/player.png" # -> standart img
        self.velocity.dx = 0 # -> stop mooving (right and left)
        if self.center.y > 250: # if player jump (under the ground)
            self.velocity.dy = -1 * RUN_SPEED # -> slowly down
        else: # when player on the ground
            self.velocity.dy = 0 # stop mooving (up and down)
        
    def draw(self):
        """
        Draw an object. (Image)
        """
        texture = arcade.load_texture(self.img) # -> load an image

        arcade.draw_texture_rectangle(self.center.x, self.center.y,  # -> draw image with the center at the point with Point() value
                                      texture.width, texture.height, #    width = image width, height = image height
                                      texture, 0, 255)               #    draw loaded image with zero angle and full transparency.

    def move(self, key):
        """
        If the user presses the left key, then the player should run left, if the right key is pressed, the player will run right, if the upper key is presse the player will jump.
        """
        if key == 'l' and ((self.center.x) > SCREEN_WIDTH/7): # if user press left and the object is more than seventh of the screen width from the left border
            self.velocity.dx = -1 * RUN_SPEED # -> run left
        if key == 'r' and ((self.center.x) < SCREEN_WIDTH*6/7): # if user press right and the object is less than six sevenths of the screen width from the right border
            self.velocity.dx = RUN_SPEED # -> run right
        if key == "u" and ((self.center.y) < SCREEN_HEIGHT*2/3): # if user press up and the object is less than two thirds of the screen height from the top border
            self.velocity.dy = RUN_SPEED # -> jump

class Barrier(MoovingObjects):
    """
    The class describes the main characteristics of the barriers on the planet and draws it.
    """
    def __init__(self, i, type, planet_imgs):
        """
        Basic stat initialization.

        It uses:
        i - index of the barrier in the list
        type - type of the barrier (there are 3 types)
        planet_imgs - the list of 3 barriers for each planet
        """
        super().__init__() # Copy characteristics from the parent class Point(), Velocity() and speed
        self.img = planet_imgs # -> the list with paths to the images
        self.type = type # -> type of barrier
        self.center.x = SCREEN_WIDTH + (i+1)*700 # -> x-coordinate changed according to the planet distance
        self.center.y = 200 # -> y-coordinate changed to the default
        self.velocity.dx = -5 # -> movement value for x-coordinate is constant
        self.radius = 47.5 # -> radius of the barrier for checking of collision

    def draw(self):
        """
        Draw an object. (Image)
        """
        texture = arcade.load_texture(self.img[self.type]) # -> load an image from the list

        arcade.draw_texture_rectangle(self.center.x, self.center.y,  # -> draw image with the center at the point with Point() value
                                      texture.width, texture.height, #    width = image width, height = image height
                                      texture, 0, 255)               #    draw loaded image with zero angle and full transparency.

class PlanetShip(MoovingObjects):
    """
    The class describes the main characteristics of the Ship on the planet and draws it.
    """
    def __init__(self, barrriersNum):
        """
        Basic stat initialization.

        It uses:
        barrierNum - for calculating the starting x-coordinate
        """
        super().__init__()  # Copy characteristics from the parent class Point(), Velocity()
        self.img = "Game/images/ship.png" # -> the path to the image
        self.center.x = SCREEN_WIDTH + (barrriersNum + 1)*700 # -> x-coordinate changed according to the planet distance
        self.center.y = 300 # -> y-coordinate changed to the default
        self.velocity.dx = -5  # -> movement value for x-coordinate is constant
        self.radius = 0 # -> radius of the ship for checking of collision

    def draw(self):
        """
        Draw an object. (Image)
        """
        texture = arcade.load_texture(self.img) # -> load an image

        arcade.draw_texture_rectangle(self.center.x, self.center.y,  # -> draw image with the center at the point with Point() value
                                      texture.width, texture.height, #    width = image width, height = image height
                                      texture, 0, 255)               #    draw loaded image with appropriate angle and full transparency.
    
    def advance(self):
        """
        Rewrite.
        Change of position. By this method an object will move through the update() method in the Game class. Next it will be redraw.
        By default, the object does not move.
        """
        if self.center.x > SCREEN_WIDTH*5/6: # if the object is more than five sixths of the screen width from the right border
            self.center.x += self.velocity.dx # -> change the x-center position
        if self.center.y < SCREEN_HEIGHT + 150: # if the object is less than 150 units from the top border
            self.center.y += self.velocity.dy # -> change the y-center position

class PlanetRoom:
    """
    The class describes the main characteristics of the planet room and draws it.
    """
    def __init__(self, planet):
        """
        Basic stat initialization.

        It uses:
        planet - list of the images for planet (background and 3 barriers)
        """
        self.end_game = False # -> is the game ended (default false)
        self.audio = arcade.load_sound('Game/sounds/PlanetSound.mp3', False) # -> load audio for planet room
        self.vol = 0.2 # -> set the value for volume of the audio

        self.planet = planet # -> save list of images
        self.bg = self.planet[0] # -> backgrount is the first (0-index) item in the list
        self.player = Player() # -> player created

        self.barriers = [] # -> list for barriers created
        barriersNum = random.randint(1, 3) # -> random number of barriers
        for i in range(barriersNum): # populate the list with objects
            self.barriers.append(Barrier(i, random.randint(0, 2), self.planet[1:4]))
        
        self.ship = PlanetShip(barriersNum) # -> ship created

    def draw(self):
        """
        Draw an object. (Player, background, barriers and ship)
        """
        # Draw each object
        # draw the background
        texture = arcade.load_texture(self.bg) # -> load an image for background
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, # -> draw image with the center at the point with Point() value
                                      texture.width, texture.height,   #    width = image width, height = image height
                                      texture, 0, 255)                 #    draw loaded image with zero angle and full transparency.

        if self.player.alive and not self.end_game: # if player is alive and game is not ended
            self.player.draw() # -> the player is drawn

            for barrier in self.barriers:
                barrier.draw() # -> all barriers are drawn
        elif not self.end_game: # if player die (game do not ended)
            arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 # -> draw a rectangle with the center at the center of the screen
                                        ,400, 50                         # width = 400, height = 50
                                        ,arcade.color.BEIGE, 0)          # color Beige with zero angle
            arcade.draw_text("Press Space for Restart",                 # -> draw a text
                            start_x=320, start_y=287.5,                 #    which will start at the point (320, 287.5)
                            font_size=25, color=arcade.color.NAVY_BLUE) # font size 25, color Navy Blue

        self.ship.draw() # -> ship is drawn

    def advance(self):
        """
        Change of position of all mooving objects in this room. By this method an object will move through the update() method in the Game class. Next it will be redraw.
        """
        if self.player.alive and not self.end_game: # if player is alive and game is not ended
            self.player.advance()  # -> player position changed if needed
                
            for barrier in self.barriers:
                barrier.advance()  # -> barrier position changed if needed

            self.check_collision() # -> if player will be close anough to barrier player will die

        self.ship.advance() # -> ship position changed if needed

    def check_collision(self):
        """
        If player is close enough to barrier player should die.
        If player is close enough to ship player shoul fly away.
        """
        for barrier in self.barriers: # Checking all barriers
            if self.player.alive: # if player alive
                too_close = self.player.radius + barrier.radius # -> Calculate the closiness with barrier

                if (abs(self.player.center.x - barrier.center.x) < too_close and abs(self.player.center.y - barrier.center.y) < too_close): # Check if the playe and barrier are close to each other 
                    self.player.alive = False # -> player die

        if self.player.alive: # if player alive
            too_close = self.player.radius + self.ship.radius # -> Calculate the closiness with ship

            if (abs(self.player.center.x - self.ship.center.x) < too_close): # if player and ship are close anough to each other
                    self.ship.velocity.dy = 10 # -> ship goes up
                    self.end_game = True # -> game ended
    
    def next_room(self):
        """
        Here it is determined if it is necessary to move to another 
        (space) room. This is determined by the fact that the 
        player must be close enough to the ship.
        The ship shoud go out of the screen.
        """
        next = -1 # -> this value meen that we can not move to another room
        if self.ship.center.y > SCREEN_HEIGHT + 140: # if ship go ot of the screen
            self.restart() # Call the restart method. So we can play again if will return to this planet
            next = 0 # the index of the next (space-main) room
        return next # -> Passing the value where to go

    def restart(self):
        """
        Reset the parameters for the room so that when it returns, it has the correct position
        """
        self.end_game = False # -> is the game ended (default false)
        self.player = Player() # -> player created

        self.barriers = [] # -> list for barriers created
        barriersNum = random.randint(1, 3) # -> random number of barriers
        for i in range(barriersNum): # populate the list with objects
            self.barriers.append(Barrier(i, random.randint(0, 2), self.planet[1:4]))
        
        self.ship = PlanetShip(barriersNum) # -> ship created

    def check_keys(self, held_keys):
        """
        Key processing. This function checks for keys that are being held down.

        It uses:
        held_keys - The value of the key that was activated
        """
        if arcade.key.LEFT in held_keys: # if user press left
            self.player.move('l') # call the move method and start to move left

        if arcade.key.RIGHT in held_keys: # if user press right
            self.player.move('r') # call the move method and start to move right

        if arcade.key.UP in held_keys: # if user press up
            self.player.move('u') # call the move method and start to move up (jump)

        if arcade.key.SPACE in held_keys: # if user press space
            if not self.player.alive: # if player die
                self.restart() # Call the restart and start the game again
