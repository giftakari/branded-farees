# FareRuleText


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_fare_rule** | [**List[TextFareRule]**](TextFareRule.md) |  | 

## Example

```python
from openapi_client.models.fare_rule_text import FareRuleText

# TODO update the JSON string below
json = "{}"
# create an instance of FareRuleText from a JSON string
fare_rule_text_instance = FareRuleText.from_json(json)
# print the JSON string representation of the object
print FareRuleText.to_json()

# convert the object into a dict
fare_rule_text_dict = fare_rule_text_instance.to_dict()
# create an instance of FareRuleText from a dict
fare_rule_text_form_dict = fare_rule_text.from_dict(fare_rule_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


