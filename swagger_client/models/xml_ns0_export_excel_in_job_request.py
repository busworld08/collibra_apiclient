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


class XmlNs0ExportExcelInJobRequest(object):
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
        'header_row': 'bool',
        'send_notification': 'bool',
        'sheet_name': 'str',
        'table_view_config': 'str',
        'use_xlsx': 'bool'
    }

    attribute_map = {
        'file_name': 'fileName',
        'header_row': 'headerRow',
        'send_notification': 'sendNotification',
        'sheet_name': 'sheetName',
        'table_view_config': 'tableViewConfig',
        'use_xlsx': 'useXLSX'
    }

    def __init__(self, file_name=None, header_row=None, send_notification=None, sheet_name=None, table_view_config=None, use_xlsx=None):  # noqa: E501
        """XmlNs0ExportExcelInJobRequest - a model defined in Swagger"""  # noqa: E501

        self._file_name = None
        self._header_row = None
        self._send_notification = None
        self._sheet_name = None
        self._table_view_config = None
        self._use_xlsx = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if header_row is not None:
            self.header_row = header_row
        if send_notification is not None:
            self.send_notification = send_notification
        if sheet_name is not None:
            self.sheet_name = sheet_name
        if table_view_config is not None:
            self.table_view_config = table_view_config
        if use_xlsx is not None:
            self.use_xlsx = use_xlsx

    @property
    def file_name(self):
        """Gets the file_name of this XmlNs0ExportExcelInJobRequest.  # noqa: E501

        The name of the file. By default the file name will be generated  # noqa: E501

        :return: The file_name of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this XmlNs0ExportExcelInJobRequest.

        The name of the file. By default the file name will be generated  # noqa: E501

        :param file_name: The file_name of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def header_row(self):
        """Gets the header_row of this XmlNs0ExportExcelInJobRequest.  # noqa: E501

        Whether a response should include a header (true) or not (false). Default value is true  # noqa: E501

        :return: The header_row of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._header_row

    @header_row.setter
    def header_row(self, header_row):
        """Sets the header_row of this XmlNs0ExportExcelInJobRequest.

        Whether a response should include a header (true) or not (false). Default value is true  # noqa: E501

        :param header_row: The header_row of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :type: bool
        """

        self._header_row = header_row

    @property
    def send_notification(self):
        """Gets the send_notification of this XmlNs0ExportExcelInJobRequest.  # noqa: E501

        Whether an e-mail must be sent on completion of the job  # noqa: E501

        :return: The send_notification of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this XmlNs0ExportExcelInJobRequest.

        Whether an e-mail must be sent on completion of the job  # noqa: E501

        :param send_notification: The send_notification of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :type: bool
        """

        self._send_notification = send_notification

    @property
    def sheet_name(self):
        """Gets the sheet_name of this XmlNs0ExportExcelInJobRequest.  # noqa: E501

        The name of the sheet. By default no sheet name is set  # noqa: E501

        :return: The sheet_name of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        """Sets the sheet_name of this XmlNs0ExportExcelInJobRequest.

        The name of the sheet. By default no sheet name is set  # noqa: E501

        :param sheet_name: The sheet_name of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :type: str
        """

        self._sheet_name = sheet_name

    @property
    def table_view_config(self):
        """Gets the table_view_config of this XmlNs0ExportExcelInJobRequest.  # noqa: E501

        The JSON representation of Table View Config that describes the query to be performed  # noqa: E501

        :return: The table_view_config of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._table_view_config

    @table_view_config.setter
    def table_view_config(self, table_view_config):
        """Sets the table_view_config of this XmlNs0ExportExcelInJobRequest.

        The JSON representation of Table View Config that describes the query to be performed  # noqa: E501

        :param table_view_config: The table_view_config of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :type: str
        """

        self._table_view_config = table_view_config

    @property
    def use_xlsx(self):
        """Gets the use_xlsx of this XmlNs0ExportExcelInJobRequest.  # noqa: E501

        Whether the Excel file to export will be '.xlsx' file (true) or a '.xls' file (false. Default value is true  # noqa: E501

        :return: The use_xlsx of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_xlsx

    @use_xlsx.setter
    def use_xlsx(self, use_xlsx):
        """Sets the use_xlsx of this XmlNs0ExportExcelInJobRequest.

        Whether the Excel file to export will be '.xlsx' file (true) or a '.xls' file (false. Default value is true  # noqa: E501

        :param use_xlsx: The use_xlsx of this XmlNs0ExportExcelInJobRequest.  # noqa: E501
        :type: bool
        """

        self._use_xlsx = use_xlsx

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
        if not isinstance(other, XmlNs0ExportExcelInJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
