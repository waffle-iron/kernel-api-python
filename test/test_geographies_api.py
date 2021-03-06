# coding: utf-8

"""
    Kernel API

    Access Kernel insights programmatically

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kernel_api_client
from kernel_api_client.rest import ApiException
from kernel_api_client.apis.geographies_api import GeographiesApi


class TestGeographiesApi(unittest.TestCase):
    """ GeographiesApi unit test stubs """

    def setUp(self):
        self.api = kernel_api_client.apis.geographies_api.GeographiesApi()

    def tearDown(self):
        pass

    def test_geographies_get(self):
        """
        Test case for geographies_get

        Available geographies
        """
        pass

    def test_geographies_levels_get(self):
        """
        Test case for geographies_levels_get

        Available geography levels
        """
        pass


if __name__ == '__main__':
    unittest.main()
