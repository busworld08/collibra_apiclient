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


class JsonDropdownValueImpl(object):
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
        'text': 'str',
        'parents': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'parents': 'parents'
    }

    def __init__(self, id=None, text=None, parents=None):  # noqa: E501
        """JsonDropdownValueImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._text = None
        self._parents = None
        self.discriminator = None

        self.id = id
        if text is not None:
            self.text = text
        if parents is not None:
            self.parents = parents

    @property
    def id(self):
        """Gets the id of this JsonDropdownValueImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonDropdownValueImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonDropdownValueImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonDropdownValueImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def text(self):
        """Gets the text of this JsonDropdownValueImpl.  # noqa: E501

        The text  # noqa: E501

        :return: The text of this JsonDropdownValueImpl.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this JsonDropdownValueImpl.

        The text  # noqa: E501

        :param text: The text of this JsonDropdownValueImpl.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def parents(self):
        """Gets the parents of this JsonDropdownValueImpl.  # noqa: E501

        The list of parents  # noqa: E501

        :return: The parents of this JsonDropdownValueImpl.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this JsonDropdownValueImpl.

        The list of parents  # noqa: E501

        :param parents: The parents of this JsonDropdownValueImpl.  # noqa: E501
        :type: list[str]
        """

        self._parents = parents

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
        if not isinstance(other, JsonDropdownValueImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
