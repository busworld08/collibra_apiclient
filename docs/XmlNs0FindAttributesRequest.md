# XmlNs0FindAttributesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**asset_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the asset to find the attributes in | [optional] 
**sort_field** | [**XmlNs0SortField**](XmlNs0SortField.md) | The field on which the results are sorted | [optional] 
**sort_order** | [**XmlNs0SortOrder**](XmlNs0SortOrder.md) | The sorting order | [optional] 
**type_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the attribute types the found attributes should have | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


