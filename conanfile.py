#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostMoveConan(base.BoostBaseConan):
    name = "boost_move"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_move"
    lib_short_names = ["move"]
    header_only_libs = ["move"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_static_assert"
    ]
