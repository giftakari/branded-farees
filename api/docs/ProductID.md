# ProductID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**product_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_id import ProductID

# TODO update the JSON string below
json = "{}"
# create an instance of ProductID from a JSON string
product_id_instance = ProductID.from_json(json)
# print the JSON string representation of the object
print ProductID.to_json()

# convert the object into a dict
product_id_dict = product_id_instance.to_dict()
# create an instance of ProductID from a dict
product_id_form_dict = product_id.from_dict(product_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


