# TicketListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_list_response** | [**TicketListResponse**](TicketListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_list_response_wrapper import TicketListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TicketListResponseWrapper from a JSON string
ticket_list_response_wrapper_instance = TicketListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print TicketListResponseWrapper.to_json()

# convert the object into a dict
ticket_list_response_wrapper_dict = ticket_list_response_wrapper_instance.to_dict()
# create an instance of TicketListResponseWrapper from a dict
ticket_list_response_wrapper_form_dict = ticket_list_response_wrapper.from_dict(ticket_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


