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

from swagger_client.models.json_assigned_characteristic_type_impl import JsonAssignedCharacteristicTypeImpl  # noqa: F401,E501
from swagger_client.models.json_relation_type_direction import JsonRelationTypeDirection  # noqa: F401,E501


class JsonAssignedRelationTypeImpl(object):
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
        'minimum_occurrences': 'float',
        'maximum_occurrences': 'float',
        'read_only': 'bool',
        'system': 'bool',
        'role_direction': 'JsonRelationTypeDirection',
        'relation_type': 'object'
    }

    attribute_map = {
        'id': 'id',
        'minimum_occurrences': 'minimumOccurrences',
        'maximum_occurrences': 'maximumOccurrences',
        'read_only': 'readOnly',
        'system': 'system',
        'role_direction': 'roleDirection',
        'relation_type': 'relationType'
    }

    def __init__(self, id=None, minimum_occurrences=None, maximum_occurrences=None, read_only=None, system=None, role_direction=None, relation_type=None):  # noqa: E501
        """JsonAssignedRelationTypeImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._minimum_occurrences = None
        self._maximum_occurrences = None
        self._read_only = None
        self._system = None
        self._role_direction = None
        self._relation_type = None
        self.discriminator = None

        self.id = id
        if minimum_occurrences is not None:
            self.minimum_occurrences = minimum_occurrences
        if maximum_occurrences is not None:
            self.maximum_occurrences = maximum_occurrences
        if read_only is not None:
            self.read_only = read_only
        if system is not None:
            self.system = system
        if role_direction is not None:
            self.role_direction = role_direction
        if relation_type is not None:
            self.relation_type = relation_type

    @property
    def id(self):
        """Gets the id of this JsonAssignedRelationTypeImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonAssignedRelationTypeImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def minimum_occurrences(self):
        """Gets the minimum_occurrences of this JsonAssignedRelationTypeImpl.  # noqa: E501

        How many times at least the assigned characteristic must be added to the resource. Zero means no restriction  # noqa: E501

        :return: The minimum_occurrences of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: float
        """
        return self._minimum_occurrences

    @minimum_occurrences.setter
    def minimum_occurrences(self, minimum_occurrences):
        """Sets the minimum_occurrences of this JsonAssignedRelationTypeImpl.

        How many times at least the assigned characteristic must be added to the resource. Zero means no restriction  # noqa: E501

        :param minimum_occurrences: The minimum_occurrences of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: float
        """

        self._minimum_occurrences = minimum_occurrences

    @property
    def maximum_occurrences(self):
        """Gets the maximum_occurrences of this JsonAssignedRelationTypeImpl.  # noqa: E501

        How many times at least the assigned characteristic may be added to the resource. Null means no limit  # noqa: E501

        :return: The maximum_occurrences of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: float
        """
        return self._maximum_occurrences

    @maximum_occurrences.setter
    def maximum_occurrences(self, maximum_occurrences):
        """Sets the maximum_occurrences of this JsonAssignedRelationTypeImpl.

        How many times at least the assigned characteristic may be added to the resource. Null means no limit  # noqa: E501

        :param maximum_occurrences: The maximum_occurrences of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: float
        """

        self._maximum_occurrences = maximum_occurrences

    @property
    def read_only(self):
        """Gets the read_only of this JsonAssignedRelationTypeImpl.  # noqa: E501

        Whether the characteristic value of the assigned type can be edited by the user  # noqa: E501

        :return: The read_only of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this JsonAssignedRelationTypeImpl.

        Whether the characteristic value of the assigned type can be edited by the user  # noqa: E501

        :param read_only: The read_only of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def system(self):
        """Gets the system of this JsonAssignedRelationTypeImpl.  # noqa: E501

        Whether the characteristic type can be unassigned  # noqa: E501

        :return: The system of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this JsonAssignedRelationTypeImpl.

        Whether the characteristic type can be unassigned  # noqa: E501

        :param system: The system of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def role_direction(self):
        """Gets the role_direction of this JsonAssignedRelationTypeImpl.  # noqa: E501

        The direction of the relation type  # noqa: E501

        :return: The role_direction of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: JsonRelationTypeDirection
        """
        return self._role_direction

    @role_direction.setter
    def role_direction(self, role_direction):
        """Sets the role_direction of this JsonAssignedRelationTypeImpl.

        The direction of the relation type  # noqa: E501

        :param role_direction: The role_direction of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: JsonRelationTypeDirection
        """

        self._role_direction = role_direction

    @property
    def relation_type(self):
        """Gets the relation_type of this JsonAssignedRelationTypeImpl.  # noqa: E501

        The relation type to be assigned  # noqa: E501

        :return: The relation_type of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :rtype: object
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this JsonAssignedRelationTypeImpl.

        The relation type to be assigned  # noqa: E501

        :param relation_type: The relation_type of this JsonAssignedRelationTypeImpl.  # noqa: E501
        :type: object
        """

        self._relation_type = relation_type

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
        if not isinstance(other, JsonAssignedRelationTypeImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
