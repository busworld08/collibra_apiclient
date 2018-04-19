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
from swagger_client.api.attributes_api import AttributesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAttributesApi(unittest.TestCase):
    """AttributesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.attributes_api.AttributesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_attribute_resource_add_attribute_post(self):
        """Test case for resource_attribute_resource_add_attribute_post

        Adds a new attribute to an asset.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_add_attributes_post(self):
        """Test case for resource_attribute_resource_add_attributes_post

        Adds multiple attributes.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_change_attribute_patch(self):
        """Test case for resource_attribute_resource_change_attribute_patch

        Changes the attribute with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_change_attributes_patch(self):
        """Test case for resource_attribute_resource_change_attributes_patch

        Changes multiple attributes with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_find_attributes_get(self):
        """Test case for resource_attribute_resource_find_attributes_get

        Returns attributes matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_get_attribute_get(self):
        """Test case for resource_attribute_resource_get_attribute_get

        Returns the attribute identified by given id.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_remove_attribute_delete(self):
        """Test case for resource_attribute_resource_remove_attribute_delete

        Removes the attribute identified by given id.  # noqa: E501
        """
        pass

    def test_resource_attribute_resource_remove_attributes_delete(self):
        """Test case for resource_attribute_resource_remove_attributes_delete

        Removes the attributes identified by given ids.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()