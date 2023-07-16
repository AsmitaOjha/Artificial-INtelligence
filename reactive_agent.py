import random
class ReactiveAgent:
    def __init__(self):
        self.position = (0,1)
    def update_position(self,action):
        if action == 'up':
            self.position = (self.position[0],self.position[1]+1)
        elif action =='down':
            self.position = (self.position[0],self.position[1]-1)
        elif action == 'left':
            self.position = (self.position[0] - 1, self.position[1])
        elif action == 'right':
            self.position = (self.position[0] + 1, self.position[1])
    def choose_action(self):
        x,y = self.position
        if x>0 and y>0:
            return 'down' if random.random()< 0.5 else 'left'
        elif x>0 and y==0:
            return 'down'
        elif x==0 and y>0:
            return 'left'
        else:
            return 'right'
#usage example:
agent = ReactiveAgent()
for _ in range(5):
    chosen_action = agent.choose_action()
    print("Chosen action:",chosen_action)
    agent.update_position(chosen_action)
    print("New position:", agent.position)