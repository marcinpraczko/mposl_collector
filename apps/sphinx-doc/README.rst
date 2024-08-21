Sphinx-doc Docker Image
=======================

Over the years I have been using Sphinx-doc for documentation purposes.
I had a lot of issues with the installation of the Sphinx-doc and its dependencies.

Finally I decided to create a docker image with Sphinx-doc and all its dependencies,
configuration and some additional tools.

Usage
=====

Following are the steps to use the Sphinx-doc docker image.

All commands
------------

-  To see all options please run

.. code-block:: bash

    # All commands should be run from apps/sphinx-doc folder
    make


Build the Docker Images
-----------------------

- To build images locally

.. code-block:: bash

    make build-docker-images


Build the built-in Documentation
--------------------------------

This project has a built-in documentation. To build the documentation, please run the following command:

- Please build images first

.. code-block:: bash

    make run-sphinx-doc-docs

- This should run docker container which can be accessed at http://localhost:8080


Resources
---------

Please refer to the following resources for more information:

-  Sphinx-doc: ``docs`` folder
