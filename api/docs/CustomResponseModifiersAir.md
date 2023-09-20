# CustomResponseModifiersAir

Modifiers to customize the result set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**brand_attribute_inclusion** | [**List[BrandAttributeInclusion]**](BrandAttributeInclusion.md) |  | [optional] 
**search_representation** | [**SearchRepresentationENUM**](SearchRepresentationENUM.md) |  | [optional] 
**exclude_penalties_ind** | **bool** | If true, Penalties will be excluded from the response | [optional] 
**exclude_baggage_fees_ind** | **bool** | If true, Baggage Fees will be inhibited from the response | [optional] 
**include_fare_calculation_ind** | **bool** | if true, the fare calculation string will be returned in the response | [optional] 
**exclude_surcharges_ind** | **bool** | If true, the surcharge breakdown will be excluded from Price_Detail | [optional] 
**exclude_unbundled_fares_ind** | **bool** | If true, unbundled fares will not be returned in the response | [optional] 

## Example

```python
from openapi_client.models.custom_response_modifiers_air import CustomResponseModifiersAir

# TODO update the JSON string below
json = "{}"
# create an instance of CustomResponseModifiersAir from a JSON string
custom_response_modifiers_air_instance = CustomResponseModifiersAir.from_json(json)
# print the JSON string representation of the object
print CustomResponseModifiersAir.to_json()

# convert the object into a dict
custom_response_modifiers_air_dict = custom_response_modifiers_air_instance.to_dict()
# create an instance of CustomResponseModifiersAir from a dict
custom_response_modifiers_air_form_dict = custom_response_modifiers_air.from_dict(custom_response_modifiers_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


