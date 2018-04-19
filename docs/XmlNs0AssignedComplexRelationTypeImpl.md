# XmlNs0AssignedComplexRelationTypeImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the represented object (entity) | [optional] 
**maximum_occurrences** | **float** | How many times at least the assigned characteristic may be added to the resource. Null means no limit | [optional] 
**minimum_occurrences** | **float** | How many times at least the assigned characteristic must be added to the resource. Zero means no restriction | [optional] 
**read_only** | **bool** | Whether the characteristic value of the assigned type can be edited by the user | [optional] 
**system** | **bool** | Whether the characteristic type can be unassigned | [optional] 
**complex_relation_type** | **object** | The complex relation type to be assigned | [optional] 
**matching_leg_types_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s that should match the legs of the complex relation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


