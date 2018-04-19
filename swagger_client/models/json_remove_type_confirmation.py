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


class JsonRemoveTypeConfirmation(object):
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
        'type_id': 'str',
        'instance_count': 'float'
    }

    attribute_map = {
        'type_id': 'typeId',
        'instance_count': 'instanceCount'
    }

    def __init__(self, type_id=None, instance_count=None):  # noqa: E501
        """JsonRemoveTypeConfirmation - a model defined in Swagger"""  # noqa: E501

        self._type_id = None
        self._instance_count = None
        self.discriminator = None

        if type_id is not None:
            self.type_id = type_id
        if instance_count is not None:
            self.instance_count = instance_count

    @property
    def type_id(self):
        """Gets the type_id of this JsonRemoveTypeConfirmation.  # noqa: E501

          # noqa: E501

        :return: The type_id of this JsonRemoveTypeConfirmation.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this JsonRemoveTypeConfirmation.

          # noqa: E501

        :param type_id: The type_id of this JsonRemoveTypeConfirmation.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

    @property
    def instance_count(self):
        """Gets the instance_count of this JsonRemoveTypeConfirmation.  # noqa: E501

          # noqa: E501

        :return: The instance_count of this JsonRemoveTypeConfirmation.  # noqa: E501
        :rtype: float
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """Sets the instance_count of this JsonRemoveTypeConfirmation.

          # noqa: E501

        :param instance_count: The instance_count of this JsonRemoveTypeConfirmation.  # noqa: E501
        :type: float
        """

        self._instance_count = instance_count

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
        if not isinstance(other, JsonRemoveTypeConfirmation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
