# PriceBreakdownAncillary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The quantity of ancillary items included in this PriceBreakdown | [optional] 
**description** | [**AncillaryDescription**](AncillaryDescription.md) |  | [optional] 
**product_ref** | **str** | The product ref this PriceBreakdown applies to. If no productRef exists then the PriceBreakdown applies to all Products within the Offer. | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**traveler_identifier_ref** | [**TravelerIdentifierRef**](TravelerIdentifierRef.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_breakdown_ancillary import PriceBreakdownAncillary

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBreakdownAncillary from a JSON string
price_breakdown_ancillary_instance = PriceBreakdownAncillary.from_json(json)
# print the JSON string representation of the object
print PriceBreakdownAncillary.to_json()

# convert the object into a dict
price_breakdown_ancillary_dict = price_breakdown_ancillary_instance.to_dict()
# create an instance of PriceBreakdownAncillary from a dict
price_breakdown_ancillary_form_dict = price_breakdown_ancillary.from_dict(price_breakdown_ancillary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


