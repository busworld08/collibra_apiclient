# JsonWorkflowInstanceImpl

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
**workflow_definition** | [**JsonWorkflowDefinitionReferenceImpl**](JsonWorkflowDefinitionReferenceImpl.md) | The reference to the workflow definition | [optional] 
**sub_instances** | [**list[JsonWorkflowInstanceImpl]**](JsonWorkflowInstanceImpl.md) | The sub process instances of this instance | [optional] 
**business_item** | [**JsonResourceReferenceImpl**](JsonResourceReferenceImpl.md) | The optional business item Resource related to the process instance | [optional] 
**tasks** | [**list[JsonWorkflowTaskImpl]**](JsonWorkflowTaskImpl.md) | The List of WorkflowTasks in this process instance | [optional] 
**start_date** | **float** | The start date of this process instance | [optional] 
**ended** | **bool** | Whether this process instance is already ended | [optional] 
**created_asset_id** | **str** | The optional &lt;code&gt;id&lt;/code&gt; of the created asset if the process instance ended, created a term and it is configured for it | [optional] 
**in_error** | **bool** | Whether this process instance is in error. This means that there was a problem with a async continuation of the process instance | [optional] 
**error_message** | **str** | The optional error message of any error in a async continuation of this process instance. Only present if inError is true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


