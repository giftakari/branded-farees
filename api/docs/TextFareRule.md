# TextFareRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**language** | **str** | A three letter code for the representation of names of languages defined by ISO639-3 | [optional] 
**name** | **str** | The name of the text fare rule | [optional] 

## Example

```python
from openapi_client.models.text_fare_rule import TextFareRule

# TODO update the JSON string below
json = "{}"
# create an instance of TextFareRule from a JSON string
text_fare_rule_instance = TextFareRule.from_json(json)
# print the JSON string representation of the object
print TextFareRule.to_json()

# convert the object into a dict
text_fare_rule_dict = text_fare_rule_instance.to_dict()
# create an instance of TextFareRule from a dict
text_fare_rule_form_dict = text_fare_rule.from_dict(text_fare_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


