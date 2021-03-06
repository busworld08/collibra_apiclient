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

from swagger_client.models.json_attribute_value import JsonAttributeValue  # noqa: F401,E501
from swagger_client.models.json_complex_relation_leg_request import JsonComplexRelationLegRequest  # noqa: F401,E501
from swagger_client.models.json_related_asset_id import JsonRelatedAssetId  # noqa: F401,E501


class JsonChangeComplexRelationRequest(object):
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
        'legs': 'list[JsonComplexRelationLegRequest]',
        'relations': 'list[dict(str, JsonRelatedAssetId)]',
        'attributes': 'list[dict(str, JsonAttributeValue)]'
    }

    attribute_map = {
        'legs': 'legs',
        'relations': 'relations',
        'attributes': 'attributes'
    }

    def __init__(self, legs=None, relations=None, attributes=None):  # noqa: E501
        """JsonChangeComplexRelationRequest - a model defined in Swagger"""  # noqa: E501

        self._legs = None
        self._relations = None
        self._attributes = None
        self.discriminator = None

        if legs is not None:
            self.legs = legs
        if relations is not None:
            self.relations = relations
        if attributes is not None:
            self.attributes = attributes

    @property
    def legs(self):
        """Gets the legs of this JsonChangeComplexRelationRequest.  # noqa: E501

        The new list of legs that the changed complex relation should contain  # noqa: E501

        :return: The legs of this JsonChangeComplexRelationRequest.  # noqa: E501
        :rtype: list[JsonComplexRelationLegRequest]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this JsonChangeComplexRelationRequest.

        The new list of legs that the changed complex relation should contain  # noqa: E501

        :param legs: The legs of this JsonChangeComplexRelationRequest.  # noqa: E501
        :type: list[JsonComplexRelationLegRequest]
        """

        self._legs = legs

    @property
    def relations(self):
        """Gets the relations of this JsonChangeComplexRelationRequest.  # noqa: E501

        The new relations that the new complex relation should contain  # noqa: E501

        :return: The relations of this JsonChangeComplexRelationRequest.  # noqa: E501
        :rtype: list[dict(str, JsonRelatedAssetId)]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this JsonChangeComplexRelationRequest.

        The new relations that the new complex relation should contain  # noqa: E501

        :param relations: The relations of this JsonChangeComplexRelationRequest.  # noqa: E501
        :type: list[dict(str, JsonRelatedAssetId)]
        """

        self._relations = relations

    @property
    def attributes(self):
        """Gets the attributes of this JsonChangeComplexRelationRequest.  # noqa: E501

        The new attributes that the new complex relation should contain  # noqa: E501

        :return: The attributes of this JsonChangeComplexRelationRequest.  # noqa: E501
        :rtype: list[dict(str, JsonAttributeValue)]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this JsonChangeComplexRelationRequest.

        The new attributes that the new complex relation should contain  # noqa: E501

        :param attributes: The attributes of this JsonChangeComplexRelationRequest.  # noqa: E501
        :type: list[dict(str, JsonAttributeValue)]
        """

        self._attributes = attributes

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
        if not isinstance(other, JsonChangeComplexRelationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
