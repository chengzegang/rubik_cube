"""YourUWNetID_Q_Learn.py

Rename this file using your own UWNetID, and rename it where it is imported
in TOH_MDP.py
Implement Q-Learning in this file by completing the implementations
of the functions whose stubs are present.
Add or change code wherever you see #*** ADD OR CHANGE CODE HERE ***

This is part of the UW Intro to AI Starter Code for Reinforcement Learning.

"""

import random

STATES_VISITED = []
ACTIONS = None
UQV_callback = None
Q_VALUES = None
is_valid_goal_state = None
USE_EXPLORATION_FUNCTION = None
INITIAL_STATE = None


def setup(actions, update_q_value_callback, goal_test, use_exp_fn=False):
    """This method is called by the GUI the first time a Q_Learning
    menu item is selected. It may be called again after the user has
    restarted from the File menu.
    Q_VALUES starts out with all Q-values at 0.0 and a separate key
    for each (s, a) pair."""
    global ACTIONS, UQV_callback, Q_VALUES, is_valid_goal_state
    global USE_EXPLORATION_FUNCTION
    ACTIONS = actions
    UQV_callback = update_q_value_callback
    is_valid_goal_state = goal_test
    USE_EXPLORATION_FUNCTION = use_exp_fn


PREVIOUS_STATE = None
LAST_ACTION = None


def set_starting_state(s):
    """This is called by the GUI when a new episode starts.
    Do not change this function."""
    global INITIAL_STATE, PREVIOUS_STATE
    print("In Q_Learn, setting the starting state to " + str(s))
    INITIAL_STATE = s
    PREVIOUS_STATE = s


ALPHA = 0.5
EPSILON = 0.5
GAMMA = 0.9
ETA = 0.1


def set_learning_parameters(alpha, epsilon, gamma, eta):
    """ Called by the system. Do not change this function."""
    global ALPHA, EPSILON, CUSTOM_ALPHA, CUSTOM_EPSILON, GAMMA, ETA
    ALPHA = alpha
    EPSILON = epsilon
    GAMMA = gamma
    ETA = eta


def update_Q_value(previous_state, previous_action, new_value):
    """Whenever your code changes a value in Q_VALUES, it should
    also call this method, so the changes can be reflected in the
    display.
    Do not change this function."""
    UQV_callback(previous_state, previous_action, new_value)


def choose_next_action(s, r):
    """When the GUI or engine calls this, the agent is now in state s,
    and it receives reward r.
    If terminated==True, it's the end of the episode, and this method
    can just return None after you have handled the transition.

    Use this information to update the q-value for the previous state
    and action pair.
    Then the agent needs to choose its action and return that.
    """
    global INITIAL_STATE, PREVIOUS_STATE, LAST_ACTION, ETA
    # Unless s is the initial state, compute a new q-value for the
    # previous state and action.
    some_action = ACTIONS[0]
    if not (s == INITIAL_STATE):
        # Compute your update here.
        # if CUSTOM_ALPHA is True, manage the alpha values over time.
        # Otherwise go with the fixed value.
        some_action = find_policy(s)
        delta = r + GAMMA * compute_Q(s, some_action) - compute_Q(PREVIOUS_STATE, LAST_ACTION)
        f_vector = construct_feature_vector(PREVIOUS_STATE, LAST_ACTION)
        for i in range(1, N_of_features):
            WEIGHT[i] = WEIGHT[i] + ETA * delta * f_vector[i]

    if EPSILON > 0 or CUSTOM_EPSILON:
        p = random.random()
        if p < EPSILON:
            some_action = random.choice(ACTIONS)

    LAST_ACTION = some_action
    PREVIOUS_STATE = s
    return some_action


def compute_Q(s, a):
    f_vector = construct_feature_vector(s, a)
    sum1 = 0
    for i in range(1, N_of_features):
        sum1 = sum1 + f_vector[i] * WEIGHT[i]
    return sum1


def find_policy(s):

    max_v = -99
    action = ACTIONS[0]
    for a in ACTIONS:
        q_value = compute_Q(s, a)
        if q_value > max_v:
            max_v = q_value
            action = a
    return action


WEIGHT = []
N_of_features = 5


