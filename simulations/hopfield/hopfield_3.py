import numpy as np
import matplotlib.pyplot as plt

def compute_next_state(state, weight):
    """
    This implements the syncrhonous update rule in a Hopfield network:
    all the units are updated at the same time in one iteration.

    Parameters
    ----------
    state: array of shape (N,)
        state vector with binary values, coded as +1 or -1
    weight: 2d array of shape (N, N)
        weight matrix where weight[i, j] is the connection weight between
        unit i and unit j (connections are symmetric in a Hopfield network)

    Returns
    -------
    next_state: array of shape (N,)
    """
    # Note: '@' is a shorthand for 'np.matmul()'. Numpy automatically promotes
    # 1D arrays (vectors) into 2D arrays (matrices) before applying the
    # matrix multiplication, turning the right operand (here 'state') into a
    # matrix of shape (N, 1). After applying the matrix multiplication,
    # numpy then perform the inverse transformation to give back a 1D array.
    next_state = np.where(weight @ state >= 0, +1, -1)
    return next_state

def compute_final_state(initial_state, weight, max_iter=1000):
    """
    Returns
    -------
    final_state: array of shape (N,)
    is_stable: bool
        whether the final state is a stable state
    n_iter: int
        number of iterations of compute_next_state performed
    """
    previous_state = initial_state
    next_state = compute_next_state(previous_state, weight)
    is_stable = np.all(previous_state == next_state)
    n_iter = 0
    while (not is_stable) and (n_iter <= max_iter):
        previous_state = next_state
        next_state = compute_next_state(previous_state, weight)
        is_stable = np.all(previous_state == next_state)
        n_iter += 1

    return previous_state, is_stable, n_iter

def weight_to_memorize_states(states):
    """
    Parameters
    ----------
    states: sequence of arrays of shape (N,)
        the states to be memorized
    
    Returns
    -------
    weight: 2d array of shape (N, N)
        the weight matrix that will memorize the given states
    """
    # concatenate into a matrix with each state as one column of this matrix 
    states_matrix = np.column_stack(states)
    # this will compute the sum of the outer products of each column vectors
    # in the matrix, which are the given states
    weight = states_matrix @ states_matrix.T
    # zero out the diagonal (there are no self-recurrent connections in Hopfield
    # networks)
    np.fill_diagonal(weight, 0)
    return weight

def im_from_string(s):
    # extract each line which correspond to one row of the image
    lines = s.strip().split()
    # convert each character into a digit and concatenate them into a 2d array
    digits = [[(1 if c == '1' else -1) for c in line] for line in lines]
    return np.array(digits)

def state_from_im(im):
    return im.reshape((-1,))

def im_from_state(state, width):
    return state.reshape((-1, width))

str_L = """
        1....
        1....
        1....
        1....
        11111
        """

str_P = """
        11111
        1...1
        11111
        1....
        1....
        """

str_S = """
        11111
        1....
        11111
        ....1
        11111
        """

str_X = """
        1...1
        .1.1.
        ..1..
        .1.1.
        1...1
        """

if __name__ == '__main__':

    for s in [str_L, str_P, str_S, str_X]:
        im = im_from_string(s)
        width = im.shape[1]
        print("im", im)
        state = state_from_im(im)
        print("state", state)
        im_back = im_from_state(state, width)
        print("im_back equals im?", np.all(im_back == im))

        plt.imshow(im, cmap='binary')
        plt.show()

