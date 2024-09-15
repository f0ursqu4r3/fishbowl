import pygame as pg

from fishbowl.config import config
from fishbowl.entities import Inhabitant
from fishbowl.world import World


class Fishbowl:
    def __init__(self):
        self.screen = pg.display.set_mode(
            (
                int(config.get("display.width")),
                int(config.get("display.height")),
            )
        )
        self.clock = pg.time.Clock()
        self.dt = 0
        self.fps = int(config.get("game.fps"))
        self.show_fps = bool(config.get("debug.show_fps"))
        self.running = True

        self.world = World()
        self.world.add_entity(
            Inhabitant(
                x=self.screen.get_width() // 2,
                y=self.screen.get_height() // 2,
            )
        )

    def run(self):
        while self.running:
            self.dt = self.clock.tick(self.fps)
            self.handle_events()
            self.update()
            self.draw()
            pg.display.flip()
            if self.show_fps:
                pg.display.set_caption(f"FPS: {self.clock.get_fps()}")

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.world.draw(self.screen)
