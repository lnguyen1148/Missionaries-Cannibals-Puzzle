from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal
    
    def result(self, state, action):
        new_state = list(state)

        if new_state[2] == True:
            new_state[0] -= action.count('M')
            new_state[1] -= action.count('C')
            new_state[2] = False
        else:
            new_state[0] += action.count('M')
            new_state[1] += action.count('C')
            new_state[2] = True
        
        return tuple(new_state)
    
    def actions(self, state):
        possible_actions = []

        m_left = state[0]
        c_left = state[1]
        m_right = self.M - m_left
        c_right = self.C - c_left

        if state[2] == True:                
            if m_left > c_left and (m_right != 0 or c_right == 1):
                possible_actions.append('M')
            if m_left > c_left + 1 or m_left == 2:
                possible_actions.append('MM')
            if m_left == c_left and m_left > 0:
                possible_actions.append('MC')
            if c_left > 0 and (c_right < m_right or m_right == 0):
                possible_actions.append('C')
            if c_left > 1 and (c_right < m_right or m_right == 0):
                possible_actions.append('CC')

        else:                
            if m_right > c_right and (m_left != 0 or c_left == 1):
                possible_actions.append('M')
            if m_right > c_right + 1 or m_right == 2:
                possible_actions.append('MM')
            if m_right == c_right and m_right > 0:
                possible_actions.append('MC')
            if c_right > 0 and (c_left < m_left or m_left == 0):
                possible_actions.append('C')
            if c_right > 1 and (c_left < m_left or m_left == 0):
                possible_actions.append('CC')

        return possible_actions

if __name__ == '__main__':
    mc = MissCannibals(M=3, C=3)
    print(mc.actions((3, 2, True))) # Test your code as you develop! This should return  ['CC', 'C', 'M']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
