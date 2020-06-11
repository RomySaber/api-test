#!/usr/bin/env python
# -*- coding: utf-8 -*-


class globaltoken():
        def _init(self):
            global _global_dict
            _global_dict = {}

        def set_value(self,name, value):
            _global_dict[name] = value

        def get_value(self,name):
            defValue = None
            try:
                return _global_dict[name]
            except KeyError:
                return defValue
