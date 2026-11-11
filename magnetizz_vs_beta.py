# LIBRARIES
import Ising_tools
import numpy as np
import matplotlib.pyplot as plt
import time

# MAGNETIZZAZIONE(T) IN PARALLELO

# --- PARAMETRI ---
L = np.array([10], dtype=int)    # lattice sizes
beta = np.arange(0.6,0.7,0.005)
n_simulation = 1000
metropolis_steps = np.zeros(len(L), dtype=int)
for i in range(len(L)):
    metropolis_steps[i] = 100 * (L[i] ** 2)
m_samples = np.zeros((len(L), len(beta)))

t0 = time.time()

# Warm-up della compilazione JIT
spin_warmup = np.random.choice(np.array([-1, 1], dtype=np.int8), size=(L[0], L[0]))
_ = Ising_tools.metropolis_parallel(spin_warmup, beta[0], 1)

# Esecuzione principale
for j in range(len(L)):
    for i in range(len(beta)):
        m_sum = 0
        for _ in range(n_simulation):
            spin_matrix = np.random.choice(np.array([-1, 1], dtype=np.int8), size=(L[j], L[j]))
            Ising_tools.metropolis_parallel(spin_matrix, 1/beta[i], metropolis_steps[j])
            m_sum += np.abs(Ising_tools.magnetization(spin_matrix))
        m_samples[j, i] = m_sum / n_simulation

t1 = time.time()
print(f"Tempo di esecuzione del ciclo: {t1 - t0:.2f} secondi")

# --- Istogramma ---
for j in range(len(L)):
    plt.scatter(beta, m_samples[j, :], label=f'L={L[j]}')
plt.title(f'Magnetizzazione media per spin (in modulo) in funzione della beta')
plt.xlabel('beta')
plt.ylabel('<|m|>')
plt.legend()
plt.show()