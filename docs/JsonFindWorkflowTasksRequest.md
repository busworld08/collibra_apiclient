# JsonFindWorkflowTasksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**business_item_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the business item | [optional] 
**business_item_type** | [**JsonBusinessItemType**](JsonBusinessItemType.md) | The type of the business item | [optional] 
**workflow_task_user_relation** | [**JsonWorkflowTaskUserRelation**](JsonWorkflowTaskUserRelation.md) | The type of relation between user and searched tasks &lt;p&gt; This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user. | [optional] 
**business_item_name** | **str** | The part of the name of the business item | [optional] 
**user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user for which the tasks need to be returned. If empty, the current logged in user will be used | [optional] 
**create_date** | **float** | The creation date of the task. It is the timestamp (in UTC time standard) | [optional] 
**due_date** | **float** | The due date of the task. It is the timestamp (in UTC time standard) | [optional] 
**title** | **str** | The title/name of the task | [optional] 
**type** | **str** | The task type | [optional] 
**sort_field** | [**JsonSortFieldFindWorkflowTasksRequest**](JsonSortFieldFindWorkflowTasksRequest.md) | The field on which the results are sorted. On due date by default. For possible values see SortField | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The sorting order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


