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

from swagger_client.models.json_data_quality_metric_impl import JsonDataQualityMetricImpl  # noqa: F401,E501
from swagger_client.models.json_named_described_resource_impl import JsonNamedDescribedResourceImpl  # noqa: F401,E501
from swagger_client.models.json_relation_trace_impl import JsonRelationTraceImpl  # noqa: F401,E501
from swagger_client.models.json_resource_reference_impl import JsonResourceReferenceImpl  # noqa: F401,E501


class JsonDataQualityRuleImpl(object):
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
        'name': 'str',
        'description': 'str',
        'categorization_relation_type': 'JsonResourceReferenceImpl',
        'relation_trace': 'JsonRelationTraceImpl',
        'data_quality_metrics': 'list[JsonDataQualityMetricImpl]'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'name': 'name',
        'description': 'description',
        'categorization_relation_type': 'categorizationRelationType',
        'relation_trace': 'relationTrace',
        'data_quality_metrics': 'dataQualityMetrics'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, name=None, description=None, categorization_relation_type=None, relation_trace=None, data_quality_metrics=None):  # noqa: E501
        """JsonDataQualityRuleImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._name = None
        self._description = None
        self._categorization_relation_type = None
        self._relation_trace = None
        self._data_quality_metrics = None
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
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if categorization_relation_type is not None:
            self.categorization_relation_type = categorization_relation_type
        if relation_trace is not None:
            self.relation_trace = relation_trace
        if data_quality_metrics is not None:
            self.data_quality_metrics = data_quality_metrics

    @property
    def id(self):
        """Gets the id of this JsonDataQualityRuleImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonDataQualityRuleImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this JsonDataQualityRuleImpl.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JsonDataQualityRuleImpl.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this JsonDataQualityRuleImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this JsonDataQualityRuleImpl.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this JsonDataQualityRuleImpl.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this JsonDataQualityRuleImpl.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this JsonDataQualityRuleImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this JsonDataQualityRuleImpl.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this JsonDataQualityRuleImpl.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this JsonDataQualityRuleImpl.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this JsonDataQualityRuleImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this JsonDataQualityRuleImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this JsonDataQualityRuleImpl.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The name of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonDataQualityRuleImpl.

        The name of the resource  # noqa: E501

        :param name: The name of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this JsonDataQualityRuleImpl.  # noqa: E501

        The description of the resource  # noqa: E501

        :return: The description of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonDataQualityRuleImpl.

        The description of the resource  # noqa: E501

        :param description: The description of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def categorization_relation_type(self):
        """Gets the categorization_relation_type of this JsonDataQualityRuleImpl.  # noqa: E501

        The categorization relation type  # noqa: E501

        :return: The categorization_relation_type of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: JsonResourceReferenceImpl
        """
        return self._categorization_relation_type

    @categorization_relation_type.setter
    def categorization_relation_type(self, categorization_relation_type):
        """Sets the categorization_relation_type of this JsonDataQualityRuleImpl.

        The categorization relation type  # noqa: E501

        :param categorization_relation_type: The categorization_relation_type of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: JsonResourceReferenceImpl
        """

        self._categorization_relation_type = categorization_relation_type

    @property
    def relation_trace(self):
        """Gets the relation_trace of this JsonDataQualityRuleImpl.  # noqa: E501

          # noqa: E501

        :return: The relation_trace of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: JsonRelationTraceImpl
        """
        return self._relation_trace

    @relation_trace.setter
    def relation_trace(self, relation_trace):
        """Sets the relation_trace of this JsonDataQualityRuleImpl.

          # noqa: E501

        :param relation_trace: The relation_trace of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: JsonRelationTraceImpl
        """

        self._relation_trace = relation_trace

    @property
    def data_quality_metrics(self):
        """Gets the data_quality_metrics of this JsonDataQualityRuleImpl.  # noqa: E501

          # noqa: E501

        :return: The data_quality_metrics of this JsonDataQualityRuleImpl.  # noqa: E501
        :rtype: list[JsonDataQualityMetricImpl]
        """
        return self._data_quality_metrics

    @data_quality_metrics.setter
    def data_quality_metrics(self, data_quality_metrics):
        """Sets the data_quality_metrics of this JsonDataQualityRuleImpl.

          # noqa: E501

        :param data_quality_metrics: The data_quality_metrics of this JsonDataQualityRuleImpl.  # noqa: E501
        :type: list[JsonDataQualityMetricImpl]
        """

        self._data_quality_metrics = data_quality_metrics

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
        if not isinstance(other, JsonDataQualityRuleImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
