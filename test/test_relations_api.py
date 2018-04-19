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
from swagger_client.api.relations_api import RelationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRelationsApi(unittest.TestCase):
    """RelationsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.relations_api.RelationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_relation_resource_add_relation_post(self):
        """Test case for resource_relation_resource_add_relation_post

        Adds a new relation.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_add_relations_post(self):
        """Test case for resource_relation_resource_add_relations_post

        Adds multiple relations in one go.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_change_relation_patch(self):
        """Test case for resource_relation_resource_change_relation_patch

        Change the relation with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_change_relations_patch(self):
        """Test case for resource_relation_resource_change_relations_patch

        Changes multiple relations with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_find_relations_get(self):
        """Test case for resource_relation_resource_find_relations_get

        Returns relations matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_get_relation_get(self):
        """Test case for resource_relation_resource_get_relation_get

        Returns an relation identified by given id.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_remove_relation_delete(self):
        """Test case for resource_relation_resource_remove_relation_delete

        Removes relations identified by given ids.  # noqa: E501
        """
        pass

    def test_resource_relation_resource_remove_relation_delete_0(self):
        """Test case for resource_relation_resource_remove_relation_delete_0

        Removes an relation identified by given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()