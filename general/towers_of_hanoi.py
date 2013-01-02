"""
solution to Towers of Hanoi problem

At the begining - 3 stacks - on one - elements on the stack in ascending order
Rules:
* only one disk can be moved at a time
* each move - taking the upper disk from one of the rods and sliding it onto another 
  rod on top of the other disk that may be presented on that rod
* no disk may be places on top of the smallest disk

2^n -1 moves

Iterative solution:
a) even number of disks:
    * make the legal move between A & B
    * make the legal move between A & C
    * make the legal move between B & C
b) odd bumber of disks:
    * make the legal move between A & C
    * make the legal move betweeb A & B
    * make the legal move between B & C
"""
from time import sleep

class TowerHanoi(object):

    def __init__(self, number_elements):
        ''' initialize game '''
        self.number_elements = number_elements
        self.stack_A = [i for i in xrange(number_elements, 0, -1)]
        self.stack_B = []
        self.stack_C = []
        print self.stack_A

    def __str__(self):
        ''' stacks at each step '''
        result = []
        result.append(str(self.stack_A))
        result.append(str(self.stack_B))
        result.append(str(self.stack_C))
        return "\n".join(result)

    def _make_move(self, stack1, stack2):
        ''' make legal move between two stacks '''
        if len(stack1) < 1:
            element = stack2.pop()
            stack1.append(element)
        elif len(stack2) < 1:
            element = stack1.pop()
            stack2.append(element)
        else:
            if stack1[-1] > stack2[-1]:
                element = stack2.pop()
                stack1.append(element)
            else:
                element = stack1.pop()
                stack2.append(element)
  
    def _pick_move(self, turn):
        ''' pick next move based on turn '''
        # even 
        if self.number_elements % 2 == 0:
            if turn % 3 == 1:
                self._make_move(self.stack_A, self.stack_B)
            elif turn % 3 == 2:
                self._make_move(self.stack_A, self.stack_C)
            else:
                self._make_move(self.stack_B, self.stack_C)
        # odd
        else:
            if turn % 3 == 1:
                self._make_move(self.stack_A, self.stack_C)
            elif turn % 3 == 2:
                self._make_move(self.stack_A, self.stack_B)
            else:
                self._make_move(self.stack_B, self.stack_C)

    def _is_solved(self):
        ''' check if puzzle is solved '''
        if len(self.stack_A) == self.number_elements or\
           len(self.stack_B) == self.number_elements or\
           len(self.stack_C) == self.number_elements:
            return True
        return False

    def solve(self):
        # make first move and than after that check if it is solved
        turn = 1
        self._pick_move(turn)
        print 'towers: '
        print self
        sleep(2)
        while not self._is_solved():
            turn += 1
            self._pick_move(turn)
            print 'towers: '
            print self
            sleep(2)


# even 
towers = TowerHanoi(4)
print towers
towers.solve()

# odd
towers = TowerHanoi(5)
print towers
towers.solve()
