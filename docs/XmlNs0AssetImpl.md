# XmlNs0AssetImpl

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
**name** | **str** | The name of the resource | [optional] 
**articulation_score** | **float** | The articulation score for this asset. &lt;p&gt; Expresses how well this asset is articulated. The articulation score is a percentage number ranging from 0 to 100. The articulation rules can be configured to calculate the articulation score. Whenever the asset is modified, by changing its attributes or statuses, the articulation score is re-evaluated | [optional] 
**domain** | **object** | The domain this asset is part of | [optional] 
**excluded_from_auto_hyperlinking** | **bool** | Whether this asset is excluded from hyperlinking or not | [optional] 
**status** | **object** | The status of this asset | [optional] 
**type** | **object** | The type of this asset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


