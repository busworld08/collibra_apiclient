# XmlNs0FindAttributeTypesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**is_integer** | **bool** | Whether only integer-type attribute types should be searched or not | [optional] 
**kind** | [**XmlNs0AttributeKind**](XmlNs0AttributeKind.md) | The kind of the attribute type to search for | [optional] 
**language** | **str** | The language of the attribute type to search for | [optional] 
**name** | **str** | The name of the attribute type to search for | [optional] 
**name_match_mode** | [**XmlNs0MatchMode**](XmlNs0MatchMode.md) | The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] 
**sort_field** | [**XmlNs0SortField**](XmlNs0SortField.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**XmlNs0SortOrder**](XmlNs0SortOrder.md) | The order of sorting | [optional] 
**statistics_enabled** | **bool** | Whether the attribute types should be searched with statistics enabled or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


