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

from swagger_client.models.xml_ns0_activity_filter_category import XmlNs0ActivityFilterCategory  # noqa: F401,E501
from swagger_client.models.xml_ns0_activity_type import XmlNs0ActivityType  # noqa: F401,E501
from swagger_client.models.xml_ns0_paged_request import XmlNs0PagedRequest  # noqa: F401,E501
from swagger_client.models.xml_ns0_resource_type import XmlNs0ResourceType  # noqa: F401,E501


class XmlNs0FindActivitiesRequest(object):
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
        'activity_type': 'XmlNs0ActivityType',
        'call_id': 'str',
        'categories': 'XmlNs0ActivityFilterCategory',
        'context_id': 'str',
        'end_date': 'float',
        'involved_people_ids': 'str',
        'involved_role_ids': 'str',
        'performed_by_role_ids': 'str',
        'performed_by_user_id': 'str',
        'resource_types': 'XmlNs0ResourceType',
        'start_date': 'float',
        'task_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'activity_type': 'activityType',
        'call_id': 'callId',
        'categories': 'categories',
        'context_id': 'contextId',
        'end_date': 'endDate',
        'involved_people_ids': 'involvedPeopleIds',
        'involved_role_ids': 'involvedRoleIds',
        'performed_by_role_ids': 'performedByRoleIds',
        'performed_by_user_id': 'performedByUserId',
        'resource_types': 'resourceTypes',
        'start_date': 'startDate',
        'task_id': 'taskId'
    }

    def __init__(self, limit=None, offset=None, activity_type=None, call_id=None, categories=None, context_id=None, end_date=None, involved_people_ids=None, involved_role_ids=None, performed_by_role_ids=None, performed_by_user_id=None, resource_types=None, start_date=None, task_id=None):  # noqa: E501
        """XmlNs0FindActivitiesRequest - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._offset = None
        self._activity_type = None
        self._call_id = None
        self._categories = None
        self._context_id = None
        self._end_date = None
        self._involved_people_ids = None
        self._involved_role_ids = None
        self._performed_by_role_ids = None
        self._performed_by_user_id = None
        self._resource_types = None
        self._start_date = None
        self._task_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if activity_type is not None:
            self.activity_type = activity_type
        if call_id is not None:
            self.call_id = call_id
        if categories is not None:
            self.categories = categories
        if context_id is not None:
            self.context_id = context_id
        if end_date is not None:
            self.end_date = end_date
        if involved_people_ids is not None:
            self.involved_people_ids = involved_people_ids
        if involved_role_ids is not None:
            self.involved_role_ids = involved_role_ids
        if performed_by_role_ids is not None:
            self.performed_by_role_ids = performed_by_role_ids
        if performed_by_user_id is not None:
            self.performed_by_user_id = performed_by_user_id
        if resource_types is not None:
            self.resource_types = resource_types
        if start_date is not None:
            self.start_date = start_date
        if task_id is not None:
            self.task_id = task_id

    @property
    def limit(self):
        """Gets the limit of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :return: The limit of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this XmlNs0FindActivitiesRequest.

        The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used  # noqa: E501

        :param limit: The limit of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :return: The offset of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this XmlNs0FindActivitiesRequest.

        The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>  # noqa: E501

        :param offset: The offset of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def activity_type(self):
        """Gets the activity_type of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The type of the activity  # noqa: E501

        :return: The activity_type of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: XmlNs0ActivityType
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """Sets the activity_type of this XmlNs0FindActivitiesRequest.

        The type of the activity  # noqa: E501

        :param activity_type: The activity_type of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: XmlNs0ActivityType
        """

        self._activity_type = activity_type

    @property
    def call_id(self):
        """Gets the call_id of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The <code>id</code> of the call  # noqa: E501

        :return: The call_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._call_id

    @call_id.setter
    def call_id(self, call_id):
        """Sets the call_id of this XmlNs0FindActivitiesRequest.

        The <code>id</code> of the call  # noqa: E501

        :param call_id: The call_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._call_id = call_id

    @property
    def categories(self):
        """Gets the categories of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT, STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS]  # noqa: E501

        :return: The categories of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: XmlNs0ActivityFilterCategory
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this XmlNs0FindActivitiesRequest.

        The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT, STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS]  # noqa: E501

        :param categories: The categories of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: XmlNs0ActivityFilterCategory
        """

        self._categories = categories

    @property
    def context_id(self):
        """Gets the context_id of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The <code>id</code> of the context which the activities should be searched for  # noqa: E501

        :return: The context_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this XmlNs0FindActivitiesRequest.

        The <code>id</code> of the context which the activities should be searched for  # noqa: E501

        :param context_id: The context_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._context_id = context_id

    @property
    def end_date(self):
        """Gets the end_date of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The end date of the searched activities. It is the timestamp (in UTC time standard)  # noqa: E501

        :return: The end_date of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: float
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this XmlNs0FindActivitiesRequest.

        The end date of the searched activities. It is the timestamp (in UTC time standard)  # noqa: E501

        :param end_date: The end_date of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: float
        """

        self._end_date = end_date

    @property
    def involved_people_ids(self):
        """Gets the involved_people_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The list of <code>id</code>s of the people that should be involved in searched activities  # noqa: E501

        :return: The involved_people_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._involved_people_ids

    @involved_people_ids.setter
    def involved_people_ids(self, involved_people_ids):
        """Sets the involved_people_ids of this XmlNs0FindActivitiesRequest.

        The list of <code>id</code>s of the people that should be involved in searched activities  # noqa: E501

        :param involved_people_ids: The involved_people_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._involved_people_ids = involved_people_ids

    @property
    def involved_role_ids(self):
        """Gets the involved_role_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The list of <code>id</code>s of the roles that should be involved in searched activities  # noqa: E501

        :return: The involved_role_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._involved_role_ids

    @involved_role_ids.setter
    def involved_role_ids(self, involved_role_ids):
        """Sets the involved_role_ids of this XmlNs0FindActivitiesRequest.

        The list of <code>id</code>s of the roles that should be involved in searched activities  # noqa: E501

        :param involved_role_ids: The involved_role_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._involved_role_ids = involved_role_ids

    @property
    def performed_by_role_ids(self):
        """Gets the performed_by_role_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The list of <code>id</code>s of the roles assigned to users who performed searched activities  # noqa: E501

        :return: The performed_by_role_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._performed_by_role_ids

    @performed_by_role_ids.setter
    def performed_by_role_ids(self, performed_by_role_ids):
        """Sets the performed_by_role_ids of this XmlNs0FindActivitiesRequest.

        The list of <code>id</code>s of the roles assigned to users who performed searched activities  # noqa: E501

        :param performed_by_role_ids: The performed_by_role_ids of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._performed_by_role_ids = performed_by_role_ids

    @property
    def performed_by_user_id(self):
        """Gets the performed_by_user_id of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The <code>id</code> of the user who performed searched activities  # noqa: E501

        :return: The performed_by_user_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._performed_by_user_id

    @performed_by_user_id.setter
    def performed_by_user_id(self, performed_by_user_id):
        """Sets the performed_by_user_id of this XmlNs0FindActivitiesRequest.

        The <code>id</code> of the user who performed searched activities  # noqa: E501

        :param performed_by_user_id: The performed_by_user_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._performed_by_user_id = performed_by_user_id

    @property
    def resource_types(self):
        """Gets the resource_types of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_types of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: XmlNs0ResourceType
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this XmlNs0FindActivitiesRequest.

        The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_types: The resource_types of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: XmlNs0ResourceType
        """

        self._resource_types = resource_types

    @property
    def start_date(self):
        """Gets the start_date of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The start date of the searched activities. It is the timestamp (in UTC time standard)  # noqa: E501

        :return: The start_date of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: float
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this XmlNs0FindActivitiesRequest.

        The start date of the searched activities. It is the timestamp (in UTC time standard)  # noqa: E501

        :param start_date: The start_date of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: float
        """

        self._start_date = start_date

    @property
    def task_id(self):
        """Gets the task_id of this XmlNs0FindActivitiesRequest.  # noqa: E501

        The <code>id</code> of the task which contains the basic find activities request  # noqa: E501

        :return: The task_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this XmlNs0FindActivitiesRequest.

        The <code>id</code> of the task which contains the basic find activities request  # noqa: E501

        :param task_id: The task_id of this XmlNs0FindActivitiesRequest.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

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
        if not isinstance(other, XmlNs0FindActivitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
