Ising_tools
===========

Description of the functions implemented in the module `Ising_tools.py` for simulating the 2D Ising model on a honeycomb lattice.

.. py:function:: metropolis(spin_matrix, T)

   Executes a single step of the Metropolis algorithm for the 2D Ising model on a honeycomb lattice and updates the spin matrix.

   :param spin_matrix: bidimensional matrix representing the spin grid (+1 or -1).
   :type spin_matrix: numpy.ndarray
   :param T: Temperature of the system in dimensionless units.
   :type T: float
   :returns: The new configuration of the spin matrix after the flip attempt.
   :rtype: numpy.ndarray
   :raises ValueError: If the spin matrix contains values different from +1 and -1.

   **Example:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import metropolis

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Esecuzione dello step a temperatura T=2.26
      nuovo_stato = metropolis(spin_grid, T=2.26)

.. py:function:: magnetization(spin_matrix)

   Computes the magnetization per site of a given spin configuration.

   :param spin_matrix: bidimensional matrix representing the spin grid (+1 or -1).
   :type spin_matrix: numpy.ndarray
   :returns: The magnetization per site of the spin configuration.
   :rtype: float

   **Example:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import magnetization

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Calcolo della magnetizzazione per sito
      m = magnetization(spin_grid)

.. py:function:: magnetic_susceptibility(spin_matrix)

   Computes the magnetic susceptibility per site of a given spin configuration.

   :param spin_matrix: bidimensional matrix representing the spin grid (+1 or -1).
   :type spin_matrix: numpy.ndarray
   :returns: The magnetic susceptibility per site of the spin configuration.
   :rtype: float

   **Example:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import magnetic_susceptibility

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Calcolo della suscettività magnetica per sito
      chi = magnetic_susceptibility(spin_grid)

.. py:function:: mod_magnetic_susceptibility(spin_matrix)

   Computes the modified magnetic susceptibility per site of a given spin configuration, using the absolute value of the magnetization instead of the magnetization.

   :param spin_matrix: bidimensional matrix representing the spin grid (+1 or -1).
   :type spin_matrix: numpy.ndarray
   :returns: The modified magnetic susceptibility per site of the spin configuration.
   :rtype: float

   **Example:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import mod_magnetic_susceptibility

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Calcolo della suscettività magnetica modificata per sito
      chi_mod = mod_magnetic_susceptibility(spin_grid)

.. py:function:: energy(spin_matrix, J)

   Computes the energy of a given spin configuration.

   :param spin_matrix: bidimensional matrix representing the spin grid (+1 or -1).
   :type spin_matrix: numpy.ndarray
   :param J: Coupling constant (interaction strength) between neighboring spins.
   :type J: float
   :returns: The energy of the spin configuration.
   :rtype: float

   **Example:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import energy

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Calcolo dell'energia della configurazione di spin
      E = energy(spin_grid, J=1.0)