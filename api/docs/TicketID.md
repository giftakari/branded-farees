# TicketID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**obj_id** | **str** |  | [optional] 
**ticket_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_id import TicketID

# TODO update the JSON string below
json = "{}"
# create an instance of TicketID from a JSON string
ticket_id_instance = TicketID.from_json(json)
# print the JSON string representation of the object
print TicketID.to_json()

# convert the object into a dict
ticket_id_dict = ticket_id_instance.to_dict()
# create an instance of TicketID from a dict
ticket_id_form_dict = ticket_id.from_dict(ticket_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


