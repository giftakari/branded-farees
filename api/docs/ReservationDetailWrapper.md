# ReservationDetailWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_detail** | [**ReservationDetail**](ReservationDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_detail_wrapper import ReservationDetailWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationDetailWrapper from a JSON string
reservation_detail_wrapper_instance = ReservationDetailWrapper.from_json(json)
# print the JSON string representation of the object
print ReservationDetailWrapper.to_json()

# convert the object into a dict
reservation_detail_wrapper_dict = reservation_detail_wrapper_instance.to_dict()
# create an instance of ReservationDetailWrapper from a dict
reservation_detail_wrapper_form_dict = reservation_detail_wrapper.from_dict(reservation_detail_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


