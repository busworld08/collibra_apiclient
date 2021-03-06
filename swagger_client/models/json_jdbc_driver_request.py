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

from swagger_client.models.json_connection_string_parameter_jdbc_driver_request import JsonConnectionStringParameterJdbcDriverRequest  # noqa: F401,E501


class JsonJdbcDriverRequest(object):
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
        'database_name': 'str',
        'database_version': 'str',
        'driver': 'str',
        'connection_string': 'str',
        'connection_string_parameters': 'list[JsonConnectionStringParameterJdbcDriverRequest]'
    }

    attribute_map = {
        'database_name': 'databaseName',
        'database_version': 'databaseVersion',
        'driver': 'driver',
        'connection_string': 'connectionString',
        'connection_string_parameters': 'connectionStringParameters'
    }

    def __init__(self, database_name=None, database_version=None, driver=None, connection_string=None, connection_string_parameters=None):  # noqa: E501
        """JsonJdbcDriverRequest - a model defined in Swagger"""  # noqa: E501

        self._database_name = None
        self._database_version = None
        self._driver = None
        self._connection_string = None
        self._connection_string_parameters = None
        self.discriminator = None

        self.database_name = database_name
        self.database_version = database_version
        self.driver = driver
        self.connection_string = connection_string
        self.connection_string_parameters = connection_string_parameters

    @property
    def database_name(self):
        """Gets the database_name of this JsonJdbcDriverRequest.  # noqa: E501

          # noqa: E501

        :return: The database_name of this JsonJdbcDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this JsonJdbcDriverRequest.

          # noqa: E501

        :param database_name: The database_name of this JsonJdbcDriverRequest.  # noqa: E501
        :type: str
        """
        if database_name is None:
            raise ValueError("Invalid value for `database_name`, must not be `None`")  # noqa: E501

        self._database_name = database_name

    @property
    def database_version(self):
        """Gets the database_version of this JsonJdbcDriverRequest.  # noqa: E501

          # noqa: E501

        :return: The database_version of this JsonJdbcDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """Sets the database_version of this JsonJdbcDriverRequest.

          # noqa: E501

        :param database_version: The database_version of this JsonJdbcDriverRequest.  # noqa: E501
        :type: str
        """
        if database_version is None:
            raise ValueError("Invalid value for `database_version`, must not be `None`")  # noqa: E501

        self._database_version = database_version

    @property
    def driver(self):
        """Gets the driver of this JsonJdbcDriverRequest.  # noqa: E501

          # noqa: E501

        :return: The driver of this JsonJdbcDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this JsonJdbcDriverRequest.

          # noqa: E501

        :param driver: The driver of this JsonJdbcDriverRequest.  # noqa: E501
        :type: str
        """
        if driver is None:
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

    @property
    def connection_string(self):
        """Gets the connection_string of this JsonJdbcDriverRequest.  # noqa: E501

          # noqa: E501

        :return: The connection_string of this JsonJdbcDriverRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this JsonJdbcDriverRequest.

          # noqa: E501

        :param connection_string: The connection_string of this JsonJdbcDriverRequest.  # noqa: E501
        :type: str
        """
        if connection_string is None:
            raise ValueError("Invalid value for `connection_string`, must not be `None`")  # noqa: E501

        self._connection_string = connection_string

    @property
    def connection_string_parameters(self):
        """Gets the connection_string_parameters of this JsonJdbcDriverRequest.  # noqa: E501

          # noqa: E501

        :return: The connection_string_parameters of this JsonJdbcDriverRequest.  # noqa: E501
        :rtype: list[JsonConnectionStringParameterJdbcDriverRequest]
        """
        return self._connection_string_parameters

    @connection_string_parameters.setter
    def connection_string_parameters(self, connection_string_parameters):
        """Sets the connection_string_parameters of this JsonJdbcDriverRequest.

          # noqa: E501

        :param connection_string_parameters: The connection_string_parameters of this JsonJdbcDriverRequest.  # noqa: E501
        :type: list[JsonConnectionStringParameterJdbcDriverRequest]
        """
        if connection_string_parameters is None:
            raise ValueError("Invalid value for `connection_string_parameters`, must not be `None`")  # noqa: E501

        self._connection_string_parameters = connection_string_parameters

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
        if not isinstance(other, JsonJdbcDriverRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
