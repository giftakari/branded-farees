# Commission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**application** | [**CommissionEnum**](CommissionEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.commission import Commission

# TODO update the JSON string below
json = "{}"
# create an instance of Commission from a JSON string
commission_instance = Commission.from_json(json)
# print the JSON string representation of the object
print Commission.to_json()

# convert the object into a dict
commission_dict = commission_instance.to_dict()
# create an instance of Commission from a dict
commission_form_dict = commission.from_dict(commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


