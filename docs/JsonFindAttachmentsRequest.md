# JsonFindAttachmentsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**file_name** | **str** | The name of the file representing searched attachment | [optional] 
**file_content_type** | **str** | The type of the content of the file representing searched attachment | [optional] 
**upload_date** | **float** | The date of attachment upload. It is the timestamp (in UTC time standard) | [optional] 
**user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user who uploaded the attachment | [optional] 
**base_resource_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the resource the attachment refers to | [optional] 
**sort_field** | [**JsonSortField**](JsonSortField.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The order of sorting | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


