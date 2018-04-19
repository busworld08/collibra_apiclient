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

from swagger_client.models.xml_ns0_named_described_resource_impl import XmlNs0NamedDescribedResourceImpl  # noqa: F401,E501
from swagger_client.models.xml_ns0_resource_type import XmlNs0ResourceType  # noqa: F401,E501
from swagger_client.models.xml_ns0_sharing_rule import XmlNs0SharingRule  # noqa: F401,E501
from swagger_client.models.xml_ns0_view_assignment_rule import XmlNs0ViewAssignmentRule  # noqa: F401,E501
from swagger_client.models.xml_ns0_view_type import XmlNs0ViewType  # noqa: F401,E501


class XmlNs0View(object):
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
        'assignment_rules': 'XmlNs0ViewAssignmentRule',
        'config': 'str',
        'is_default': 'bool',
        'is_preferred': 'bool',
        'is_working_view': 'bool',
        'location': 'str',
        'original_view_id': 'str',
        'sharing_rules': 'XmlNs0SharingRule',
        'type': 'XmlNs0ViewType'
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
        'assignment_rules': 'assignmentRules',
        'config': 'config',
        'is_default': 'isDefault',
        'is_preferred': 'isPreferred',
        'is_working_view': 'isWorkingView',
        'location': 'location',
        'original_view_id': 'originalViewId',
        'sharing_rules': 'sharingRules',
        'type': 'type'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, resource_type=None, system=None, name=None, description=None, assignment_rules=None, config=None, is_default=None, is_preferred=None, is_working_view=None, location=None, original_view_id=None, sharing_rules=None, type=None):  # noqa: E501
        """XmlNs0View - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._resource_type = None
        self._system = None
        self._name = None
        self._description = None
        self._assignment_rules = None
        self._config = None
        self._is_default = None
        self._is_preferred = None
        self._is_working_view = None
        self._location = None
        self._original_view_id = None
        self._sharing_rules = None
        self._type = None
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
        if assignment_rules is not None:
            self.assignment_rules = assignment_rules
        if config is not None:
            self.config = config
        if is_default is not None:
            self.is_default = is_default
        if is_preferred is not None:
            self.is_preferred = is_preferred
        if is_working_view is not None:
            self.is_working_view = is_working_view
        if location is not None:
            self.location = location
        if original_view_id is not None:
            self.original_view_id = original_view_id
        if sharing_rules is not None:
            self.sharing_rules = sharing_rules
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this XmlNs0View.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0View.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this XmlNs0View.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this XmlNs0View.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this XmlNs0View.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this XmlNs0View.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this XmlNs0View.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this XmlNs0View.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this XmlNs0View.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this XmlNs0View.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this XmlNs0View.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this XmlNs0View.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this XmlNs0View.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this XmlNs0View.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def resource_type(self):
        """Gets the resource_type of this XmlNs0View.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this XmlNs0View.  # noqa: E501
        :rtype: XmlNs0ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this XmlNs0View.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this XmlNs0View.  # noqa: E501
        :type: XmlNs0ResourceType
        """

        self._resource_type = resource_type

    @property
    def system(self):
        """Gets the system of this XmlNs0View.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this XmlNs0View.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this XmlNs0View.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this XmlNs0View.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def name(self):
        """Gets the name of this XmlNs0View.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The name of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0View.

        The name of the resource  # noqa: E501

        :param name: The name of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XmlNs0View.  # noqa: E501

        The description of the resource  # noqa: E501

        :return: The description of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XmlNs0View.

        The description of the resource  # noqa: E501

        :param description: The description of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def assignment_rules(self):
        """Gets the assignment_rules of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The assignment_rules of this XmlNs0View.  # noqa: E501
        :rtype: XmlNs0ViewAssignmentRule
        """
        return self._assignment_rules

    @assignment_rules.setter
    def assignment_rules(self, assignment_rules):
        """Sets the assignment_rules of this XmlNs0View.

          # noqa: E501

        :param assignment_rules: The assignment_rules of this XmlNs0View.  # noqa: E501
        :type: XmlNs0ViewAssignmentRule
        """

        self._assignment_rules = assignment_rules

    @property
    def config(self):
        """Gets the config of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The config of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this XmlNs0View.

          # noqa: E501

        :param config: The config of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._config = config

    @property
    def is_default(self):
        """Gets the is_default of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The is_default of this XmlNs0View.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this XmlNs0View.

          # noqa: E501

        :param is_default: The is_default of this XmlNs0View.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_preferred(self):
        """Gets the is_preferred of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The is_preferred of this XmlNs0View.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred

    @is_preferred.setter
    def is_preferred(self, is_preferred):
        """Sets the is_preferred of this XmlNs0View.

          # noqa: E501

        :param is_preferred: The is_preferred of this XmlNs0View.  # noqa: E501
        :type: bool
        """

        self._is_preferred = is_preferred

    @property
    def is_working_view(self):
        """Gets the is_working_view of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The is_working_view of this XmlNs0View.  # noqa: E501
        :rtype: bool
        """
        return self._is_working_view

    @is_working_view.setter
    def is_working_view(self, is_working_view):
        """Sets the is_working_view of this XmlNs0View.

          # noqa: E501

        :param is_working_view: The is_working_view of this XmlNs0View.  # noqa: E501
        :type: bool
        """

        self._is_working_view = is_working_view

    @property
    def location(self):
        """Gets the location of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The location of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this XmlNs0View.

          # noqa: E501

        :param location: The location of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def original_view_id(self):
        """Gets the original_view_id of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The original_view_id of this XmlNs0View.  # noqa: E501
        :rtype: str
        """
        return self._original_view_id

    @original_view_id.setter
    def original_view_id(self, original_view_id):
        """Sets the original_view_id of this XmlNs0View.

          # noqa: E501

        :param original_view_id: The original_view_id of this XmlNs0View.  # noqa: E501
        :type: str
        """

        self._original_view_id = original_view_id

    @property
    def sharing_rules(self):
        """Gets the sharing_rules of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The sharing_rules of this XmlNs0View.  # noqa: E501
        :rtype: XmlNs0SharingRule
        """
        return self._sharing_rules

    @sharing_rules.setter
    def sharing_rules(self, sharing_rules):
        """Sets the sharing_rules of this XmlNs0View.

          # noqa: E501

        :param sharing_rules: The sharing_rules of this XmlNs0View.  # noqa: E501
        :type: XmlNs0SharingRule
        """

        self._sharing_rules = sharing_rules

    @property
    def type(self):
        """Gets the type of this XmlNs0View.  # noqa: E501

          # noqa: E501

        :return: The type of this XmlNs0View.  # noqa: E501
        :rtype: XmlNs0ViewType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XmlNs0View.

          # noqa: E501

        :param type: The type of this XmlNs0View.  # noqa: E501
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
        if not isinstance(other, XmlNs0View):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other