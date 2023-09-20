# CatalogOfferingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**search_control_console_channel_id** | [**SearchControlConsoleChannelID**](SearchControlConsoleChannelID.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_offerings_request import CatalogOfferingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogOfferingsRequest from a JSON string
catalog_offerings_request_instance = CatalogOfferingsRequest.from_json(json)
# print the JSON string representation of the object
print CatalogOfferingsRequest.to_json()

# convert the object into a dict
catalog_offerings_request_dict = catalog_offerings_request_instance.to_dict()
# create an instance of CatalogOfferingsRequest from a dict
catalog_offerings_request_form_dict = catalog_offerings_request.from_dict(catalog_offerings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


