# JsonFindResponsibilitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**resource_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the resources for which the responsibilities should be found | [optional] 
**owner_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the owners for which the responsibilities should be found | [optional] 
**role_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the roles for which the responsibilities should be found | [optional] 
**include_inherited** | **bool** | Whether inherited responsibilities should be included in the search results | [optional] 
**global_only** | **bool** | Whether only global responsibilities should be searched | [optional] 
**sort_field** | [**JsonSortFieldFindResponsibilitiesRequest**](JsonSortFieldFindResponsibilitiesRequest.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The order of sorting | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


