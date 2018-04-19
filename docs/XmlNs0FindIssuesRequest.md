# XmlNs0FindIssuesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**only_open_issues** | **bool** | Whether only open issues should be returned | [optional] 
**sort_field** | [**XmlNs0SortField**](XmlNs0SortField.md) | The field on which the results are sorted. Default is NAME | [optional] 
**sort_order** | [**XmlNs0SortOrder**](XmlNs0SortOrder.md) | The sorting order of the results | [optional] 
**user_relation** | [**XmlNs0IssueUserRelation**](XmlNs0IssueUserRelation.md) | The relation of the user with the issues to be returned. By default all issues for the current user will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


