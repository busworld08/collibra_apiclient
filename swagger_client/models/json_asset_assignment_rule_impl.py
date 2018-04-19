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

from swagger_client.models.json_entity_impl import JsonEntityImpl  # noqa: F401,E501
from swagger_client.models.json_named_resource_reference_impl import JsonNamedResourceReferenceImpl  # noqa: F401,E501


class JsonAssetAssignmentRuleImpl(object):
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
        'asset_type': 'JsonNamedResourceReferenceImpl',
        'domain': 'JsonNamedResourceReferenceImpl',
        'community': 'JsonNamedResourceReferenceImpl'
    }

    attribute_map = {
        'id': 'id',
        'asset_type': 'assetType',
        'domain': 'domain',
        'community': 'community'
    }

    def __init__(self, id=None, asset_type=None, domain=None, community=None):  # noqa: E501
        """JsonAssetAssignmentRuleImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._asset_type = None
        self._domain = None
        self._community = None
        self.discriminator = None

        self.id = id
        if asset_type is not None:
            self.asset_type = asset_type
        if domain is not None:
            self.domain = domain
        if community is not None:
            self.community = community

    @property
    def id(self):
        """Gets the id of this JsonAssetAssignmentRuleImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonAssetAssignmentRuleImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def asset_type(self):
        """Gets the asset_type of this JsonAssetAssignmentRuleImpl.  # noqa: E501

        The reference to the asset type  # noqa: E501

        :return: The asset_type of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :rtype: JsonNamedResourceReferenceImpl
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this JsonAssetAssignmentRuleImpl.

        The reference to the asset type  # noqa: E501

        :param asset_type: The asset_type of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :type: JsonNamedResourceReferenceImpl
        """

        self._asset_type = asset_type

    @property
    def domain(self):
        """Gets the domain of this JsonAssetAssignmentRuleImpl.  # noqa: E501

        The reference to the domain  # noqa: E501

        :return: The domain of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :rtype: JsonNamedResourceReferenceImpl
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this JsonAssetAssignmentRuleImpl.

        The reference to the domain  # noqa: E501

        :param domain: The domain of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :type: JsonNamedResourceReferenceImpl
        """

        self._domain = domain

    @property
    def community(self):
        """Gets the community of this JsonAssetAssignmentRuleImpl.  # noqa: E501

        The reference to the community  # noqa: E501

        :return: The community of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :rtype: JsonNamedResourceReferenceImpl
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this JsonAssetAssignmentRuleImpl.

        The reference to the community  # noqa: E501

        :param community: The community of this JsonAssetAssignmentRuleImpl.  # noqa: E501
        :type: JsonNamedResourceReferenceImpl
        """

        self._community = community

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
        if not isinstance(other, JsonAssetAssignmentRuleImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other