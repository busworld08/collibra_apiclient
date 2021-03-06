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


class JsonFormDataImpl(object):
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
        'form_key': 'str',
        'form_properties': 'list[object]'
    }

    attribute_map = {
        'form_key': 'formKey',
        'form_properties': 'formProperties'
    }

    def __init__(self, form_key=None, form_properties=None):  # noqa: E501
        """JsonFormDataImpl - a model defined in Swagger"""  # noqa: E501

        self._form_key = None
        self._form_properties = None
        self.discriminator = None

        if form_key is not None:
            self.form_key = form_key
        if form_properties is not None:
            self.form_properties = form_properties

    @property
    def form_key(self):
        """Gets the form_key of this JsonFormDataImpl.  # noqa: E501

        Returns the form key.  # noqa: E501

        :return: The form_key of this JsonFormDataImpl.  # noqa: E501
        :rtype: str
        """
        return self._form_key

    @form_key.setter
    def form_key(self, form_key):
        """Sets the form_key of this JsonFormDataImpl.

        Returns the form key.  # noqa: E501

        :param form_key: The form_key of this JsonFormDataImpl.  # noqa: E501
        :type: str
        """

        self._form_key = form_key

    @property
    def form_properties(self):
        """Gets the form_properties of this JsonFormDataImpl.  # noqa: E501

        Returns the List of FormProperty.  # noqa: E501

        :return: The form_properties of this JsonFormDataImpl.  # noqa: E501
        :rtype: list[object]
        """
        return self._form_properties

    @form_properties.setter
    def form_properties(self, form_properties):
        """Sets the form_properties of this JsonFormDataImpl.

        Returns the List of FormProperty.  # noqa: E501

        :param form_properties: The form_properties of this JsonFormDataImpl.  # noqa: E501
        :type: list[object]
        """

        self._form_properties = form_properties

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
        if not isinstance(other, JsonFormDataImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
