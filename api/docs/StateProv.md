# StateProv

The standard code or abbreviation for the state, province, or region with optional name

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**name** | **str** | State,province or region name or code needed to identify location | [optional] 

## Example

```python
from openapi_client.models.state_prov import StateProv

# TODO update the JSON string below
json = "{}"
# create an instance of StateProv from a JSON string
state_prov_instance = StateProv.from_json(json)
# print the JSON string representation of the object
print StateProv.to_json()

# convert the object into a dict
state_prov_dict = state_prov_instance.to_dict()
# create an instance of StateProv from a dict
state_prov_form_dict = state_prov.from_dict(state_prov_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


