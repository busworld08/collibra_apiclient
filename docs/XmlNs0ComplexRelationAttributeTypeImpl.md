# XmlNs0ComplexRelationAttributeTypeImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the represented object (entity) | [optional] 
**created_by** | **str** | The id of the user that created this resource | [optional] 
**created_on** | **float** | The timestamp (in UTC time standard) of the creation of this resource | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time | [optional] 
**last_modified_on** | **float** | The timestamp (in UTC time standard) of the last modification of this resource | [optional] 
**resource_type** | [**XmlNs0ResourceType**](XmlNs0ResourceType.md) | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] | [optional] 
**system** | **bool** | Whether this is a system resource or not | [optional] 
**attribute_type** | **object** | The attribute type that can be assigned to the complex relation | [optional] 
**maximum_occurrences** | **float** | How many times the assigned attribute may be added to the resource. Null means no restriction | [optional] 
**minimum_occurrences** | **float** | How many times at least the assigned attribute must be added to the resource. Zero means no restriction | [optional] 
**read_only** | **bool** | Whether the characteristic value of the assigned type can be edited by the user or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


