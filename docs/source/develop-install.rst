
Developer install
=================


To install a developer version of canopy_charts, you will first need to clone
the repository::

    git clone https://github.com//canopy-charts-jupyter
    cd canopy-charts-jupyter

Next, install it with a develop install using pip::

    pip install -e .


If you are planning on working on the JS/frontend code, you should also do
a link installation of the extension::

    jupyter nbextension install [--sys-prefix / --user / --system] --symlink --py canopy_charts

    jupyter nbextension enable [--sys-prefix / --user / --system] --py canopy_charts

with the `appropriate flag`_. Or, if you are using Jupyterlab::

    jupyter labextension install .


.. links

.. _`appropriate flag`: https://jupyter-notebook.readthedocs.io/en/stable/extending/frontend_extensions.html#installing-and-enabling-extensions
