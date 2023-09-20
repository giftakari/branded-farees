# SpecialServiceWheelchairAirlineSupplied


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cannot_ascend_stairs_ind** | **bool** | if true, traveler needs assistance ascending and descending stairs | [optional] 
**traveler_immobile_ind** | **bool** | if true, traveler is completely immobile and requires assistance to/from aircraft/mobile lounge and ascending/descending stairs | [optional] 

## Example

```python
from openapi_client.models.special_service_wheelchair_airline_supplied import SpecialServiceWheelchairAirlineSupplied

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServiceWheelchairAirlineSupplied from a JSON string
special_service_wheelchair_airline_supplied_instance = SpecialServiceWheelchairAirlineSupplied.from_json(json)
# print the JSON string representation of the object
print SpecialServiceWheelchairAirlineSupplied.to_json()

# convert the object into a dict
special_service_wheelchair_airline_supplied_dict = special_service_wheelchair_airline_supplied_instance.to_dict()
# create an instance of SpecialServiceWheelchairAirlineSupplied from a dict
special_service_wheelchair_airline_supplied_form_dict = special_service_wheelchair_airline_supplied.from_dict(special_service_wheelchair_airline_supplied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


