Dataset Cheatsheet
==================
.. .. note::

..     This dataset statistics table is a **work in progress**.
..     Please consider helping us filling its content by providing statistics for individual datasets.

Graph Cheatsheet
----------------

Heterogeneous Graph Datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. .. list-table::
..     :widths: 50 50
..     :header-rows: 1
..     :class: custom-table

..     * - Name
..       - nodes

..     * - :class:`~rllm.datasets.DBLP` 
..       - 
..     * - └─ authors
..       - 4057
..     * - └─ papers
..       - 14382
..     * - └─ terms
..       - 7723
..     * - └─ conferences
..       - 20
..     * - :class:`~rllm.datasets.IMDB` 
..       - 
..     * - └─ movie
..       - 4278
..     * - └─ actors
..       - 5257
..     * - └─ directors   
..       - 2081

.. currentmodule:: rllm.datasets

.. autosummary::
   :nosignatures:
   :template: autosummary/class.rst

   DBLP
   IMDB


Homogeneous Graph Datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. .. list-table::
..     :widths: 20 20 20 20 20
..     :header-rows: 1
..     :class: custom-table
   
..     * - Name
..       - nodes
..       - edges
..       - features
..       - classes

..     * - :class:`~rllm.datasets.PlanetoidDataset` 
..       - 
..       - 
..       -
..       -
..     * - └─ Cora
..       - 2708
..       - 10556
..       - 1433
..       - 7
..     * - └─ CiteSeer
..       - 3327
..       - 9104
..       - 3703
..       - 6
..     * - └─ PubMed
..       - 19717
..       - 88648
..       - 500
..       - 3
.. currentmodule:: rllm.datasets

.. autosummary::
   :nosignatures:
   :template: autosummary/class.rst

   PlanetoidDataset
   TAPEDataset
   TAGDataset

Table Cheatsheet
----------------

Single Table Datasets
^^^^^^^^^^^^^^^^^^^^^^
.. .. list-table::
..     :widths: 50 50
..     :header-rows: 1
..     :class: custom-table

..     * - Name
..       - size

..     * - :class:`~rllm.datasets.Titanic` 
..       - 
..     * - └─ passengers
..       - 891
..     * - └─ features
..       - 12

.. currentmodule:: rllm.datasets

.. autosummary::
   :nosignatures:
   :template: autosummary/class.rst

   Titanic


Multi-Table Datasets
^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: rllm.datasets

.. autosummary::
   :nosignatures:
   :template: autosummary/class.rst

   TML1MDataset

.. .. list-table::
..     :widths: 50 50 50
..     :header-rows: 1
..     :class: custom-table

..     * - Name
..       - size
..       - nodes
..     * - :class:`~rllm.datasets.TML1MDataset` 
..       - 
..       - 
..     * - └─ users
..       - 6040
..       - 
..     * - └─ movies
..       - 
..       - 3883
..     * - └─ ratings
..       - 
..       - 1,000,209 
..     * - └─ features
..       - 5
..       - 11
..     * - └─ survived
..       - 
..       - 4

