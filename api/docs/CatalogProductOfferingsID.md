# CatalogProductOfferingsID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offerings_id import CatalogProductOfferingsID

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingsID from a JSON string
catalog_product_offerings_id_instance = CatalogProductOfferingsID.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingsID.to_json()

# convert the object into a dict
catalog_product_offerings_id_dict = catalog_product_offerings_id_instance.to_dict()
# create an instance of CatalogProductOfferingsID from a dict
catalog_product_offerings_id_form_dict = catalog_product_offerings_id.from_dict(catalog_product_offerings_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


