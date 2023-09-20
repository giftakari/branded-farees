# Seat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**location** | **str** | The seat location | [optional] 
**seat_type** | **str** | The type of seat | [optional] 
**characteristic** | **List[str]** |  | [optional] 
**seat_feature** | [**SpaceFeature**](SpaceFeature.md) |  | 

## Example

```python
from openapi_client.models.seat import Seat

# TODO update the JSON string below
json = "{}"
# create an instance of Seat from a JSON string
seat_instance = Seat.from_json(json)
# print the JSON string representation of the object
print Seat.to_json()

# convert the object into a dict
seat_dict = seat_instance.to_dict()
# create an instance of Seat from a dict
seat_form_dict = seat.from_dict(seat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


