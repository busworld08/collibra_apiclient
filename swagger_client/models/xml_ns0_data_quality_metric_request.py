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

from swagger_client.models.xml_ns0_data_quality_count_operation import XmlNs0DataQualityCountOperation  # noqa: F401,E501


class XmlNs0DataQualityMetricRequest(object):
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
        'count_operation': 'XmlNs0DataQualityCountOperation'
    }

    attribute_map = {
        'attribute_type_id': 'attributeTypeId',
        'count_operation': 'countOperation'
    }

    def __init__(self, attribute_type_id=None, count_operation=None):  # noqa: E501
        """XmlNs0DataQualityMetricRequest - a model defined in Swagger"""  # noqa: E501

        self._attribute_type_id = None
        self._count_operation = None
        self.discriminator = None

        if attribute_type_id is not None:
            self.attribute_type_id = attribute_type_id
        if count_operation is not None:
            self.count_operation = count_operation

    @property
    def attribute_type_id(self):
        """Gets the attribute_type_id of this XmlNs0DataQualityMetricRequest.  # noqa: E501

        The <code>id</code> of the attribute type that defines the value that is used as the data quality metric  # noqa: E501

        :return: The attribute_type_id of this XmlNs0DataQualityMetricRequest.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type_id

    @attribute_type_id.setter
    def attribute_type_id(self, attribute_type_id):
        """Sets the attribute_type_id of this XmlNs0DataQualityMetricRequest.

        The <code>id</code> of the attribute type that defines the value that is used as the data quality metric  # noqa: E501

        :param attribute_type_id: The attribute_type_id of this XmlNs0DataQualityMetricRequest.  # noqa: E501
        :type: str
        """

        self._attribute_type_id = attribute_type_id

    @property
    def count_operation(self):
        """Gets the count_operation of this XmlNs0DataQualityMetricRequest.  # noqa: E501

        The operation that should be performed when aggregating the quality results  # noqa: E501

        :return: The count_operation of this XmlNs0DataQualityMetricRequest.  # noqa: E501
        :rtype: XmlNs0DataQualityCountOperation
        """
        return self._count_operation

    @count_operation.setter
    def count_operation(self, count_operation):
        """Sets the count_operation of this XmlNs0DataQualityMetricRequest.

        The operation that should be performed when aggregating the quality results  # noqa: E501

        :param count_operation: The count_operation of this XmlNs0DataQualityMetricRequest.  # noqa: E501
        :type: XmlNs0DataQualityCountOperation
        """

        self._count_operation = count_operation

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
        if not isinstance(other, XmlNs0DataQualityMetricRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
