# JsonDiagramPictureImpl

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
**config** | **str** |  | [optional] 
**svg** | **str** |  | [optional] 
**original_view_id** | **str** |  | [optional] 
**is_preferred** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**sharing_rules** | [**list[JsonSharingRule]**](JsonSharingRule.md) |  | [optional] 
**assignment_rules** | **list[object]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


