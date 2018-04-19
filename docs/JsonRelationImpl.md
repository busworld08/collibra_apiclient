# JsonRelationImpl

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
**source** | [**JsonNamedResourceReferenceImpl**](JsonNamedResourceReferenceImpl.md) | The reference to the source asset of the relation | [optional] 
**target** | [**JsonNamedResourceReferenceImpl**](JsonNamedResourceReferenceImpl.md) | The reference to the target asset of the relation | [optional] 
**type** | [**JsonResourceReferenceImpl**](JsonResourceReferenceImpl.md) | The type of the relation | [optional] 
**starting_date** | **float** | The timestamp representing the starting date of the relation | [optional] 
**ending_date** | **float** | The timestamp representing the ending date of the relation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


