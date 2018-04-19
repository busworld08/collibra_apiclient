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


class XmlNs0ComplexRelationAttributeTypeRequest(object):
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
        'id': 'str',
        'max': 'float',
        'min': 'float'
    }

    attribute_map = {
        'attribute_type_id': 'attributeTypeId',
        'id': 'id',
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, attribute_type_id=None, id=None, max=None, min=None):  # noqa: E501
        """XmlNs0ComplexRelationAttributeTypeRequest - a model defined in Swagger"""  # noqa: E501

        self._attribute_type_id = None
        self._id = None
        self._max = None
        self._min = None
        self.discriminator = None

        if attribute_type_id is not None:
            self.attribute_type_id = attribute_type_id
        if id is not None:
            self.id = id
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def attribute_type_id(self):
        """Gets the attribute_type_id of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501

        The <code>id</code> of the attribute type  # noqa: E501

        :return: The attribute_type_id of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type_id

    @attribute_type_id.setter
    def attribute_type_id(self, attribute_type_id):
        """Sets the attribute_type_id of this XmlNs0ComplexRelationAttributeTypeRequest.

        The <code>id</code> of the attribute type  # noqa: E501

        :param attribute_type_id: The attribute_type_id of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :type: str
        """

        self._attribute_type_id = attribute_type_id

    @property
    def id(self):
        """Gets the id of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501

        The <code>id</code> of the complex relation attribute type. It will be created with this id or updated. If left empty on update the complex attribute type will be recreated.  # noqa: E501

        :return: The id of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0ComplexRelationAttributeTypeRequest.

        The <code>id</code> of the complex relation attribute type. It will be created with this id or updated. If left empty on update the complex attribute type will be recreated.  # noqa: E501

        :param id: The id of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def max(self):
        """Gets the max of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501

        The maximum number of attribute type occurrences  # noqa: E501

        :return: The max of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this XmlNs0ComplexRelationAttributeTypeRequest.

        The maximum number of attribute type occurrences  # noqa: E501

        :param max: The max of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501

        The minimum number of attribute type occurrences  # noqa: E501

        :return: The min of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this XmlNs0ComplexRelationAttributeTypeRequest.

        The minimum number of attribute type occurrences  # noqa: E501

        :param min: The min of this XmlNs0ComplexRelationAttributeTypeRequest.  # noqa: E501
        :type: float
        """

        self._min = min

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
        if not isinstance(other, XmlNs0ComplexRelationAttributeTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
