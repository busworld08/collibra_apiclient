# coding: utf-8

"""
    \"Data Governance Center: REST API v2\"

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.saml_api import SAMLApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSAMLApi(unittest.TestCase):
    """SAMLApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.saml_api.SAMLApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_saml_resource_get_sp_metadata_as_string_get(self):
        """Test case for resource_saml_resource_get_sp_metadata_as_string_get

        Returns the SAML Service Provider metadata for a this instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()