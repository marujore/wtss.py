#
# This file is part of Python Client Library for WTSS.
# Copyright (C) 2020 INPE.
#
# Python Client Library for WTSS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows how the various text representation for services and coverages."""

from wtss import *

service = WTSS('http://www.esensing.dpi.inpe.br')

print(service)
print(str(service))
print(repr(service))
print(service._repr_html_())


print(service.MOD13Q1)
print(str(service.MOD13Q1))
print(repr(service.MOD13Q1))
print(service.MOD13Q1._repr_html_())
