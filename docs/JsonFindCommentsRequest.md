# JsonFindCommentsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**parent_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the comment which the reply comments should be searched for | [optional] 
**user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user who created the comment | [optional] 
**base_resource_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the resource which the searched comments refer to | [optional] 
**root_comment** | **bool** | Whether the searched comments should be root comments (not reply comments) | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The order of sorting on the date the comment was created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


