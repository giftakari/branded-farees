# BrandID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**brand_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.brand_id import BrandID

# TODO update the JSON string below
json = "{}"
# create an instance of BrandID from a JSON string
brand_id_instance = BrandID.from_json(json)
# print the JSON string representation of the object
print BrandID.to_json()

# convert the object into a dict
brand_id_dict = brand_id_instance.to_dict()
# create an instance of BrandID from a dict
brand_id_form_dict = brand_id.from_dict(brand_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


