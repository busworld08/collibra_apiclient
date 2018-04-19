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
from swagger_client.api.roles_api import RolesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_role_resource_add_role_post(self):
        """Test case for resource_role_resource_add_role_post

        Adds new role.  # noqa: E501
        """
        pass

    def test_resource_role_resource_change_role_patch(self):
        """Test case for resource_role_resource_change_role_patch

        Changes the role with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_role_resource_find_roles_get(self):
        """Test case for resource_role_resource_find_roles_get

        Returns roles matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_role_resource_get_role_get(self):
        """Test case for resource_role_resource_get_role_get

        Returns role identified by given id.  # noqa: E501
        """
        pass

    def test_resource_role_resource_remove_role_delete(self):
        """Test case for resource_role_resource_remove_role_delete

        Removes role identified by given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
