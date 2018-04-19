# JsonWorkflowDefinitionImpl

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
**process_id** | **str** | The &lt;code&gt;id&lt;/code&gt; that uniquely identifies a workflow definition in the application. It is present in the BPMN notation in the ID property of the &#39;&lt;process..&#39; tag. Deploying a BPMN in DGC creates a new version if a process with the same ID already exists. | [optional] 
**start_label** | **str** | The label used for starting this workflow | [optional] 
**form_required** | **bool** | Whether the start form for this workflow requires user interaction through a form or not | [optional] 
**enabled** | **bool** | Whether workflow is enabled or not. A workflow has to be enabled for a user to be able to start a workflow. A workflow is enabled if it&#39;s status is put on the status &#39;enabled&#39; | [optional] 
**domain_assignment_rules** | [**list[JsonDomainAssignmentRuleImpl]**](JsonDomainAssignmentRuleImpl.md) | The list of domain assignment rules | [optional] 
**asset_assignment_rules** | [**list[JsonAssetAssignmentRuleImpl]**](JsonAssetAssignmentRuleImpl.md) | The list of asset assignment rules | [optional] 
**business_item_resource_type** | [**JsonWorkflowBusinessItemType**](JsonWorkflowBusinessItemType.md) | The type of business item that the workflow can refer to. This could be either Community, Domain, Asset, or global | [optional] 
**exclusivity** | [**JsonWorkflowExclusivity**](JsonWorkflowExclusivity.md) | The exclusivity of this workflow. This determines how many times a workflow can be started for a specific resource | [optional] 
**guest_user_accessible** | **bool** | Whether this workflow definition is guest user accessible | [optional] 
**registered_user_accessible** | **bool** | Whether the workflow definition is accessible by any registered user | [optional] 
**candidate_user_check_enabled** | **bool** | Whether the candidate user check for this workflow is enabled | [optional] 
**start_events** | [**list[JsonWorkflowStartEventType]**](JsonWorkflowStartEventType.md) | The start events in a list of WorkflowStartEventType enums | [optional] 
**configuration_variables** | **dict(str, str)** | The map of configuration variable key-value pairs | [optional] 
**start_roles** | [**list[JsonRoleImpl]**](JsonRoleImpl.md) | The roles allowed to start the process | [optional] 
**stop_roles** | [**list[JsonRoleImpl]**](JsonRoleImpl.md) | The roles allowed to stop processes/tasks | [optional] 
**reassign_roles** | [**list[JsonRoleImpl]**](JsonRoleImpl.md) | The roles allowed to reassign tasks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


