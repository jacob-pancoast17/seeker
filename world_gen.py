import arcade
import constants as c
from hostile_object import Hostile
from noise import pnoise1
import numpy as np
from obstacle_object import Obstacle
import random

class WorldGen():
    def __init__(self):
        self.num_rows = 15
        self.seed = random.random() * 1000

        self.rows = np.zeros(self.num_rows)
        self.generate_array()

    def generate_array(self):
        self.rows[0] = 0
        self.rows[1] = 0
        self.rows[2] = 0
        for i in range(self.num_rows - 3):
            x = self.seed + i * .3
            noise = pnoise1(x)
            if (noise > -1 and
                noise < -0.1):
                self.rows[i + 3] = -1
            elif (noise > -0.1 and
                noise < 0.1):
                self.rows[i + 3] = 0
            elif (noise > 0.1 and
                noise < 1):
                self.rows[i + 3] = 1
            else:
                print("ERROR GENERATING ARRAY IN WORLD_GEN.PY")
                exit()

    def generate_row(self, row):
        if self.rows[row] == -1:
            return self.generate_cars(row)
        elif self.rows[row] == 0:
            return self.generate_grassy(row)
        elif self.rows[row] == 1:
            return self.generate_river(row)
        else:
            print("PROBLEM IN GENERATION.")
            exit()
    
    def generate_cars(self, row):
        pass

    def generate_grassy(self, row):
        grass = np.random.normal(loc = 0, scale = 1.1, size = c.COLUMN_COUNT)
        grass = np.sort(grass)

        sprites = arcade.SpriteList()

        # FOR TESTING PURPOSES
        # spawn_list = []

        for i in range(c.COLUMN_COUNT):
            if (grass[i] < -1 or
                grass[i] > 1):
                # Spawn border trees
                sprites.append(Obstacle(c.TILE_SIZE, i, row, arcade.csscolor.DARK_GREEN).to_sprite())

                #spawn_list.append("TREE")
            else:
                # outcomes = ["THING", "     "]
                # weights = [40, 60]
                # spawn_list.append(random.choices(outcomes, weights=weights))

                if random.random() < .3:
                    sprites.append(Obstacle(c.TILE_SIZE, i, row, arcade.csscolor.DARK_GRAY).to_sprite())
        
        # print(grass)
        # print(spawn_list)
        # print(sprites)
        return sprites

    def generate_river(self, row):
        pass
        

gen = WorldGen()
gen.generate_row(0)