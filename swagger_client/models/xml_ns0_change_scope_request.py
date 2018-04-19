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


class XmlNs0ChangeScopeRequest(object):
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
        'community_ids': 'str',
        'description': 'str',
        'domain_ids': 'str',
        'name': 'str'
    }

    attribute_map = {
        'community_ids': 'communityIds',
        'description': 'description',
        'domain_ids': 'domainIds',
        'name': 'name'
    }

    def __init__(self, community_ids=None, description=None, domain_ids=None, name=None):  # noqa: E501
        """XmlNs0ChangeScopeRequest - a model defined in Swagger"""  # noqa: E501

        self._community_ids = None
        self._description = None
        self._domain_ids = None
        self._name = None
        self.discriminator = None

        if community_ids is not None:
            self.community_ids = community_ids
        if description is not None:
            self.description = description
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if name is not None:
            self.name = name

    @property
    def community_ids(self):
        """Gets the community_ids of this XmlNs0ChangeScopeRequest.  # noqa: E501

        The new list of <code>id</code>s of communities that should included in the scope  # noqa: E501

        :return: The community_ids of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :rtype: str
        """
        return self._community_ids

    @community_ids.setter
    def community_ids(self, community_ids):
        """Sets the community_ids of this XmlNs0ChangeScopeRequest.

        The new list of <code>id</code>s of communities that should included in the scope  # noqa: E501

        :param community_ids: The community_ids of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :type: str
        """

        self._community_ids = community_ids

    @property
    def description(self):
        """Gets the description of this XmlNs0ChangeScopeRequest.  # noqa: E501

        The new description for the scope  # noqa: E501

        :return: The description of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XmlNs0ChangeScopeRequest.

        The new description for the scope  # noqa: E501

        :param description: The description of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def domain_ids(self):
        """Gets the domain_ids of this XmlNs0ChangeScopeRequest.  # noqa: E501

        The new list of <code>id</code>s of domains that should included in the scope  # noqa: E501

        :return: The domain_ids of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        """Sets the domain_ids of this XmlNs0ChangeScopeRequest.

        The new list of <code>id</code>s of domains that should included in the scope  # noqa: E501

        :param domain_ids: The domain_ids of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :type: str
        """

        self._domain_ids = domain_ids

    @property
    def name(self):
        """Gets the name of this XmlNs0ChangeScopeRequest.  # noqa: E501

        The new name for the scope  # noqa: E501

        :return: The name of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0ChangeScopeRequest.

        The new name for the scope  # noqa: E501

        :param name: The name of this XmlNs0ChangeScopeRequest.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, XmlNs0ChangeScopeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
