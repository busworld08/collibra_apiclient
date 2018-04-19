# XmlNs0FindResponsibilitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**global_only** | **bool** | Whether only global responsibilities should be searched | [optional] 
**include_inherited** | **bool** | Whether inherited responsibilities should be included in the search results | [optional] 
**owner_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the owners for which the responsibilities should be found | [optional] 
**resource_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the resources for which the responsibilities should be found | [optional] 
**role_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the roles for which the responsibilities should be found | [optional] 
**sort_field** | [**XmlNs0SortField**](XmlNs0SortField.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**XmlNs0SortOrder**](XmlNs0SortOrder.md) | The order of sorting | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


