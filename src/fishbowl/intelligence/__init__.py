"""
Intelligence module
We'll use this to handle the AI of our inhabitants using GOAP.
"""

import heapq

from fishbowl.intelligence import actions


class Planner:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def plan(self, world_state, goal_state):
        frontier = [(0, world_state, [])]
        came_from = {}
        cost_so_far = {str(world_state): 0}

        while frontier:
            current_cost, current_state, path = heapq.heappop(frontier)

            if all(item in current_state.items() for item in goal_state.items()):
                return path

            for action in self.actions:
                if all(
                    item in current_state.items()
                    for item in action.preconditions.items()
                ):
                    new_state = dict(current_state)
                    new_state.update(action.effects)
                    new_cost = current_cost + action.cost

                    if (
                        str(new_state) not in cost_so_far
                        or new_cost < cost_so_far[str(new_state)]
                    ):
                        cost_so_far[str(new_state)] = new_cost
                        priority = new_cost + self.heuristic(new_state, goal_state)
                        heapq.heappush(frontier, (priority, new_state, path + [action]))
                        came_from[str(new_state)] = current_state

        return None

    def heuristic(self, state, goal_state):
        return len(set(goal_state.items()) - set(state.items()))


class InhabitantPlanner:
    def __init__(self):
        self.actions = [
            actions.eat,
            actions.sleep,
            actions.cook,
        ]

    def plan(self, world_state, goal_state):
        return self.planner.plan(world_state, goal_state)
