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


class XmlNs0FormPropertyImpl(object):
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
        'asset_type': 'object',
        'date_time_type': 'str',
        'default_dropdown_values': 'object',
        'default_from_resource': 'bool',
        'enum_values': 'object',
        'id': 'str',
        'multi_default_dropdown_values': 'object',
        'multi_proposed_dropdown_values': 'object',
        'multi_value': 'bool',
        'name': 'str',
        'proposed_dropdown_values': 'object',
        'proposed_fixed': 'bool',
        'required': 'bool',
        'type': 'str',
        'value': 'str',
        'writable': 'bool'
    }

    attribute_map = {
        'asset_type': 'assetType',
        'date_time_type': 'dateTimeType',
        'default_dropdown_values': 'defaultDropdownValues',
        'default_from_resource': 'defaultFromResource',
        'enum_values': 'enumValues',
        'id': 'id',
        'multi_default_dropdown_values': 'multiDefaultDropdownValues',
        'multi_proposed_dropdown_values': 'multiProposedDropdownValues',
        'multi_value': 'multiValue',
        'name': 'name',
        'proposed_dropdown_values': 'proposedDropdownValues',
        'proposed_fixed': 'proposedFixed',
        'required': 'required',
        'type': 'type',
        'value': 'value',
        'writable': 'writable'
    }

    def __init__(self, asset_type=None, date_time_type=None, default_dropdown_values=None, default_from_resource=None, enum_values=None, id=None, multi_default_dropdown_values=None, multi_proposed_dropdown_values=None, multi_value=None, name=None, proposed_dropdown_values=None, proposed_fixed=None, required=None, type=None, value=None, writable=None):  # noqa: E501
        """XmlNs0FormPropertyImpl - a model defined in Swagger"""  # noqa: E501

        self._asset_type = None
        self._date_time_type = None
        self._default_dropdown_values = None
        self._default_from_resource = None
        self._enum_values = None
        self._id = None
        self._multi_default_dropdown_values = None
        self._multi_proposed_dropdown_values = None
        self._multi_value = None
        self._name = None
        self._proposed_dropdown_values = None
        self._proposed_fixed = None
        self._required = None
        self._type = None
        self._value = None
        self._writable = None
        self.discriminator = None

        if asset_type is not None:
            self.asset_type = asset_type
        if date_time_type is not None:
            self.date_time_type = date_time_type
        if default_dropdown_values is not None:
            self.default_dropdown_values = default_dropdown_values
        if default_from_resource is not None:
            self.default_from_resource = default_from_resource
        if enum_values is not None:
            self.enum_values = enum_values
        if id is not None:
            self.id = id
        if multi_default_dropdown_values is not None:
            self.multi_default_dropdown_values = multi_default_dropdown_values
        if multi_proposed_dropdown_values is not None:
            self.multi_proposed_dropdown_values = multi_proposed_dropdown_values
        if multi_value is not None:
            self.multi_value = multi_value
        if name is not None:
            self.name = name
        if proposed_dropdown_values is not None:
            self.proposed_dropdown_values = proposed_dropdown_values
        if proposed_fixed is not None:
            self.proposed_fixed = proposed_fixed
        if required is not None:
            self.required = required
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if writable is not None:
            self.writable = writable

    @property
    def asset_type(self):
        """Gets the asset_type of this XmlNs0FormPropertyImpl.  # noqa: E501

        The asset type  # noqa: E501

        :return: The asset_type of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: object
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this XmlNs0FormPropertyImpl.

        The asset type  # noqa: E501

        :param asset_type: The asset_type of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: object
        """

        self._asset_type = asset_type

    @property
    def date_time_type(self):
        """Gets the date_time_type of this XmlNs0FormPropertyImpl.  # noqa: E501

        The datetime type in case the property is of type datetime  # noqa: E501

        :return: The date_time_type of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: str
        """
        return self._date_time_type

    @date_time_type.setter
    def date_time_type(self, date_time_type):
        """Sets the date_time_type of this XmlNs0FormPropertyImpl.

        The datetime type in case the property is of type datetime  # noqa: E501

        :param date_time_type: The date_time_type of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: str
        """

        self._date_time_type = date_time_type

    @property
    def default_dropdown_values(self):
        """Gets the default_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501

        The property's default droprownd values  # noqa: E501

        :return: The default_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: object
        """
        return self._default_dropdown_values

    @default_dropdown_values.setter
    def default_dropdown_values(self, default_dropdown_values):
        """Sets the default_dropdown_values of this XmlNs0FormPropertyImpl.

        The property's default droprownd values  # noqa: E501

        :param default_dropdown_values: The default_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: object
        """

        self._default_dropdown_values = default_dropdown_values

    @property
    def default_from_resource(self):
        """Gets the default_from_resource of this XmlNs0FormPropertyImpl.  # noqa: E501

        Whether the property's default value is the current resource  # noqa: E501

        :return: The default_from_resource of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: bool
        """
        return self._default_from_resource

    @default_from_resource.setter
    def default_from_resource(self, default_from_resource):
        """Sets the default_from_resource of this XmlNs0FormPropertyImpl.

        Whether the property's default value is the current resource  # noqa: E501

        :param default_from_resource: The default_from_resource of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: bool
        """

        self._default_from_resource = default_from_resource

    @property
    def enum_values(self):
        """Gets the enum_values of this XmlNs0FormPropertyImpl.  # noqa: E501

        The property's enum values  # noqa: E501

        :return: The enum_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: object
        """
        return self._enum_values

    @enum_values.setter
    def enum_values(self, enum_values):
        """Sets the enum_values of this XmlNs0FormPropertyImpl.

        The property's enum values  # noqa: E501

        :param enum_values: The enum_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: object
        """

        self._enum_values = enum_values

    @property
    def id(self):
        """Gets the id of this XmlNs0FormPropertyImpl.  # noqa: E501

        The id of the property  # noqa: E501

        :return: The id of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0FormPropertyImpl.

        The id of the property  # noqa: E501

        :param id: The id of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def multi_default_dropdown_values(self):
        """Gets the multi_default_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501

        The multi default dropdown values  # noqa: E501

        :return: The multi_default_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: object
        """
        return self._multi_default_dropdown_values

    @multi_default_dropdown_values.setter
    def multi_default_dropdown_values(self, multi_default_dropdown_values):
        """Sets the multi_default_dropdown_values of this XmlNs0FormPropertyImpl.

        The multi default dropdown values  # noqa: E501

        :param multi_default_dropdown_values: The multi_default_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: object
        """

        self._multi_default_dropdown_values = multi_default_dropdown_values

    @property
    def multi_proposed_dropdown_values(self):
        """Gets the multi_proposed_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501

        The multi proposed dropdown values  # noqa: E501

        :return: The multi_proposed_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: object
        """
        return self._multi_proposed_dropdown_values

    @multi_proposed_dropdown_values.setter
    def multi_proposed_dropdown_values(self, multi_proposed_dropdown_values):
        """Sets the multi_proposed_dropdown_values of this XmlNs0FormPropertyImpl.

        The multi proposed dropdown values  # noqa: E501

        :param multi_proposed_dropdown_values: The multi_proposed_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: object
        """

        self._multi_proposed_dropdown_values = multi_proposed_dropdown_values

    @property
    def multi_value(self):
        """Gets the multi_value of this XmlNs0FormPropertyImpl.  # noqa: E501

        Whether the property allows multiple values  # noqa: E501

        :return: The multi_value of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: bool
        """
        return self._multi_value

    @multi_value.setter
    def multi_value(self, multi_value):
        """Sets the multi_value of this XmlNs0FormPropertyImpl.

        Whether the property allows multiple values  # noqa: E501

        :param multi_value: The multi_value of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: bool
        """

        self._multi_value = multi_value

    @property
    def name(self):
        """Gets the name of this XmlNs0FormPropertyImpl.  # noqa: E501

        The name of the property  # noqa: E501

        :return: The name of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0FormPropertyImpl.

        The name of the property  # noqa: E501

        :param name: The name of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def proposed_dropdown_values(self):
        """Gets the proposed_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501

        The property's proposed dropdown values  # noqa: E501

        :return: The proposed_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: object
        """
        return self._proposed_dropdown_values

    @proposed_dropdown_values.setter
    def proposed_dropdown_values(self, proposed_dropdown_values):
        """Sets the proposed_dropdown_values of this XmlNs0FormPropertyImpl.

        The property's proposed dropdown values  # noqa: E501

        :param proposed_dropdown_values: The proposed_dropdown_values of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: object
        """

        self._proposed_dropdown_values = proposed_dropdown_values

    @property
    def proposed_fixed(self):
        """Gets the proposed_fixed of this XmlNs0FormPropertyImpl.  # noqa: E501

        Whether the property's proposed values are the only set of allowed values to select  # noqa: E501

        :return: The proposed_fixed of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: bool
        """
        return self._proposed_fixed

    @proposed_fixed.setter
    def proposed_fixed(self, proposed_fixed):
        """Sets the proposed_fixed of this XmlNs0FormPropertyImpl.

        Whether the property's proposed values are the only set of allowed values to select  # noqa: E501

        :param proposed_fixed: The proposed_fixed of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: bool
        """

        self._proposed_fixed = proposed_fixed

    @property
    def required(self):
        """Gets the required of this XmlNs0FormPropertyImpl.  # noqa: E501

        Whether the property is required  # noqa: E501

        :return: The required of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this XmlNs0FormPropertyImpl.

        Whether the property is required  # noqa: E501

        :param required: The required of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def type(self):
        """Gets the type of this XmlNs0FormPropertyImpl.  # noqa: E501

        The property type  # noqa: E501

        :return: The type of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XmlNs0FormPropertyImpl.

        The property type  # noqa: E501

        :param type: The type of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this XmlNs0FormPropertyImpl.  # noqa: E501

        The property (default) value  # noqa: E501

        :return: The value of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this XmlNs0FormPropertyImpl.

        The property (default) value  # noqa: E501

        :param value: The value of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def writable(self):
        """Gets the writable of this XmlNs0FormPropertyImpl.  # noqa: E501

        Whether the property is writable  # noqa: E501

        :return: The writable of this XmlNs0FormPropertyImpl.  # noqa: E501
        :rtype: bool
        """
        return self._writable

    @writable.setter
    def writable(self, writable):
        """Sets the writable of this XmlNs0FormPropertyImpl.

        Whether the property is writable  # noqa: E501

        :param writable: The writable of this XmlNs0FormPropertyImpl.  # noqa: E501
        :type: bool
        """

        self._writable = writable

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
        if not isinstance(other, XmlNs0FormPropertyImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
