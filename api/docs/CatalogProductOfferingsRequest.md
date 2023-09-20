# CatalogProductOfferingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**search_control_console_channel_id** | [**SearchControlConsoleChannelID**](SearchControlConsoleChannelID.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_product_offerings_request import CatalogProductOfferingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProductOfferingsRequest from a JSON string
catalog_product_offerings_request_instance = CatalogProductOfferingsRequest.from_json(json)
# print the JSON string representation of the object
print CatalogProductOfferingsRequest.to_json()

# convert the object into a dict
catalog_product_offerings_request_dict = catalog_product_offerings_request_instance.to_dict()
# create an instance of CatalogProductOfferingsRequest from a dict
catalog_product_offerings_request_form_dict = catalog_product_offerings_request.from_dict(catalog_product_offerings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


