# JsonJdbcDriver

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
**database_name** | **str** |  | [optional] 
**database_version** | **str** |  | [optional] 
**driver** | **str** |  | [optional] 
**connection_string** | **str** |  | [optional] 
**jdbc_driver_files** | [**list[JsonJdbcDriverFile]**](JsonJdbcDriverFile.md) |  | [optional] 
**connection_string_parameters** | [**list[JsonConnectionStringParameter]**](JsonConnectionStringParameter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


