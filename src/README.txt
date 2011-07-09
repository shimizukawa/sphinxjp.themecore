A sphinx theme plugin extension.

Features
========
* provide theme template collection by using setuptools plugin mechanism.


Setup
=====
Make environment with easy_install::

    $ easy_install sphinxjp.themecore


Make your plugins
===================
themes
-------
If you want to integrate new theme, write ``sphinx_themes`` entry_points
in your setup.py::

    entry_points = """
        [sphinx_themes]
        path = sphinxjp.themes.s6:get_path
    """

and write `get_path` function that return path of ``Sphinx themes``.
``Sphinx themes`` directory include one or more theme directories.

directives
-----------
If you want to integrate new directive, write ``sphinx_directives``
entry_points in your setup.py::

    entry_points = """
        [sphinx_directives]
        setup = sphinxjp.themes.s6:setup_directives
    """

and write `setup_directives` function that receive `app` argument
and return None. setup_directives is same as sphinx extension's setup
function. See Sphinx extension document for more information.


Requirements
============
* Python 2.4 or later (not support 3.x)
* sphinx 1.0.x


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.

