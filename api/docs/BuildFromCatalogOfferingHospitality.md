# BuildFromCatalogOfferingHospitality


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**catalog_offering_identifier** | [**Identifier**](Identifier.md) |  | [optional] 
**number_of_rooms** | **int** | Number of rooms required. | [optional] 

## Example

```python
from openapi_client.models.build_from_catalog_offering_hospitality import BuildFromCatalogOfferingHospitality

# TODO update the JSON string below
json = "{}"
# create an instance of BuildFromCatalogOfferingHospitality from a JSON string
build_from_catalog_offering_hospitality_instance = BuildFromCatalogOfferingHospitality.from_json(json)
# print the JSON string representation of the object
print BuildFromCatalogOfferingHospitality.to_json()

# convert the object into a dict
build_from_catalog_offering_hospitality_dict = build_from_catalog_offering_hospitality_instance.to_dict()
# create an instance of BuildFromCatalogOfferingHospitality from a dict
build_from_catalog_offering_hospitality_form_dict = build_from_catalog_offering_hospitality.from_dict(build_from_catalog_offering_hospitality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


