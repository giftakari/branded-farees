# DocumentTicketRetained


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_retained_ind** | **bool** | If true the Document Ticket Value has been retained for future use | [optional] 

## Example

```python
from openapi_client.models.document_ticket_retained import DocumentTicketRetained

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTicketRetained from a JSON string
document_ticket_retained_instance = DocumentTicketRetained.from_json(json)
# print the JSON string representation of the object
print DocumentTicketRetained.to_json()

# convert the object into a dict
document_ticket_retained_dict = document_ticket_retained_instance.to_dict()
# create an instance of DocumentTicketRetained from a dict
document_ticket_retained_form_dict = document_ticket_retained.from_dict(document_ticket_retained_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


