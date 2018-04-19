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
from swagger_client.api.data_quality_rules_api import DataQualityRulesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDataQualityRulesApi(unittest.TestCase):
    """DataQualityRulesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.data_quality_rules_api.DataQualityRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_data_quality_rule_resource_add_data_quality_rule_post(self):
        """Test case for resource_data_quality_rule_resource_add_data_quality_rule_post

        Adds new data quality rule.  # noqa: E501
        """
        pass

    def test_resource_data_quality_rule_resource_change_data_quality_rule_patch(self):
        """Test case for resource_data_quality_rule_resource_change_data_quality_rule_patch

        Changes the data quality rule with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_data_quality_rule_resource_find_data_quality_rules_get(self):
        """Test case for resource_data_quality_rule_resource_find_data_quality_rules_get

        Returns data quality rules matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_data_quality_rule_resource_get_data_quality_rule_get(self):
        """Test case for resource_data_quality_rule_resource_get_data_quality_rule_get

        Returns data quality rule identified by given id.  # noqa: E501
        """
        pass

    def test_resource_data_quality_rule_resource_remove_data_quality_rule_delete(self):
        """Test case for resource_data_quality_rule_resource_remove_data_quality_rule_delete

        Removes data quality rule identified by given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()