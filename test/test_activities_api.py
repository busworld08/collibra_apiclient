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
from swagger_client.api.activities_api import ActivitiesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.activities_api.ActivitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_activity_stream_resource_get_activities_get(self):
        """Test case for resource_activity_stream_resource_get_activities_get

        Returns activities matching the given search criteria.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
