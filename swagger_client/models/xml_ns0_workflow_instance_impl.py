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

from swagger_client.models.xml_ns0_resource_impl import XmlNs0ResourceImpl  # noqa: F401,E501
from swagger_client.models.xml_ns0_resource_type import XmlNs0ResourceType  # noqa: F401,E501


class XmlNs0WorkflowInstanceImpl(object):
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
        'business_item': 'object',
        'created_asset_id': 'str',
        'ended': 'bool',
        'error_message': 'str',
        'in_error': 'bool',
        'start_date': 'float',
        'sub_instances': 'object',
        'tasks': 'object',
        'workflow_definition': 'object'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'resource_type': 'resourceType',
        'system': 'system',
        'business_item': 'businessItem',
        'created_asset_id': 'createdAssetId',
        'ended': 'ended',
        'error_message': 'errorMessage',
        'in_error': 'inError',
        'start_date': 'startDate',
        'sub_instances': 'subInstances',
        'tasks': 'tasks',
        'workflow_definition': 'workflowDefinition'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, resource_type=None, system=None, business_item=None, created_asset_id=None, ended=None, error_message=None, in_error=None, start_date=None, sub_instances=None, tasks=None, workflow_definition=None):  # noqa: E501
        """XmlNs0WorkflowInstanceImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._resource_type = None
        self._system = None
        self._business_item = None
        self._created_asset_id = None
        self._ended = None
        self._error_message = None
        self._in_error = None
        self._start_date = None
        self._sub_instances = None
        self._tasks = None
        self._workflow_definition = None
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
        if business_item is not None:
            self.business_item = business_item
        if created_asset_id is not None:
            self.created_asset_id = created_asset_id
        if ended is not None:
            self.ended = ended
        if error_message is not None:
            self.error_message = error_message
        if in_error is not None:
            self.in_error = in_error
        if start_date is not None:
            self.start_date = start_date
        if sub_instances is not None:
            self.sub_instances = sub_instances
        if tasks is not None:
            self.tasks = tasks
        if workflow_definition is not None:
            self.workflow_definition = workflow_definition

    @property
    def id(self):
        """Gets the id of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0WorkflowInstanceImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this XmlNs0WorkflowInstanceImpl.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this XmlNs0WorkflowInstanceImpl.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this XmlNs0WorkflowInstanceImpl.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this XmlNs0WorkflowInstanceImpl.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def resource_type(self):
        """Gets the resource_type of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: XmlNs0ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this XmlNs0WorkflowInstanceImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: XmlNs0ResourceType
        """

        self._resource_type = resource_type

    @property
    def system(self):
        """Gets the system of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this XmlNs0WorkflowInstanceImpl.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def business_item(self):
        """Gets the business_item of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The optional business item Resource related to the process instance  # noqa: E501

        :return: The business_item of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: object
        """
        return self._business_item

    @business_item.setter
    def business_item(self, business_item):
        """Sets the business_item of this XmlNs0WorkflowInstanceImpl.

        The optional business item Resource related to the process instance  # noqa: E501

        :param business_item: The business_item of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: object
        """

        self._business_item = business_item

    @property
    def created_asset_id(self):
        """Gets the created_asset_id of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The optional <code>id</code> of the created asset if the process instance ended, created a term and it is configured for it  # noqa: E501

        :return: The created_asset_id of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_asset_id

    @created_asset_id.setter
    def created_asset_id(self, created_asset_id):
        """Sets the created_asset_id of this XmlNs0WorkflowInstanceImpl.

        The optional <code>id</code> of the created asset if the process instance ended, created a term and it is configured for it  # noqa: E501

        :param created_asset_id: The created_asset_id of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: str
        """

        self._created_asset_id = created_asset_id

    @property
    def ended(self):
        """Gets the ended of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        Whether this process instance is already ended  # noqa: E501

        :return: The ended of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: bool
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this XmlNs0WorkflowInstanceImpl.

        Whether this process instance is already ended  # noqa: E501

        :param ended: The ended of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: bool
        """

        self._ended = ended

    @property
    def error_message(self):
        """Gets the error_message of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The optional error message of any error in a async continuation of this process instance. Only present if inError is true  # noqa: E501

        :return: The error_message of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this XmlNs0WorkflowInstanceImpl.

        The optional error message of any error in a async continuation of this process instance. Only present if inError is true  # noqa: E501

        :param error_message: The error_message of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def in_error(self):
        """Gets the in_error of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        Whether this process instance is in error. This means that there was a problem with a async continuation of the process instance  # noqa: E501

        :return: The in_error of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: bool
        """
        return self._in_error

    @in_error.setter
    def in_error(self, in_error):
        """Sets the in_error of this XmlNs0WorkflowInstanceImpl.

        Whether this process instance is in error. This means that there was a problem with a async continuation of the process instance  # noqa: E501

        :param in_error: The in_error of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: bool
        """

        self._in_error = in_error

    @property
    def start_date(self):
        """Gets the start_date of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The start date of this process instance  # noqa: E501

        :return: The start_date of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: float
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this XmlNs0WorkflowInstanceImpl.

        The start date of this process instance  # noqa: E501

        :param start_date: The start_date of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: float
        """

        self._start_date = start_date

    @property
    def sub_instances(self):
        """Gets the sub_instances of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The sub process instances of this instance  # noqa: E501

        :return: The sub_instances of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: object
        """
        return self._sub_instances

    @sub_instances.setter
    def sub_instances(self, sub_instances):
        """Sets the sub_instances of this XmlNs0WorkflowInstanceImpl.

        The sub process instances of this instance  # noqa: E501

        :param sub_instances: The sub_instances of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: object
        """

        self._sub_instances = sub_instances

    @property
    def tasks(self):
        """Gets the tasks of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The List of WorkflowTasks in this process instance  # noqa: E501

        :return: The tasks of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: object
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this XmlNs0WorkflowInstanceImpl.

        The List of WorkflowTasks in this process instance  # noqa: E501

        :param tasks: The tasks of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: object
        """

        self._tasks = tasks

    @property
    def workflow_definition(self):
        """Gets the workflow_definition of this XmlNs0WorkflowInstanceImpl.  # noqa: E501

        The reference to the workflow definition  # noqa: E501

        :return: The workflow_definition of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :rtype: object
        """
        return self._workflow_definition

    @workflow_definition.setter
    def workflow_definition(self, workflow_definition):
        """Sets the workflow_definition of this XmlNs0WorkflowInstanceImpl.

        The reference to the workflow definition  # noqa: E501

        :param workflow_definition: The workflow_definition of this XmlNs0WorkflowInstanceImpl.  # noqa: E501
        :type: object
        """

        self._workflow_definition = workflow_definition

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
        if not isinstance(other, XmlNs0WorkflowInstanceImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other