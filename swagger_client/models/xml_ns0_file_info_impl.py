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


class XmlNs0FileInfoImpl(object):
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
        'content_type': 'str',
        'extension': 'str',
        'id': 'str',
        'name': 'str',
        'size': 'float'
    }

    attribute_map = {
        'content_type': 'contentType',
        'extension': 'extension',
        'id': 'id',
        'name': 'name',
        'size': 'size'
    }

    def __init__(self, content_type=None, extension=None, id=None, name=None, size=None):  # noqa: E501
        """XmlNs0FileInfoImpl - a model defined in Swagger"""  # noqa: E501

        self._content_type = None
        self._extension = None
        self._id = None
        self._name = None
        self._size = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if extension is not None:
            self.extension = extension
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size

    @property
    def content_type(self):
        """Gets the content_type of this XmlNs0FileInfoImpl.  # noqa: E501

        The MIME type of the file content  # noqa: E501

        :return: The content_type of this XmlNs0FileInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this XmlNs0FileInfoImpl.

        The MIME type of the file content  # noqa: E501

        :param content_type: The content_type of this XmlNs0FileInfoImpl.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def extension(self):
        """Gets the extension of this XmlNs0FileInfoImpl.  # noqa: E501

        The extension of the file  # noqa: E501

        :return: The extension of this XmlNs0FileInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this XmlNs0FileInfoImpl.

        The extension of the file  # noqa: E501

        :param extension: The extension of this XmlNs0FileInfoImpl.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def id(self):
        """Gets the id of this XmlNs0FileInfoImpl.  # noqa: E501

        The <code>id</code> of the file  # noqa: E501

        :return: The id of this XmlNs0FileInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0FileInfoImpl.

        The <code>id</code> of the file  # noqa: E501

        :param id: The id of this XmlNs0FileInfoImpl.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this XmlNs0FileInfoImpl.  # noqa: E501

        The name of the file  # noqa: E501

        :return: The name of this XmlNs0FileInfoImpl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0FileInfoImpl.

        The name of the file  # noqa: E501

        :param name: The name of this XmlNs0FileInfoImpl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this XmlNs0FileInfoImpl.  # noqa: E501

        The size of the file  # noqa: E501

        :return: The size of this XmlNs0FileInfoImpl.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this XmlNs0FileInfoImpl.

        The size of the file  # noqa: E501

        :param size: The size of this XmlNs0FileInfoImpl.  # noqa: E501
        :type: float
        """

        self._size = size

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
        if not isinstance(other, XmlNs0FileInfoImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
