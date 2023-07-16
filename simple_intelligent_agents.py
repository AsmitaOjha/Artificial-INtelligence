import random
class RandomAgent:
    def __init__(self, actions):
        self.actions = actions
    def choose_action(self):
        return random.choice(self.actions)
# usage example:
actions = ['up','down','left','right']
agent = RandomAgent(actions)
chosen_action = agent.choose_action()
print("Randomly chosen action:",chosen_action)