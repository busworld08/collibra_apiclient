# JsonComplexRelationTypeImpl

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
**symbol_data** | [**JsonSymbolDataImpl**](JsonSymbolDataImpl.md) | The symbol data of the complex relation type | [optional] 
**attribute_types** | [**list[JsonComplexRelationAttributeTypeImpl]**](JsonComplexRelationAttributeTypeImpl.md) | The list of the attribute types that are accepted for the complex relation of this type | [optional] 
**leg_types** | [**list[JsonComplexRelationLegTypeImpl]**](JsonComplexRelationLegTypeImpl.md) | The list of the leg types representing assets related within complex relation type with given role and co-role | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


