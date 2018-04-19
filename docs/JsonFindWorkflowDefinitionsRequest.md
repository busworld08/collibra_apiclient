# JsonFindWorkflowDefinitionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**asset_ids** | **list[str]** | The list of the &lt;code&gt;id&lt;/code&gt;s of business items (assets) for which the workflow definitions should be found | [optional] 
**domain_ids** | **list[str]** | The list of the &lt;code&gt;id&lt;/code&gt;s of business items (domains) for which the workflow definitions should be found | [optional] 
**community_ids** | **list[str]** | The list of the &lt;code&gt;id&lt;/code&gt;s of business items (communities) for which the workflow definitions should be found | [optional] 
**enabled** | **bool** | Whether the found workflow definitions should be enabled | [optional] 
**_global** | **bool** | Whether the found workflow definitions should be global | [optional] 
**name** | **str** | The name (could be partial) of the workflow definition to search for | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


