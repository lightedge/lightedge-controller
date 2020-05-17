#!/usr/bin/env python3
#
# Copyright (c) 2019 Roberto Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""Full unit test suite."""

import unittest

from .measrepue import TestMeasRepUe


def full_suite():
    """Full unit test suite."""

    suite = unittest.TestSuite()

    suite.addTest(TestMeasRepUe('test_create_meas_rep_ue'))

    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(full_suite())
