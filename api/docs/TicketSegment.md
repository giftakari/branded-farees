# TicketSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**sequence** | **int** | The order in which you checked in to your flight | [optional] 
**class_of_service** | **str** | The booking class of service fare bases code assigned to this ticket segment example :F - First Class, J - Business Class, W - Premium Economy, Y - Economy/Coach | [optional] 
**fare_basis_code** | **str** | The Fare Basis is the code that appears on the ticket in the Fare Basis box | [optional] 
**status** | [**TicketStatusEnum**](TicketStatusEnum.md) |  | [optional] 
**carrier** | **str** | The marketing carrier of the flight on this ticket segment. | 
**number** | **str** | The flight number. | 
**departure** | [**Departure**](Departure.md) |  | 
**arrival** | [**Arrival**](Arrival.md) |  | 
**flight_status_code** | **str** | A status code indicates the status of an air segment | 
**valid_date_range** | [**DateRange**](DateRange.md) |  | 
**ticket_baggage** | [**TicketBaggage**](TicketBaggage.md) |  | 
**connection_ind** | **bool** | If true, the ticketSegment is a connecting segment | [optional] 

## Example

```python
from openapi_client.models.ticket_segment import TicketSegment

# TODO update the JSON string below
json = "{}"
# create an instance of TicketSegment from a JSON string
ticket_segment_instance = TicketSegment.from_json(json)
# print the JSON string representation of the object
print TicketSegment.to_json()

# convert the object into a dict
ticket_segment_dict = ticket_segment_instance.to_dict()
# create an instance of TicketSegment from a dict
ticket_segment_form_dict = ticket_segment.from_dict(ticket_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


