# JsonFindAttributesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**type_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the attribute types the found attributes should have | [optional] 
**asset_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the asset to find the attributes in | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The sorting order | [optional] 
**sort_field** | [**JsonSortFieldFindAttributesRequest**](JsonSortFieldFindAttributesRequest.md) | The field on which the results are sorted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

