.. Honeycomb_2D_Ising documentation master file, created by
   sphinx-quickstart on Thu Nov  5 15:20:49 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Honeycomb_2D_Ising documentation
================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Indice Contenuti:

Ising_tools
=============================

In questo documento descriviamo la funzione principale utilizzata nella simulazione.

..autofunction:: Ising_tools.metropolis

La funzione calcola l'evoluzione dello stato di spin sul reticolo ad nido d'ape.

* **Parametri di ingresso:** Matrice di spin, temperatura $T$.
* **Output:** Configurazione finale degli spin.

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

   Ising_tools
   Ising_model_2D_honeycomb