"""
A world is a collection of entities.
"""


class World:
    def __init__(self):
        # we want this to be as efficient as possible, so we use a list
        # and we sort it by the y-index
        # this allows us to draw the entities in the correct order
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self, surface):
        # sort the entities by y-index
        self.entities.sort(key=lambda x: x.y)
        for entity in self.entities:
            entity.draw(surface)
