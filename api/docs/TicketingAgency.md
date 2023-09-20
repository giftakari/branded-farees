# TicketingAgency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**code** | **str** | The code of the ticketing agency | 
**product_ref** | **List[str]** | The Product Ref the TicketingAgency applies to | [optional] 
**segment_sequence_list** | **List[int]** | The segmentSequenceList the TicketingAgency applies to | [optional] 

## Example

```python
from openapi_client.models.ticketing_agency import TicketingAgency

# TODO update the JSON string below
json = "{}"
# create an instance of TicketingAgency from a JSON string
ticketing_agency_instance = TicketingAgency.from_json(json)
# print the JSON string representation of the object
print TicketingAgency.to_json()

# convert the object into a dict
ticketing_agency_dict = ticketing_agency_instance.to_dict()
# create an instance of TicketingAgency from a dict
ticketing_agency_form_dict = ticketing_agency.from_dict(ticketing_agency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


