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


class JsonComplexRelationAttributeRequest(object):
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
        'attribute_type_id': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'attribute_type_id': 'attributeTypeId',
        'value': 'value'
    }

    def __init__(self, attribute_type_id=None, value=None):  # noqa: E501
        """JsonComplexRelationAttributeRequest - a model defined in Swagger"""  # noqa: E501

        self._attribute_type_id = None
        self._value = None
        self.discriminator = None

        self.attribute_type_id = attribute_type_id
        if value is not None:
            self.value = value

    @property
    def attribute_type_id(self):
        """Gets the attribute_type_id of this JsonComplexRelationAttributeRequest.  # noqa: E501

        The <code>id</code> of the type of the single attribute for complex relation  # noqa: E501

        :return: The attribute_type_id of this JsonComplexRelationAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type_id

    @attribute_type_id.setter
    def attribute_type_id(self, attribute_type_id):
        """Sets the attribute_type_id of this JsonComplexRelationAttributeRequest.

        The <code>id</code> of the type of the single attribute for complex relation  # noqa: E501

        :param attribute_type_id: The attribute_type_id of this JsonComplexRelationAttributeRequest.  # noqa: E501
        :type: str
        """
        if attribute_type_id is None:
            raise ValueError("Invalid value for `attribute_type_id`, must not be `None`")  # noqa: E501

        self._attribute_type_id = attribute_type_id

    @property
    def value(self):
        """Gets the value of this JsonComplexRelationAttributeRequest.  # noqa: E501

        The value of the attribute attached to the complex relation  # noqa: E501

        :return: The value of this JsonComplexRelationAttributeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JsonComplexRelationAttributeRequest.

        The value of the attribute attached to the complex relation  # noqa: E501

        :param value: The value of this JsonComplexRelationAttributeRequest.  # noqa: E501
        :type: list[str]
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
        if not isinstance(other, JsonComplexRelationAttributeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
