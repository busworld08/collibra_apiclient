# XmlNs0FindUsersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**group_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the group the searched users should belong to | [optional] 
**include_disabled** | **bool** | Whether disabled users should be included in the search results | [optional] 
**name** | **str** | The name of the user. The search will occur in the username, firstname and lastname (and a combination) | [optional] 
**only_logged_in** | **bool** | Whether only currently logged in users should be returned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


