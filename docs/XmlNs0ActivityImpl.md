# XmlNs0ActivityImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the represented object (entity) | [optional] 
**activity_type** | [**XmlNs0ActivityType**](XmlNs0ActivityType.md) | The type of the activity, which could be ADD, UPDATE or DELETE | [optional] 
**call_count** | **float** | The number of calls standing behind the activity | [optional] 
**call_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the call that resulted in an activity | [optional] 
**cause** | [**XmlNs0ActivityCause**](XmlNs0ActivityCause.md) | The cause of the activity | [optional] 
**description** | **str** | The description of the activity. It&#39;s the string in json format. It&#39;s exact content depends on activityType and on the type of the resource that was affected by the change. Possible fields are: &lt;ul&gt; &lt;li&gt; affected - always there, consists of id, type and name, it&#39;s the reference to the resource that was added, deleted or updated with the activity. &lt;/li&gt; &lt;li&gt; new, old - for all activities of ActivityType.UPDATE, respectively new and old value of the field. It can be either the reference to another object (same as affected) or just a string (eg. name change). &lt;/li&gt; &lt;li&gt; field - for ActivityType.UPDATE the name of the field that was changed, eg. status, name, target etc. &lt;/li&gt; &lt;li&gt; role, people, resource - only for the responsibility activities, people means owner (user or group). &lt;/li&gt; &lt;li&gt; source, target, role, coRole - only for relations (including complex relation legs). &lt;/li&gt; &lt;li&gt; complexRelation, legs - only for complex relations, legs here stands for all the legs that the complex relation consists of. &lt;/li&gt; &lt;li&gt; kind - only for attributes, it&#39;s attribute kind, eg. boolean, string, numeric etc. &lt;/li&gt; &lt;li&gt; businessItem - only for workflows, reference to an object that is the business item for non-global workflows. &lt;/li&gt; &lt;li&gt; attachmentFile - only for attachments, it&#39;s the name of the file that was attached. &lt;/li&gt; &lt;/ul&gt; | [optional] 
**timestamp** | **float** | The time when the activity happened. It is the timestamp (in UTC time standard) | [optional] 
**user** | **object** | The reference to the user who performed the activity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


