# PricingAgency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**product_ref** | **List[str]** |  | [optional] 
**code** | **str** | The Pricing Agency PCC | 
**segment_sequence_list** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.pricing_agency import PricingAgency

# TODO update the JSON string below
json = "{}"
# create an instance of PricingAgency from a JSON string
pricing_agency_instance = PricingAgency.from_json(json)
# print the JSON string representation of the object
print PricingAgency.to_json()

# convert the object into a dict
pricing_agency_dict = pricing_agency_instance.to_dict()
# create an instance of PricingAgency from a dict
pricing_agency_form_dict = pricing_agency.from_dict(pricing_agency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


