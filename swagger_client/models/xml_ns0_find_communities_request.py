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

from swagger_client.models.xml_ns0_match_mode import XmlNs0MatchMode  # noqa: F401,E501
from swagger_client.models.xml_ns0_paged_request import XmlNs0PagedRequest  # noqa: F401,E501
from swagger_client.models.xml_ns0_sort_field import XmlNs0SortField  # noqa: F401,E501
from swagger_client.models.xml_ns0_sort_order import XmlNs0SortOrder  # noqa: F401,E501


class XmlNs0FindCommunitiesRequest(object):
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
        'exclude_meta': 'bool',
        'name': 'str',
        'name_match_mode': 'XmlNs0MatchMode',
        'parent_id': 'str',
        'sort_field': 'XmlNs0SortField',
        'sort_order': 'XmlNs0SortOrder'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'exclude_meta': 'excludeMeta',
        'name': 'name',
        'name_match_mode': 'nameMatchMode',
        'parent_id': 'parentId',
        'sort_field': 'sortField',
        'sort_order': 'sortOrder'
    }

    def __init__(self, limit=None, offset=None, exclude_meta=None, name=None, name_match_mode=None, parent_id=None, sort_field=None, sort_order=None):  # noqa: E501
        """XmlNs0FindCommunitiesRequest - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._offset = None
        self._exclude_meta = None
        self._name = None
        self._name_match_mode = None
        self._parent_id = None
        self._sort_field = None
        self._sort_order = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if exclude_meta is not None:
            self.exclude_meta = exclude_meta
        if name is not None:
            self.name = name
        if name_match_mode is not None:
            self.name_match_mode = name_match_mode
        if parent_id is not None:
            self.parent_id = parent_id
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def limit(self):
        """Gets the limit of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this XmlNs0FindCommunitiesRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this XmlNs0FindCommunitiesRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def exclude_meta(self):
        """Gets the exclude_meta of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The exclude meta flag. If this is set to true then the meta communities will not be returned (meta communities are i.e. communities not created manually by the user)  # noqa: E501

        :return: The exclude_meta of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_meta

    @exclude_meta.setter
    def exclude_meta(self, exclude_meta):
        """Sets the exclude_meta of this XmlNs0FindCommunitiesRequest.

        The exclude meta flag. If this is set to true then the meta communities will not be returned (meta communities are i.e. communities not created manually by the user)  # noqa: E501

        :param exclude_meta: The exclude_meta of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: bool
        """

        self._exclude_meta = exclude_meta

    @property
    def name(self):
        """Gets the name of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The name of the community to search for  # noqa: E501

        :return: The name of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0FindCommunitiesRequest.

        The name of the community to search for  # noqa: E501

        :param name: The name of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_match_mode(self):
        """Gets the name_match_mode of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The match mode used to compare <code>name</code>  # noqa: E501

        :return: The name_match_mode of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: XmlNs0MatchMode
        """
        return self._name_match_mode

    @name_match_mode.setter
    def name_match_mode(self, name_match_mode):
        """Sets the name_match_mode of this XmlNs0FindCommunitiesRequest.

        The match mode used to compare <code>name</code>  # noqa: E501

        :param name_match_mode: The name_match_mode of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: XmlNs0MatchMode
        """

        self._name_match_mode = name_match_mode

    @property
    def parent_id(self):
        """Gets the parent_id of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The <code>id</code> of the parent community to find the communities in  # noqa: E501

        :return: The parent_id of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this XmlNs0FindCommunitiesRequest.

        The <code>id</code> of the parent community to find the communities in  # noqa: E501

        :param parent_id: The parent_id of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def sort_field(self):
        """Gets the sort_field of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The field on which the results are sorted  # noqa: E501

        :return: The sort_field of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: XmlNs0SortField
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this XmlNs0FindCommunitiesRequest.

        The field on which the results are sorted  # noqa: E501

        :param sort_field: The sort_field of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: XmlNs0SortField
        """

        self._sort_field = sort_field

    @property
    def sort_order(self):
        """Gets the sort_order of this XmlNs0FindCommunitiesRequest.  # noqa: E501

        The sorting order  # noqa: E501

        :return: The sort_order of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :rtype: XmlNs0SortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this XmlNs0FindCommunitiesRequest.

        The sorting order  # noqa: E501

        :param sort_order: The sort_order of this XmlNs0FindCommunitiesRequest.  # noqa: E501
        :type: XmlNs0SortOrder
        """

        self._sort_order = sort_order

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
        if not isinstance(other, XmlNs0FindCommunitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
