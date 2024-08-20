Docker Usage
============

This section will guide you on how to user this Docker Sphinx image.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Overview
--------

There are two docker images available in this project:

- ``mpc-sphinx-doc-utils`` - This image contains the necessary tools to build a Sphinx documentation project.
- ``mpc-sphinx-doc-docs`` - This image contains documentation about the tools available in the ``mpc-sphinx-doc-utils`` image.

Mpc-sphinx-doc-docs image
-------------------------

.. note::

    - The ``mpc-sphinx-doc-docs`` image is based on the ``mpc-sphinx-doc-utils`` image.
    - Both images needs to be built before you can use them.

To build the documentation, you can use the following command:

.. code-block:: bash

    cd docs
    docker run --rm -it --user $(id -u):$(id -g) -v $(pwd):/usr/local/src/app-build mpc-sphinx-doc-utils:0.1.1 make html
