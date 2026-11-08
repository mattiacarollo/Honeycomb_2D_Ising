import numpy as np

# METROPOLIS ALGORITHM

def metropolis(spin_matrix, T):
    rand_i = np.random.randint(0, spin_matrix.shape[0])
    rand_j = np.random.randint(0, spin_matrix.shape[1])
    rand_spin = spin_matrix[rand_i, rand_j]     # randomly chosen spin

    L = spin_matrix.shape[0]     # size of the (square) spin matrix
    if rand_j % 2 == 0:     # for rand_j even, the neighbours are (i-1,j) , (i,j+-1)
        neighbors = [spin_matrix[(rand_i - 1) % L, rand_j],
                     spin_matrix[rand_i, (rand_j - 1) % L],
                     spin_matrix[rand_i, (rand_j + 1) % L]]
    else:                   # for rand_j odd, the neighbours are (i+1,j) , (i,j+-1)
        neighbors = [spin_matrix[(rand_i + 1) % L, rand_j],
                     spin_matrix[rand_i, (rand_j - 1) % L],
                     spin_matrix[rand_i, (rand_j + 1) % L]]

    neighbours_sum = sum(neighbors)     # sum of the spins of the neighbours
    dE = 2 * rand_spin * neighbours_sum     # energy difference between the new configuration and the old one

    if rand_spin * neighbours_sum <= 0:     # if the new configuration (with rand_spin flipped) has lower energy, we accept it and flip the spin
        spin_matrix[rand_i, rand_j] *= -1
    elif np.random.rand() < np.exp(-dE / T):  # if the new configuration has higher energy, we accept it with probability exp(-(E'-E)/T)
        spin_matrix[rand_i, rand_j] *= -1

    return spin_matrix