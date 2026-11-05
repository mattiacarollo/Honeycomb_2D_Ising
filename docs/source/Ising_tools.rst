Ising_tools
===========

In questo documento descriviamo la funzione principale utilizzata nella simulazione.

.. autofunction:: Ising_tools.metropolis

La funzione calcola l'evoluzione dello stato di spin sul reticolo ad nido d'ape.

- **Parametri di ingresso:** Matrice di spin, temperatura :math:`T`.
- **Output:** Configurazione finale degli spin.

Esempio di Utilizzo
~~~~~~~~~~~~~~~~~~~

Di seguito un blocco di codice dimostrativo:

.. code-block:: python

   import numpy as np
   # Esempio di chiamata
   # magnetizzazione = calcola_magnetizzazione(spin_grid, T=2.26)

Link al Notebook
----------------

Per consultare l'esecuzione completa del codice e i grafici:

.. toctree::
   :maxdepth: 1

   Ising_model_2D_honeycomb