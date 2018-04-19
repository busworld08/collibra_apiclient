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
from swagger_client.api.complex_relations_api import ComplexRelationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestComplexRelationsApi(unittest.TestCase):
    """ComplexRelationsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.complex_relations_api.ComplexRelationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_complex_relation_resource_add_complex_relation_post(self):
        """Test case for resource_complex_relation_resource_add_complex_relation_post

        Adds new complex relation.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_resource_change_complex_relation_patch(self):
        """Test case for resource_complex_relation_resource_change_complex_relation_patch

        Change the complex relation with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_resource_find_complex_relations_get(self):
        """Test case for resource_complex_relation_resource_find_complex_relations_get

        Returns complex relations matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_resource_get_complex_relation_get(self):
        """Test case for resource_complex_relation_resource_get_complex_relation_get

        Returns complex relation identified by given id.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_resource_remove_complex_relation_delete(self):
        """Test case for resource_complex_relation_resource_remove_complex_relation_delete

        Removes complex relation identified by given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
