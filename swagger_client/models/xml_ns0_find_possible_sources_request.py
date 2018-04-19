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

from swagger_client.models.xml_ns0_abstract_source_target_request import XmlNs0AbstractSourceTargetRequest  # noqa: F401,E501


class XmlNs0FindPossibleSourcesRequest(object):
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
        'name': 'str',
        'relation_type_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'relation_type_id': 'relationTypeId'
    }

    def __init__(self, limit=None, offset=None, name=None, relation_type_id=None):  # noqa: E501
        """XmlNs0FindPossibleSourcesRequest - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._offset = None
        self._name = None
        self._relation_type_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if relation_type_id is not None:
            self.relation_type_id = relation_type_id

    @property
    def limit(self):
        """Gets the limit of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this XmlNs0FindPossibleSourcesRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this XmlNs0FindPossibleSourcesRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def name(self):
        """Gets the name of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501

          # noqa: E501

        :return: The name of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0FindPossibleSourcesRequest.

          # noqa: E501

        :param name: The name of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def relation_type_id(self):
        """Gets the relation_type_id of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501

          # noqa: E501

        :return: The relation_type_id of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_id

    @relation_type_id.setter
    def relation_type_id(self, relation_type_id):
        """Sets the relation_type_id of this XmlNs0FindPossibleSourcesRequest.

          # noqa: E501

        :param relation_type_id: The relation_type_id of this XmlNs0FindPossibleSourcesRequest.  # noqa: E501
        :type: str
        """

        self._relation_type_id = relation_type_id

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
        if not isinstance(other, XmlNs0FindPossibleSourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
