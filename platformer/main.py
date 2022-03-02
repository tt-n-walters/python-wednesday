import arcade


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("platformer/PNG/Characters/platformChar_idle.png")
        self.left = 300
        self.bottom = 200
        


class Platformer(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Platformer")
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = Player()

        self.ground_sprites = arcade.SpriteList()
        for i in range(10):
            if i not in range(5, 8):
                ground = Ground()
                ground.bottom = 0
                ground.left = ground.width * i
                self.ground_sprites.append(ground)
        self.player.change_angle = 4

        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.ground_sprites)

    def on_draw(self):
        arcade.start_render()
        # self.player.update()
        self.physics.update()
        self.player.draw()
        self.ground_sprites.draw()

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
