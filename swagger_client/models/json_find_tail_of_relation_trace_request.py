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


class JsonFindTailOfRelationTraceRequest(object):
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
        'assets_to_apply_trace_on_ids': 'list[str]',
        'relation_type_id': 'str',
        'relation_trace_entries': 'list[object]',
        'apply_relation_trace_on_target': 'bool'
    }

    attribute_map = {
        'assets_to_apply_trace_on_ids': 'assetsToApplyTraceOnIds',
        'relation_type_id': 'relationTypeId',
        'relation_trace_entries': 'relationTraceEntries',
        'apply_relation_trace_on_target': 'applyRelationTraceOnTarget'
    }

    def __init__(self, assets_to_apply_trace_on_ids=None, relation_type_id=None, relation_trace_entries=None, apply_relation_trace_on_target=None):  # noqa: E501
        """JsonFindTailOfRelationTraceRequest - a model defined in Swagger"""  # noqa: E501

        self._assets_to_apply_trace_on_ids = None
        self._relation_type_id = None
        self._relation_trace_entries = None
        self._apply_relation_trace_on_target = None
        self.discriminator = None

        self.assets_to_apply_trace_on_ids = assets_to_apply_trace_on_ids
        self.relation_type_id = relation_type_id
        self.relation_trace_entries = relation_trace_entries
        if apply_relation_trace_on_target is not None:
            self.apply_relation_trace_on_target = apply_relation_trace_on_target

    @property
    def assets_to_apply_trace_on_ids(self):
        """Gets the assets_to_apply_trace_on_ids of this JsonFindTailOfRelationTraceRequest.  # noqa: E501

          # noqa: E501

        :return: The assets_to_apply_trace_on_ids of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._assets_to_apply_trace_on_ids

    @assets_to_apply_trace_on_ids.setter
    def assets_to_apply_trace_on_ids(self, assets_to_apply_trace_on_ids):
        """Sets the assets_to_apply_trace_on_ids of this JsonFindTailOfRelationTraceRequest.

          # noqa: E501

        :param assets_to_apply_trace_on_ids: The assets_to_apply_trace_on_ids of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :type: list[str]
        """
        if assets_to_apply_trace_on_ids is None:
            raise ValueError("Invalid value for `assets_to_apply_trace_on_ids`, must not be `None`")  # noqa: E501

        self._assets_to_apply_trace_on_ids = assets_to_apply_trace_on_ids

    @property
    def relation_type_id(self):
        """Gets the relation_type_id of this JsonFindTailOfRelationTraceRequest.  # noqa: E501

          # noqa: E501

        :return: The relation_type_id of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_id

    @relation_type_id.setter
    def relation_type_id(self, relation_type_id):
        """Sets the relation_type_id of this JsonFindTailOfRelationTraceRequest.

          # noqa: E501

        :param relation_type_id: The relation_type_id of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :type: str
        """
        if relation_type_id is None:
            raise ValueError("Invalid value for `relation_type_id`, must not be `None`")  # noqa: E501

        self._relation_type_id = relation_type_id

    @property
    def relation_trace_entries(self):
        """Gets the relation_trace_entries of this JsonFindTailOfRelationTraceRequest.  # noqa: E501

          # noqa: E501

        :return: The relation_trace_entries of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._relation_trace_entries

    @relation_trace_entries.setter
    def relation_trace_entries(self, relation_trace_entries):
        """Sets the relation_trace_entries of this JsonFindTailOfRelationTraceRequest.

          # noqa: E501

        :param relation_trace_entries: The relation_trace_entries of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :type: list[object]
        """
        if relation_trace_entries is None:
            raise ValueError("Invalid value for `relation_trace_entries`, must not be `None`")  # noqa: E501

        self._relation_trace_entries = relation_trace_entries

    @property
    def apply_relation_trace_on_target(self):
        """Gets the apply_relation_trace_on_target of this JsonFindTailOfRelationTraceRequest.  # noqa: E501

          # noqa: E501

        :return: The apply_relation_trace_on_target of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._apply_relation_trace_on_target

    @apply_relation_trace_on_target.setter
    def apply_relation_trace_on_target(self, apply_relation_trace_on_target):
        """Sets the apply_relation_trace_on_target of this JsonFindTailOfRelationTraceRequest.

          # noqa: E501

        :param apply_relation_trace_on_target: The apply_relation_trace_on_target of this JsonFindTailOfRelationTraceRequest.  # noqa: E501
        :type: bool
        """

        self._apply_relation_trace_on_target = apply_relation_trace_on_target

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
        if not isinstance(other, JsonFindTailOfRelationTraceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other