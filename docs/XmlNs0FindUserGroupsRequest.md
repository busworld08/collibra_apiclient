# XmlNs0FindUserGroupsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**include_everyone** | **bool** |  | [optional] 
**name** | **str** | The name of the user group | [optional] 
**name_match_mode** | [**XmlNs0MatchMode**](XmlNs0MatchMode.md) | The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] 
**user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user who should belong to searched user groups | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


