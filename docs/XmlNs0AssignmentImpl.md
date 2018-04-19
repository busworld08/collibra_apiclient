# XmlNs0AssignmentImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the represented object (entity) | [optional] 
**created_by** | **str** | The id of the user that created this resource | [optional] 
**created_on** | **float** | The timestamp (in UTC time standard) of the creation of this resource | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time | [optional] 
**last_modified_on** | **float** | The timestamp (in UTC time standard) of the last modification of this resource | [optional] 
**resource_type** | [**XmlNs0ResourceType**](XmlNs0ResourceType.md) | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] | [optional] 
**system** | **bool** | Whether this is a system resource or not | [optional] 
**articulation_rules** | **object** | The list of articulation rules applying with the assignment | [optional] 
**asset_type** | **object** | The reference to the asset type the assignment applies to | [optional] 
**characteristic_types** | **object** | The list of assigned characteristic types (attribute types, relation types and complex relation types) | [optional] 
**data_quality_rules** | **object** | The list of references to data quality rules applying with the assignment | [optional] 
**default_status_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the default status | [optional] 
**domain_types** | **object** | The list of references to domain types which the assignment refers to | [optional] 
**scope** | **object** | The scope contained by the assignment | [optional] 
**statuses** | **object** | The list of references to the statuses | [optional] 
**validation_rules** | **object** | The list of references to validation rules applying with the assignment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


