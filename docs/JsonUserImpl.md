# JsonUserImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the represented object (entity) | 
**created_by** | **str** | The id of the user that created this resource | [optional] 
**created_on** | **float** | The timestamp (in UTC time standard) of the creation of this resource | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time | [optional] 
**last_modified_on** | **float** | The timestamp (in UTC time standard) of the last modification of this resource | [optional] 
**system** | **bool** | Whether this is a system resource or not | [optional] 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] | [optional] 
**user_name** | **str** | The username | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**email_address** | **str** | The main email address | [optional] 
**gender** | [**JsonGender**](JsonGender.md) | The gender of the user | [optional] 
**language** | **str** | The current language preference for this user | [optional] 
**additional_email_addresses** | [**list[JsonEmailImpl]**](JsonEmailImpl.md) | The list of additional email addresses | [optional] 
**phone_numbers** | [**list[JsonPhoneNumberImpl]**](JsonPhoneNumberImpl.md) | The list of phone numbers | [optional] 
**instant_messaging_accounts** | [**list[JsonInstantMessagingAccountImpl]**](JsonInstantMessagingAccountImpl.md) | The list of instant messaging accounts | [optional] 
**websites** | [**list[JsonWebsiteImpl]**](JsonWebsiteImpl.md) | The list of websites | [optional] 
**addresses** | [**list[JsonAddressImpl]**](JsonAddressImpl.md) | The list of addresses | [optional] 
**activated** | **bool** | Whether this user account is already activated or not | [optional] 
**enabled** | **bool** | Whether this user account is already enabled or not | [optional] 
**ldap_user** | **bool** | Whether this is an LDAP user or not | [optional] 
**guest_user** | **bool** | Whether this is a guest user or not | [optional] 
**api_user** | **bool** | Whether this is API user or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


