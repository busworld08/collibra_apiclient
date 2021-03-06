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
from swagger_client.api.comments_api import CommentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCommentsApi(unittest.TestCase):
    """CommentsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.comments_api.CommentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resource_comment_resource_add_comment_post(self):
        """Test case for resource_comment_resource_add_comment_post

        Adds new comment.  # noqa: E501
        """
        pass

    def test_resource_comment_resource_change_comment_patch(self):
        """Test case for resource_comment_resource_change_comment_patch

        Changes the comment with the information that is present in the request.  # noqa: E501
        """
        pass

    def test_resource_comment_resource_find_comments_get(self):
        """Test case for resource_comment_resource_find_comments_get

        Returns comments matching the given search criteria.  # noqa: E501
        """
        pass

    def test_resource_comment_resource_get_comment_get(self):
        """Test case for resource_comment_resource_get_comment_get

        Returns comment identified by given id.  # noqa: E501
        """
        pass

    def test_resource_comment_resource_remove_comment_delete(self):
        """Test case for resource_comment_resource_remove_comment_delete

        Removes comment identified by given id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
