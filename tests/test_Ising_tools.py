import unittest
import numpy as np
import Ising_tools


class TestIsingTools(unittest.TestCase):

    def setUp(self):
        """Prepara la matrice di spin e i parametri iniziali per i test"""

        self.L = 20
        self.T = 2.26
        SEED = 68
        rng = np.random.default_rng(seed=SEED)
        self.spin_matrix = rng.choice([-1, 1], size=(self.L, self.L))

    def test_values_shape_spin_matrix_after_metropolis(self):
        """Verifica che dopo i passi di Metropolis la matrice mantenga sia la forma sia i valori +/-1."""

        grid_copy = self.spin_matrix.copy()     # Copia della matrice per evitare modifiche all'originale
        
        n_steps = self.L * self.L       # in media un tentativo per spin
        for _ in range(n_steps):
            grid_copy = Ising_tools.metropolis(grid_copy, T=2.26)

        # Check dimensions
        self.assertEqual(
            grid_copy.shape, (self.L, self.L),
            f"La dimensione è cambiata! Atteso {(self.L, self.L)}, ottenuto {grid_copy.shape}"
        )

        # Check values
        unique_vals = set(np.unique(grid_copy))
        self.assertTrue(
            unique_vals.issubset({-1, 1}),
            f"Valori non validi riscontrati dopo Metropolis: {unique_vals - {-1, 1}}"
        )