# PassengerCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**number** | **int** | Number | [optional] 
**age** | **int** | Age | [optional] 
**passenger_type_code** | **str** | Passenger Type Code | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 
**traveler_geographic_location** | [**TravelerGeographicLocation**](TravelerGeographicLocation.md) |  | [optional] 
**specified_passenger_type_code_only_ind** | **bool** | If true then the Offering/Offer will only be returned for the specific passengerTypeCode | [optional] 

## Example

```python
from openapi_client.models.passenger_criteria import PassengerCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of PassengerCriteria from a JSON string
passenger_criteria_instance = PassengerCriteria.from_json(json)
# print the JSON string representation of the object
print PassengerCriteria.to_json()

# convert the object into a dict
passenger_criteria_dict = passenger_criteria_instance.to_dict()
# create an instance of PassengerCriteria from a dict
passenger_criteria_form_dict = passenger_criteria.from_dict(passenger_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


