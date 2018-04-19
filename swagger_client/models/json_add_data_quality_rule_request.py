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

from swagger_client.models.json_data_quality_metric_request import JsonDataQualityMetricRequest  # noqa: F401,E501
from swagger_client.models.json_relation_trace_entry_request import JsonRelationTraceEntryRequest  # noqa: F401,E501


class JsonAddDataQualityRuleRequest(object):
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
        'name': 'str',
        'description': 'str',
        'categorization_relation_type_id': 'str',
        'data_quality_metrics': 'list[JsonDataQualityMetricRequest]',
        'relation_trace_entries': 'list[JsonRelationTraceEntryRequest]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'categorization_relation_type_id': 'categorizationRelationTypeId',
        'data_quality_metrics': 'dataQualityMetrics',
        'relation_trace_entries': 'relationTraceEntries'
    }

    def __init__(self, name=None, description=None, categorization_relation_type_id=None, data_quality_metrics=None, relation_trace_entries=None):  # noqa: E501
        """JsonAddDataQualityRuleRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._categorization_relation_type_id = None
        self._data_quality_metrics = None
        self._relation_trace_entries = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.categorization_relation_type_id = categorization_relation_type_id
        if data_quality_metrics is not None:
            self.data_quality_metrics = data_quality_metrics
        self.relation_trace_entries = relation_trace_entries

    @property
    def name(self):
        """Gets the name of this JsonAddDataQualityRuleRequest.  # noqa: E501

        The name of the new data quality rule. Should be unique within all data quality rules  # noqa: E501

        :return: The name of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonAddDataQualityRuleRequest.

        The name of the new data quality rule. Should be unique within all data quality rules  # noqa: E501

        :param name: The name of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this JsonAddDataQualityRuleRequest.  # noqa: E501

        The description of the new data quality rule  # noqa: E501

        :return: The description of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonAddDataQualityRuleRequest.

        The description of the new data quality rule  # noqa: E501

        :param description: The description of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def categorization_relation_type_id(self):
        """Gets the categorization_relation_type_id of this JsonAddDataQualityRuleRequest.  # noqa: E501

        The <code>id</code> of the categorization relation type  # noqa: E501

        :return: The categorization_relation_type_id of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._categorization_relation_type_id

    @categorization_relation_type_id.setter
    def categorization_relation_type_id(self, categorization_relation_type_id):
        """Sets the categorization_relation_type_id of this JsonAddDataQualityRuleRequest.

        The <code>id</code> of the categorization relation type  # noqa: E501

        :param categorization_relation_type_id: The categorization_relation_type_id of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :type: str
        """
        if categorization_relation_type_id is None:
            raise ValueError("Invalid value for `categorization_relation_type_id`, must not be `None`")  # noqa: E501

        self._categorization_relation_type_id = categorization_relation_type_id

    @property
    def data_quality_metrics(self):
        """Gets the data_quality_metrics of this JsonAddDataQualityRuleRequest.  # noqa: E501

        The Data Quality Metrics that should be assigned to the rule that is going to be created  # noqa: E501

        :return: The data_quality_metrics of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :rtype: list[JsonDataQualityMetricRequest]
        """
        return self._data_quality_metrics

    @data_quality_metrics.setter
    def data_quality_metrics(self, data_quality_metrics):
        """Sets the data_quality_metrics of this JsonAddDataQualityRuleRequest.

        The Data Quality Metrics that should be assigned to the rule that is going to be created  # noqa: E501

        :param data_quality_metrics: The data_quality_metrics of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :type: list[JsonDataQualityMetricRequest]
        """

        self._data_quality_metrics = data_quality_metrics

    @property
    def relation_trace_entries(self):
        """Gets the relation_trace_entries of this JsonAddDataQualityRuleRequest.  # noqa: E501

        The list of entries that describes relations along which the data quality result is calculated  # noqa: E501

        :return: The relation_trace_entries of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :rtype: list[JsonRelationTraceEntryRequest]
        """
        return self._relation_trace_entries

    @relation_trace_entries.setter
    def relation_trace_entries(self, relation_trace_entries):
        """Sets the relation_trace_entries of this JsonAddDataQualityRuleRequest.

        The list of entries that describes relations along which the data quality result is calculated  # noqa: E501

        :param relation_trace_entries: The relation_trace_entries of this JsonAddDataQualityRuleRequest.  # noqa: E501
        :type: list[JsonRelationTraceEntryRequest]
        """
        if relation_trace_entries is None:
            raise ValueError("Invalid value for `relation_trace_entries`, must not be `None`")  # noqa: E501

        self._relation_trace_entries = relation_trace_entries

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
        if not isinstance(other, JsonAddDataQualityRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
