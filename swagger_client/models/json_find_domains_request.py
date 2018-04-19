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

from swagger_client.models.json_match_mode import JsonMatchMode  # noqa: F401,E501
from swagger_client.models.json_paged_request import JsonPagedRequest  # noqa: F401,E501


class JsonFindDomainsRequest(object):
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
        'offset': 'float',
        'limit': 'float',
        'name': 'str',
        'name_match_mode': 'JsonMatchMode',
        'exclude_meta': 'bool',
        'community_id': 'str',
        'type_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'name_match_mode': 'nameMatchMode',
        'exclude_meta': 'excludeMeta',
        'community_id': 'communityId',
        'type_id': 'typeId'
    }

    def __init__(self, offset=None, limit=None, name=None, name_match_mode=None, exclude_meta=None, community_id=None, type_id=None):  # noqa: E501
        """JsonFindDomainsRequest - a model defined in Swagger"""  # noqa: E501

        self._offset = None
        self._limit = None
        self._name = None
        self._name_match_mode = None
        self._exclude_meta = None
        self._community_id = None
        self._type_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if name_match_mode is not None:
            self.name_match_mode = name_match_mode
        if exclude_meta is not None:
            self.exclude_meta = exclude_meta
        if community_id is not None:
            self.community_id = community_id
        if type_id is not None:
            self.type_id = type_id

    @property
    def offset(self):
        """Gets the offset of this JsonFindDomainsRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this JsonFindDomainsRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this JsonFindDomainsRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this JsonFindDomainsRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this JsonFindDomainsRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this JsonFindDomainsRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def name(self):
        """Gets the name of this JsonFindDomainsRequest.  # noqa: E501

        The name of the domain to search for  # noqa: E501

        :return: The name of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonFindDomainsRequest.

        The name of the domain to search for  # noqa: E501

        :param name: The name of this JsonFindDomainsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_match_mode(self):
        """Gets the name_match_mode of this JsonFindDomainsRequest.  # noqa: E501

        The match mode used to compare <code>name</code>  # noqa: E501

        :return: The name_match_mode of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: JsonMatchMode
        """
        return self._name_match_mode

    @name_match_mode.setter
    def name_match_mode(self, name_match_mode):
        """Sets the name_match_mode of this JsonFindDomainsRequest.

        The match mode used to compare <code>name</code>  # noqa: E501

        :param name_match_mode: The name_match_mode of this JsonFindDomainsRequest.  # noqa: E501
        :type: JsonMatchMode
        """

        self._name_match_mode = name_match_mode

    @property
    def exclude_meta(self):
        """Gets the exclude_meta of this JsonFindDomainsRequest.  # noqa: E501

        The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user)  # noqa: E501

        :return: The exclude_meta of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_meta

    @exclude_meta.setter
    def exclude_meta(self, exclude_meta):
        """Sets the exclude_meta of this JsonFindDomainsRequest.

        The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user)  # noqa: E501

        :param exclude_meta: The exclude_meta of this JsonFindDomainsRequest.  # noqa: E501
        :type: bool
        """

        self._exclude_meta = exclude_meta

    @property
    def community_id(self):
        """Gets the community_id of this JsonFindDomainsRequest.  # noqa: E501

        The <code>id</code> of the community to find the domains in  # noqa: E501

        :return: The community_id of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._community_id

    @community_id.setter
    def community_id(self, community_id):
        """Sets the community_id of this JsonFindDomainsRequest.

        The <code>id</code> of the community to find the domains in  # noqa: E501

        :param community_id: The community_id of this JsonFindDomainsRequest.  # noqa: E501
        :type: str
        """

        self._community_id = community_id

    @property
    def type_id(self):
        """Gets the type_id of this JsonFindDomainsRequest.  # noqa: E501

        The <code>id</code> of the domain type to search for. Returned domains are of this type  # noqa: E501

        :return: The type_id of this JsonFindDomainsRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this JsonFindDomainsRequest.

        The <code>id</code> of the domain type to search for. Returned domains are of this type  # noqa: E501

        :param type_id: The type_id of this JsonFindDomainsRequest.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

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
        if not isinstance(other, JsonFindDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other