def construct_feature_vector(s, a):
    l = []
    sp = a.apply(s)
    # number of lines of three same color bases:
    f0 = 1
    l.append(f0)
    f1 = 0
    for i in range(6):
        if sp.c[i][0][0] == sp.c[i][0][1] == sp.c[i][0][2]:
            f1 = f1 + 1

        if sp.c[i][1][0] == sp.c[i][0][1] == sp.c[i][0][2]:
            f1 = f1 + 1

        if sp.c[i][2][0] == sp.c[i][0][1] == sp.c[i][0][2]:
            f1 = f1 + 1

        if sp.c[i][0][0] == sp.c[i][1][0] == sp.c[i][2][0]:
            f1 = f1 + 1

        if sp.c[i][0][1] == sp.c[i][1][1] == sp.c[i][2][1]:
            f1 = f1 + 1

        if sp.c[i][0][2] == sp.c[i][1][2] == sp.c[i][2][2]:
            f1 = f1 + 1

        if sp.c[i][0][0] == sp.c[i][1][1] == sp.c[i][2][2]:
            f1 = f1 + 1

        if sp.c[i][0][2] == sp.c[i][1][1] == sp.c[i][2][0]:
            f1 = f1 + 1

    l.append(f1)

    # number of 'T' form bases:

    f2 = 0
    for i in range(6):
        if sp.c[i][0][0] == sp.c[i][0][1] == sp.c[i][0][2] == sp.c[i][1][1] == sp.c[i][2][1]:
            f2 = f2 + 1

        if sp.c[i][0][0] == sp.c[i][1][0] == sp.c[i][2][0] == sp.c[i][1][1] == sp.c[i][1][2]:
            f2 = f2 + 1

        if sp.c[i][0][2] == sp.c[i][1][2] == sp.c[i][2][2] == sp.c[i][1][1] == sp.c[i][1][0]:
            f2 = f2 + 1

        if sp.c[i][2][0] == sp.c[i][2][1] == sp.c[i][2][2] == sp.c[i][1][1] == sp.c[i][0][1]:
            f2 = f2 + 1

    l.append(f2)
    # number of 2 * 2 square of same color bases:

    f3 = 0
    for i in range(6):
        if sp.c[i][0][0] == sp.c[i][0][1] == sp.c[i][1][0] == sp.c[i][1][1]:
            f3 = f3 + 1
        if sp.c[i][0][1] == sp.c[i][0][2] == sp.c[i][1][1] == sp.c[i][1][2]:
            f3 = f3 + 1
        if sp.c[i][1][0] == sp.c[i][1][1] == sp.c[i][2][0] == sp.c[i][2][1]:
            f3 = f3 + 1
        if sp.c[i][1][1] == sp.c[i][1][2] == sp.c[i][2][1] == sp.c[i][2][2]:
            f3 = f3 + 1

    l.append(f3)

    # number of 2 * 3
    f4 = 0
    for i in range(6):
        if sp.c[i][0][0] == sp.c[i][0][1] == sp.c[i][0][2] == sp.c[i][1][0] == sp.c[i][1][1] == sp.c[i][1][2]:
            f4 = f4 + 1

        if sp.c[i][0][0] == sp.c[i][0][1] == sp.c[i][1][0] == sp.c[i][1][1] == sp.c[i][2][0] == sp.c[i][2][1]:
            f4 = f4 + 1

        if sp.c[i][1][0] == sp.c[i][1][1] == sp.c[i][1][2] == sp.c[i][2][0] == sp.c[i][2][1] == sp.c[i][2][2]:
            f4 = f4 + 1

        if sp.c[i][0][1] == sp.c[i][0][2] == sp.c[i][1][1] == sp.c[i][1][2] == sp.c[i][2][1] == sp.c[i][2][2]:
            f4 = f4 + 1

    l.append(f4)

    #number of faces of same color
    f5 = 0
    for i in range(6):
        color = sp.c[i][0][0]
        all_same = True
        for j in range(3):
            for k in range(3):
                if not sp.c[i][j][k] == color:
                    all_same = False
        if all_same:
            f5 = f5 + 1

    l.append(f5)


    return l


def initialize_weight_vector():
    global WEIGHT, N_of_features
    for i in range(N_of_features + 1):
        WEIGHT.append(random.random())
