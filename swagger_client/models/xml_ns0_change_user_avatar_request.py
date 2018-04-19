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


class XmlNs0ChangeUserAvatarRequest(object):
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
        'file_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'file_id': 'fileId',
        'id': 'id'
    }

    def __init__(self, file_id=None, id=None):  # noqa: E501
        """XmlNs0ChangeUserAvatarRequest - a model defined in Swagger"""  # noqa: E501

        self._file_id = None
        self._id = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if id is not None:
            self.id = id

    @property
    def file_id(self):
        """Gets the file_id of this XmlNs0ChangeUserAvatarRequest.  # noqa: E501

        The <code>id</code> of the file representing to avatar that should be assigned to the user  # noqa: E501

        :return: The file_id of this XmlNs0ChangeUserAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this XmlNs0ChangeUserAvatarRequest.

        The <code>id</code> of the file representing to avatar that should be assigned to the user  # noqa: E501

        :param file_id: The file_id of this XmlNs0ChangeUserAvatarRequest.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def id(self):
        """Gets the id of this XmlNs0ChangeUserAvatarRequest.  # noqa: E501

        The <code>id</code> of the user the avatar should be changed for  # noqa: E501

        :return: The id of this XmlNs0ChangeUserAvatarRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0ChangeUserAvatarRequest.

        The <code>id</code> of the user the avatar should be changed for  # noqa: E501

        :param id: The id of this XmlNs0ChangeUserAvatarRequest.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, XmlNs0ChangeUserAvatarRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other