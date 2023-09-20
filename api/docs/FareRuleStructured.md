# FareRuleStructured


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structured_fare_rules** | [**List[StructuredFareRules]**](StructuredFareRules.md) |  | 

## Example

```python
from openapi_client.models.fare_rule_structured import FareRuleStructured

# TODO update the JSON string below
json = "{}"
# create an instance of FareRuleStructured from a JSON string
fare_rule_structured_instance = FareRuleStructured.from_json(json)
# print the JSON string representation of the object
print FareRuleStructured.to_json()

# convert the object into a dict
fare_rule_structured_dict = fare_rule_structured_instance.to_dict()
# create an instance of FareRuleStructured from a dict
fare_rule_structured_form_dict = fare_rule_structured.from_dict(fare_rule_structured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


