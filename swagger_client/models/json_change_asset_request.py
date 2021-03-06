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


class JsonChangeAssetRequest(object):
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
        'type_id': 'str',
        'status_id': 'str',
        'domain_id': 'str',
        'excluded_from_auto_hyperlinking': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type_id': 'typeId',
        'status_id': 'statusId',
        'domain_id': 'domainId',
        'excluded_from_auto_hyperlinking': 'excludedFromAutoHyperlinking'
    }

    def __init__(self, id=None, name=None, type_id=None, status_id=None, domain_id=None, excluded_from_auto_hyperlinking=None):  # noqa: E501
        """JsonChangeAssetRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._type_id = None
        self._status_id = None
        self._domain_id = None
        self._excluded_from_auto_hyperlinking = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if type_id is not None:
            self.type_id = type_id
        if status_id is not None:
            self.status_id = status_id
        if domain_id is not None:
            self.domain_id = domain_id
        if excluded_from_auto_hyperlinking is not None:
            self.excluded_from_auto_hyperlinking = excluded_from_auto_hyperlinking

    @property
    def id(self):
        """Gets the id of this JsonChangeAssetRequest.  # noqa: E501

        The <code>id</code> of the asset to be changed. Silently ignored if the <code>id</code> is provided as path parameter of the request  # noqa: E501

        :return: The id of this JsonChangeAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonChangeAssetRequest.

        The <code>id</code> of the asset to be changed. Silently ignored if the <code>id</code> is provided as path parameter of the request  # noqa: E501

        :param id: The id of this JsonChangeAssetRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this JsonChangeAssetRequest.  # noqa: E501

        The new name for the asset  # noqa: E501

        :return: The name of this JsonChangeAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonChangeAssetRequest.

        The new name for the asset  # noqa: E501

        :param name: The name of this JsonChangeAssetRequest.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type_id(self):
        """Gets the type_id of this JsonChangeAssetRequest.  # noqa: E501

        The <code>id</code> of the new asset type for the asset  # noqa: E501

        :return: The type_id of this JsonChangeAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this JsonChangeAssetRequest.

        The <code>id</code> of the new asset type for the asset  # noqa: E501

        :param type_id: The type_id of this JsonChangeAssetRequest.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

    @property
    def status_id(self):
        """Gets the status_id of this JsonChangeAssetRequest.  # noqa: E501

        The <code>id</code> of the new status for the asset  # noqa: E501

        :return: The status_id of this JsonChangeAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this JsonChangeAssetRequest.

        The <code>id</code> of the new status for the asset  # noqa: E501

        :param status_id: The status_id of this JsonChangeAssetRequest.  # noqa: E501
        :type: str
        """

        self._status_id = status_id

    @property
    def domain_id(self):
        """Gets the domain_id of this JsonChangeAssetRequest.  # noqa: E501

        The <code>id</code> of the new domain for the asset  # noqa: E501

        :return: The domain_id of this JsonChangeAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this JsonChangeAssetRequest.

        The <code>id</code> of the new domain for the asset  # noqa: E501

        :param domain_id: The domain_id of this JsonChangeAssetRequest.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def excluded_from_auto_hyperlinking(self):
        """Gets the excluded_from_auto_hyperlinking of this JsonChangeAssetRequest.  # noqa: E501

        Whether the asset should be excluded from hyperlinking or not  # noqa: E501

        :return: The excluded_from_auto_hyperlinking of this JsonChangeAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._excluded_from_auto_hyperlinking

    @excluded_from_auto_hyperlinking.setter
    def excluded_from_auto_hyperlinking(self, excluded_from_auto_hyperlinking):
        """Sets the excluded_from_auto_hyperlinking of this JsonChangeAssetRequest.

        Whether the asset should be excluded from hyperlinking or not  # noqa: E501

        :param excluded_from_auto_hyperlinking: The excluded_from_auto_hyperlinking of this JsonChangeAssetRequest.  # noqa: E501
        :type: bool
        """

        self._excluded_from_auto_hyperlinking = excluded_from_auto_hyperlinking

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
        if not isinstance(other, JsonChangeAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
