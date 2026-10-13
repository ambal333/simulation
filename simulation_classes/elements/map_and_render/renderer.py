from simulation_classes.elements.map_and_render.game_map import Map


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
