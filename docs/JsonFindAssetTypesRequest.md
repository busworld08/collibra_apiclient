# JsonFindAssetTypesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**name** | **str** | The name of the asset type to search for | [optional] 
**name_match_mode** | [**JsonMatchMode**](JsonMatchMode.md) | The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] 
**parent_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the parent to find the asset types in | [optional] 
**exclude_meta** | **bool** | Whether the meta asset types should be excluded from search or not | [optional] 
**top_level** | **bool** | Whether only top level asset types should be searched or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


