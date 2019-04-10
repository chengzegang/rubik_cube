import Q_Learn

from RubikCube import *

Compare_QLearn_to_VI = False

ACTIONS = [op for op in OPERATORS]
NOISE = 0
LIVING_REWARD = 0
GAMMA = 0.9
ALPHA = 0.1
EPSILON = 0.1
NEED_Q_LEARN_SETUP = True
QUIET_MODE = False  # Used during long Q-learning runs.

CLOSED = None

ALL_STATES = None
# Q_VALUES = {}
Q_VALUES = {}
POLICY_from_QL = {}

GOLDEN_PATH = []


def is_valid_goal_state(s):
    if goal_test(s): return True
    return False



def R(s):
    '''Rules: Exiting from the correct goal state yields a
    reward of +100.  Exiting from an alternative goal state
    yields a reward of +10.
    The cost of living reward is -0.1.
    '''
    # Handle goal state transitions first...
    if goal_test(s):
        return 1000.0

    r = 0
    for i in range(6):
        all_same = True
        color = s.c[i][0][0]
        for j in range(3):
            for k in range(3):
                if s.c[i][j][k] != color:
                    all_same = False
        if all_same:
            r = r + 10
    return r


LAST_REWARD = None
Agent_state = None
TERMINATED = None


def initialize_episode():
    global LAST_REWARD, TERMINATED, Agent_state
    LAST_REWARD = 0
    Agent_state = ALL_STATES[0]
    TERMINATED = False
    Q_Learn.set_starting_state(Agent_state)


def update_q_value(previous_state, previous_action, new_value):
    Q_VALUES[(previous_state, previous_action)] = new_value


def client():
    print("ALPHA: " + str(ALPHA))
    print("GAMMA: " + str(GAMMA))
    print("EPSILON:" + str(EPSILON))

    global PREVIOUS_STATE
    state = random_initialize()
    PREVIOUS_STATE = state
    Q_Learn.setup(ACTIONS, update_q_value, goal_test, True)
    Q_Learn.set_starting_state(state)
    Q_Learn.set_learning_parameters(0.1, 0.1, 0.9, 0.1)
    Q_Learn.initialize_weight_vector()
    while True:

        print("How many times of tranning iterations?: ")
        times = int(input())
        train(times)
        print("training completed")
        input()


PREVIOUS_STATE = None
LAST_ACTION = None


def train(times):
    global PREVIOUS_STATE, LAST_ACTION
    for i in range(times):
        if i % 10000 == 0:
            print("iteration times: " + str(i))
            for j in range(6):
                for k in range(3):
                    print(PREVIOUS_STATE.c[j][k])
                print()

        if not LAST_ACTION:
            LAST_ACTION = Q_Learn.choose_next_action(PREVIOUS_STATE, 0)
        else:
            sp = LAST_ACTION.apply(PREVIOUS_STATE)
            r = R(PREVIOUS_STATE)
            LAST_ACTION = Q_Learn.choose_next_action(PREVIOUS_STATE, r)
            PREVIOUS_STATE = sp


def one_step():
    global PREVIOUS_STATE, LAST_ACTION
    if not LAST_ACTION:
        LAST_ACTION = Q_Learn.choose_next_action(PREVIOUS_STATE, 0)
    else:
        sp = LAST_ACTION.apply(PREVIOUS_STATE)
        r = R(PREVIOUS_STATE)
        LAST_ACTION = Q_Learn.choose_next_action(PREVIOUS_STATE, r)
        PREVIOUS_STATE = sp


client()
