# JsonAddAssetTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the new asset type. Should be unique within all asset types. It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**name** | **str** | The name of the new asset type. Should be unique within all asset types | 
**description** | **str** | The description of the new asset type | [optional] 
**color** | **str** | The color of the symbol, in a hex format e.g. &#39;#000000&#39;.  This format always includes the &#39;#&#39; and has a size of 7 | [optional] 
**symbol_type** | [**JsonAssetTypeSymbolType**](JsonAssetTypeSymbolType.md) | The symbol type | 
**icon_code** | **str** | The icon code, a code representing the icon that should be shown | [optional] 
**acronym_code** | **str** | The acronym code, a code representing the acronym that should be shown | [optional] 
**parent_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the parent for new asset type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


