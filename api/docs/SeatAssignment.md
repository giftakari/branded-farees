# SeatAssignment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**seat** | **str** | Seat | 
**characteristic** | **List[str]** |  | 
**seat_feature** | [**List[SpaceFeature]**](SpaceFeature.md) |  | [optional] 

## Example

```python
from openapi_client.models.seat_assignment import SeatAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of SeatAssignment from a JSON string
seat_assignment_instance = SeatAssignment.from_json(json)
# print the JSON string representation of the object
print SeatAssignment.to_json()

# convert the object into a dict
seat_assignment_dict = seat_assignment_instance.to_dict()
# create an instance of SeatAssignment from a dict
seat_assignment_form_dict = seat_assignment.from_dict(seat_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


