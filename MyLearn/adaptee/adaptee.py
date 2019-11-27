class MappingAdapter:
    def __init__(self, adapter):
        self.adapter = adapter
        self.lights = []
        self.obstacles = []

    def lighten(self, grid):
        self.adapter.set_dim((len(grid[0]), len(grid)))
        self.lights = [(i2, i1) for i1, e1 in enumerate(grid) for i2, e2 in enumerate(e1) if e2 == 1]
        self.obstacles = [(i2, i1) for i1, e1 in enumerate(grid) for i2, e2 in enumerate(e1) if e2 == -1]
        self.adapter.set_lights(self.lights)
        self.adapter.set_obstacles(self.obstacles)
        return self.adapter.generate_lights()



