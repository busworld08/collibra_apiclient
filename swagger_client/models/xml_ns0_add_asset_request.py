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


class XmlNs0AddAssetRequest(object):
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
        'domain_id': 'str',
        'name': 'str',
        'type_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domainId',
        'name': 'name',
        'type_id': 'typeId'
    }

    def __init__(self, domain_id=None, name=None, type_id=None):  # noqa: E501
        """XmlNs0AddAssetRequest - a model defined in Swagger"""  # noqa: E501

        self._domain_id = None
        self._name = None
        self._type_id = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if type_id is not None:
            self.type_id = type_id

    @property
    def domain_id(self):
        """Gets the domain_id of this XmlNs0AddAssetRequest.  # noqa: E501

        The <code>id</code> of the domain that the new asset should be added to  # noqa: E501

        :return: The domain_id of this XmlNs0AddAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this XmlNs0AddAssetRequest.

        The <code>id</code> of the domain that the new asset should be added to  # noqa: E501

        :param domain_id: The domain_id of this XmlNs0AddAssetRequest.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this XmlNs0AddAssetRequest.  # noqa: E501

        The name of the new asset. Should be unique within the domain  # noqa: E501

        :return: The name of this XmlNs0AddAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0AddAssetRequest.

        The name of the new asset. Should be unique within the domain  # noqa: E501

        :param name: The name of this XmlNs0AddAssetRequest.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type_id(self):
        """Gets the type_id of this XmlNs0AddAssetRequest.  # noqa: E501

        The <code>id</code> of the asset type of the new asset  # noqa: E501

        :return: The type_id of this XmlNs0AddAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this XmlNs0AddAssetRequest.

        The <code>id</code> of the asset type of the new asset  # noqa: E501

        :param type_id: The type_id of this XmlNs0AddAssetRequest.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

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
        if not isinstance(other, XmlNs0AddAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other