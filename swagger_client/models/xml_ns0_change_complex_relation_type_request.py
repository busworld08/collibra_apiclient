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

from swagger_client.models.xml_ns0_asset_type_symbol_type import XmlNs0AssetTypeSymbolType  # noqa: F401,E501
from swagger_client.models.xml_ns0_complex_relation_attribute_type_request import XmlNs0ComplexRelationAttributeTypeRequest  # noqa: F401,E501
from swagger_client.models.xml_ns0_complex_relation_leg_type_request import XmlNs0ComplexRelationLegTypeRequest  # noqa: F401,E501


class XmlNs0ChangeComplexRelationTypeRequest(object):
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
        'acronym_code': 'str',
        'attribute_types': 'XmlNs0ComplexRelationAttributeTypeRequest',
        'color': 'str',
        'description': 'str',
        'icon_code': 'str',
        'leg_types': 'XmlNs0ComplexRelationLegTypeRequest',
        'name': 'str',
        'symbol_type': 'XmlNs0AssetTypeSymbolType'
    }

    attribute_map = {
        'acronym_code': 'acronymCode',
        'attribute_types': 'attributeTypes',
        'color': 'color',
        'description': 'description',
        'icon_code': 'iconCode',
        'leg_types': 'legTypes',
        'name': 'name',
        'symbol_type': 'symbolType'
    }

    def __init__(self, acronym_code=None, attribute_types=None, color=None, description=None, icon_code=None, leg_types=None, name=None, symbol_type=None):  # noqa: E501
        """XmlNs0ChangeComplexRelationTypeRequest - a model defined in Swagger"""  # noqa: E501

        self._acronym_code = None
        self._attribute_types = None
        self._color = None
        self._description = None
        self._icon_code = None
        self._leg_types = None
        self._name = None
        self._symbol_type = None
        self.discriminator = None

        if acronym_code is not None:
            self.acronym_code = acronym_code
        if attribute_types is not None:
            self.attribute_types = attribute_types
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if icon_code is not None:
            self.icon_code = icon_code
        if leg_types is not None:
            self.leg_types = leg_types
        if name is not None:
            self.name = name
        if symbol_type is not None:
            self.symbol_type = symbol_type

    @property
    def acronym_code(self):
        """Gets the acronym_code of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new acronym code for the complex relation type  # noqa: E501

        :return: The acronym_code of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._acronym_code

    @acronym_code.setter
    def acronym_code(self, acronym_code):
        """Sets the acronym_code of this XmlNs0ChangeComplexRelationTypeRequest.

        The new acronym code for the complex relation type  # noqa: E501

        :param acronym_code: The acronym_code of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if acronym_code is not None and not re.search('^([A-Za-z0-9]{1,4})$', acronym_code):  # noqa: E501
            raise ValueError("Invalid value for `acronym_code`, must be a follow pattern or equal to `/^([A-Za-z0-9]{1,4})$/`")  # noqa: E501

        self._acronym_code = acronym_code

    @property
    def attribute_types(self):
        """Gets the attribute_types of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new list of attribute types for the complex relation type  # noqa: E501

        :return: The attribute_types of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: XmlNs0ComplexRelationAttributeTypeRequest
        """
        return self._attribute_types

    @attribute_types.setter
    def attribute_types(self, attribute_types):
        """Sets the attribute_types of this XmlNs0ChangeComplexRelationTypeRequest.

        The new list of attribute types for the complex relation type  # noqa: E501

        :param attribute_types: The attribute_types of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: XmlNs0ComplexRelationAttributeTypeRequest
        """

        self._attribute_types = attribute_types

    @property
    def color(self):
        """Gets the color of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The color of the symbol, in a hex format e.g. '#000000'.  This format always includes the '#' and has a size of 7  # noqa: E501

        :return: The color of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this XmlNs0ChangeComplexRelationTypeRequest.

        The color of the symbol, in a hex format e.g. '#000000'.  This format always includes the '#' and has a size of 7  # noqa: E501

        :param color: The color of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if color is not None and len(color) > 7:
            raise ValueError("Invalid value for `color`, length must be less than or equal to `7`")  # noqa: E501
        if color is not None and len(color) < 0:
            raise ValueError("Invalid value for `color`, length must be greater than or equal to `0`")  # noqa: E501
        if color is not None and not re.search('^#([A-Fa-f0-9]{6})$', color):  # noqa: E501
            raise ValueError("Invalid value for `color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6})$/`")  # noqa: E501

        self._color = color

    @property
    def description(self):
        """Gets the description of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new description for the complex relation type  # noqa: E501

        :return: The description of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XmlNs0ChangeComplexRelationTypeRequest.

        The new description for the complex relation type  # noqa: E501

        :param description: The description of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 4000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4000`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def icon_code(self):
        """Gets the icon_code of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new icon code for the complex relation type  # noqa: E501

        :return: The icon_code of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._icon_code

    @icon_code.setter
    def icon_code(self, icon_code):
        """Sets the icon_code of this XmlNs0ChangeComplexRelationTypeRequest.

        The new icon code for the complex relation type  # noqa: E501

        :param icon_code: The icon_code of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._icon_code = icon_code

    @property
    def leg_types(self):
        """Gets the leg_types of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new list of leg types for the complex relation type  # noqa: E501

        :return: The leg_types of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: XmlNs0ComplexRelationLegTypeRequest
        """
        return self._leg_types

    @leg_types.setter
    def leg_types(self, leg_types):
        """Sets the leg_types of this XmlNs0ChangeComplexRelationTypeRequest.

        The new list of leg types for the complex relation type  # noqa: E501

        :param leg_types: The leg_types of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: XmlNs0ComplexRelationLegTypeRequest
        """

        self._leg_types = leg_types

    @property
    def name(self):
        """Gets the name of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new name for the complex relation type  # noqa: E501

        :return: The name of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0ChangeComplexRelationTypeRequest.

        The new name for the complex relation type  # noqa: E501

        :param name: The name of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def symbol_type(self):
        """Gets the symbol_type of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501

        The new symbol type  # noqa: E501

        :return: The symbol_type of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :rtype: XmlNs0AssetTypeSymbolType
        """
        return self._symbol_type

    @symbol_type.setter
    def symbol_type(self, symbol_type):
        """Sets the symbol_type of this XmlNs0ChangeComplexRelationTypeRequest.

        The new symbol type  # noqa: E501

        :param symbol_type: The symbol_type of this XmlNs0ChangeComplexRelationTypeRequest.  # noqa: E501
        :type: XmlNs0AssetTypeSymbolType
        """

        self._symbol_type = symbol_type

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
        if not isinstance(other, XmlNs0ChangeComplexRelationTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
