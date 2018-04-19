# XmlNs0FindRelationTypesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**co_role** | **str** | The name of the role that the target plays to search for | [optional] 
**role** | **str** | The name of the role that the source plays to search for | [optional] 
**role_co_role_logical_operator** | [**XmlNs0LogicalOperator**](XmlNs0LogicalOperator.md) | The logical operator determining how to combine the role and coRole criteria: AND or OR | [optional] 
**sort_field** | [**XmlNs0SortField**](XmlNs0SortField.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**XmlNs0SortOrder**](XmlNs0SortOrder.md) | The order of sorting | [optional] 
**source_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the source type of the relation type to search for | [optional] 
**source_type_name** | **str** | The name of the source type of the relation type to search for | [optional] 
**target_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the target type of the relation type to search for | [optional] 
**target_type_name** | **str** | The name of the target type of the relation type to search for | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


