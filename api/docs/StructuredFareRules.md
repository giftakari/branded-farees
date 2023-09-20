# StructuredFareRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**passenger_type_codes** | **List[str]** | List of passenger type codes | [optional] 
**penalties** | [**List[Penalties]**](Penalties.md) |  | [optional] 
**minimum_stay** | [**List[MinimumStay]**](MinimumStay.md) |  | [optional] 
**maximum_stay** | [**List[MaximumStay]**](MaximumStay.md) |  | [optional] 
**advance_reservation** | [**List[AdvanceReservation]**](AdvanceReservation.md) |  | [optional] 
**advance_payment** | [**List[AdvancePayment]**](AdvancePayment.md) |  | [optional] 
**stopover** | [**List[Stopover]**](Stopover.md) |  | [optional] 

## Example

```python
from openapi_client.models.structured_fare_rules import StructuredFareRules

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredFareRules from a JSON string
structured_fare_rules_instance = StructuredFareRules.from_json(json)
# print the JSON string representation of the object
print StructuredFareRules.to_json()

# convert the object into a dict
structured_fare_rules_dict = structured_fare_rules_instance.to_dict()
# create an instance of StructuredFareRules from a dict
structured_fare_rules_form_dict = structured_fare_rules.from_dict(structured_fare_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


