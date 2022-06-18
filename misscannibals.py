from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def result (self, state, action):
        """ Given state, make a new state with the given action.
            Action assumed to be valid."""

        new_state = list(state)

        for letter in action:
            # boat is on the left side
            if new_state[2]:
                if letter == "M":
                    new_state[0] -= 1
                if letter == "C":
                    new_state[1] -= 1
            # boat is on the right side
            else:
                if letter == "M":
                    new_state[0] += 1
                if letter == "C":
                    new_state[1] += 1
            
        return tuple(new_state)


    def actions(self, state):
        """Given state, return a list of all valid actions."""

        valid_actions = []
        m_left = state[0]
        c_left = state[1]
        m_right = self.M - m_left
        c_right = self.C - c_left

        print("ml cl mr cr")
        print(m_left, c_left, m_right, c_right, sep="  ")

        # check for invalid starting state
        # if c_left > m_left or c_right > m_right:
        #     valid_actions.append("invalid state")
        # else: 
            # boat is on the left side
        if state[2]:
            if m_left >= c_left + 2 and m_left >= 2:
                valid_actions.append("MM")
            if m_left >= c_left + 1 and m_left >= 1:
                valid_actions.append("M")
            if (m_right >= c_right + 2 or m_right == 0) and c_left >= 2:
                valid_actions.append("CC")
            if (m_right >= c_right + 1 or m_right == 0) and c_left >= 1:
                valid_actions.append("C")
        # boat is on the right side
        else:
            if (m_right >= c_right + 2 or m_right == 2) and m_right >= 2:
                valid_actions.append("MM")
            if (m_right >= c_right + 1 or m_right == 1) and m_right >= 1:
                valid_actions.append("M")
            if (m_left >= c_left + 2 or m_left == 0) and c_right >= 2:
                valid_actions.append("CC")
            if (m_left >= c_left + 1 or m_left == 0) and c_right >= 1:
                valid_actions.append("C")
            

        return (valid_actions)

if __name__ == '__main__':
    mc = MissCannibals(M=3, C=3)
    # m, c, onLeft
    test_state = (5, 6, True)
    test_action = "MC"

    print()
    print( "Test state:", mc.goal_test(test_state) ) 
    print( "'", test_action, "' : ", mc.result(test_state, test_action), sep="")
    print()
    
    print(mc.actions((3, 2, True)))  # ['CC', 'C', 'M']
    print()
    print(mc.actions((2, 2, False))) # ['M']
    print()
    print(mc.actions((1, 1, False))) # ['MM']

    # path = depth_first_graph_search(mc).solution()
    # print(path)
    # path = breadth_first_graph_search(mc).solution()
    # print(path)
