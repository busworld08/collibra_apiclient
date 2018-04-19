# JsonFindDomainsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**name** | **str** | The name of the domain to search for | [optional] 
**name_match_mode** | [**JsonMatchMode**](JsonMatchMode.md) | The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] 
**exclude_meta** | **bool** | The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user) | [optional] 
**community_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the community to find the domains in | [optional] 
**type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the domain type to search for. Returned domains are of this type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


