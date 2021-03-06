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


class XmlNs0BrowserSearchRequest(object):
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
        'asset_type_ids': 'str',
        'domain_type_id': 'str',
        'limit': 'float',
        'name': 'str'
    }

    attribute_map = {
        'asset_type_ids': 'assetTypeIds',
        'domain_type_id': 'domainTypeId',
        'limit': 'limit',
        'name': 'name'
    }

    def __init__(self, asset_type_ids=None, domain_type_id=None, limit=None, name=None):  # noqa: E501
        """XmlNs0BrowserSearchRequest - a model defined in Swagger"""  # noqa: E501

        self._asset_type_ids = None
        self._domain_type_id = None
        self._limit = None
        self._name = None
        self.discriminator = None

        if asset_type_ids is not None:
            self.asset_type_ids = asset_type_ids
        if domain_type_id is not None:
            self.domain_type_id = domain_type_id
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name

    @property
    def asset_type_ids(self):
        """Gets the asset_type_ids of this XmlNs0BrowserSearchRequest.  # noqa: E501

          # noqa: E501

        :return: The asset_type_ids of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_type_ids

    @asset_type_ids.setter
    def asset_type_ids(self, asset_type_ids):
        """Sets the asset_type_ids of this XmlNs0BrowserSearchRequest.

          # noqa: E501

        :param asset_type_ids: The asset_type_ids of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :type: str
        """

        self._asset_type_ids = asset_type_ids

    @property
    def domain_type_id(self):
        """Gets the domain_type_id of this XmlNs0BrowserSearchRequest.  # noqa: E501

          # noqa: E501

        :return: The domain_type_id of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_type_id

    @domain_type_id.setter
    def domain_type_id(self, domain_type_id):
        """Sets the domain_type_id of this XmlNs0BrowserSearchRequest.

          # noqa: E501

        :param domain_type_id: The domain_type_id of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :type: str
        """

        self._domain_type_id = domain_type_id

    @property
    def limit(self):
        """Gets the limit of this XmlNs0BrowserSearchRequest.  # noqa: E501

          # noqa: E501

        :return: The limit of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this XmlNs0BrowserSearchRequest.

          # noqa: E501

        :param limit: The limit of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def name(self):
        """Gets the name of this XmlNs0BrowserSearchRequest.  # noqa: E501

          # noqa: E501

        :return: The name of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0BrowserSearchRequest.

          # noqa: E501

        :param name: The name of this XmlNs0BrowserSearchRequest.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, XmlNs0BrowserSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
