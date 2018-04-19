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

from swagger_client.models.xml_ns0_jdbc_driver import XmlNs0JdbcDriver  # noqa: F401,E501
from swagger_client.models.xml_ns0_resource_impl import XmlNs0ResourceImpl  # noqa: F401,E501
from swagger_client.models.xml_ns0_resource_type import XmlNs0ResourceType  # noqa: F401,E501


class XmlNs0JdbcIngestionProperties(object):
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
        'cron_expression': 'str',
        'cron_time_zone': 'str',
        'detect_advanced_data_types': 'bool',
        'execute_profiling': 'bool',
        'extract_data_sample': 'bool',
        'jdbc_driver': 'XmlNs0JdbcDriver',
        'jdbc_properties': 'object',
        'schema': 'object',
        'tables_to_skip': 'str',
        'user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'resource_type': 'resourceType',
        'system': 'system',
        'cron_expression': 'cronExpression',
        'cron_time_zone': 'cronTimeZone',
        'detect_advanced_data_types': 'detectAdvancedDataTypes',
        'execute_profiling': 'executeProfiling',
        'extract_data_sample': 'extractDataSample',
        'jdbc_driver': 'jdbcDriver',
        'jdbc_properties': 'jdbcProperties',
        'schema': 'schema',
        'tables_to_skip': 'tablesToSkip',
        'user': 'user'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, resource_type=None, system=None, cron_expression=None, cron_time_zone=None, detect_advanced_data_types=None, execute_profiling=None, extract_data_sample=None, jdbc_driver=None, jdbc_properties=None, schema=None, tables_to_skip=None, user=None):  # noqa: E501
        """XmlNs0JdbcIngestionProperties - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._resource_type = None
        self._system = None
        self._cron_expression = None
        self._cron_time_zone = None
        self._detect_advanced_data_types = None
        self._execute_profiling = None
        self._extract_data_sample = None
        self._jdbc_driver = None
        self._jdbc_properties = None
        self._schema = None
        self._tables_to_skip = None
        self._user = None
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
        if cron_expression is not None:
            self.cron_expression = cron_expression
        if cron_time_zone is not None:
            self.cron_time_zone = cron_time_zone
        if detect_advanced_data_types is not None:
            self.detect_advanced_data_types = detect_advanced_data_types
        if execute_profiling is not None:
            self.execute_profiling = execute_profiling
        if extract_data_sample is not None:
            self.extract_data_sample = extract_data_sample
        if jdbc_driver is not None:
            self.jdbc_driver = jdbc_driver
        if jdbc_properties is not None:
            self.jdbc_properties = jdbc_properties
        if schema is not None:
            self.schema = schema
        if tables_to_skip is not None:
            self.tables_to_skip = tables_to_skip
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0JdbcIngestionProperties.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this XmlNs0JdbcIngestionProperties.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this XmlNs0JdbcIngestionProperties.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this XmlNs0JdbcIngestionProperties.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this XmlNs0JdbcIngestionProperties.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def resource_type(self):
        """Gets the resource_type of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: XmlNs0ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this XmlNs0JdbcIngestionProperties.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: XmlNs0ResourceType
        """

        self._resource_type = resource_type

    @property
    def system(self):
        """Gets the system of this XmlNs0JdbcIngestionProperties.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this XmlNs0JdbcIngestionProperties.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def cron_expression(self):
        """Gets the cron_expression of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The cron_expression of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param cron_expression: The cron_expression of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._cron_expression = cron_expression

    @property
    def cron_time_zone(self):
        """Gets the cron_time_zone of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The cron_time_zone of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._cron_time_zone

    @cron_time_zone.setter
    def cron_time_zone(self, cron_time_zone):
        """Sets the cron_time_zone of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param cron_time_zone: The cron_time_zone of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._cron_time_zone = cron_time_zone

    @property
    def detect_advanced_data_types(self):
        """Gets the detect_advanced_data_types of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The detect_advanced_data_types of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._detect_advanced_data_types

    @detect_advanced_data_types.setter
    def detect_advanced_data_types(self, detect_advanced_data_types):
        """Sets the detect_advanced_data_types of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param detect_advanced_data_types: The detect_advanced_data_types of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: bool
        """

        self._detect_advanced_data_types = detect_advanced_data_types

    @property
    def execute_profiling(self):
        """Gets the execute_profiling of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The execute_profiling of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._execute_profiling

    @execute_profiling.setter
    def execute_profiling(self, execute_profiling):
        """Sets the execute_profiling of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param execute_profiling: The execute_profiling of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: bool
        """

        self._execute_profiling = execute_profiling

    @property
    def extract_data_sample(self):
        """Gets the extract_data_sample of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The extract_data_sample of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._extract_data_sample

    @extract_data_sample.setter
    def extract_data_sample(self, extract_data_sample):
        """Sets the extract_data_sample of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param extract_data_sample: The extract_data_sample of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: bool
        """

        self._extract_data_sample = extract_data_sample

    @property
    def jdbc_driver(self):
        """Gets the jdbc_driver of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The jdbc_driver of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: XmlNs0JdbcDriver
        """
        return self._jdbc_driver

    @jdbc_driver.setter
    def jdbc_driver(self, jdbc_driver):
        """Sets the jdbc_driver of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param jdbc_driver: The jdbc_driver of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: XmlNs0JdbcDriver
        """

        self._jdbc_driver = jdbc_driver

    @property
    def jdbc_properties(self):
        """Gets the jdbc_properties of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The jdbc_properties of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: object
        """
        return self._jdbc_properties

    @jdbc_properties.setter
    def jdbc_properties(self, jdbc_properties):
        """Sets the jdbc_properties of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param jdbc_properties: The jdbc_properties of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: object
        """

        self._jdbc_properties = jdbc_properties

    @property
    def schema(self):
        """Gets the schema of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The schema of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: object
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param schema: The schema of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: object
        """

        self._schema = schema

    @property
    def tables_to_skip(self):
        """Gets the tables_to_skip of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The tables_to_skip of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._tables_to_skip

    @tables_to_skip.setter
    def tables_to_skip(self, tables_to_skip):
        """Sets the tables_to_skip of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param tables_to_skip: The tables_to_skip of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._tables_to_skip = tables_to_skip

    @property
    def user(self):
        """Gets the user of this XmlNs0JdbcIngestionProperties.  # noqa: E501

          # noqa: E501

        :return: The user of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this XmlNs0JdbcIngestionProperties.

          # noqa: E501

        :param user: The user of this XmlNs0JdbcIngestionProperties.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if not isinstance(other, XmlNs0JdbcIngestionProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
