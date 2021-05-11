from random import choice
from copy import deepcopy    


'''''''''
T       D



        P
'''''''''

class Taxi:
    
    def __init__(self):
        self.width = 5
        self.height = 4
        self.taxi = (0, 0)
        self.PASS = (4, 3)
        self.passenger = self.PASS
        self.destination = (4, 0)
        self.fuel = 30
        
    def __str__(self):
        s = ''
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.taxi:
                    s += 'T'
                elif (x, y) == self.passenger:
                    s += 'P'
                elif (x, y) == self.destination:
                    s += 'D'
                else:
                    s += '-'
            s += '\n'
        return s

    def actions(self):
        actions = []
        tx, ty = self.taxi
        if tx > 0:
            actions.append('w')
        if ty > 0:
            actions.append('n')
        if tx < self.width - 1:
            actions.append('e')
        if ty < self.height - 1:
            actions.append('s')
        if self.taxi == self.passenger:
            actions.append('p')
        return actions
            
    def do(self, a):
        tx, ty = self.taxi
        if a == 'n':
            ty -= 1
        if a == 's':
            ty += 1
        if a == 'w':
            tx -= 1
        if a == 'e':
            tx += 1
        if a == 'p':
            self.passenger = 'intaxi'
        self.taxi = (tx, ty)
        self.fuel -= 1
    
    def terminal(self):        
        if self.passenger == 'intaxi' and self.taxi == self.destination:
            return True
        if self.fuel <= 0:
            return True
        return False

    def reward(self):
        if self.passenger == 'intaxi' and self.taxi == self.destination:
            return 1.0
        return 0.0
        
    def state(self): # 20 x 2 x 30
        return (self.taxi, self.passenger, self.fuel)

def random_rollout(taxi):
    while not taxi.terminal():
        a = choice(taxi.actions())
        taxi.do(a)
    return taxi.reward()

def best_action(taxi):
    action_values = {}
    for a in taxi.actions():
        v = 0
        for i in range(300):
            taxi_copy = deepcopy(taxi)
            taxi_copy.do(a)
            v += random_rollout(taxi_copy)
        action_values[a] = v
    print(action_values)
    return max(action_values, key=lambda a:action_values[a])

if __name__ == '__main__':
    taxi = Taxi()
    cnt = 0
    while not taxi.terminal():
        print(taxi)
        a = best_action(taxi)
        taxi.do(a)
        cnt += 1
    
    print(taxi, taxi.fuel, 'cnt', cnt)                

    '''
    taxi.taxi = (3,3)
    v = 0
    for i in range(1000):
        taxi_copy = deepcopy(taxi)
        v += random_rollout(taxi_copy)
    
    print(v)
    '''
    
    '''
    while not taxi.terminal():
        print(taxi)
        a = choice(taxi.actions())
        taxi.do(a)
    
    print(taxi, taxi.fuel)                
    '''        
