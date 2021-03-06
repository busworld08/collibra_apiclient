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


class JsonExploreFilters(object):
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
        'outgoing_relation_types': 'list[str]',
        'incoming_relation_types': 'list[str]'
    }

    attribute_map = {
        'outgoing_relation_types': 'outgoingRelationTypes',
        'incoming_relation_types': 'incomingRelationTypes'
    }

    def __init__(self, outgoing_relation_types=None, incoming_relation_types=None):  # noqa: E501
        """JsonExploreFilters - a model defined in Swagger"""  # noqa: E501

        self._outgoing_relation_types = None
        self._incoming_relation_types = None
        self.discriminator = None

        if outgoing_relation_types is not None:
            self.outgoing_relation_types = outgoing_relation_types
        if incoming_relation_types is not None:
            self.incoming_relation_types = incoming_relation_types

    @property
    def outgoing_relation_types(self):
        """Gets the outgoing_relation_types of this JsonExploreFilters.  # noqa: E501

          # noqa: E501

        :return: The outgoing_relation_types of this JsonExploreFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._outgoing_relation_types

    @outgoing_relation_types.setter
    def outgoing_relation_types(self, outgoing_relation_types):
        """Sets the outgoing_relation_types of this JsonExploreFilters.

          # noqa: E501

        :param outgoing_relation_types: The outgoing_relation_types of this JsonExploreFilters.  # noqa: E501
        :type: list[str]
        """

        self._outgoing_relation_types = outgoing_relation_types

    @property
    def incoming_relation_types(self):
        """Gets the incoming_relation_types of this JsonExploreFilters.  # noqa: E501

          # noqa: E501

        :return: The incoming_relation_types of this JsonExploreFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._incoming_relation_types

    @incoming_relation_types.setter
    def incoming_relation_types(self, incoming_relation_types):
        """Sets the incoming_relation_types of this JsonExploreFilters.

          # noqa: E501

        :param incoming_relation_types: The incoming_relation_types of this JsonExploreFilters.  # noqa: E501
        :type: list[str]
        """

        self._incoming_relation_types = incoming_relation_types

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
        if not isinstance(other, JsonExploreFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
