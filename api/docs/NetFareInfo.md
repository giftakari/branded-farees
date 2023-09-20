# NetFareInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passenger_type_code** | **str** | PassengerTypeCode | [optional] 
**net_fare_breakdown_construction** | [**List[NetFareBreakdownConstruction]**](NetFareBreakdownConstruction.md) |  | [optional] 
**ticket_base_audit** | [**FiledAmount**](FiledAmount.md) |  | [optional] 
**ticket_base_passenger** | [**TicketBasePassenger**](TicketBasePassenger.md) |  | [optional] 

## Example

```python
from openapi_client.models.net_fare_info import NetFareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetFareInfo from a JSON string
net_fare_info_instance = NetFareInfo.from_json(json)
# print the JSON string representation of the object
print NetFareInfo.to_json()

# convert the object into a dict
net_fare_info_dict = net_fare_info_instance.to_dict()
# create an instance of NetFareInfo from a dict
net_fare_info_form_dict = net_fare_info.from_dict(net_fare_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


