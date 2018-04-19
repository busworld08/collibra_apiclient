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

from swagger_client.models.json_add_attribute_request_attribute import JsonAddAttributeRequestAttribute  # noqa: F401,E501


class JsonAddSingleValueListAttributeRequest(object):
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
        'asset_id': 'str',
        'type_id': 'str',
        'value': 'str'
    }

    attribute_map = {
        'asset_id': 'assetId',
        'type_id': 'typeId',
        'value': 'value'
    }

    def __init__(self, asset_id=None, type_id=None, value=None):  # noqa: E501
        """JsonAddSingleValueListAttributeRequest - a model defined in Swagger"""  # noqa: E501

        self._asset_id = None
        self._type_id = None
        self._value = None
        self.discriminator = None

        self.asset_id = asset_id
        self.type_id = type_id
        if value is not None:
            self.value = value

    @property
    def asset_id(self):
        """Gets the asset_id of this JsonAddSingleValueListAttributeRequest.  # noqa: E501

        The <code>id</code> of the asset this attribute should belong to  # noqa: E501

        :return: The asset_id of this JsonAddSingleValueListAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this JsonAddSingleValueListAttributeRequest.

        The <code>id</code> of the asset this attribute should belong to  # noqa: E501

        :param asset_id: The asset_id of this JsonAddSingleValueListAttributeRequest.  # noqa: E501
        :type: str
        """
        if asset_id is None:
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

    @property
    def type_id(self):
        """Gets the type_id of this JsonAddSingleValueListAttributeRequest.  # noqa: E501

        The <code>id</code> of the attribute type for the new attribute  # noqa: E501

        :return: The type_id of this JsonAddSingleValueListAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this JsonAddSingleValueListAttributeRequest.

        The <code>id</code> of the attribute type for the new attribute  # noqa: E501

        :param type_id: The type_id of this JsonAddSingleValueListAttributeRequest.  # noqa: E501
        :type: str
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def value(self):
        """Gets the value of this JsonAddSingleValueListAttributeRequest.  # noqa: E501

        The string value for the attribute  # noqa: E501

        :return: The value of this JsonAddSingleValueListAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JsonAddSingleValueListAttributeRequest.

        The string value for the attribute  # noqa: E501

        :param value: The value of this JsonAddSingleValueListAttributeRequest.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, JsonAddSingleValueListAttributeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
