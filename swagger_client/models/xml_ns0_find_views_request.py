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
from swagger_client.models.xml_ns0_resource_type import XmlNs0ResourceType  # noqa: F401,E501
from swagger_client.models.xml_ns0_sort_field import XmlNs0SortField  # noqa: F401,E501
from swagger_client.models.xml_ns0_sort_order import XmlNs0SortOrder  # noqa: F401,E501
from swagger_client.models.xml_ns0_view_type import XmlNs0ViewType  # noqa: F401,E501


class XmlNs0FindViewsRequest(object):
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
        'location': 'str',
        'name': 'str',
        'preferred': 'bool',
        'resource_id': 'str',
        'resource_type': 'XmlNs0ResourceType',
        'sort_field': 'XmlNs0SortField',
        'sort_order': 'XmlNs0SortOrder',
        'type': 'XmlNs0ViewType'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'location': 'location',
        'name': 'name',
        'preferred': 'preferred',
        'resource_id': 'resourceId',
        'resource_type': 'resourceType',
        'sort_field': 'sortField',
        'sort_order': 'sortOrder',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, location=None, name=None, preferred=None, resource_id=None, resource_type=None, sort_field=None, sort_order=None, type=None):  # noqa: E501
        """XmlNs0FindViewsRequest - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._offset = None
        self._location = None
        self._name = None
        self._preferred = None
        self._resource_id = None
        self._resource_type = None
        self._sort_field = None
        self._sort_order = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if preferred is not None:
            self.preferred = preferred
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if type is not None:
            self.type = type

    @property
    def limit(self):
        """Gets the limit of this XmlNs0FindViewsRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this XmlNs0FindViewsRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this XmlNs0FindViewsRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this XmlNs0FindViewsRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def location(self):
        """Gets the location of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The location of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param location: The location of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The name of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param name: The name of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preferred(self):
        """Gets the preferred of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The preferred of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param preferred: The preferred of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: bool
        """

        self._preferred = preferred

    @property
    def resource_id(self):
        """Gets the resource_id of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The resource_id of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param resource_id: The resource_id of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The resource_type of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: XmlNs0ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param resource_type: The resource_type of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: XmlNs0ResourceType
        """

        self._resource_type = resource_type

    @property
    def sort_field(self):
        """Gets the sort_field of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The sort_field of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: XmlNs0SortField
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param sort_field: The sort_field of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: XmlNs0SortField
        """

        self._sort_field = sort_field

    @property
    def sort_order(self):
        """Gets the sort_order of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The sort_order of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: XmlNs0SortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param sort_order: The sort_order of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: XmlNs0SortOrder
        """

        self._sort_order = sort_order

    @property
    def type(self):
        """Gets the type of this XmlNs0FindViewsRequest.  # noqa: E501

          # noqa: E501

        :return: The type of this XmlNs0FindViewsRequest.  # noqa: E501
        :rtype: XmlNs0ViewType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XmlNs0FindViewsRequest.

          # noqa: E501

        :param type: The type of this XmlNs0FindViewsRequest.  # noqa: E501
        :type: XmlNs0ViewType
        """

        self._type = type

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
        if not isinstance(other, XmlNs0FindViewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
