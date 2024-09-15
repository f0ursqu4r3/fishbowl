import pygame as pg


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        assert False, "update not implemented"

    def draw(self, surface):
        assert False, "draw not implemented"


class Inhabitant(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 100
        self.surface = pg.Surface((50, 50))
        self.surface.fill((255, 255, 255))

    def update(self):
        pass

    def draw(self, surface):
        # draw the inhabitant at the correct position
        # bottom center of the surface
        surface.blit(
            self.surface,
            (self.x - self.surface.get_width() / 2, self.y - self.surface.get_height()),
        )


class Object(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self, surface):
        pass
