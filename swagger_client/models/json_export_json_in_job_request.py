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


class JsonExportJSONInJobRequest(object):
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
        'send_notification': 'bool',
        'view_config': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'send_notification': 'sendNotification',
        'view_config': 'viewConfig',
        'file_name': 'fileName'
    }

    def __init__(self, send_notification=None, view_config=None, file_name=None):  # noqa: E501
        """JsonExportJSONInJobRequest - a model defined in Swagger"""  # noqa: E501

        self._send_notification = None
        self._view_config = None
        self._file_name = None
        self.discriminator = None

        if send_notification is not None:
            self.send_notification = send_notification
        self.view_config = view_config
        if file_name is not None:
            self.file_name = file_name

    @property
    def send_notification(self):
        """Gets the send_notification of this JsonExportJSONInJobRequest.  # noqa: E501

        Whether an e-mail must be sent on completion of the job  # noqa: E501

        :return: The send_notification of this JsonExportJSONInJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this JsonExportJSONInJobRequest.

        Whether an e-mail must be sent on completion of the job  # noqa: E501

        :param send_notification: The send_notification of this JsonExportJSONInJobRequest.  # noqa: E501
        :type: bool
        """

        self._send_notification = send_notification

    @property
    def view_config(self):
        """Gets the view_config of this JsonExportJSONInJobRequest.  # noqa: E501

        The JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details  # noqa: E501

        :return: The view_config of this JsonExportJSONInJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._view_config

    @view_config.setter
    def view_config(self, view_config):
        """Sets the view_config of this JsonExportJSONInJobRequest.

        The JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details  # noqa: E501

        :param view_config: The view_config of this JsonExportJSONInJobRequest.  # noqa: E501
        :type: str
        """
        if view_config is None:
            raise ValueError("Invalid value for `view_config`, must not be `None`")  # noqa: E501

        self._view_config = view_config

    @property
    def file_name(self):
        """Gets the file_name of this JsonExportJSONInJobRequest.  # noqa: E501

        The name of the file. By default the file name will be generated  # noqa: E501

        :return: The file_name of this JsonExportJSONInJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this JsonExportJSONInJobRequest.

        The name of the file. By default the file name will be generated  # noqa: E501

        :param file_name: The file_name of this JsonExportJSONInJobRequest.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

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
        if not isinstance(other, JsonExportJSONInJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
