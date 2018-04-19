# JsonStartWorkflowInstancesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_definition_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the workflow definition | 
**business_item_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s for the business items | [optional] 
**business_item_type** | [**JsonWorkflowBusinessItemType**](JsonWorkflowBusinessItemType.md) | The resource type of the passed in business items | [optional] 
**form_properties** | **dict(str, str)** | The properties of the workflow | [optional] 
**guest_user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the guest user starting the workflow | [optional] 
**send_notification** | **bool** | Whether notification on starting the workflows should be sent | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


