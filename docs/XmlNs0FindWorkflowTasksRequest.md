# XmlNs0FindWorkflowTasksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**business_item_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the business item | [optional] 
**business_item_name** | **str** | The part of the name of the business item | [optional] 
**business_item_type** | [**XmlNs0BusinessItemType**](XmlNs0BusinessItemType.md) | The type of the business item | [optional] 
**create_date** | **float** | The creation date of the task. It is the timestamp (in UTC time standard) | [optional] 
**due_date** | **float** | The due date of the task. It is the timestamp (in UTC time standard) | [optional] 
**sort_field** | [**XmlNs0SortField**](XmlNs0SortField.md) | The field on which the results are sorted. On due date by default. For possible values see SortField | [optional] 
**sort_order** | [**XmlNs0SortOrder**](XmlNs0SortOrder.md) | The sorting order | [optional] 
**title** | **str** | The title/name of the task | [optional] 
**type** | **str** | The task type | [optional] 
**user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user for which the tasks need to be returned. If empty, the current logged in user will be used | [optional] 
**workflow_task_user_relation** | [**XmlNs0WorkflowTaskUserRelation**](XmlNs0WorkflowTaskUserRelation.md) | The type of relation between user and searched tasks &lt;p&gt; This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


