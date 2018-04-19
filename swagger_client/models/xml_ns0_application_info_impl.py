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


class XmlNs0ApplicationInfoImpl(object):
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
        'base_url': 'str',
        'build_number': 'str',
        'version': 'object'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'build_number': 'buildNumber',
        'version': 'version'
    }

    def __init__(self, base_url=None, build_number=None, version=None):  # noqa: E501
        """XmlNs0ApplicationInfoImpl - a model defined in Swagger"""  # noqa: E501

        self._base_url = None
        self._build_number = None
        self._version = None
        self.discriminator = None

        if base_url is not None:
            self.base_url = base_url
        if build_number is not None:
            self.build_number = build_number
        if version is not None:
            self.version = version

    @property
    def base_url(self):
        """Gets the base_url of this XmlNs0ApplicationInfoImpl.  # noqa: E501

        The base URL of the application  # noqa: E501

        :return: The base_url of this XmlNs0ApplicationInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this XmlNs0ApplicationInfoImpl.

        The base URL of the application  # noqa: E501

        :param base_url: The base_url of this XmlNs0ApplicationInfoImpl.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def build_number(self):
        """Gets the build_number of this XmlNs0ApplicationInfoImpl.  # noqa: E501

        The build number of the application  # noqa: E501

        :return: The build_number of this XmlNs0ApplicationInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this XmlNs0ApplicationInfoImpl.

        The build number of the application  # noqa: E501

        :param build_number: The build_number of this XmlNs0ApplicationInfoImpl.  # noqa: E501
        :type: str
        """

        self._build_number = build_number

    @property
    def version(self):
        """Gets the version of this XmlNs0ApplicationInfoImpl.  # noqa: E501

        The the version of the application  # noqa: E501

        :return: The version of this XmlNs0ApplicationInfoImpl.  # noqa: E501
        :rtype: object
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this XmlNs0ApplicationInfoImpl.

        The the version of the application  # noqa: E501

        :param version: The version of this XmlNs0ApplicationInfoImpl.  # noqa: E501
        :type: object
        """

        self._version = version

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
        if not isinstance(other, XmlNs0ApplicationInfoImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
