#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Matt Roll.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode, Dict
from ._frontend import module_name, module_version


class ExampleWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('ExampleModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('ExampleView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    defaultTable = {
        "head": [
            { "name": "Date", "type": "Date" },
            { "name": "EPS", "type": "Number" },
        ],
        "body": [
            [ "2021-09-01", 5569 ],
            [ "2021-09-02", 3421 ],
            [ "2021-09-03", 6900 ],
            [ "2021-09-04", 17244 ],
            [ "2021-09-05", 3895 ],
            [ "2021-09-06", 4282 ],
            [ "2021-09-07", 5569 ],
            [ "2021-09-08", 8845 ],
            [ "2021-09-09", 2567 ],
            [ "2021-09-10", 4398 ],
        ]
    }

    # Your widget state goes here. Make sure to update the corresponding
    # JavaScript widget state (defaultModelProperties) in widget.ts
    id    = Unicode('618538ffca80bec41403105e').tag(sync=True)
    table = Dict(defaultTable).tag(sync=True)
