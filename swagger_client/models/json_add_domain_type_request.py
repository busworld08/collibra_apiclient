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


class JsonAddDomainTypeRequest(object):
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
        'parent_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'parent_id': 'parentId'
    }

    def __init__(self, id=None, name=None, description=None, parent_id=None):  # noqa: E501
        """JsonAddDomainTypeRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._parent_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this JsonAddDomainTypeRequest.  # noqa: E501

        The <code>id</code> of the new domain type. Should be unique within all domain types. It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix  # noqa: E501

        :return: The id of this JsonAddDomainTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonAddDomainTypeRequest.

        The <code>id</code> of the new domain type. Should be unique within all domain types. It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix  # noqa: E501

        :param id: The id of this JsonAddDomainTypeRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this JsonAddDomainTypeRequest.  # noqa: E501

        The name of the new domain type. Should be unique within all domain types  # noqa: E501

        :return: The name of this JsonAddDomainTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonAddDomainTypeRequest.

        The name of the new domain type. Should be unique within all domain types  # noqa: E501

        :param name: The name of this JsonAddDomainTypeRequest.  # noqa: E501
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
        """Gets the description of this JsonAddDomainTypeRequest.  # noqa: E501

        The description of the new domain type  # noqa: E501

        :return: The description of this JsonAddDomainTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonAddDomainTypeRequest.

        The description of the new domain type  # noqa: E501

        :param description: The description of this JsonAddDomainTypeRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 4000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4000`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def parent_id(self):
        """Gets the parent_id of this JsonAddDomainTypeRequest.  # noqa: E501

        The <code>id</code> of the parent for new domain type  # noqa: E501

        :return: The parent_id of this JsonAddDomainTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this JsonAddDomainTypeRequest.

        The <code>id</code> of the parent for new domain type  # noqa: E501

        :param parent_id: The parent_id of this JsonAddDomainTypeRequest.  # noqa: E501
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
        if not isinstance(other, JsonAddDomainTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
