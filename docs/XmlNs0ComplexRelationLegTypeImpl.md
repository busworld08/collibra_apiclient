# XmlNs0ComplexRelationLegTypeImpl

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
**asset_type** | **object** | The reference to the asset type contained by this leg type. Only asset with asset type equal to or inherited from this asset type can be contained with this leg type. | [optional] 
**co_role** | **str** | The name of the role that target plays in the relation | [optional] 
**maximum_occurrences** | **float** | The maximum number of occurrences of this leg type within complex relation | [optional] 
**minimum_occurrences** | **float** | The minimum number of occurrences of this leg type within complex relation | [optional] 
**relation_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the relation type | [optional] 
**role** | **str** | The name of the role that source plays in the relation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


