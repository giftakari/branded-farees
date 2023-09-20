# PriceBreakdownHospitality


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_pricing_type** | [**PricingEnum**](PricingEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**nightly_rate** | [**List[NightlyRate]**](NightlyRate.md) |  | [optional] 
**average_nightly_rate** | [**List[CurrencyAmount]**](CurrencyAmount.md) |  | [optional] 
**amenity_surcharges** | [**AmenitySurchargesDetail**](AmenitySurchargesDetail.md) |  | [optional] 
**price_changes_during_stay_ind** | **bool** | If present and true, indicates the nightly price changes one or more times during the stay | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_hospitality import PriceBreakdownHospitality

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownHospitality from a JSON string
price_breakdown_hospitality_instance = PriceBreakdownHospitality.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownHospitality.to_json()

# convert the object into a dict
price_breakdown_hospitality_dict = price_breakdown_hospitality_instance.to_dict()
# create an instance of PriceBreakdownHospitality from a dict
price_breakdown_hospitality_form_dict = price_breakdown_hospitality.from_dict(price_breakdown_hospitality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


