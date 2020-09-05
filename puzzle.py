import sys
from copy import deepcopy


class Puzzle:
    
    LENGTH = 3
    
    def __init__(self, state, depth = 0 , cost = 0, expansion_order = None):
        self.state = state
        self.depth = depth
        self.cost = cost
        self.expansion_order = expansion_order
        
    @staticmethod    
    def swap(state, piece1, piece2):
        state[piece1], state[piece2] = state[piece2], state[piece1]
        return state        
        
    def can_up(self):
        return self.state.index(0) >= Puzzle.LENGTH
    
    def can_down(self):
        return self.state.index(0) < Puzzle.LENGTH * (Puzzle.LENGTH - 1)
    
    def can_left(self):
        return self.state.index(0) % Puzzle.LENGTH != 0
    
    def can_right(self):
        return (self.state.index(0) + 1) % Puzzle.LENGTH != 0

    def move_up(self):
        new_state = self.state.copy()
        index = new_state.index(0)
        return self.swap(new_state, index - Puzzle.LENGTH, index)
    
    def move_down(self):
        new_state = self.state.copy()
        index = new_state.index(0)
        return self.swap(new_state, index + Puzzle.LENGTH, index)
    
    def move_left(self):
        new_state = self.state.copy()
        index = new_state.index(0)
        return self.swap(new_state, index - 1, index)
    
    def move_right(self):
        new_state = self.state.copy()
        index = new_state.index(0)
        return self.swap(new_state, index + 1, index)
    
    
# a = [1,2,3,4,0,5,7,8,6]

# p = Puzzle(a)

# if p.can_up():
#     b = p.move_up()
#     print(b)
    
# if p.can_down():
#     b = p.move_down()
#     print(b)
    
# if p.can_left():
#     b = p.move_left()
#     print(b)
    
# if p.can_right():
#     b = p.move_right()
#     print(b)