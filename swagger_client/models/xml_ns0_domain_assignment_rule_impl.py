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

from swagger_client.models.xml_ns0_entity_impl import XmlNs0EntityImpl  # noqa: F401,E501


class XmlNs0DomainAssignmentRuleImpl(object):
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
        'community': 'object',
        'domain_type': 'object'
    }

    attribute_map = {
        'id': 'id',
        'community': 'community',
        'domain_type': 'domainType'
    }

    def __init__(self, id=None, community=None, domain_type=None):  # noqa: E501
        """XmlNs0DomainAssignmentRuleImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._community = None
        self._domain_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if community is not None:
            self.community = community
        if domain_type is not None:
            self.domain_type = domain_type

    @property
    def id(self):
        """Gets the id of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0DomainAssignmentRuleImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def community(self):
        """Gets the community of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501

        The reference to the community  # noqa: E501

        :return: The community of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501
        :rtype: object
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this XmlNs0DomainAssignmentRuleImpl.

        The reference to the community  # noqa: E501

        :param community: The community of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501
        :type: object
        """

        self._community = community

    @property
    def domain_type(self):
        """Gets the domain_type of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501

        The reference to the domain type  # noqa: E501

        :return: The domain_type of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501
        :rtype: object
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this XmlNs0DomainAssignmentRuleImpl.

        The reference to the domain type  # noqa: E501

        :param domain_type: The domain_type of this XmlNs0DomainAssignmentRuleImpl.  # noqa: E501
        :type: object
        """

        self._domain_type = domain_type

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
        if not isinstance(other, XmlNs0DomainAssignmentRuleImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
