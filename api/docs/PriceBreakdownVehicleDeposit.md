# PriceBreakdownVehicleDeposit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_payable_now_ind** | **bool** | If True the Amount is the total amount payable now | [optional] 
**total_payable_later_ind** | **bool** | If True the Amount is the total amount payable later | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_vehicle_deposit import PriceBreakdownVehicleDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownVehicleDeposit from a JSON string
price_breakdown_vehicle_deposit_instance = PriceBreakdownVehicleDeposit.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownVehicleDeposit.to_json()

# convert the object into a dict
price_breakdown_vehicle_deposit_dict = price_breakdown_vehicle_deposit_instance.to_dict()
# create an instance of PriceBreakdownVehicleDeposit from a dict
price_breakdown_vehicle_deposit_form_dict = price_breakdown_vehicle_deposit.from_dict(price_breakdown_vehicle_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


