# TicketBaggage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**quantity** | **int** | How many baggage allowed | [optional] 
**measurement** | [**List[Measurement]**](Measurement.md) | The total dimensions  of baggage | [optional] 

## Example

```python
from openapi_client.models.ticket_baggage import TicketBaggage

# TODO update the JSON string below
json = "{}"
# create an instance of TicketBaggage from a JSON string
ticket_baggage_instance = TicketBaggage.from_json(json)
# print the JSON string representation of the object
print TicketBaggage.to_json()

# convert the object into a dict
ticket_baggage_dict = ticket_baggage_instance.to_dict()
# create an instance of TicketBaggage from a dict
ticket_baggage_form_dict = ticket_baggage.from_dict(ticket_baggage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


