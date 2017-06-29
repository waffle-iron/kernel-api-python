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
from kernel_api_client.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = kernel_api_client.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_user_get(self):
        """
        Test case for user_get

        Retrieve User profile information
        """
        pass

    def test_user_put(self):
        """
        Test case for user_put

        Update user profile information
        """
        pass


if __name__ == '__main__':
    unittest.main()
