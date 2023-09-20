# Brand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Assigned Type: ctbr-1100:BrandName | 
**tier** | **int** | Assigned Type: c-1100:NumberSingleDigit | [optional] 
**shelf_numbers** | **List[int]** | Assigned Type: ctbr-1100:ShelfNumbers | [optional] 
**brand_attribute** | [**List[BrandAttribute]**](BrandAttribute.md) |  | [optional] 
**additional_brand_attribute** | [**List[AdditionalBrandAttribute]**](AdditionalBrandAttribute.md) |  | [optional] 
**image_url** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.brand import Brand

# TODO update the JSON string below
json = "{}"
# create an instance of Brand from a JSON string
brand_instance = Brand.from_json(json)
# print the JSON string representation of the object
print Brand.to_json()

# convert the object into a dict
brand_dict = brand_instance.to_dict()
# create an instance of Brand from a dict
brand_form_dict = brand.from_dict(brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


