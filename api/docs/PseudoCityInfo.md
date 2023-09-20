# PseudoCityInfo

a pseudo city information contains the details about the corporate user of a computer reservation system (CRS) or global distribution system (GDS), typically a travel agency.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**provider_code** | **str** | Assigned Type: c-1100:SupplierCode | [optional] 

## Example

```python
from openapi_client.models.pseudo_city_info import PseudoCityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PseudoCityInfo from a JSON string
pseudo_city_info_instance = PseudoCityInfo.from_json(json)
# print the JSON string representation of the object
print PseudoCityInfo.to_json()

# convert the object into a dict
pseudo_city_info_dict = pseudo_city_info_instance.to_dict()
# create an instance of PseudoCityInfo from a dict
pseudo_city_info_form_dict = pseudo_city_info.from_dict(pseudo_city_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


