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

from swagger_client.models.xml_ns0_input_stream import XmlNs0InputStream  # noqa: F401,E501


class XmlNs0DeployWorkflowDefinitionRequest(object):
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
        'file_name': 'str',
        'file_stream': 'XmlNs0InputStream'
    }

    attribute_map = {
        'file_name': 'fileName',
        'file_stream': 'fileStream'
    }

    def __init__(self, file_name=None, file_stream=None):  # noqa: E501
        """XmlNs0DeployWorkflowDefinitionRequest - a model defined in Swagger"""  # noqa: E501

        self._file_name = None
        self._file_stream = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_stream is not None:
            self.file_stream = file_stream

    @property
    def file_name(self):
        """Gets the file_name of this XmlNs0DeployWorkflowDefinitionRequest.  # noqa: E501

        The name of the file  # noqa: E501

        :return: The file_name of this XmlNs0DeployWorkflowDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this XmlNs0DeployWorkflowDefinitionRequest.

        The name of the file  # noqa: E501

        :param file_name: The file_name of this XmlNs0DeployWorkflowDefinitionRequest.  # noqa: E501
        :type: str
        """
        if file_name is not None and len(file_name) > 255:
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `255`")  # noqa: E501
        if file_name is not None and len(file_name) < 1:
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._file_name = file_name

    @property
    def file_stream(self):
        """Gets the file_stream of this XmlNs0DeployWorkflowDefinitionRequest.  # noqa: E501

        The file describing the workflow to be deployed  # noqa: E501

        :return: The file_stream of this XmlNs0DeployWorkflowDefinitionRequest.  # noqa: E501
        :rtype: XmlNs0InputStream
        """
        return self._file_stream

    @file_stream.setter
    def file_stream(self, file_stream):
        """Sets the file_stream of this XmlNs0DeployWorkflowDefinitionRequest.

        The file describing the workflow to be deployed  # noqa: E501

        :param file_stream: The file_stream of this XmlNs0DeployWorkflowDefinitionRequest.  # noqa: E501
        :type: XmlNs0InputStream
        """

        self._file_stream = file_stream

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
        if not isinstance(other, XmlNs0DeployWorkflowDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
