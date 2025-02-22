#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

# pyre-unsafe

"""
We should revisit this at some point. Config classes shouldn't subclass from this.
"""

import dataclasses
from typing import cast


class BaseDataClass:
    def _replace(self, **kwargs):
        return cast(type(self), dataclasses.replace(self, **kwargs))
