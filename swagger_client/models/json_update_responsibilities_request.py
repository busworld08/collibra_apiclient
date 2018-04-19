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


class JsonUpdateResponsibilitiesRequest(object):
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
        'role_id': 'str',
        'owner_ids': 'list[str]',
        'resource_references': 'list[object]'
    }

    attribute_map = {
        'role_id': 'roleId',
        'owner_ids': 'ownerIds',
        'resource_references': 'resourceReferences'
    }

    def __init__(self, role_id=None, owner_ids=None, resource_references=None):  # noqa: E501
        """JsonUpdateResponsibilitiesRequest - a model defined in Swagger"""  # noqa: E501

        self._role_id = None
        self._owner_ids = None
        self._resource_references = None
        self.discriminator = None

        self.role_id = role_id
        self.owner_ids = owner_ids
        if resource_references is not None:
            self.resource_references = resource_references

    @property
    def role_id(self):
        """Gets the role_id of this JsonUpdateResponsibilitiesRequest.  # noqa: E501

          # noqa: E501

        :return: The role_id of this JsonUpdateResponsibilitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this JsonUpdateResponsibilitiesRequest.

          # noqa: E501

        :param role_id: The role_id of this JsonUpdateResponsibilitiesRequest.  # noqa: E501
        :type: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def owner_ids(self):
        """Gets the owner_ids of this JsonUpdateResponsibilitiesRequest.  # noqa: E501

          # noqa: E501

        :return: The owner_ids of this JsonUpdateResponsibilitiesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this JsonUpdateResponsibilitiesRequest.

          # noqa: E501

        :param owner_ids: The owner_ids of this JsonUpdateResponsibilitiesRequest.  # noqa: E501
        :type: list[str]
        """
        if owner_ids is None:
            raise ValueError("Invalid value for `owner_ids`, must not be `None`")  # noqa: E501

        self._owner_ids = owner_ids

    @property
    def resource_references(self):
        """Gets the resource_references of this JsonUpdateResponsibilitiesRequest.  # noqa: E501

          # noqa: E501

        :return: The resource_references of this JsonUpdateResponsibilitiesRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._resource_references

    @resource_references.setter
    def resource_references(self, resource_references):
        """Sets the resource_references of this JsonUpdateResponsibilitiesRequest.

          # noqa: E501

        :param resource_references: The resource_references of this JsonUpdateResponsibilitiesRequest.  # noqa: E501
        :type: list[object]
        """

        self._resource_references = resource_references

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
        if not isinstance(other, JsonUpdateResponsibilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
