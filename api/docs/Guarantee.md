# Guarantee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**code** | **str** | Guarantee code | [optional] 
**guarantee_type** | [**GuaranteeTypeEnum**](GuaranteeTypeEnum.md) |  | [optional] 
**credentials_required_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.guarantee import Guarantee

# TODO update the JSON string below
json = "{}"
# create an instance of Guarantee from a JSON string
guarantee_instance = Guarantee.from_json(json)
# print the JSON string representation of the object
print Guarantee.to_json()

# convert the object into a dict
guarantee_dict = guarantee_instance.to_dict()
# create an instance of Guarantee from a dict
guarantee_form_dict = guarantee.from_dict(guarantee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


