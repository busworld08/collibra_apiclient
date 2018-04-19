# XmlNs0WorkflowTaskImpl

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
**aggregation_key** | **str** | The key for aggregation purposes. If empty, the task can&#39;t be aggregated | [optional] 
**business_item** | **object** | The reference to the business item Resource related to the task | [optional] 
**cancelable** | **bool** | Whether this workflow task is cancelable or not | [optional] 
**candidate_users** | **object** | The list of candidate users | [optional] 
**contains_activity_stream** | **bool** | Whether this task contains an activity stream or not | [optional] 
**create_time** | **float** | The create time | [optional] 
**custom_buttons** | **object** | The list of custom buttons | [optional] 
**description** | **str** | The description of the workflow task | [optional] 
**due_date** | **float** | The due date | [optional] 
**error_message** | **str** | The error message in case this task is in error | [optional] 
**form_required** | **bool** | Whether this task requires a form or not | [optional] 
**in_error** | **bool** | Whether this task is in error or not | [optional] 
**key** | **str** | The key | [optional] 
**owner** | **str** | The owner | [optional] 
**priority** | **float** | The priority | [optional] 
**reassignable** | **bool** | Whether this workflow task is reassignable or not | [optional] 
**title** | **str** | The title of the task | [optional] 
**type** | **str** | The type | [optional] 
**workflow_definition** | **object** | The reference to the workflow definition | [optional] 
**workflow_instance_id** | **str** | The UUID of the workflow instance | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


