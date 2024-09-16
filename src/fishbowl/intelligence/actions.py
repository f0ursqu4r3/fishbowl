"""
Actions for our inhabitants.
"""


class Action:
    def __init__(self, name, preconditions, effects, cost=1):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


eat = Action(
    name="eat", preconditions={"hunger": True}, effects={"hunger": False}, cost=1
)

sleep = Action(
    name="sleep",
    preconditions={"tiredness": True},
    effects={"tiredness": False},
    cost=1,
)

cook = Action(
    name="cook",
    preconditions={"hunger": True, "food": True},
    effects={"hunger": False, "food": False},
    cost=1,
)
