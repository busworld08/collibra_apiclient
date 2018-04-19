# JsonChangeWorkflowDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_variables** | **dict(str, str)** | The configuration variables | [optional] 
**start_events** | [**list[JsonWorkflowStartEventType]**](JsonWorkflowStartEventType.md) | The list of workflow start event types | [optional] 
**business_item_resource_type** | [**JsonWorkflowBusinessItemType**](JsonWorkflowBusinessItemType.md) | The type of the business item corresponding to the workflow | [optional] 
**exclusivity** | [**JsonWorkflowExclusivity**](JsonWorkflowExclusivity.md) | Defines the number of times a resource workflow is able to be start (see WorkflowExclusivity) | [optional] 
**guest_user_accessible** | **bool** | Whether the workflow should be accessible by the guest user | [optional] 
**registered_user_accessible** | **bool** | Whether the workflow should be accessible by the registered user | [optional] 
**candidate_user_check_disabled** | **bool** | Whether the candidate user check for the workflow should be disabled | [optional] 
**start_label** | **str** | The start label of the workflow | [optional] 
**start_role_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s identifying the roles allowing to start the workflow | [optional] 
**stop_role_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s identifying the roles allowing to stop the workflow | [optional] 
**reassign_role_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s identifying the roles allowing to reassign the workflow | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


