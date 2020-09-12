import sys
import heapq


class Puzzle:
    
    LENGTH = 3
    goal_state = [1,2,3,4,5,6,7,8,0]
        
    def __init__(self, state, depth = 0, cost_type = None):
        self.state = state
        self.depth = depth
        self.expansion_order = 0
        if cost_type:
            self.set_cost(cost_type)
        else:
            self.cost = None
            
        
            
    def __str__(self):
        string = ''
        string = string + '+---+---+---+\n'
        for i in range(3):
            for j in range(3):
                tile = self.state[i * 3 + j]
                string = string + '| {} '.format(' ' if tile == 0 else tile)
            string = string + '|\n' + '+---+---+---+\n'
        
        string = string +  '|     {}     |\n'.format('-' if self.expansion_order == 0 else self.expansion_order) + '+-----------+\n'
        string = string + f'|  {self.depth}  |  {self.cost}  |\n' + '+-----------+\n'
        return string
    
        
    """ Função que troca uma peça de lugar com a outra"""
    @staticmethod    
    def swap(state, piece1, piece2):
        state[piece1], state[piece2] = state[piece2], state[piece1]
        return state
      

    """ Função que verifica quantas peças estão fora do lugar """
    @staticmethod
    def out_of_place(state):
        out = 0
        for x in state:
            if state[x] != 0 and state[x]!= Puzzle.goal_state[x]:
                out = out +1
        return out
    
    @staticmethod
    def manhattam_distance(state):
        return sum(abs(b%3 - g%3) + abs(b//3 - g//3)
            for b, g in ((state.index(i), Puzzle.goal_state.index(i)) for i in range(1, 9)))
    
    """ Funções que verificam para qual direção é possível mover o espaço vazio """                  
    def can_up(self):
        return self.state.index(0) >= Puzzle.LENGTH
    
    def can_down(self):
        return self.state.index(0) < Puzzle.LENGTH * (Puzzle.LENGTH - 1)
    
    def can_left(self):
        return self.state.index(0) % Puzzle.LENGTH != 0
    
    def can_right(self):
        return (self.state.index(0) + 1) % Puzzle.LENGTH != 0
    
    
    """ Funções que movem o espaço vazio """
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
    
    
    """ Função para definir um estado meta diferente do padrão """    
    def set_goal_state(self, goal):
        if len(goal) == Puzzle.LENGTH * Puzzle.LENGTH:
            Puzzle.goal_state = goal
            return True
        else:
            sys.exit("Error: Not valid state")
            
    def set_cost(self, cost_type):
        if cost_type == "manhattam":
            self.cost = self.manhattam_distance(self.state) + self.depth
        elif cost_type == "outplace":
            self.cost = self.out_of_place(self.state) + self.depth
        else:
            print("Err: Heurística desconhecida")
            sys.exit(1)
        
        
            
            
    """ Função que espande um estado, e retorna todos os estados possíveis numa lista ordenada por custo """        
    def expand(self,board = None,level_depth = 0, cost_type = None ):
        
        if not board:
            board = self
                    
        expansions_list = []
        
        if board.can_up():
            expansions_list.append(Puzzle(board.move_up(),level_depth, cost_type))
            
        if board.can_down():
            expansions_list.append(Puzzle(board.move_down(),level_depth, cost_type))
            
        if board.can_left():
            expansions_list.append(Puzzle(board.move_left(),level_depth, cost_type))
            
        if board.can_right():
            expansions_list.append(Puzzle(board.move_right(),level_depth, cost_type))
            
        expansions_list.sort(key=lambda x: x.cost, reverse=True)
            
        return expansions_list
    
    
    """ Função que resolve o puzzle """
    def solve(self, cost_type):
        
        results = []
        depth = 0
        
        self.depth = depth  
        self.expansion_order = 1
        self.set_cost(cost_type)
        
        stack = []        
        stack.append(self)        
        
        while stack:
            
            depth += 1
            actual_board = stack.pop()
            
            expansions = actual_board.expand(level_depth=depth, cost_type = cost_type)
            
            results.append((actual_board, expansions.copy()))
            
            min_cost_puzzle = expansions.pop()
            
            draw_list = []            
            for board in expansions:
                if board.cost == min_cost_puzzle.cost:
                    draw_list.append(board)
            
            if draw_list:
                draw_list.append(min_cost_puzzle)
                for board in draw_list:
                    temp = (board.expand(level_depth=depth)).pop()
                    if temp.cost < min_cost_puzzle.cost:
                        min_cost_puzzle = temp                
                         
            min_cost_puzzle.expansion_order = depth + 1
            
            if min_cost_puzzle.cost == depth:
                return results
            else:
                stack.append(min_cost_puzzle)
    