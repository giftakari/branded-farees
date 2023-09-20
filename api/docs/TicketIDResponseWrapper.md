# TicketIDResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id_response** | [**TicketIdResponse**](TicketIdResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_id_response_wrapper import TicketIDResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TicketIDResponseWrapper from a JSON string
ticket_id_response_wrapper_instance = TicketIDResponseWrapper.from_json(json)
# print the JSON string representation of the object
print TicketIDResponseWrapper.to_json()

# convert the object into a dict
ticket_id_response_wrapper_dict = ticket_id_response_wrapper_instance.to_dict()
# create an instance of TicketIDResponseWrapper from a dict
ticket_id_response_wrapper_form_dict = ticket_id_response_wrapper.from_dict(ticket_id_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


