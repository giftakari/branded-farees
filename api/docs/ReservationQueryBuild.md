# ReservationQueryBuild


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**reservation_build** | [**ReservationBuild**](ReservationBuild.md) |  | 

## Example

```python
from openapi_client.models.reservation_query_build import ReservationQueryBuild

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationQueryBuild from a JSON string
reservation_query_build_instance = ReservationQueryBuild.from_json(json)
# print the JSON string representation of the object
print ReservationQueryBuild.to_json()

# convert the object into a dict
reservation_query_build_dict = reservation_query_build_instance.to_dict()
# create an instance of ReservationQueryBuild from a dict
reservation_query_build_form_dict = reservation_query_build.from_dict(reservation_query_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


