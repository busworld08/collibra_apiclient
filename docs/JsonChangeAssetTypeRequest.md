# JsonChangeAssetTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the asset type to be changed. Silently ignored if the &lt;code&gt;id&lt;/code&gt; is provided as path parameter of the request | 
**name** | **str** | The new name for the asset type | [optional] 
**description** | **str** | The new description for the asset type | [optional] 
**parent_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the new parent for the asset type | [optional] 
**color** | **str** | The color of the symbol, in a hex format e.g. &#39;#000000&#39;.  This format always includes the &#39;#&#39; and has a size of 7 | [optional] 
**symbol_type** | [**JsonAssetTypeSymbolType**](JsonAssetTypeSymbolType.md) | The symbol type | [optional] 
**icon_code** | **str** | The icon code, a code representing the icon that should be shown | [optional] 
**acronym_code** | **str** | The acronym code, a code representing the acronym that should be shown | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


