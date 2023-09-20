# TicketDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sell_amount** | [**AlternateAmount**](AlternateAmount.md) |  | [optional] 
**pricing_pcc** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_detail import TicketDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TicketDetail from a JSON string
ticket_detail_instance = TicketDetail.from_json(json)
# print the JSON string representation of the object
print TicketDetail.to_json()

# convert the object into a dict
ticket_detail_dict = ticket_detail_instance.to_dict()
# create an instance of TicketDetail from a dict
ticket_detail_form_dict = ticket_detail.from_dict(ticket_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


