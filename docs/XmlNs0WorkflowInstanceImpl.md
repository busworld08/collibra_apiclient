# XmlNs0WorkflowInstanceImpl

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
**business_item** | **object** | The optional business item Resource related to the process instance | [optional] 
**created_asset_id** | **str** | The optional &lt;code&gt;id&lt;/code&gt; of the created asset if the process instance ended, created a term and it is configured for it | [optional] 
**ended** | **bool** | Whether this process instance is already ended | [optional] 
**error_message** | **str** | The optional error message of any error in a async continuation of this process instance. Only present if inError is true | [optional] 
**in_error** | **bool** | Whether this process instance is in error. This means that there was a problem with a async continuation of the process instance | [optional] 
**start_date** | **float** | The start date of this process instance | [optional] 
**sub_instances** | **object** | The sub process instances of this instance | [optional] 
**tasks** | **object** | The List of WorkflowTasks in this process instance | [optional] 
**workflow_definition** | **object** | The reference to the workflow definition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


