# ProductIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**product_ref** | **str** | Used to reference another instance of this object in the same message | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_identifier import ProductIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ProductIdentifier from a JSON string
product_identifier_instance = ProductIdentifier.from_json(json)
# print the JSON string representation of the object
print ProductIdentifier.to_json()

# convert the object into a dict
product_identifier_dict = product_identifier_instance.to_dict()
# create an instance of ProductIdentifier from a dict
product_identifier_form_dict = product_identifier.from_dict(product_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


