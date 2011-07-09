# -*- coding: utf-8 -*-

import pkg_resources


class PathDictProxy(dict):
    _proxies = {}

    def __init__(self, *args, **kw):
        super(PathDictProxy, self).__init__(*args, **kw)
        self._proxies = {}

    def set_proxy(self, key, value):
        self._proxies[key] = value

    def __setitem__(self, key, value):
        if key in self._proxies:
            value = self._proxies[key] + value
        return super(PathDictProxy, self).__setitem__(key, value)


def setup_themes(app):
    theme_paths = []

    for plugin in pkg_resources.iter_entry_points('sphinx_themes'):
        m = plugin.load()
        if callable(m):
            path = m()
        else:
            path = m
        theme_paths.append(path)

    if theme_paths:
        theme_paths.extend(app.config.html_theme_path)
        app.config.__dict__ = PathDictProxy(app.config.__dict__)
        app.config.__dict__.set_proxy('html_theme_path', theme_paths)


def setup_directives(app):
    for plugin in pkg_resources.iter_entry_points('sphinx_directives'):
        module_setup = plugin.load()
        module_setup(app)


def setup(app):
    setup_themes(app)
    setup_directives(app)
