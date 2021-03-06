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

from swagger_client.models.json_address_impl import JsonAddressImpl  # noqa: F401,E501
from swagger_client.models.json_email_impl import JsonEmailImpl  # noqa: F401,E501
from swagger_client.models.json_gender import JsonGender  # noqa: F401,E501
from swagger_client.models.json_instant_messaging_account_impl import JsonInstantMessagingAccountImpl  # noqa: F401,E501
from swagger_client.models.json_phone_number_impl import JsonPhoneNumberImpl  # noqa: F401,E501
from swagger_client.models.json_resource_impl import JsonResourceImpl  # noqa: F401,E501
from swagger_client.models.json_website_impl import JsonWebsiteImpl  # noqa: F401,E501


class JsonUserImpl(object):
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
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str',
        'gender': 'JsonGender',
        'language': 'str',
        'additional_email_addresses': 'list[JsonEmailImpl]',
        'phone_numbers': 'list[JsonPhoneNumberImpl]',
        'instant_messaging_accounts': 'list[JsonInstantMessagingAccountImpl]',
        'websites': 'list[JsonWebsiteImpl]',
        'addresses': 'list[JsonAddressImpl]',
        'activated': 'bool',
        'enabled': 'bool',
        'ldap_user': 'bool',
        'guest_user': 'bool',
        'api_user': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'user_name': 'userName',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress',
        'gender': 'gender',
        'language': 'language',
        'additional_email_addresses': 'additionalEmailAddresses',
        'phone_numbers': 'phoneNumbers',
        'instant_messaging_accounts': 'instantMessagingAccounts',
        'websites': 'websites',
        'addresses': 'addresses',
        'activated': 'activated',
        'enabled': 'enabled',
        'ldap_user': 'ldapUser',
        'guest_user': 'guestUser',
        'api_user': 'apiUser'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, user_name=None, first_name=None, last_name=None, email_address=None, gender=None, language=None, additional_email_addresses=None, phone_numbers=None, instant_messaging_accounts=None, websites=None, addresses=None, activated=None, enabled=None, ldap_user=None, guest_user=None, api_user=None):  # noqa: E501
        """JsonUserImpl - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._gender = None
        self._language = None
        self._additional_email_addresses = None
        self._phone_numbers = None
        self._instant_messaging_accounts = None
        self._websites = None
        self._addresses = None
        self._activated = None
        self._enabled = None
        self._ldap_user = None
        self._guest_user = None
        self._api_user = None
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
        if user_name is not None:
            self.user_name = user_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if gender is not None:
            self.gender = gender
        if language is not None:
            self.language = language
        if additional_email_addresses is not None:
            self.additional_email_addresses = additional_email_addresses
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if instant_messaging_accounts is not None:
            self.instant_messaging_accounts = instant_messaging_accounts
        if websites is not None:
            self.websites = websites
        if addresses is not None:
            self.addresses = addresses
        if activated is not None:
            self.activated = activated
        if enabled is not None:
            self.enabled = enabled
        if ldap_user is not None:
            self.ldap_user = ldap_user
        if guest_user is not None:
            self.guest_user = guest_user
        if api_user is not None:
            self.api_user = api_user

    @property
    def id(self):
        """Gets the id of this JsonUserImpl.  # noqa: E501

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :return: The id of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonUserImpl.

        The <code>id</code> of the represented object (entity)  # noqa: E501

        :param id: The id of this JsonUserImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this JsonUserImpl.  # noqa: E501

        The id of the user that created this resource  # noqa: E501

        :return: The created_by of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JsonUserImpl.

        The id of the user that created this resource  # noqa: E501

        :param created_by: The created_by of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this JsonUserImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :return: The created_on of this JsonUserImpl.  # noqa: E501
        :rtype: float
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this JsonUserImpl.

        The timestamp (in UTC time standard) of the creation of this resource  # noqa: E501

        :param created_on: The created_on of this JsonUserImpl.  # noqa: E501
        :type: float
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this JsonUserImpl.  # noqa: E501

        The id of the user who modified this resource the last time  # noqa: E501

        :return: The last_modified_by of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this JsonUserImpl.

        The id of the user who modified this resource the last time  # noqa: E501

        :param last_modified_by: The last_modified_by of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this JsonUserImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :return: The last_modified_on of this JsonUserImpl.  # noqa: E501
        :rtype: float
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this JsonUserImpl.

        The timestamp (in UTC time standard) of the last modification of this resource  # noqa: E501

        :param last_modified_on: The last_modified_on of this JsonUserImpl.  # noqa: E501
        :type: float
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this JsonUserImpl.  # noqa: E501

        Whether this is a system resource or not  # noqa: E501

        :return: The system of this JsonUserImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this JsonUserImpl.

        Whether this is a system resource or not  # noqa: E501

        :param system: The system of this JsonUserImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this JsonUserImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :return: The resource_type of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this JsonUserImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]  # noqa: E501

        :param resource_type: The resource_type of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def user_name(self):
        """Gets the user_name of this JsonUserImpl.  # noqa: E501

        The username  # noqa: E501

        :return: The user_name of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this JsonUserImpl.

        The username  # noqa: E501

        :param user_name: The user_name of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this JsonUserImpl.  # noqa: E501

        The first name of the user  # noqa: E501

        :return: The first_name of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this JsonUserImpl.

        The first name of the user  # noqa: E501

        :param first_name: The first_name of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this JsonUserImpl.  # noqa: E501

        The last name of the user  # noqa: E501

        :return: The last_name of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this JsonUserImpl.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this JsonUserImpl.  # noqa: E501

        The main email address  # noqa: E501

        :return: The email_address of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this JsonUserImpl.

        The main email address  # noqa: E501

        :param email_address: The email_address of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def gender(self):
        """Gets the gender of this JsonUserImpl.  # noqa: E501

        The gender of the user  # noqa: E501

        :return: The gender of this JsonUserImpl.  # noqa: E501
        :rtype: JsonGender
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this JsonUserImpl.

        The gender of the user  # noqa: E501

        :param gender: The gender of this JsonUserImpl.  # noqa: E501
        :type: JsonGender
        """

        self._gender = gender

    @property
    def language(self):
        """Gets the language of this JsonUserImpl.  # noqa: E501

        The current language preference for this user  # noqa: E501

        :return: The language of this JsonUserImpl.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this JsonUserImpl.

        The current language preference for this user  # noqa: E501

        :param language: The language of this JsonUserImpl.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def additional_email_addresses(self):
        """Gets the additional_email_addresses of this JsonUserImpl.  # noqa: E501

        The list of additional email addresses  # noqa: E501

        :return: The additional_email_addresses of this JsonUserImpl.  # noqa: E501
        :rtype: list[JsonEmailImpl]
        """
        return self._additional_email_addresses

    @additional_email_addresses.setter
    def additional_email_addresses(self, additional_email_addresses):
        """Sets the additional_email_addresses of this JsonUserImpl.

        The list of additional email addresses  # noqa: E501

        :param additional_email_addresses: The additional_email_addresses of this JsonUserImpl.  # noqa: E501
        :type: list[JsonEmailImpl]
        """

        self._additional_email_addresses = additional_email_addresses

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this JsonUserImpl.  # noqa: E501

        The list of phone numbers  # noqa: E501

        :return: The phone_numbers of this JsonUserImpl.  # noqa: E501
        :rtype: list[JsonPhoneNumberImpl]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this JsonUserImpl.

        The list of phone numbers  # noqa: E501

        :param phone_numbers: The phone_numbers of this JsonUserImpl.  # noqa: E501
        :type: list[JsonPhoneNumberImpl]
        """

        self._phone_numbers = phone_numbers

    @property
    def instant_messaging_accounts(self):
        """Gets the instant_messaging_accounts of this JsonUserImpl.  # noqa: E501

        The list of instant messaging accounts  # noqa: E501

        :return: The instant_messaging_accounts of this JsonUserImpl.  # noqa: E501
        :rtype: list[JsonInstantMessagingAccountImpl]
        """
        return self._instant_messaging_accounts

    @instant_messaging_accounts.setter
    def instant_messaging_accounts(self, instant_messaging_accounts):
        """Sets the instant_messaging_accounts of this JsonUserImpl.

        The list of instant messaging accounts  # noqa: E501

        :param instant_messaging_accounts: The instant_messaging_accounts of this JsonUserImpl.  # noqa: E501
        :type: list[JsonInstantMessagingAccountImpl]
        """

        self._instant_messaging_accounts = instant_messaging_accounts

    @property
    def websites(self):
        """Gets the websites of this JsonUserImpl.  # noqa: E501

        The list of websites  # noqa: E501

        :return: The websites of this JsonUserImpl.  # noqa: E501
        :rtype: list[JsonWebsiteImpl]
        """
        return self._websites

    @websites.setter
    def websites(self, websites):
        """Sets the websites of this JsonUserImpl.

        The list of websites  # noqa: E501

        :param websites: The websites of this JsonUserImpl.  # noqa: E501
        :type: list[JsonWebsiteImpl]
        """

        self._websites = websites

    @property
    def addresses(self):
        """Gets the addresses of this JsonUserImpl.  # noqa: E501

        The list of addresses  # noqa: E501

        :return: The addresses of this JsonUserImpl.  # noqa: E501
        :rtype: list[JsonAddressImpl]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this JsonUserImpl.

        The list of addresses  # noqa: E501

        :param addresses: The addresses of this JsonUserImpl.  # noqa: E501
        :type: list[JsonAddressImpl]
        """

        self._addresses = addresses

    @property
    def activated(self):
        """Gets the activated of this JsonUserImpl.  # noqa: E501

        Whether this user account is already activated or not  # noqa: E501

        :return: The activated of this JsonUserImpl.  # noqa: E501
        :rtype: bool
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this JsonUserImpl.

        Whether this user account is already activated or not  # noqa: E501

        :param activated: The activated of this JsonUserImpl.  # noqa: E501
        :type: bool
        """

        self._activated = activated

    @property
    def enabled(self):
        """Gets the enabled of this JsonUserImpl.  # noqa: E501

        Whether this user account is already enabled or not  # noqa: E501

        :return: The enabled of this JsonUserImpl.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this JsonUserImpl.

        Whether this user account is already enabled or not  # noqa: E501

        :param enabled: The enabled of this JsonUserImpl.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def ldap_user(self):
        """Gets the ldap_user of this JsonUserImpl.  # noqa: E501

        Whether this is an LDAP user or not  # noqa: E501

        :return: The ldap_user of this JsonUserImpl.  # noqa: E501
        :rtype: bool
        """
        return self._ldap_user

    @ldap_user.setter
    def ldap_user(self, ldap_user):
        """Sets the ldap_user of this JsonUserImpl.

        Whether this is an LDAP user or not  # noqa: E501

        :param ldap_user: The ldap_user of this JsonUserImpl.  # noqa: E501
        :type: bool
        """

        self._ldap_user = ldap_user

    @property
    def guest_user(self):
        """Gets the guest_user of this JsonUserImpl.  # noqa: E501

        Whether this is a guest user or not  # noqa: E501

        :return: The guest_user of this JsonUserImpl.  # noqa: E501
        :rtype: bool
        """
        return self._guest_user

    @guest_user.setter
    def guest_user(self, guest_user):
        """Sets the guest_user of this JsonUserImpl.

        Whether this is a guest user or not  # noqa: E501

        :param guest_user: The guest_user of this JsonUserImpl.  # noqa: E501
        :type: bool
        """

        self._guest_user = guest_user

    @property
    def api_user(self):
        """Gets the api_user of this JsonUserImpl.  # noqa: E501

        Whether this is API user or not  # noqa: E501

        :return: The api_user of this JsonUserImpl.  # noqa: E501
        :rtype: bool
        """
        return self._api_user

    @api_user.setter
    def api_user(self, api_user):
        """Sets the api_user of this JsonUserImpl.

        Whether this is API user or not  # noqa: E501

        :param api_user: The api_user of this JsonUserImpl.  # noqa: E501
        :type: bool
        """

        self._api_user = api_user

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
        if not isinstance(other, JsonUserImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
