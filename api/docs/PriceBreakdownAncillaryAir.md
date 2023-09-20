# PriceBreakdownAncillaryAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passenger_type_code** | **str** | The passenger type code the ancillary is valid for | [optional] 
**approximate_ind** | **bool** | Used to indicate that the Price is approximate. Often used to allow for currency fluctuations when supplier currency is different to agency currency. | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_ancillary_air import PriceBreakdownAncillaryAir

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownAncillaryAir from a JSON string
price_breakdown_ancillary_air_instance = PriceBreakdownAncillaryAir.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownAncillaryAir.to_json()

# convert the object into a dict
price_breakdown_ancillary_air_dict = price_breakdown_ancillary_air_instance.to_dict()
# create an instance of PriceBreakdownAncillaryAir from a dict
price_breakdown_ancillary_air_form_dict = price_breakdown_ancillary_air.from_dict(price_breakdown_ancillary_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


