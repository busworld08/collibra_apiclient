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
from swagger_client.api.complex_relation_types_api import ComplexRelationTypesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestComplexRelationTypesApi(unittest.TestCase):
    """ComplexRelationTypesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.complex_relation_types_api.ComplexRelationTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_complex_relation_type_resource_add_complex_relation_type_post(self):
        """Test case for resource_complex_relation_type_resource_add_complex_relation_type_post

        Adds new complex relation type.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_type_resource_change_relation_type_patch(self):
        """Test case for resource_complex_relation_type_resource_change_relation_type_patch

        Changes the complex relation type with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_type_resource_get_all_complex_relation_types_get(self):
        """Test case for resource_complex_relation_type_resource_get_all_complex_relation_types_get

        Returns all complex relation types.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_type_resource_get_complex_relation_type_get(self):
        """Test case for resource_complex_relation_type_resource_get_complex_relation_type_get

        Returns complex relation type identified by given id.  # noqa: E501
        """
        pass

    def test_resource_complex_relation_type_resource_remove_complex_relation_type_delete(self):
        """Test case for resource_complex_relation_type_resource_remove_complex_relation_type_delete

        Removes complex relation type identified by given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()