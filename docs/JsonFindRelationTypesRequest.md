# JsonFindRelationTypesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**source_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the source type of the relation type to search for | [optional] 
**source_type_name** | **str** | The name of the source type of the relation type to search for | [optional] 
**role** | **str** | The name of the role that the source plays to search for | [optional] 
**target_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the target type of the relation type to search for | [optional] 
**target_type_name** | **str** | The name of the target type of the relation type to search for | [optional] 
**co_role** | **str** | The name of the role that the target plays to search for | [optional] 
**sort_field** | [**JsonSortFieldFindRelationTypesRequest**](JsonSortFieldFindRelationTypesRequest.md) | The field that should be used as reference for sorting | [optional] 
**sort_order** | [**JsonSortOrder**](JsonSortOrder.md) | The order of sorting | [optional] 
**role_co_role_logical_operator** | [**JsonLogicalOperator**](JsonLogicalOperator.md) | The logical operator determining how to combine the role and coRole criteria: AND or OR | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


