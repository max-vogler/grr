#!/usr/bin/env python
# Copyright 2011 Google Inc. All Rights Reserved.
"""Tests the fake data store - in memory implementation."""



from grr.client import conf

# pylint: disable=unused-import,g-bad-import-order
from grr.lib import server_plugins
# pylint: enable=unused-import,g-bad-import-order

from grr.lib import data_store_test
from grr.lib import test_lib


class FakeDataStoreTest(data_store_test.DataStoreTest):
  """Test the fake data store."""


def main(args):
  test_lib.main(args)

if __name__ == "__main__":
  conf.StartMain(main)