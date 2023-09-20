# NetFareBreakdownConstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**fare_type** | **str** | Assigned Type: c-1100:StringTiny | [optional] 
**rate_of_exchange** | **float** | The rate of exchange applied to the fare breakdown | [optional] 

## Example

```python
from openapi_client.models.net_fare_breakdown_construction import NetFareBreakdownConstruction

# TODO update the JSON string below
json = "{}"
# create an instance of NetFareBreakdownConstruction from a JSON string
net_fare_breakdown_construction_instance = NetFareBreakdownConstruction.from_json(json)
# print the JSON string representation of the object
print NetFareBreakdownConstruction.to_json()

# convert the object into a dict
net_fare_breakdown_construction_dict = net_fare_breakdown_construction_instance.to_dict()
# create an instance of NetFareBreakdownConstruction from a dict
net_fare_breakdown_construction_form_dict = net_fare_breakdown_construction.from_dict(net_fare_breakdown_construction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


