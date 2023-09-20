# ProductAncillary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancillary** | [**Ancillary**](Ancillary.md) |  | [optional] 
**selected_by_default_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.product_ancillary import ProductAncillary

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAncillary from a JSON string
product_ancillary_instance = ProductAncillary.from_json(json)
# print the JSON string representation of the object
print ProductAncillary.to_json()

# convert the object into a dict
product_ancillary_dict = product_ancillary_instance.to_dict()
# create an instance of ProductAncillary from a dict
product_ancillary_form_dict = product_ancillary.from_dict(product_ancillary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


