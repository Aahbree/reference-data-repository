# This file is part of the Reference Data Repository (refdata).
#
# Copyright (C) 2021 New York University.
#
# refdata is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Unit tests for the file checksum library."""

import os
import pytest

from refdata.checksum import hash_file


"""Use `countries.json` for checksum tests."""
DIR = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(DIR, './.files/countries.json')

"""Expected checksum for the test file. Needs to be adjusted if we ever change
the test file.
"""
CHECKSUM = '403126a5fb62f83b2ff65fb2bd7a3e87d57c0041cc086da813134035e7b0157c'


@pytest.mark.parametrize('chunk_size', [None, 100, 256, 1000, 10000])
def test_file_checksum(chunk_size):
    """Test computing checksum for a file. Uses the `countries.json` file from
    the test file folder. Ensure that using different chunk sizes does not have
    an impact on the result.
    """
    assert hash_file(filename=INPUT_FILE, chunk_size=chunk_size) == CHECKSUM
