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
from swagger_client.api.asset_types_api import AssetTypesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAssetTypesApi(unittest.TestCase):
    """AssetTypesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.asset_types_api.AssetTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_asset_type_resource_add_asset_type_post(self):
        """Test case for resource_asset_type_resource_add_asset_type_post

        Adds new asset type.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_add_asset_types_post(self):
        """Test case for resource_asset_type_resource_add_asset_types_post

        Adds multiple asset types.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_change_asset_type_patch(self):
        """Test case for resource_asset_type_resource_change_asset_type_patch

        Changes the asset type with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_change_asset_types_patch(self):
        """Test case for resource_asset_type_resource_change_asset_types_patch

        Changes multiple asset types.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_find_asset_types_get(self):
        """Test case for resource_asset_type_resource_find_asset_types_get

        Returns asset types matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_find_sub_asset_types_get(self):
        """Test case for resource_asset_type_resource_find_sub_asset_types_get

        Finds all the sub types of the asset type as described in the request object.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_get_asset_type_get(self):
        """Test case for resource_asset_type_resource_get_asset_type_get

        Returns asset type identified by given UUID.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_remove_asset_type_delete(self):
        """Test case for resource_asset_type_resource_remove_asset_type_delete

        Removes asset type identified by given UUID.  # noqa: E501
        """
        pass

    def test_resource_asset_type_resource_remove_asset_types_delete(self):
        """Test case for resource_asset_type_resource_remove_asset_types_delete

        Removes multiple asset types.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
