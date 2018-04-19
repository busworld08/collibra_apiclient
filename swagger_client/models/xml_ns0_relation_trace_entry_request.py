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


class XmlNs0RelationTraceEntryRequest(object):
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
        'relation_type_id': 'str',
        'role_direction': 'bool'
    }

    attribute_map = {
        'relation_type_id': 'relationTypeId',
        'role_direction': 'roleDirection'
    }

    def __init__(self, relation_type_id=None, role_direction=None):  # noqa: E501
        """XmlNs0RelationTraceEntryRequest - a model defined in Swagger"""  # noqa: E501

        self._relation_type_id = None
        self._role_direction = None
        self.discriminator = None

        if relation_type_id is not None:
            self.relation_type_id = relation_type_id
        if role_direction is not None:
            self.role_direction = role_direction

    @property
    def relation_type_id(self):
        """Gets the relation_type_id of this XmlNs0RelationTraceEntryRequest.  # noqa: E501

        The <code>id</code> of the relation type for the relation trace entry  # noqa: E501

        :return: The relation_type_id of this XmlNs0RelationTraceEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_id

    @relation_type_id.setter
    def relation_type_id(self, relation_type_id):
        """Sets the relation_type_id of this XmlNs0RelationTraceEntryRequest.

        The <code>id</code> of the relation type for the relation trace entry  # noqa: E501

        :param relation_type_id: The relation_type_id of this XmlNs0RelationTraceEntryRequest.  # noqa: E501
        :type: str
        """

        self._relation_type_id = relation_type_id

    @property
    def role_direction(self):
        """Gets the role_direction of this XmlNs0RelationTraceEntryRequest.  # noqa: E501

        The direction of the relation to take, true if the relation is followed in role direction  # noqa: E501

        :return: The role_direction of this XmlNs0RelationTraceEntryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._role_direction

    @role_direction.setter
    def role_direction(self, role_direction):
        """Sets the role_direction of this XmlNs0RelationTraceEntryRequest.

        The direction of the relation to take, true if the relation is followed in role direction  # noqa: E501

        :param role_direction: The role_direction of this XmlNs0RelationTraceEntryRequest.  # noqa: E501
        :type: bool
        """

        self._role_direction = role_direction

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
        if not isinstance(other, XmlNs0RelationTraceEntryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other