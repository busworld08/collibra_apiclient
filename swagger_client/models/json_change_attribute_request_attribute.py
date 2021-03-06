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


class JsonChangeAttributeRequestAttribute(object):
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
        'id': 'str',
        'value': 'object'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value'
    }

    def __init__(self, id=None, value=None):  # noqa: E501
        """JsonChangeAttributeRequestAttribute - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._value = None
        self.discriminator = None

        self.id = id
        self.value = value

    @property
    def id(self):
        """Gets the id of this JsonChangeAttributeRequestAttribute.  # noqa: E501

        The <code>id</code> of the asset this attribute should belong to. Silently ignored if the <code>id</code> is provided as path parameter of the request  # noqa: E501

        :return: The id of this JsonChangeAttributeRequestAttribute.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonChangeAttributeRequestAttribute.

        The <code>id</code> of the asset this attribute should belong to. Silently ignored if the <code>id</code> is provided as path parameter of the request  # noqa: E501

        :param id: The id of this JsonChangeAttributeRequestAttribute.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def value(self):
        """Gets the value of this JsonChangeAttributeRequestAttribute.  # noqa: E501

        The value of this attribute. Expected type of the value depends on the type of the attribute. Following list presents type of the value depending on the kind of the attribute <p><ul> <li> kind: Numeric               -> value type: number or string <li> kind: Script                -> value type: string <li> kind: Single Value List     -> value type: string <li> kind: Date                  -> value type: number or string <li> kind: String                -> value type: string <li> kind: Boolean               -> value type: boolean or string <li> kind: Multi Value List      -> value type: array of strings </ul><p>  # noqa: E501

        :return: The value of this JsonChangeAttributeRequestAttribute.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JsonChangeAttributeRequestAttribute.

        The value of this attribute. Expected type of the value depends on the type of the attribute. Following list presents type of the value depending on the kind of the attribute <p><ul> <li> kind: Numeric               -> value type: number or string <li> kind: Script                -> value type: string <li> kind: Single Value List     -> value type: string <li> kind: Date                  -> value type: number or string <li> kind: String                -> value type: string <li> kind: Boolean               -> value type: boolean or string <li> kind: Multi Value List      -> value type: array of strings </ul><p>  # noqa: E501

        :param value: The value of this JsonChangeAttributeRequestAttribute.  # noqa: E501
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, JsonChangeAttributeRequestAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
