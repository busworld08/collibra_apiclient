# JsonSetAssetRelationsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the relation type for the relations to be set | 
**related_asset_ids** | **list[str]** | The &lt;code&gt;id&lt;/code&gt;s of the related assets | 
**relation_direction** | [**JsonRelationDirection**](JsonRelationDirection.md) | The relation direction. If TO_SOURCE then related assets will become source assets. Otherwise they will become target assets for created relations | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


