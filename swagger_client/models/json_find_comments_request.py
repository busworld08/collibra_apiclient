# coding: utf-8

"""
    \"Data Governance Center: REST API v2\"

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.json_paged_request import JsonPagedRequest  # noqa: F401,E501
from swagger_client.models.json_sort_order import JsonSortOrder  # noqa: F401,E501


class JsonFindCommentsRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'offset': 'float',
        'limit': 'float',
        'parent_id': 'str',
        'user_id': 'str',
        'base_resource_id': 'str',
        'root_comment': 'bool',
        'sort_order': 'JsonSortOrder'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'parent_id': 'parentId',
        'user_id': 'userId',
        'base_resource_id': 'baseResourceId',
        'root_comment': 'rootComment',
        'sort_order': 'sortOrder'
    }

    def __init__(self, offset=None, limit=None, parent_id=None, user_id=None, base_resource_id=None, root_comment=None, sort_order=None):  # noqa: E501
        """JsonFindCommentsRequest - a model defined in Swagger"""  # noqa: E501

        self._offset = None
        self._limit = None
        self._parent_id = None
        self._user_id = None
        self._base_resource_id = None
        self._root_comment = None
        self._sort_order = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if parent_id is not None:
            self.parent_id = parent_id
        if user_id is not None:
            self.user_id = user_id
        if base_resource_id is not None:
            self.base_resource_id = base_resource_id
        if root_comment is not None:
            self.root_comment = root_comment
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def offset(self):
        """Gets the offset of this JsonFindCommentsRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this JsonFindCommentsRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this JsonFindCommentsRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this JsonFindCommentsRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this JsonFindCommentsRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this JsonFindCommentsRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def parent_id(self):
        """Gets the parent_id of this JsonFindCommentsRequest.  # noqa: E501

        The <code>id</code> of the comment which the reply comments should be searched for  # noqa: E501

        :return: The parent_id of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this JsonFindCommentsRequest.

        The <code>id</code> of the comment which the reply comments should be searched for  # noqa: E501

        :param parent_id: The parent_id of this JsonFindCommentsRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def user_id(self):
        """Gets the user_id of this JsonFindCommentsRequest.  # noqa: E501

        The <code>id</code> of the user who created the comment  # noqa: E501

        :return: The user_id of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this JsonFindCommentsRequest.

        The <code>id</code> of the user who created the comment  # noqa: E501

        :param user_id: The user_id of this JsonFindCommentsRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def base_resource_id(self):
        """Gets the base_resource_id of this JsonFindCommentsRequest.  # noqa: E501

        The <code>id</code> of the resource which the searched comments refer to  # noqa: E501

        :return: The base_resource_id of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_resource_id

    @base_resource_id.setter
    def base_resource_id(self, base_resource_id):
        """Sets the base_resource_id of this JsonFindCommentsRequest.

        The <code>id</code> of the resource which the searched comments refer to  # noqa: E501

        :param base_resource_id: The base_resource_id of this JsonFindCommentsRequest.  # noqa: E501
        :type: str
        """

        self._base_resource_id = base_resource_id

    @property
    def root_comment(self):
        """Gets the root_comment of this JsonFindCommentsRequest.  # noqa: E501

        Whether the searched comments should be root comments (not reply comments)  # noqa: E501

        :return: The root_comment of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._root_comment

    @root_comment.setter
    def root_comment(self, root_comment):
        """Sets the root_comment of this JsonFindCommentsRequest.

        Whether the searched comments should be root comments (not reply comments)  # noqa: E501

        :param root_comment: The root_comment of this JsonFindCommentsRequest.  # noqa: E501
        :type: bool
        """

        self._root_comment = root_comment

    @property
    def sort_order(self):
        """Gets the sort_order of this JsonFindCommentsRequest.  # noqa: E501

        The order of sorting on the date the comment was created  # noqa: E501

        :return: The sort_order of this JsonFindCommentsRequest.  # noqa: E501
        :rtype: JsonSortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this JsonFindCommentsRequest.

        The order of sorting on the date the comment was created  # noqa: E501

        :param sort_order: The sort_order of this JsonFindCommentsRequest.  # noqa: E501
        :type: JsonSortOrder
        """

        self._sort_order = sort_order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JsonFindCommentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
