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

from swagger_client.models.json_application_version_impl import JsonApplicationVersionImpl  # noqa: F401,E501


class JsonApplicationInfoImpl(object):
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
        'version': 'JsonApplicationVersionImpl',
        'build_number': 'str'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'version': 'version',
        'build_number': 'buildNumber'
    }

    def __init__(self, base_url=None, version=None, build_number=None):  # noqa: E501
        """JsonApplicationInfoImpl - a model defined in Swagger"""  # noqa: E501

        self._base_url = None
        self._version = None
        self._build_number = None
        self.discriminator = None

        if base_url is not None:
            self.base_url = base_url
        if version is not None:
            self.version = version
        if build_number is not None:
            self.build_number = build_number

    @property
    def base_url(self):
        """Gets the base_url of this JsonApplicationInfoImpl.  # noqa: E501

        The base URL of the application  # noqa: E501

        :return: The base_url of this JsonApplicationInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this JsonApplicationInfoImpl.

        The base URL of the application  # noqa: E501

        :param base_url: The base_url of this JsonApplicationInfoImpl.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def version(self):
        """Gets the version of this JsonApplicationInfoImpl.  # noqa: E501

        The the version of the application  # noqa: E501

        :return: The version of this JsonApplicationInfoImpl.  # noqa: E501
        :rtype: JsonApplicationVersionImpl
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JsonApplicationInfoImpl.

        The the version of the application  # noqa: E501

        :param version: The version of this JsonApplicationInfoImpl.  # noqa: E501
        :type: JsonApplicationVersionImpl
        """

        self._version = version

    @property
    def build_number(self):
        """Gets the build_number of this JsonApplicationInfoImpl.  # noqa: E501

        The build number of the application  # noqa: E501

        :return: The build_number of this JsonApplicationInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this JsonApplicationInfoImpl.

        The build number of the application  # noqa: E501

        :param build_number: The build_number of this JsonApplicationInfoImpl.  # noqa: E501
        :type: str
        """

        self._build_number = build_number

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
        if not isinstance(other, JsonApplicationInfoImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
