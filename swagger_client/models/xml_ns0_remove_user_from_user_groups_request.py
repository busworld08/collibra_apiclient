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


class XmlNs0RemoveUserFromUserGroupsRequest(object):
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
        'user_group_ids': 'str'
    }

    attribute_map = {
        'user_group_ids': 'userGroupIds'
    }

    def __init__(self, user_group_ids=None):  # noqa: E501
        """XmlNs0RemoveUserFromUserGroupsRequest - a model defined in Swagger"""  # noqa: E501

        self._user_group_ids = None
        self.discriminator = None

        if user_group_ids is not None:
            self.user_group_ids = user_group_ids

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this XmlNs0RemoveUserFromUserGroupsRequest.  # noqa: E501

        The list of <code>id</code>s of the user groups which the user should be removed from  # noqa: E501

        :return: The user_group_ids of this XmlNs0RemoveUserFromUserGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this XmlNs0RemoveUserFromUserGroupsRequest.

        The list of <code>id</code>s of the user groups which the user should be removed from  # noqa: E501

        :param user_group_ids: The user_group_ids of this XmlNs0RemoveUserFromUserGroupsRequest.  # noqa: E501
        :type: str
        """
        if user_group_ids is not None and len(user_group_ids) > 2147483647:
            raise ValueError("Invalid value for `user_group_ids`, length must be less than or equal to `2147483647`")  # noqa: E501
        if user_group_ids is not None and len(user_group_ids) < 1:
            raise ValueError("Invalid value for `user_group_ids`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_group_ids = user_group_ids

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
        if not isinstance(other, XmlNs0RemoveUserFromUserGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
