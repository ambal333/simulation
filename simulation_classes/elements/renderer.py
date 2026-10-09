from simulation_classes.elements.game_map import Map


class Renderer:
    def __init__(self, game_map: "Map"):
        self.map = game_map

    def visual_map(self):
        for i in range(self.map.height):
            line = ""
            for j in range(self.map.width):
                entity = self.map.get_entity((j, i))
                if entity is not None:
                    symbol = entity.get_symbol()
                    line += f"{symbol}\t"
                else:
                    line += f"-\t"
            print(line)


# grass = Grass((0,0))
# rock = Rock((2,3))
# map_1 = Map(10,10)
# map_1.add_entity(grass)
# map_1.add_entity(rock)
# render = Renderer(map_1)
# render.visual_map()
