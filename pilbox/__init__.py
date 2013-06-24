#!/usr/bin/env python
#
# Copyright 2013 Adam Gschwender
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Pilbox server and tools

Versions:

  * 0.1: Image resizing fit
  * 0.1.1: Image cropping
  * 0.1.2: Image scaling
  * 0.2: Configuration integration
  * 0.3: Signature generation
  * 0.3.1: Signature command-line tool
  * 0.4: Backend support
  * 0.4.1: File backend
  * 0.4.2: S3 backend
  * 0.4.3: Memcache backend
"""

# human-readable version number
version = "0.3.0"

# The first three numbers are the components of the version number.
# The fourth is zero for an official release, positive for a development
# branch, or negative for a release candidate or beta (after the base version
# number has been incremented)
version_info = (0, 3, 0, 1)