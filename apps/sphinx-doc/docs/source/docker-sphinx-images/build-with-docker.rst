Build docker images with Docker
===============================

Following snippets are from scripts that can be used to build the docker images.

Image: mpc-sphinx-doc-utils
---------------------------

Please run following commands:

.. literalinclude:: ../helpers/docker-sphinx-utils-build.sh
    :language: bash
    :caption: docker-sphinx-utils-build.sh
    :start-after: # Build docker image

Image: mpc-sphinx-doc-docs 
--------------------------

.. note::

    - The ``mpc-sphinx-doc-docs`` image is based on the ``mpc-sphinx-doc-utils`` image.

Please run following commands:

.. literalinclude:: ../helpers/docker-sphinx-docs-build.sh
    :language: bash
    :caption: docker-sphinx-docs-build.sh
    :start-after: # Build docker image
