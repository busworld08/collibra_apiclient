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


class XmlNs0ComplexRelationLegTypeRequest(object):
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
        'asset_type_id': 'str',
        'co_role': 'str',
        'id': 'str',
        'max': 'float',
        'min': 'float',
        'role': 'str'
    }

    attribute_map = {
        'asset_type_id': 'assetTypeId',
        'co_role': 'coRole',
        'id': 'id',
        'max': 'max',
        'min': 'min',
        'role': 'role'
    }

    def __init__(self, asset_type_id=None, co_role=None, id=None, max=None, min=None, role=None):  # noqa: E501
        """XmlNs0ComplexRelationLegTypeRequest - a model defined in Swagger"""  # noqa: E501

        self._asset_type_id = None
        self._co_role = None
        self._id = None
        self._max = None
        self._min = None
        self._role = None
        self.discriminator = None

        if asset_type_id is not None:
            self.asset_type_id = asset_type_id
        if co_role is not None:
            self.co_role = co_role
        if id is not None:
            self.id = id
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if role is not None:
            self.role = role

    @property
    def asset_type_id(self):
        """Gets the asset_type_id of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501

        The <code>id</code> of the asset type for relation  # noqa: E501

        :return: The asset_type_id of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, asset_type_id):
        """Sets the asset_type_id of this XmlNs0ComplexRelationLegTypeRequest.

        The <code>id</code> of the asset type for relation  # noqa: E501

        :param asset_type_id: The asset_type_id of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :type: str
        """

        self._asset_type_id = asset_type_id

    @property
    def co_role(self):
        """Gets the co_role of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501

        The name of the role that the target plays  # noqa: E501

        :return: The co_role of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._co_role

    @co_role.setter
    def co_role(self, co_role):
        """Sets the co_role of this XmlNs0ComplexRelationLegTypeRequest.

        The name of the role that the target plays  # noqa: E501

        :param co_role: The co_role of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :type: str
        """

        self._co_role = co_role

    @property
    def id(self):
        """Gets the id of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501

        The id of the complex relation leg type. The leg type will be created with this id or updated. If left empty on update the leg type will be recreated.  # noqa: E501

        :return: The id of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0ComplexRelationLegTypeRequest.

        The id of the complex relation leg type. The leg type will be created with this id or updated. If left empty on update the leg type will be recreated.  # noqa: E501

        :param id: The id of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def max(self):
        """Gets the max of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501

        The maximum number of leg type occurrences  # noqa: E501

        :return: The max of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this XmlNs0ComplexRelationLegTypeRequest.

        The maximum number of leg type occurrences  # noqa: E501

        :param max: The max of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501

        The minimum number of leg type occurrences  # noqa: E501

        :return: The min of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this XmlNs0ComplexRelationLegTypeRequest.

        The minimum number of leg type occurrences  # noqa: E501

        :param min: The min of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def role(self):
        """Gets the role of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501

        The name of the role that the source plays  # noqa: E501

        :return: The role of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this XmlNs0ComplexRelationLegTypeRequest.

        The name of the role that the source plays  # noqa: E501

        :param role: The role of this XmlNs0ComplexRelationLegTypeRequest.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if not isinstance(other, XmlNs0ComplexRelationLegTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
