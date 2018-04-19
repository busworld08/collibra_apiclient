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

from swagger_client.models.xml_ns0_paged_request import XmlNs0PagedRequest  # noqa: F401,E501


class XmlNs0FindUsersRequest(object):
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
        'limit': 'float',
        'offset': 'float',
        'group_id': 'str',
        'include_disabled': 'bool',
        'name': 'str',
        'only_logged_in': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'group_id': 'groupId',
        'include_disabled': 'includeDisabled',
        'name': 'name',
        'only_logged_in': 'onlyLoggedIn'
    }

    def __init__(self, limit=None, offset=None, group_id=None, include_disabled=None, name=None, only_logged_in=None):  # noqa: E501
        """XmlNs0FindUsersRequest - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._offset = None
        self._group_id = None
        self._include_disabled = None
        self._name = None
        self._only_logged_in = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if group_id is not None:
            self.group_id = group_id
        if include_disabled is not None:
            self.include_disabled = include_disabled
        if name is not None:
            self.name = name
        if only_logged_in is not None:
            self.only_logged_in = only_logged_in

    @property
    def limit(self):
        """Gets the limit of this XmlNs0FindUsersRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this XmlNs0FindUsersRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this XmlNs0FindUsersRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this XmlNs0FindUsersRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this XmlNs0FindUsersRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this XmlNs0FindUsersRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this XmlNs0FindUsersRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this XmlNs0FindUsersRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def group_id(self):
        """Gets the group_id of this XmlNs0FindUsersRequest.  # noqa: E501

        The <code>id</code> of the group the searched users should belong to  # noqa: E501

        :return: The group_id of this XmlNs0FindUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this XmlNs0FindUsersRequest.

        The <code>id</code> of the group the searched users should belong to  # noqa: E501

        :param group_id: The group_id of this XmlNs0FindUsersRequest.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def include_disabled(self):
        """Gets the include_disabled of this XmlNs0FindUsersRequest.  # noqa: E501

        Whether disabled users should be included in the search results  # noqa: E501

        :return: The include_disabled of this XmlNs0FindUsersRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_disabled

    @include_disabled.setter
    def include_disabled(self, include_disabled):
        """Sets the include_disabled of this XmlNs0FindUsersRequest.

        Whether disabled users should be included in the search results  # noqa: E501

        :param include_disabled: The include_disabled of this XmlNs0FindUsersRequest.  # noqa: E501
        :type: bool
        """

        self._include_disabled = include_disabled

    @property
    def name(self):
        """Gets the name of this XmlNs0FindUsersRequest.  # noqa: E501

        The name of the user. The search will occur in the username, firstname and lastname (and a combination)  # noqa: E501

        :return: The name of this XmlNs0FindUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0FindUsersRequest.

        The name of the user. The search will occur in the username, firstname and lastname (and a combination)  # noqa: E501

        :param name: The name of this XmlNs0FindUsersRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def only_logged_in(self):
        """Gets the only_logged_in of this XmlNs0FindUsersRequest.  # noqa: E501

        Whether only currently logged in users should be returned  # noqa: E501

        :return: The only_logged_in of this XmlNs0FindUsersRequest.  # noqa: E501
        :rtype: bool
        """
        return self._only_logged_in

    @only_logged_in.setter
    def only_logged_in(self, only_logged_in):
        """Sets the only_logged_in of this XmlNs0FindUsersRequest.

        Whether only currently logged in users should be returned  # noqa: E501

        :param only_logged_in: The only_logged_in of this XmlNs0FindUsersRequest.  # noqa: E501
        :type: bool
        """

        self._only_logged_in = only_logged_in

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
        if not isinstance(other, XmlNs0FindUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
