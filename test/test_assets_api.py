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
from swagger_client.api.assets_api import AssetsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAssetsApi(unittest.TestCase):
    """AssetsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.assets_api.AssetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_asset_resource_add_asset_post(self):
        """Test case for resource_asset_resource_add_asset_post

        Adds a new asset into a domain.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_add_assets_post(self):
        """Test case for resource_asset_resource_add_assets_post

        Adds multiple assets.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_add_tags_to_asset_post(self):
        """Test case for resource_asset_resource_add_tags_to_asset_post

        Adds tags to given asset.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_change_asset_patch(self):
        """Test case for resource_asset_resource_change_asset_patch

        Change the asset with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_change_assets_patch(self):
        """Test case for resource_asset_resource_change_assets_patch

        Changes multiple assets.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_find_assets_get(self):
        """Test case for resource_asset_resource_find_assets_get

        Returns assets matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_get_asset_get(self):
        """Test case for resource_asset_resource_get_asset_get

        Returns an asset identified by given id.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_get_asset_tags_get(self):
        """Test case for resource_asset_resource_get_asset_tags_get

        Returns all tags of given asset.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_remove_asset_delete(self):
        """Test case for resource_asset_resource_remove_asset_delete

        Removes an asset identified by given id.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_remove_assets_delete(self):
        """Test case for resource_asset_resource_remove_assets_delete

        Removes multiple assets.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_remove_tags_from_asset_delete(self):
        """Test case for resource_asset_resource_remove_tags_from_asset_delete

        Remove tags from given asset.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_set_asset_attributes_put(self):
        """Test case for resource_asset_resource_set_asset_attributes_put

        Replaces all the attributes of the asset (of given attribute type) with the attributes from the request, except matching attributes, these are retained.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_set_asset_relations_put(self):
        """Test case for resource_asset_resource_set_asset_relations_put

        Sets relations for given asset.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_set_asset_responsibilities_put(self):
        """Test case for resource_asset_resource_set_asset_responsibilities_put

        Sets responsibilities for given asset.  # noqa: E501
        """
        pass

    def test_resource_asset_resource_set_tags_for_asset_put(self):
        """Test case for resource_asset_resource_set_tags_for_asset_put

        Sets tags for given asset.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()