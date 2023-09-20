# ReservationListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_response** | [**ReservationResponse**](ReservationResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.reservation_list_response_wrapper import ReservationListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationListResponseWrapper from a JSON string
reservation_list_response_wrapper_instance = ReservationListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print ReservationListResponseWrapper.to_json()

# convert the object into a dict
reservation_list_response_wrapper_dict = reservation_list_response_wrapper_instance.to_dict()
# create an instance of ReservationListResponseWrapper from a dict
reservation_list_response_wrapper_form_dict = reservation_list_response_wrapper.from_dict(reservation_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


