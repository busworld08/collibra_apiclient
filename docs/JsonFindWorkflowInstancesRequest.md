# JsonFindWorkflowInstancesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**business_item_name** | **str** | The name of the business item that should be contained by the searched workflows | [optional] 
**workflow_definition_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the workflow definition | [optional] 
**sort_field** | [**JsonSortFieldFindWorkflowInstancesRequest**](JsonSortFieldFindWorkflowInstancesRequest.md) | The field on which the results are sorted | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The sorting order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


