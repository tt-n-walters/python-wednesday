import arcade
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("PNG/Characters/platformChar_idle.png")
        self.left = 300
        self.bottom = 200

        self.direction = "right"
        self.last_texture_change = 0        # When animation was last update
        self.texture_change_rate = 0.2        # How quickly to update animation
        self.texture_index = -1             # Which texture is being displayed

        # Standing still textures
        self.stand_right_texture, self.stand_left_texture = arcade.load_texture_pair("PNG/Characters/platformChar_idle.png")

        # Jumping texture
        self.jump_right_texture, self.jump_left_texture = arcade.load_texture_pair("PNG/Characters/platformChar_jump.png")
        
        # Walking textures
        walk_right_1, walk_left_1 = arcade.load_texture_pair("PNG/Characters/platformChar_walk1.png")
        walk_right_2, walk_left_2 = arcade.load_texture_pair("PNG/Characters/platformChar_walk2.png")

        self.walk_right_textures = [
            walk_right_1,
            walk_right_2
        ]
        self.walk_left_textures = [
            walk_left_1,
            walk_left_2
        ]
        
    # Code for updating everything about the player
    def update_animation(self, is_touching_ground):
        if not is_touching_ground:      # jumping
            if self.direction == "right":
                self.texture = self.jump_right_texture
            elif self.direction == "left":
                self.texture = self.jump_left_texture

        elif self.change_x > 0:       # walking right
            self.direction = "right"
            if time.time() > self.last_texture_change + self.texture_change_rate:       # Check if enough time has passed
                self.last_texture_change = time.time()                                  # Save the current time
                self.texture_index += 1                                                 # Change to the next texture
                if self.texture_index >= len(self.walk_right_textures):                 # When we run out of textures, reset
                    self.texture_index = 0                                              #   back to the first

            self.texture = self.walk_right_textures[self.texture_index]

        elif self.change_x < 0:       # walking left
            self.direction = "left"
            if time.time() > self.last_texture_change + self.texture_change_rate:       # Check if enough time has passed
                self.last_texture_change = time.time()                                  # Save the current time
                self.texture_index += 1                                                 # Change to the next texture
                if self.texture_index >= len(self.walk_left_textures):                # When we run out of textures, reset
                    self.texture_index = 0                                              #   back to the first

            self.texture = self.walk_left_textures[self.texture_index]

        elif self.change_x == 0:      # stopped
            if self.direction == "right":
                self.texture = self.stand_right_texture
            elif self.direction == "left":
                self.texture = self.stand_left_texture

        


class Platformer(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Platformer", resizable=True)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = Player()

        self.map = arcade.load_tilemap("map.tmj")
        self.ground = self.map.sprite_lists["Tile Layer 1"]

        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.ground)

    def on_draw(self):
        arcade.start_render()
        self.ground.draw()
        self.player.draw()
    

    def on_update(self, delta_time):
        self.physics.update()
        if self.player.center_y < -200:
            self.player.left = 300
            self.player.bottom = 200
        self.player.update_animation(self.physics.can_jump())


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.player.change_x = 4
        if symbol == arcade.key.A:
            self.player.change_x = -4
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 4
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = -4
        if symbol == arcade.key.SPACE:
            self.physics.jump(10)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = 0



class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__("platformer/PNG/Tiles/platformPack_tile001.png")


Platformer()
arcade.run()
