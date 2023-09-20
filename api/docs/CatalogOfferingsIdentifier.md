# CatalogOfferingsIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_offerings_identifier import CatalogOfferingsIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogOfferingsIdentifier from a JSON string
catalog_offerings_identifier_instance = CatalogOfferingsIdentifier.from_json(json)
# print the JSON string representation of the object
print CatalogOfferingsIdentifier.to_json()

# convert the object into a dict
catalog_offerings_identifier_dict = catalog_offerings_identifier_instance.to_dict()
# create an instance of CatalogOfferingsIdentifier from a dict
catalog_offerings_identifier_form_dict = catalog_offerings_identifier.from_dict(catalog_offerings_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


