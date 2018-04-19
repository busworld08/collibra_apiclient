# XmlNs0WorkflowDefinitionImpl

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
**asset_assignment_rules** | **object** | The list of asset assignment rules | [optional] 
**business_item_resource_type** | [**XmlNs0WorkflowBusinessItemType**](XmlNs0WorkflowBusinessItemType.md) | The type of business item that the workflow can refer to. This could be either Community, Domain, Asset, or global | [optional] 
**candidate_user_check_enabled** | **bool** | Whether the candidate user check for this workflow is enabled | [optional] 
**configuration_variables** | **object** | The map of configuration variable key-value pairs | [optional] 
**domain_assignment_rules** | **object** | The list of domain assignment rules | [optional] 
**enabled** | **bool** | Whether workflow is enabled or not. A workflow has to be enabled for a user to be able to start a workflow. A workflow is enabled if it&#39;s status is put on the status &#39;enabled&#39; | [optional] 
**exclusivity** | [**XmlNs0WorkflowExclusivity**](XmlNs0WorkflowExclusivity.md) | The exclusivity of this workflow. This determines how many times a workflow can be started for a specific resource | [optional] 
**form_required** | **bool** | Whether the start form for this workflow requires user interaction through a form or not | [optional] 
**guest_user_accessible** | **bool** | Whether this workflow definition is guest user accessible | [optional] 
**process_id** | **str** | The &lt;code&gt;id&lt;/code&gt; that uniquely identifies a workflow definition in the application. It is present in the BPMN notation in the ID property of the &#39;&lt;process..&#39; tag. Deploying a BPMN in DGC creates a new version if a process with the same ID already exists. | [optional] 
**reassign_roles** | **object** | The roles allowed to reassign tasks | [optional] 
**registered_user_accessible** | **bool** | Whether the workflow definition is accessible by any registered user | [optional] 
**start_events** | [**XmlNs0WorkflowStartEventType**](XmlNs0WorkflowStartEventType.md) | The start events in a list of WorkflowStartEventType enums | [optional] 
**start_label** | **str** | The label used for starting this workflow | [optional] 
**start_roles** | **object** | The roles allowed to start the process | [optional] 
**stop_roles** | **object** | The roles allowed to stop processes/tasks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


