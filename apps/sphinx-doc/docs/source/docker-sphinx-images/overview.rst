Overview
========

There are two docker images available in this project:

- ``mpc-sphinx-doc-utils`` - This image contains the necessary tools to build a Sphinx documentation project.
- ``mpc-sphinx-doc-docs`` - This image contains documentation about the tools available in the ``mpc-sphinx-doc-utils`` image.

Following solutions will help to build and run a Sphinx documentation project using Docker:

.. note::

    Reason of having two images is to separate the tools and the documentation about the tools.

    - The ``mpc-sphinx-doc-utils`` image can be build less frequently.
    - The ``mpc-sphinx-doc-docs`` image can be used to build the documentation with examples, tutorials, etc.
      And this should not require rebuilding the ``mpc-sphinx-doc-utils`` image over and over again.

