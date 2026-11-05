Ising_tools
===========

In questo documento descriviamo le funzioni utilizzate nella simulazione del reticolo ad nido d'ape.

.. py:function:: metropolis(spin_matrix, T)

   Esegue un passo dell'algoritmo di Metropolis sul reticolo ad nido d'ape per aggiornare la configurazione degli spin.

   :param spin_matrix: Matrice bidimensionale rappresentante la griglia di spin (+1 o -1).
   :type spin_matrix: numpy.ndarray
   :param T: Temperatura del sistema in unità adimensionali.
   :type T: float
   :returns: La nuova configurazione della matrice degli spin dopo i tentativi di flip.
   :rtype: numpy.ndarray
   :raises ValueError: Se la matrice degli spin contiene valori diversi da +1 e -1.

   **Esempio di utilizzo:**

   .. code-block:: python

      import numpy as np
      from Ising_tools import metropolis

      # Inizializzazione griglia
      spin_grid = np.ones((10, 10))
      
      # Esecuzione dello step a temperatura T=2.26
      nuovo_stato = metropolis(spin_grid, T=2.26)