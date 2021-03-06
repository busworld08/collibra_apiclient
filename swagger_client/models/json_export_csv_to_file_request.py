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


class JsonExportCSVToFileRequest(object):
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
        'table_view_config': 'str',
        'file_name': 'str',
        'separator': 'str',
        'quote': 'str',
        'escape': 'str',
        'header_row': 'bool'
    }

    attribute_map = {
        'table_view_config': 'tableViewConfig',
        'file_name': 'fileName',
        'separator': 'separator',
        'quote': 'quote',
        'escape': 'escape',
        'header_row': 'headerRow'
    }

    def __init__(self, table_view_config=None, file_name=None, separator=None, quote=None, escape=None, header_row=None):  # noqa: E501
        """JsonExportCSVToFileRequest - a model defined in Swagger"""  # noqa: E501

        self._table_view_config = None
        self._file_name = None
        self._separator = None
        self._quote = None
        self._escape = None
        self._header_row = None
        self.discriminator = None

        self.table_view_config = table_view_config
        if file_name is not None:
            self.file_name = file_name
        if separator is not None:
            self.separator = separator
        if quote is not None:
            self.quote = quote
        if escape is not None:
            self.escape = escape
        if header_row is not None:
            self.header_row = header_row

    @property
    def table_view_config(self):
        """Gets the table_view_config of this JsonExportCSVToFileRequest.  # noqa: E501

        The JSON representation of Table View Config that describes the query to be performed  # noqa: E501

        :return: The table_view_config of this JsonExportCSVToFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._table_view_config

    @table_view_config.setter
    def table_view_config(self, table_view_config):
        """Sets the table_view_config of this JsonExportCSVToFileRequest.

        The JSON representation of Table View Config that describes the query to be performed  # noqa: E501

        :param table_view_config: The table_view_config of this JsonExportCSVToFileRequest.  # noqa: E501
        :type: str
        """
        if table_view_config is None:
            raise ValueError("Invalid value for `table_view_config`, must not be `None`")  # noqa: E501

        self._table_view_config = table_view_config

    @property
    def file_name(self):
        """Gets the file_name of this JsonExportCSVToFileRequest.  # noqa: E501

        The name of the file. By default the file name will be generated  # noqa: E501

        :return: The file_name of this JsonExportCSVToFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this JsonExportCSVToFileRequest.

        The name of the file. By default the file name will be generated  # noqa: E501

        :param file_name: The file_name of this JsonExportCSVToFileRequest.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def separator(self):
        """Gets the separator of this JsonExportCSVToFileRequest.  # noqa: E501

        The delimiter character used to separate entries. Default value is ';'  # noqa: E501

        :return: The separator of this JsonExportCSVToFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this JsonExportCSVToFileRequest.

        The delimiter character used to separate entries. Default value is ';'  # noqa: E501

        :param separator: The separator of this JsonExportCSVToFileRequest.  # noqa: E501
        :type: str
        """

        self._separator = separator

    @property
    def quote(self):
        """Gets the quote of this JsonExportCSVToFileRequest.  # noqa: E501

        The delimiter character used for quoted entries. Default value  is '\"'  # noqa: E501

        :return: The quote of this JsonExportCSVToFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this JsonExportCSVToFileRequest.

        The delimiter character used for quoted entries. Default value  is '\"'  # noqa: E501

        :param quote: The quote of this JsonExportCSVToFileRequest.  # noqa: E501
        :type: str
        """

        self._quote = quote

    @property
    def escape(self):
        """Gets the escape of this JsonExportCSVToFileRequest.  # noqa: E501

        The delimiter character used to escape separator or quote character. Default value is '\\\\'  # noqa: E501

        :return: The escape of this JsonExportCSVToFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._escape

    @escape.setter
    def escape(self, escape):
        """Sets the escape of this JsonExportCSVToFileRequest.

        The delimiter character used to escape separator or quote character. Default value is '\\\\'  # noqa: E501

        :param escape: The escape of this JsonExportCSVToFileRequest.  # noqa: E501
        :type: str
        """

        self._escape = escape

    @property
    def header_row(self):
        """Gets the header_row of this JsonExportCSVToFileRequest.  # noqa: E501

        Whether a response should include a header (true) or not (false). Default value is true  # noqa: E501

        :return: The header_row of this JsonExportCSVToFileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._header_row

    @header_row.setter
    def header_row(self, header_row):
        """Sets the header_row of this JsonExportCSVToFileRequest.

        Whether a response should include a header (true) or not (false). Default value is true  # noqa: E501

        :param header_row: The header_row of this JsonExportCSVToFileRequest.  # noqa: E501
        :type: bool
        """

        self._header_row = header_row

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
        if not isinstance(other, JsonExportCSVToFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
