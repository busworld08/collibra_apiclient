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

from swagger_client.models.json_form_property_impl import JsonFormPropertyImpl  # noqa: F401,E501
from swagger_client.models.json_resource_impl import JsonResourceImpl  # noqa: F401,E501
from swagger_client.models.json_resource_reference_impl import JsonResourceReferenceImpl  # noqa: F401,E501
from swagger_client.models.json_user_impl import JsonUserImpl  # noqa: F401,E501
from swagger_client.models.json_workflow_definition_reference_impl import JsonWorkflowDefinitionReferenceImpl  # noqa: F401,E501


class JsonWorkflowTaskImpl(object):
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
        'system': 'bool',
        'resource_type': 'str',
        'workflow_definition': 'JsonWorkflowDefinitionReferenceImpl',
        'workflow_instance_id': 'str',
        'key': 'str',
        'type': 'str',
        'aggregation_key': 'str',
        'priority': 'float',
        'owner': 'str',
        'candidate_users': 'list[JsonUserImpl]',
        'create_time': 'float',
        'due_date': 'float',
        'cancelable': 'bool',
        'reassignable': 'bool',
        'form_required': 'bool',
        'contains_activity_stream': 'bool',
        'in_error': 'bool',
        'error_message': 'str',
        'custom_buttons': 'list[JsonFormPropertyImpl]',
        'description': 'str',
        'title': 'str',
        'business_item': 'JsonResourceReferenceImpl'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'workflow_definition': 'workflowDefinition',
        'workflow_instance_id': 'workflowInstanceId',
        'key': 'key',
        'type': 'type',
        'aggregation_key': 'aggregationKey',
        'priority': 'priority',
        'owner': 'owner',
        'candidate_users': 'candidateUsers',
        'create_time': 'createTime',
        'due_date': 'dueDate',
        'cancelable': 'cancelable',
        'reassignable': 'reassignable',
        'form_required': 'formRequired',
        'contains_activity_stream': 'containsActivityStream',
        'in_error': 'inError',
        'error_message': 'errorMessage',
        'custom_buttons': 'customButtons',
        'description': 'description',
        'title': 'title',
        'business_item': 'businessItem'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, workflow_definition=None, workflow_instance_id=None, key=None, type=None, aggregation_key=None, priority=None, owner=None, candidate_users=None, create_time=None, due_date=None, cancelable=None, reassignable=None, form_required=None, contains_activity_stream=None, in_error=None, error_message=None, custom_buttons=None, description=None, title=None, business_item=None):  # noqa: E501
        """JsonWorkflowTaskImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._workflow_definition = None
        self._workflow_instance_id = None
        self._key = None
        self._type = None
        self._aggregation_key = None
        self._priority = None
        self._owner = None
        self._candidate_users = None
        self._create_time = None
        self._due_date = None
        self._cancelable = None
        self._reassignable = None
        self._form_required = None
        self._contains_activity_stream = None
        self._in_error = None
        self._error_message = None
        self._custom_buttons = None
        self._description = None
        self._title = None
        self._business_item = None
        self.discriminator = None

        self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if system is not None:
            self.system = system
        if resource_type is not None:
            self.resource_type = resource_type
        if workflow_definition is not None:
            self.workflow_definition = workflow_definition
        if workflow_instance_id is not None:
            self.workflow_instance_id = workflow_instance_id
        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if aggregation_key is not None:
            self.aggregation_key = aggregation_key
        if priority is not None:
            self.priority = priority
        if owner is not None:
            self.owner = owner
        if candidate_users is not None:
            self.candidate_users = candidate_users
        if create_time is not None:
            self.create_time = create_time
        if due_date is not None:
            self.due_date = due_date
        if cancelable is not None:
            self.cancelable = cancelable
        if reassignable is not None:
            self.reassignable = reassignable
        if form_required is not None:
            self.form_required = form_required
        if contains_activity_stream is not None:
            self.contains_activity_stream = contains_activity_stream
        if in_error is not None:
            self.in_error = in_error
        if error_message is not None:
            self.error_message = error_message
        if custom_buttons is not None:
            self.custom_buttons = custom_buttons
        if description is not None:
            self.description = description
        if title is not None:
            self.title = title
        if business_item is not None:
            self.business_item = business_item

    @property
    def id(self):
        """Gets the id of this JsonWorkflowTaskImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonWorkflowTaskImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this JsonWorkflowTaskImpl.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JsonWorkflowTaskImpl.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this JsonWorkflowTaskImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this JsonWorkflowTaskImpl.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this JsonWorkflowTaskImpl.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this JsonWorkflowTaskImpl.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this JsonWorkflowTaskImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this JsonWorkflowTaskImpl.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this JsonWorkflowTaskImpl.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this JsonWorkflowTaskImpl.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this JsonWorkflowTaskImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this JsonWorkflowTaskImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def workflow_definition(self):
        """Gets the workflow_definition of this JsonWorkflowTaskImpl.  # noqa: E501

        The reference to the workflow definition  # noqa: E501

        :return: The workflow_definition of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: JsonWorkflowDefinitionReferenceImpl
        """
        return self._workflow_definition

    @workflow_definition.setter
    def workflow_definition(self, workflow_definition):
        """Sets the workflow_definition of this JsonWorkflowTaskImpl.

        The reference to the workflow definition  # noqa: E501

        :param workflow_definition: The workflow_definition of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: JsonWorkflowDefinitionReferenceImpl
        """

        self._workflow_definition = workflow_definition

    @property
    def workflow_instance_id(self):
        """Gets the workflow_instance_id of this JsonWorkflowTaskImpl.  # noqa: E501

        The UUID of the workflow instance  # noqa: E501

        :return: The workflow_instance_id of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._workflow_instance_id

    @workflow_instance_id.setter
    def workflow_instance_id(self, workflow_instance_id):
        """Sets the workflow_instance_id of this JsonWorkflowTaskImpl.

        The UUID of the workflow instance  # noqa: E501

        :param workflow_instance_id: The workflow_instance_id of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._workflow_instance_id = workflow_instance_id

    @property
    def key(self):
        """Gets the key of this JsonWorkflowTaskImpl.  # noqa: E501

        The key  # noqa: E501

        :return: The key of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this JsonWorkflowTaskImpl.

        The key  # noqa: E501

        :param key: The key of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def type(self):
        """Gets the type of this JsonWorkflowTaskImpl.  # noqa: E501

        The type  # noqa: E501

        :return: The type of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JsonWorkflowTaskImpl.

        The type  # noqa: E501

        :param type: The type of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def aggregation_key(self):
        """Gets the aggregation_key of this JsonWorkflowTaskImpl.  # noqa: E501

        The key for aggregation purposes. If empty, the task can't be aggregated  # noqa: E501

        :return: The aggregation_key of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_key

    @aggregation_key.setter
    def aggregation_key(self, aggregation_key):
        """Sets the aggregation_key of this JsonWorkflowTaskImpl.

        The key for aggregation purposes. If empty, the task can't be aggregated  # noqa: E501

        :param aggregation_key: The aggregation_key of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._aggregation_key = aggregation_key

    @property
    def priority(self):
        """Gets the priority of this JsonWorkflowTaskImpl.  # noqa: E501

        The priority  # noqa: E501

        :return: The priority of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: float
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JsonWorkflowTaskImpl.

        The priority  # noqa: E501

        :param priority: The priority of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: float
        """

        self._priority = priority

    @property
    def owner(self):
        """Gets the owner of this JsonWorkflowTaskImpl.  # noqa: E501

        The owner  # noqa: E501

        :return: The owner of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this JsonWorkflowTaskImpl.

        The owner  # noqa: E501

        :param owner: The owner of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def candidate_users(self):
        """Gets the candidate_users of this JsonWorkflowTaskImpl.  # noqa: E501

        The list of candidate users  # noqa: E501

        :return: The candidate_users of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: list[JsonUserImpl]
        """
        return self._candidate_users

    @candidate_users.setter
    def candidate_users(self, candidate_users):
        """Sets the candidate_users of this JsonWorkflowTaskImpl.

        The list of candidate users  # noqa: E501

        :param candidate_users: The candidate_users of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: list[JsonUserImpl]
        """

        self._candidate_users = candidate_users

    @property
    def create_time(self):
        """Gets the create_time of this JsonWorkflowTaskImpl.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JsonWorkflowTaskImpl.

        The create time  # noqa: E501

        :param create_time: The create_time of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: float
        """

        self._create_time = create_time

    @property
    def due_date(self):
        """Gets the due_date of this JsonWorkflowTaskImpl.  # noqa: E501

        The due date  # noqa: E501

        :return: The due_date of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: float
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this JsonWorkflowTaskImpl.

        The due date  # noqa: E501

        :param due_date: The due_date of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: float
        """

        self._due_date = due_date

    @property
    def cancelable(self):
        """Gets the cancelable of this JsonWorkflowTaskImpl.  # noqa: E501

        Whether this workflow task is cancelable or not  # noqa: E501

        :return: The cancelable of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: bool
        """
        return self._cancelable

    @cancelable.setter
    def cancelable(self, cancelable):
        """Sets the cancelable of this JsonWorkflowTaskImpl.

        Whether this workflow task is cancelable or not  # noqa: E501

        :param cancelable: The cancelable of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: bool
        """

        self._cancelable = cancelable

    @property
    def reassignable(self):
        """Gets the reassignable of this JsonWorkflowTaskImpl.  # noqa: E501

        Whether this workflow task is reassignable or not  # noqa: E501

        :return: The reassignable of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: bool
        """
        return self._reassignable

    @reassignable.setter
    def reassignable(self, reassignable):
        """Sets the reassignable of this JsonWorkflowTaskImpl.

        Whether this workflow task is reassignable or not  # noqa: E501

        :param reassignable: The reassignable of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: bool
        """

        self._reassignable = reassignable

    @property
    def form_required(self):
        """Gets the form_required of this JsonWorkflowTaskImpl.  # noqa: E501

        Whether this task requires a form or not  # noqa: E501

        :return: The form_required of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: bool
        """
        return self._form_required

    @form_required.setter
    def form_required(self, form_required):
        """Sets the form_required of this JsonWorkflowTaskImpl.

        Whether this task requires a form or not  # noqa: E501

        :param form_required: The form_required of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: bool
        """

        self._form_required = form_required

    @property
    def contains_activity_stream(self):
        """Gets the contains_activity_stream of this JsonWorkflowTaskImpl.  # noqa: E501

        Whether this task contains an activity stream or not  # noqa: E501

        :return: The contains_activity_stream of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: bool
        """
        return self._contains_activity_stream

    @contains_activity_stream.setter
    def contains_activity_stream(self, contains_activity_stream):
        """Sets the contains_activity_stream of this JsonWorkflowTaskImpl.

        Whether this task contains an activity stream or not  # noqa: E501

        :param contains_activity_stream: The contains_activity_stream of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: bool
        """

        self._contains_activity_stream = contains_activity_stream

    @property
    def in_error(self):
        """Gets the in_error of this JsonWorkflowTaskImpl.  # noqa: E501

        Whether this task is in error or not  # noqa: E501

        :return: The in_error of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: bool
        """
        return self._in_error

    @in_error.setter
    def in_error(self, in_error):
        """Sets the in_error of this JsonWorkflowTaskImpl.

        Whether this task is in error or not  # noqa: E501

        :param in_error: The in_error of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: bool
        """

        self._in_error = in_error

    @property
    def error_message(self):
        """Gets the error_message of this JsonWorkflowTaskImpl.  # noqa: E501

        The error message in case this task is in error  # noqa: E501

        :return: The error_message of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this JsonWorkflowTaskImpl.

        The error message in case this task is in error  # noqa: E501

        :param error_message: The error_message of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def custom_buttons(self):
        """Gets the custom_buttons of this JsonWorkflowTaskImpl.  # noqa: E501

        The list of custom buttons  # noqa: E501

        :return: The custom_buttons of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: list[JsonFormPropertyImpl]
        """
        return self._custom_buttons

    @custom_buttons.setter
    def custom_buttons(self, custom_buttons):
        """Sets the custom_buttons of this JsonWorkflowTaskImpl.

        The list of custom buttons  # noqa: E501

        :param custom_buttons: The custom_buttons of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: list[JsonFormPropertyImpl]
        """

        self._custom_buttons = custom_buttons

    @property
    def description(self):
        """Gets the description of this JsonWorkflowTaskImpl.  # noqa: E501

        The description of the workflow task  # noqa: E501

        :return: The description of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonWorkflowTaskImpl.

        The description of the workflow task  # noqa: E501

        :param description: The description of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def title(self):
        """Gets the title of this JsonWorkflowTaskImpl.  # noqa: E501

        The title of the task  # noqa: E501

        :return: The title of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this JsonWorkflowTaskImpl.

        The title of the task  # noqa: E501

        :param title: The title of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def business_item(self):
        """Gets the business_item of this JsonWorkflowTaskImpl.  # noqa: E501

        The reference to the business item Resource related to the task  # noqa: E501

        :return: The business_item of this JsonWorkflowTaskImpl.  # noqa: E501
        :rtype: JsonResourceReferenceImpl
        """
        return self._business_item

    @business_item.setter
    def business_item(self, business_item):
        """Sets the business_item of this JsonWorkflowTaskImpl.

        The reference to the business item Resource related to the task  # noqa: E501

        :param business_item: The business_item of this JsonWorkflowTaskImpl.  # noqa: E501
        :type: JsonResourceReferenceImpl
        """

        self._business_item = business_item

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
        if not isinstance(other, JsonWorkflowTaskImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other