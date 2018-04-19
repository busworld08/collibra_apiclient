# JsonFindAttributeTypesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**name** | **str** | The name of the attribute type to search for | [optional] 
**name_match_mode** | [**JsonMatchMode**](JsonMatchMode.md) | The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] 
**kind** | [**JsonAttributeKind**](JsonAttributeKind.md) | The kind of the attribute type to search for | [optional] 
**language** | **str** | The language of the attribute type to search for | [optional] 
**statistics_enabled** | **bool** | Whether the attribute types should be searched with statistics enabled or not | [optional] 
**is_integer** | **bool** | Whether only integer-type attribute types should be searched or not | [optional] 
**sort_field** | [**JsonSortFieldFindAttributeTypesRequest**](JsonSortFieldFindAttributeTypesRequest.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The order of sorting | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


