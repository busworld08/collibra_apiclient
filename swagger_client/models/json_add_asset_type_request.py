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

from swagger_client.models.json_asset_type_symbol_type import JsonAssetTypeSymbolType  # noqa: F401,E501


class JsonAddAssetTypeRequest(object):
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
        'name': 'str',
        'description': 'str',
        'color': 'str',
        'symbol_type': 'JsonAssetTypeSymbolType',
        'icon_code': 'str',
        'acronym_code': 'str',
        'parent_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'color': 'color',
        'symbol_type': 'symbolType',
        'icon_code': 'iconCode',
        'acronym_code': 'acronymCode',
        'parent_id': 'parentId'
    }

    def __init__(self, id=None, name=None, description=None, color=None, symbol_type=None, icon_code=None, acronym_code=None, parent_id=None):  # noqa: E501
        """JsonAddAssetTypeRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._color = None
        self._symbol_type = None
        self._icon_code = None
        self._acronym_code = None
        self._parent_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if color is not None:
            self.color = color
        self.symbol_type = symbol_type
        if icon_code is not None:
            self.icon_code = icon_code
        if acronym_code is not None:
            self.acronym_code = acronym_code
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this JsonAddAssetTypeRequest.  # noqa: E501

        The <code>id</code> of the new asset type. Should be unique within all asset types. It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :return: The id of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonAddAssetTypeRequest.

        The <code>id</code> of the new asset type. Should be unique within all asset types. It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :param id: The id of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this JsonAddAssetTypeRequest.  # noqa: E501

        The name of the new asset type. Should be unique within all asset types  # noqa: E501

        :return: The name of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonAddAssetTypeRequest.

        The name of the new asset type. Should be unique within all asset types  # noqa: E501

        :param name: The name of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this JsonAddAssetTypeRequest.  # noqa: E501

        The description of the new asset type  # noqa: E501

        :return: The description of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonAddAssetTypeRequest.

        The description of the new asset type  # noqa: E501

        :param description: The description of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 4000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4000`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def color(self):
        """Gets the color of this JsonAddAssetTypeRequest.  # noqa: E501

        The color of the symbol, in a hex format e.g. '#000000'.  This format always includes the '#' and has a size of 7  # noqa: E501

        :return: The color of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this JsonAddAssetTypeRequest.

        The color of the symbol, in a hex format e.g. '#000000'.  This format always includes the '#' and has a size of 7  # noqa: E501

        :param color: The color of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """
        if color is not None and len(color) > 7:
            raise ValueError("Invalid value for `color`, length must be less than or equal to `7`")  # noqa: E501
        if color is not None and len(color) < 0:
            raise ValueError("Invalid value for `color`, length must be greater than or equal to `0`")  # noqa: E501
        if color is not None and not re.search('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', color):  # noqa: E501
            raise ValueError("Invalid value for `color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._color = color

    @property
    def symbol_type(self):
        """Gets the symbol_type of this JsonAddAssetTypeRequest.  # noqa: E501

        The symbol type  # noqa: E501

        :return: The symbol_type of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: JsonAssetTypeSymbolType
        """
        return self._symbol_type

    @symbol_type.setter
    def symbol_type(self, symbol_type):
        """Sets the symbol_type of this JsonAddAssetTypeRequest.

        The symbol type  # noqa: E501

        :param symbol_type: The symbol_type of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: JsonAssetTypeSymbolType
        """
        if symbol_type is None:
            raise ValueError("Invalid value for `symbol_type`, must not be `None`")  # noqa: E501

        self._symbol_type = symbol_type

    @property
    def icon_code(self):
        """Gets the icon_code of this JsonAddAssetTypeRequest.  # noqa: E501

        The icon code, a code representing the icon that should be shown  # noqa: E501

        :return: The icon_code of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._icon_code

    @icon_code.setter
    def icon_code(self, icon_code):
        """Sets the icon_code of this JsonAddAssetTypeRequest.

        The icon code, a code representing the icon that should be shown  # noqa: E501

        :param icon_code: The icon_code of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """

        self._icon_code = icon_code

    @property
    def acronym_code(self):
        """Gets the acronym_code of this JsonAddAssetTypeRequest.  # noqa: E501

        The acronym code, a code representing the acronym that should be shown  # noqa: E501

        :return: The acronym_code of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._acronym_code

    @acronym_code.setter
    def acronym_code(self, acronym_code):
        """Sets the acronym_code of this JsonAddAssetTypeRequest.

        The acronym code, a code representing the acronym that should be shown  # noqa: E501

        :param acronym_code: The acronym_code of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """
        if acronym_code is not None and not re.search('^([A-Za-z0-9]{1,4})$', acronym_code):  # noqa: E501
            raise ValueError("Invalid value for `acronym_code`, must be a follow pattern or equal to `/^([A-Za-z0-9]{1,4})$/`")  # noqa: E501

        self._acronym_code = acronym_code

    @property
    def parent_id(self):
        """Gets the parent_id of this JsonAddAssetTypeRequest.  # noqa: E501

        The <code>id</code> of the parent for new asset type  # noqa: E501

        :return: The parent_id of this JsonAddAssetTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this JsonAddAssetTypeRequest.

        The <code>id</code> of the parent for new asset type  # noqa: E501

        :param parent_id: The parent_id of this JsonAddAssetTypeRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

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
        if not isinstance(other, JsonAddAssetTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
