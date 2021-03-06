# XmlNs0FindAssetsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**community_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the community to find the assets in | [optional] 
**domain_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the domain to find the assets in | [optional] 
**exclude_meta** | **bool** | The exclude meta flag. If this is set to true then the assets from meta domains will not be returned (meta domains are the domains which were not created by the user manually) | [optional] 
**name** | **str** | The name of the asset to search for | [optional] 
**name_match_mode** | [**XmlNs0MatchMode**](XmlNs0MatchMode.md) | The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] 
**status_ids** | **str** | The list of &lt;code&gt;ids&lt;/code&gt; of the statuses. The returned assets have one of statuses specified by this parameter | [optional] 
**tag_names** | **str** | The list of names of tags. The returned assets have one of tags with names specified by this parameter | [optional] 
**type_ids** | **str** | The list of &lt;code&gt;ids&lt;/code&gt; of the asset types. The returned assets are of one of types specified by this parameter | [optional] 
**type_inheritance** | **bool** | Whether the type inheritance for the asset type filtering should be applied or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


