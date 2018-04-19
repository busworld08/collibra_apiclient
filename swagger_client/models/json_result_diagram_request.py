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

from swagger_client.models.json_visit_strategy import JsonVisitStrategy  # noqa: F401,E501


class JsonResultDiagramRequest(object):
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
        'asset_id': 'str',
        'json_template_diagram': 'str',
        'filtering_enabled': 'bool',
        'visit_strategy': 'JsonVisitStrategy'
    }

    attribute_map = {
        'asset_id': 'assetId',
        'json_template_diagram': 'jsonTemplateDiagram',
        'filtering_enabled': 'filteringEnabled',
        'visit_strategy': 'visitStrategy'
    }

    def __init__(self, asset_id=None, json_template_diagram=None, filtering_enabled=None, visit_strategy=None):  # noqa: E501
        """JsonResultDiagramRequest - a model defined in Swagger"""  # noqa: E501

        self._asset_id = None
        self._json_template_diagram = None
        self._filtering_enabled = None
        self._visit_strategy = None
        self.discriminator = None

        self.asset_id = asset_id
        self.json_template_diagram = json_template_diagram
        if filtering_enabled is not None:
            self.filtering_enabled = filtering_enabled
        if visit_strategy is not None:
            self.visit_strategy = visit_strategy

    @property
    def asset_id(self):
        """Gets the asset_id of this JsonResultDiagramRequest.  # noqa: E501

          # noqa: E501

        :return: The asset_id of this JsonResultDiagramRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this JsonResultDiagramRequest.

          # noqa: E501

        :param asset_id: The asset_id of this JsonResultDiagramRequest.  # noqa: E501
        :type: str
        """
        if asset_id is None:
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

    @property
    def json_template_diagram(self):
        """Gets the json_template_diagram of this JsonResultDiagramRequest.  # noqa: E501

          # noqa: E501

        :return: The json_template_diagram of this JsonResultDiagramRequest.  # noqa: E501
        :rtype: str
        """
        return self._json_template_diagram

    @json_template_diagram.setter
    def json_template_diagram(self, json_template_diagram):
        """Sets the json_template_diagram of this JsonResultDiagramRequest.

          # noqa: E501

        :param json_template_diagram: The json_template_diagram of this JsonResultDiagramRequest.  # noqa: E501
        :type: str
        """
        if json_template_diagram is None:
            raise ValueError("Invalid value for `json_template_diagram`, must not be `None`")  # noqa: E501

        self._json_template_diagram = json_template_diagram

    @property
    def filtering_enabled(self):
        """Gets the filtering_enabled of this JsonResultDiagramRequest.  # noqa: E501

          # noqa: E501

        :return: The filtering_enabled of this JsonResultDiagramRequest.  # noqa: E501
        :rtype: bool
        """
        return self._filtering_enabled

    @filtering_enabled.setter
    def filtering_enabled(self, filtering_enabled):
        """Sets the filtering_enabled of this JsonResultDiagramRequest.

          # noqa: E501

        :param filtering_enabled: The filtering_enabled of this JsonResultDiagramRequest.  # noqa: E501
        :type: bool
        """

        self._filtering_enabled = filtering_enabled

    @property
    def visit_strategy(self):
        """Gets the visit_strategy of this JsonResultDiagramRequest.  # noqa: E501

          # noqa: E501

        :return: The visit_strategy of this JsonResultDiagramRequest.  # noqa: E501
        :rtype: JsonVisitStrategy
        """
        return self._visit_strategy

    @visit_strategy.setter
    def visit_strategy(self, visit_strategy):
        """Sets the visit_strategy of this JsonResultDiagramRequest.

          # noqa: E501

        :param visit_strategy: The visit_strategy of this JsonResultDiagramRequest.  # noqa: E501
        :type: JsonVisitStrategy
        """

        self._visit_strategy = visit_strategy

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
        if not isinstance(other, JsonResultDiagramRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
