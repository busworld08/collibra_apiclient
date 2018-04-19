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

from swagger_client.models.xml_ns0_attribute_type_impl import XmlNs0AttributeTypeImpl  # noqa: F401,E501
from swagger_client.models.xml_ns0_resource_type import XmlNs0ResourceType  # noqa: F401,E501


class XmlNs0SingleValueListAttributeTypeImpl(object):
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
        'created_by': 'str',
        'created_on': 'float',
        'last_modified_by': 'str',
        'last_modified_on': 'float',
        'resource_type': 'XmlNs0ResourceType',
        'system': 'bool',
        'name': 'str',
        'description': 'str',
        'allowed_values': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'resource_type': 'resourceType',
        'system': 'system',
        'name': 'name',
        'description': 'description',
        'allowed_values': 'allowedValues'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, resource_type=None, system=None, name=None, description=None, allowed_values=None):  # noqa: E501
        """XmlNs0SingleValueListAttributeTypeImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._resource_type = None
        self._system = None
        self._name = None
        self._description = None
        self._allowed_values = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if resource_type is not None:
            self.resource_type = resource_type
        if system is not None:
            self.system = system
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if allowed_values is not None:
            self.allowed_values = allowed_values

    @property
    def id(self):
        """Gets the id of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0SingleValueListAttributeTypeImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this XmlNs0SingleValueListAttributeTypeImpl.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this XmlNs0SingleValueListAttributeTypeImpl.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this XmlNs0SingleValueListAttributeTypeImpl.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this XmlNs0SingleValueListAttributeTypeImpl.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def resource_type(self):
        """Gets the resource_type of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: XmlNs0ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this XmlNs0SingleValueListAttributeTypeImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: XmlNs0ResourceType
        """

        self._resource_type = resource_type

    @property
    def system(self):
        """Gets the system of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this XmlNs0SingleValueListAttributeTypeImpl.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def name(self):
        """Gets the name of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The name of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0SingleValueListAttributeTypeImpl.

        The name of the resource  # noqa: E501

        :param name: The name of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The description of the resource  # noqa: E501

        :return: The description of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XmlNs0SingleValueListAttributeTypeImpl.

        The description of the resource  # noqa: E501

        :param description: The description of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def allowed_values(self):
        """Gets the allowed_values of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501

        The allowed values for this attribute type  # noqa: E501

        :return: The allowed_values of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :rtype: str
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this XmlNs0SingleValueListAttributeTypeImpl.

        The allowed values for this attribute type  # noqa: E501

        :param allowed_values: The allowed_values of this XmlNs0SingleValueListAttributeTypeImpl.  # noqa: E501
        :type: str
        """

        self._allowed_values = allowed_values

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
        if not isinstance(other, XmlNs0SingleValueListAttributeTypeImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
