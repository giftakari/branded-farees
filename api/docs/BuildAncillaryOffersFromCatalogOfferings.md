# BuildAncillaryOffersFromCatalogOfferings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**catalog_offerings_identifier** | [**CatalogOfferingsIdentifier**](CatalogOfferingsIdentifier.md) |  | 
**catalog_offering_identifier** | [**CatalogOfferingIdentifier**](CatalogOfferingIdentifier.md) |  | 
**product_identifier** | [**ProductIdentifier**](ProductIdentifier.md) |  | 
**quantity** | **int** | The quantity of ancillaries to be included in the Offer | [optional] 
**traveler_identifier_ref** | [**TravelerIdentifierRef**](TravelerIdentifierRef.md) |  | [optional] 
**catalog_offerings_ancillary_list_identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**include_unsellable_ancillaries_ind** | **bool** | If true, the response will include unsellable ancillary options | [optional] 

## Example

```python
from openapi_client.models.build_ancillary_offers_from_catalog_offerings import BuildAncillaryOffersFromCatalogOfferings

# TODO update the JSON string below
json = "{}"
# create an instance of BuildAncillaryOffersFromCatalogOfferings from a JSON string
build_ancillary_offers_from_catalog_offerings_instance = BuildAncillaryOffersFromCatalogOfferings.from_json(json)
# print the JSON string representation of the object
print BuildAncillaryOffersFromCatalogOfferings.to_json()

# convert the object into a dict
build_ancillary_offers_from_catalog_offerings_dict = build_ancillary_offers_from_catalog_offerings_instance.to_dict()
# create an instance of BuildAncillaryOffersFromCatalogOfferings from a dict
build_ancillary_offers_from_catalog_offerings_form_dict = build_ancillary_offers_from_catalog_offerings.from_dict(build_ancillary_offers_from_catalog_offerings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


