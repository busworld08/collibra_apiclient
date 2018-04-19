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


class JsonCompleteWorkflowTasksRequest(object):
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
        'task_ids': 'list[str]',
        'form_properties': 'dict(str, str)',
        'guest_user_id': 'str'
    }

    attribute_map = {
        'task_ids': 'taskIds',
        'form_properties': 'formProperties',
        'guest_user_id': 'guestUserId'
    }

    def __init__(self, task_ids=None, form_properties=None, guest_user_id=None):  # noqa: E501
        """JsonCompleteWorkflowTasksRequest - a model defined in Swagger"""  # noqa: E501

        self._task_ids = None
        self._form_properties = None
        self._guest_user_id = None
        self.discriminator = None

        self.task_ids = task_ids
        if form_properties is not None:
            self.form_properties = form_properties
        if guest_user_id is not None:
            self.guest_user_id = guest_user_id

    @property
    def task_ids(self):
        """Gets the task_ids of this JsonCompleteWorkflowTasksRequest.  # noqa: E501

        The list of <code>id</code>s for the tasks that should be completed  # noqa: E501

        :return: The task_ids of this JsonCompleteWorkflowTasksRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this JsonCompleteWorkflowTasksRequest.

        The list of <code>id</code>s for the tasks that should be completed  # noqa: E501

        :param task_ids: The task_ids of this JsonCompleteWorkflowTasksRequest.  # noqa: E501
        :type: list[str]
        """
        if task_ids is None:
            raise ValueError("Invalid value for `task_ids`, must not be `None`")  # noqa: E501

        self._task_ids = task_ids

    @property
    def form_properties(self):
        """Gets the form_properties of this JsonCompleteWorkflowTasksRequest.  # noqa: E501

        The form properties for the workflow tasks to be completed  # noqa: E501

        :return: The form_properties of this JsonCompleteWorkflowTasksRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._form_properties

    @form_properties.setter
    def form_properties(self, form_properties):
        """Sets the form_properties of this JsonCompleteWorkflowTasksRequest.

        The form properties for the workflow tasks to be completed  # noqa: E501

        :param form_properties: The form_properties of this JsonCompleteWorkflowTasksRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._form_properties = form_properties

    @property
    def guest_user_id(self):
        """Gets the guest_user_id of this JsonCompleteWorkflowTasksRequest.  # noqa: E501

        The <code>id</code> of the guest user  # noqa: E501

        :return: The guest_user_id of this JsonCompleteWorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._guest_user_id

    @guest_user_id.setter
    def guest_user_id(self, guest_user_id):
        """Sets the guest_user_id of this JsonCompleteWorkflowTasksRequest.

        The <code>id</code> of the guest user  # noqa: E501

        :param guest_user_id: The guest_user_id of this JsonCompleteWorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._guest_user_id = guest_user_id

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
        if not isinstance(other, JsonCompleteWorkflowTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other