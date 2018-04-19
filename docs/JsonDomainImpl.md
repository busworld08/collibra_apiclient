# JsonDomainImpl

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
**name** | **str** | The name of the resource | [optional] 
**description** | **str** | The description of the resource | [optional] 
**type** | [**JsonNamedResourceReferenceImpl**](JsonNamedResourceReferenceImpl.md) | The type of this domain | [optional] 
**community** | [**JsonNamedResourceReferenceImpl**](JsonNamedResourceReferenceImpl.md) | The community this domain is part of | [optional] 
**excluded_from_auto_hyperlinking** | **bool** | Whether this domain is excluded from hyperlinking or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


