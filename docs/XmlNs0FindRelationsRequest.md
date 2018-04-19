# XmlNs0FindRelationsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**relation_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the type of relations to search for | [optional] 
**source_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the source of relations to search for | [optional] 
**source_target_logical_operator** | [**XmlNs0LogicalOperator**](XmlNs0LogicalOperator.md) | The logical operator determining how to combine the source and target criteria: AND or OR | [optional] 
**target_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the target of relations to search for | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


