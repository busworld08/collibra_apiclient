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


class XmlNs0HelpMenuItem(object):
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
        'index': 'float',
        'name': 'str',
        'show_admin_only': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'show_admin_only': 'showAdminOnly',
        'url': 'url'
    }

    def __init__(self, index=None, name=None, show_admin_only=None, url=None):  # noqa: E501
        """XmlNs0HelpMenuItem - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._name = None
        self._show_admin_only = None
        self._url = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if name is not None:
            self.name = name
        if show_admin_only is not None:
            self.show_admin_only = show_admin_only
        if url is not None:
            self.url = url

    @property
    def index(self):
        """Gets the index of this XmlNs0HelpMenuItem.  # noqa: E501

          # noqa: E501

        :return: The index of this XmlNs0HelpMenuItem.  # noqa: E501
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this XmlNs0HelpMenuItem.

          # noqa: E501

        :param index: The index of this XmlNs0HelpMenuItem.  # noqa: E501
        :type: float
        """

        self._index = index

    @property
    def name(self):
        """Gets the name of this XmlNs0HelpMenuItem.  # noqa: E501

          # noqa: E501

        :return: The name of this XmlNs0HelpMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0HelpMenuItem.

          # noqa: E501

        :param name: The name of this XmlNs0HelpMenuItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def show_admin_only(self):
        """Gets the show_admin_only of this XmlNs0HelpMenuItem.  # noqa: E501

          # noqa: E501

        :return: The show_admin_only of this XmlNs0HelpMenuItem.  # noqa: E501
        :rtype: bool
        """
        return self._show_admin_only

    @show_admin_only.setter
    def show_admin_only(self, show_admin_only):
        """Sets the show_admin_only of this XmlNs0HelpMenuItem.

          # noqa: E501

        :param show_admin_only: The show_admin_only of this XmlNs0HelpMenuItem.  # noqa: E501
        :type: bool
        """

        self._show_admin_only = show_admin_only

    @property
    def url(self):
        """Gets the url of this XmlNs0HelpMenuItem.  # noqa: E501

          # noqa: E501

        :return: The url of this XmlNs0HelpMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this XmlNs0HelpMenuItem.

          # noqa: E501

        :param url: The url of this XmlNs0HelpMenuItem.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, XmlNs0HelpMenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
