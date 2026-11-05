Ising_tools
===========

Description of the functions implemented in the module `Ising_tools.py` for simulating the 2D Ising model on a honeycomb lattice.

.. py:function:: metropolis(spin_matrix, T)

   Executes a single step of the Metropolis algorithm for the 2D Ising model on a honeycomb lattice.

   :param spin_matrix: bidimensional matrix representing the spin grid (+1 or -1).
   :type spin_matrix: numpy.ndarray
   :param T: Temperature of the system in dimensionless units.
   :type T: float
   :returns: The new configuration of the spin matrix after the flip attempt.
   :rtype: numpy.ndarray
   :raises ValueError: If the spin matrix contains values different from +1 and -1.

   **Esempio di utilizzo:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import metropolis

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Esecuzione dello step a temperatura T=2.26
      nuovo_stato = metropolis(spin_grid, T=2.26)