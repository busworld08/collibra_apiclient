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


class JsonAddDiagramPictureRequest(object):
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
        'view_id': 'str'
    }

    attribute_map = {
        'asset_id': 'assetId',
        'view_id': 'viewId'
    }

    def __init__(self, asset_id=None, view_id=None):  # noqa: E501
        """JsonAddDiagramPictureRequest - a model defined in Swagger"""  # noqa: E501

        self._asset_id = None
        self._view_id = None
        self.discriminator = None

        self.asset_id = asset_id
        self.view_id = view_id

    @property
    def asset_id(self):
        """Gets the asset_id of this JsonAddDiagramPictureRequest.  # noqa: E501

        The <code>id</code> of the Asset for which the picture should be taken.  # noqa: E501

        :return: The asset_id of this JsonAddDiagramPictureRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this JsonAddDiagramPictureRequest.

        The <code>id</code> of the Asset for which the picture should be taken.  # noqa: E501

        :param asset_id: The asset_id of this JsonAddDiagramPictureRequest.  # noqa: E501
        :type: str
        """
        if asset_id is None:
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

    @property
    def view_id(self):
        """Gets the view_id of this JsonAddDiagramPictureRequest.  # noqa: E501

        The <code>id</code>  of the View for which the picture should be taken.  # noqa: E501

        :return: The view_id of this JsonAddDiagramPictureRequest.  # noqa: E501
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this JsonAddDiagramPictureRequest.

        The <code>id</code>  of the View for which the picture should be taken.  # noqa: E501

        :param view_id: The view_id of this JsonAddDiagramPictureRequest.  # noqa: E501
        :type: str
        """
        if view_id is None:
            raise ValueError("Invalid value for `view_id`, must not be `None`")  # noqa: E501

        self._view_id = view_id

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
        if not isinstance(other, JsonAddDiagramPictureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other