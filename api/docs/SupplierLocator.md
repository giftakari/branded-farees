# SupplierLocator

The supplier and the supplier's locator code for a product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**supplier_code** | **str** | Supplier Code | [optional] 
**supplier_name** | **str** | Name of the supplier | [optional] 

## Example

```python
from openapi_client.models.supplier_locator import SupplierLocator

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierLocator from a JSON string
supplier_locator_instance = SupplierLocator.from_json(json)
# print the JSON string representation of the object
print SupplierLocator.to_json()

# convert the object into a dict
supplier_locator_dict = supplier_locator_instance.to_dict()
# create an instance of SupplierLocator from a dict
supplier_locator_form_dict = supplier_locator.from_dict(supplier_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


