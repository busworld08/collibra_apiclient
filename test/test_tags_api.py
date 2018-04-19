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
from swagger_client.api.tags_api import TagsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tags_api.TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_tag_resource_find_tags_get(self):
        """Test case for resource_tag_resource_find_tags_get

        Returns tags matching given search criteria.  # noqa: E501
        """
        pass

    def test_resource_tag_resource_get_tag_get(self):
        """Test case for resource_tag_resource_get_tag_get

        Returns a tag identified by given id.  # noqa: E501
        """
        pass

    def test_resource_tag_resource_get_tags_by_asset_id_get(self):
        """Test case for resource_tag_resource_get_tags_by_asset_id_get

        Retrieves all tags of given asset.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
