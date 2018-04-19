# XmlNs0ChangeWorkflowDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_item_resource_type** | [**XmlNs0WorkflowBusinessItemType**](XmlNs0WorkflowBusinessItemType.md) | The type of the business item corresponding to the workflow | [optional] 
**candidate_user_check_disabled** | **bool** | Whether the candidate user check for the workflow should be disabled | [optional] 
**configuration_variables** | **object** | The configuration variables | [optional] 
**exclusivity** | [**XmlNs0WorkflowExclusivity**](XmlNs0WorkflowExclusivity.md) | Defines the number of times a resource workflow is able to be start (see WorkflowExclusivity) | [optional] 
**guest_user_accessible** | **bool** | Whether the workflow should be accessible by the guest user | [optional] 
**reassign_role_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s identifying the roles allowing to reassign the workflow | [optional] 
**registered_user_accessible** | **bool** | Whether the workflow should be accessible by the registered user | [optional] 
**start_events** | [**XmlNs0WorkflowStartEventType**](XmlNs0WorkflowStartEventType.md) | The list of workflow start event types | [optional] 
**start_label** | **str** | The start label of the workflow | [optional] 
**start_role_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s identifying the roles allowing to start the workflow | [optional] 
**stop_role_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s identifying the roles allowing to stop the workflow | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


