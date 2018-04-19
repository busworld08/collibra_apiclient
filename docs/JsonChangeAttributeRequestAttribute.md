# JsonChangeAttributeRequestAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the asset this attribute should belong to. Silently ignored if the &lt;code&gt;id&lt;/code&gt; is provided as path parameter of the request | 
**value** | **object** | The value of this attribute. Expected type of the value depends on the type of the attribute. Following list presents type of the value depending on the kind of the attribute &lt;p&gt;&lt;ul&gt; &lt;li&gt; kind: Numeric               -&gt; value type: number or string &lt;li&gt; kind: Script                -&gt; value type: string &lt;li&gt; kind: Single Value List     -&gt; value type: string &lt;li&gt; kind: Date                  -&gt; value type: number or string &lt;li&gt; kind: String                -&gt; value type: string &lt;li&gt; kind: Boolean               -&gt; value type: boolean or string &lt;li&gt; kind: Multi Value List      -&gt; value type: array of strings &lt;/ul&gt;&lt;p&gt; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


