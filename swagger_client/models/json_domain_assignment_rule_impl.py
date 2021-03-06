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

from swagger_client.models.json_entity_impl import JsonEntityImpl  # noqa: F401,E501
from swagger_client.models.json_named_resource_reference_impl import JsonNamedResourceReferenceImpl  # noqa: F401,E501


class JsonDomainAssignmentRuleImpl(object):
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
        'domain_type': 'JsonNamedResourceReferenceImpl',
        'community': 'JsonNamedResourceReferenceImpl'
    }

    attribute_map = {
        'id': 'id',
        'domain_type': 'domainType',
        'community': 'community'
    }

    def __init__(self, id=None, domain_type=None, community=None):  # noqa: E501
        """JsonDomainAssignmentRuleImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._domain_type = None
        self._community = None
        self.discriminator = None

        self.id = id
        if domain_type is not None:
            self.domain_type = domain_type
        if community is not None:
            self.community = community

    @property
    def id(self):
        """Gets the id of this JsonDomainAssignmentRuleImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonDomainAssignmentRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonDomainAssignmentRuleImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonDomainAssignmentRuleImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def domain_type(self):
        """Gets the domain_type of this JsonDomainAssignmentRuleImpl.  # noqa: E501

        The reference to the domain type  # noqa: E501

        :return: The domain_type of this JsonDomainAssignmentRuleImpl.  # noqa: E501
        :rtype: JsonNamedResourceReferenceImpl
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this JsonDomainAssignmentRuleImpl.

        The reference to the domain type  # noqa: E501

        :param domain_type: The domain_type of this JsonDomainAssignmentRuleImpl.  # noqa: E501
        :type: JsonNamedResourceReferenceImpl
        """

        self._domain_type = domain_type

    @property
    def community(self):
        """Gets the community of this JsonDomainAssignmentRuleImpl.  # noqa: E501

        The reference to the community  # noqa: E501

        :return: The community of this JsonDomainAssignmentRuleImpl.  # noqa: E501
        :rtype: JsonNamedResourceReferenceImpl
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this JsonDomainAssignmentRuleImpl.

        The reference to the community  # noqa: E501

        :param community: The community of this JsonDomainAssignmentRuleImpl.  # noqa: E501
        :type: JsonNamedResourceReferenceImpl
        """

        self._community = community

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
        if not isinstance(other, JsonDomainAssignmentRuleImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
