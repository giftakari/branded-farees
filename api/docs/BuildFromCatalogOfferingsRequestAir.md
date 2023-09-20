# BuildFromCatalogOfferingsRequestAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_modifiers_air** | [**PricingModifiersAir**](PricingModifiersAir.md) |  | [optional] 
**segment_sequence** | **List[int]** | The segmentSequence within the product the action is being requested for. Used when multiple flights exist within a product. Only one product may be selected with this option. | [optional] 

## Example

```python
from openapi_client.models.build_from_catalog_offerings_request_air import BuildFromCatalogOfferingsRequestAir

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromCatalogOfferingsRequestAir from a JSON string
build_from_catalog_offerings_request_air_instance = BuildFromCatalogOfferingsRequestAir.from_json(json)
# print the JSON string representation of the object
print BuildFromCatalogOfferingsRequestAir.to_json()

# convert the object into a dict
build_from_catalog_offerings_request_air_dict = build_from_catalog_offerings_request_air_instance.to_dict()
# create an instance of BuildFromCatalogOfferingsRequestAir from a dict
build_from_catalog_offerings_request_air_form_dict = build_from_catalog_offerings_request_air.from_dict(build_from_catalog_offerings_request_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


