import numpy as np
from numba import njit

# METROPOLIS ALGORITHM

def metropolis(spin_matrix, T):
    L = spin_matrix.shape[0]     # size of the (square) spin matrix

    rand_i = np.random.randint(0, L)
    rand_j = np.random.randint(0, L)
    rand_spin = spin_matrix[rand_i, rand_j]     # randomly chosen spin

    # Sums the spins of the neighbours
    if rand_j % 2 == 0:     # for rand_j even, the neighbours are (i-1,j) , (i,j+-1)
        neighbours_sum = (spin_matrix[(rand_i - 1) % L, rand_j] +
                     spin_matrix[rand_i, (rand_j - 1) % L] +
                     spin_matrix[rand_i, (rand_j + 1) % L])
    else:                   # for rand_j odd, the neighbours are (i+1,j) , (i,j+-1)
        neighbours_sum = (spin_matrix[(rand_i + 1) % L, rand_j] +
                     spin_matrix[rand_i, (rand_j - 1) % L] +
                     spin_matrix[rand_i, (rand_j + 1) % L])

    dE = 2 * rand_spin * neighbours_sum     # energy difference between the new configuration and the old one

    if rand_spin * neighbours_sum <= 0:     # if the new configuration (with rand_spin flipped) has lower energy, we accept it and flip the spin
        spin_matrix[rand_i, rand_j] *= -1
    elif np.random.rand() < np.exp(-dE / T):  # if the new configuration has higher energy, we accept it with probability exp(-(E'-E)/T)
        spin_matrix[rand_i, rand_j] *= -1

    return spin_matrix

@njit
def metropolis_numba(spin_matrix, T, n_steps):
    L = spin_matrix.shape[0]
    
    for _ in range(n_steps):
        rand_i = np.random.randint(0, L)
        rand_j = np.random.randint(0, L)
        rand_spin = spin_matrix[rand_i, rand_j]

        # Vicini con condizioni al contorno periodiche su griglia quadrata
        if rand_j % 2 == 0:     # for rand_j even, the neighbours are (i-1,j) , (i,j+-1)
                neighbours_sum = (spin_matrix[(rand_i - 1) % L, rand_j] +
                             spin_matrix[rand_i, (rand_j - 1) % L] +
                             spin_matrix[rand_i, (rand_j + 1) % L])
        else:                   # for rand_j odd, the neighbours are (i+1,j) , (i,j+-1)
            neighbours_sum = (spin_matrix[(rand_i + 1) % L, rand_j] +
                            spin_matrix[rand_i, (rand_j - 1) % L] +
                            spin_matrix[rand_i, (rand_j + 1) % L])

        dE = 2 * rand_spin * neighbours_sum

        if dE <= 0 or np.random.rand() < np.exp(-dE / T):
            spin_matrix[rand_i, rand_j] *= -1

    return spin_matrix

# THERMODINAMIC QUANTITIES

# Magnetization per site
def magnetization(spin_matrix):
    return np.sum(spin_matrix) / spin_matrix.shape[0]**2

# Magnetic susceptibility per site
def magnetic_susceptibility(spin_matrix):
    m = magnetization(spin_matrix)
    m2 = np.sum(spin_matrix**2) / spin_matrix.shape[0]**2
    return (m2 - m**2)

# Modified magnetic susceptibility per site (absolute value of the magnetization instead of the magnetization)
def mod_magnetic_susceptibility(spin_matrix):
    abs_m = np.abs(magnetization(spin_matrix))
    m2 = np.sum(spin_matrix**2) / spin_matrix.shape[0]**2
    return (m2 - abs_m**2)

# Binder cumulant
def binder_cumulant(spin_matrix):
    return np.sum(spin_matrix**4) / (3 * np.sum(spin_matrix**2)**2)

# Energy per site
def energy(spin_matrix, J):
    L = spin_matrix.shape[0]     # size of the (square) spin matrix
    
    for i in range(L):
        for j in range(L):
            if j % 2 == 0:     # for rand_j even, the neighbours are (i-1,j) , (i,j+-1)
                neighbours_sum = (spin_matrix[(i - 1) % L, j] +
                            spin_matrix[i, (j - 1) % L] +
                            spin_matrix[i, (j + 1) % L])
            else:              # for j odd, the neighbours are (i+1,j) , (i,j+-1)
                neighbours_sum = (spin_matrix[(i + 1) % L, j] +
                            spin_matrix[i, (j - 1) % L] +
                            spin_matrix[i, (j + 1) % L])

            energy = -J * spin_matrix[i, j] * neighbours_sum