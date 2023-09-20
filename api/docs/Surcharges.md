# Surcharges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**total_surcharges** | **float** | A monetary amount, up to 4 decimal places. Decimal place needs to be included. | [optional] 
**approximate_ind** | **bool** | if true, the surcharge amounts are approximate | [optional] 

## Example

```python
from openapi_client.models.surcharges import Surcharges

# TODO update the JSON string below
json = "{}"
# create an instance of Surcharges from a JSON string
surcharges_instance = Surcharges.from_json(json)
# print the JSON string representation of the object
print Surcharges.to_json()

# convert the object into a dict
surcharges_dict = surcharges_instance.to_dict()
# create an instance of Surcharges from a dict
surcharges_form_dict = surcharges.from_dict(surcharges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


