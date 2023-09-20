# FareRuleID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.fare_rule_id import FareRuleID

# TODO update the JSON string below
json = "{}"
# create an instance of FareRuleID from a JSON string
fare_rule_id_instance = FareRuleID.from_json(json)
# print the JSON string representation of the object
print FareRuleID.to_json()

# convert the object into a dict
fare_rule_id_dict = fare_rule_id_instance.to_dict()
# create an instance of FareRuleID from a dict
fare_rule_id_form_dict = fare_rule_id.from_dict(fare_rule_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


