# FareRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_number** | **str** | The rule number of fare rule | [optional] 
**tariff_number** | **str** | Fare rule tarrif number | [optional] 
**flight** | [**List[FlightID]**](FlightID.md) |  | 

## Example

```python
from openapi_client.models.fare_rule import FareRule

# TODO update the JSON string below
json = "{}"
# create an instance of FareRule from a JSON string
fare_rule_instance = FareRule.from_json(json)
# print the JSON string representation of the object
print FareRule.to_json()

# convert the object into a dict
fare_rule_dict = fare_rule_instance.to_dict()
# create an instance of FareRule from a dict
fare_rule_form_dict = fare_rule.from_dict(fare_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


