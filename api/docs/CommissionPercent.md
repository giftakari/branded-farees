# CommissionPercent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **float** | Percent amount of commission | [optional] 

## Example

```python
from openapi_client.models.commission_percent import CommissionPercent

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionPercent from a JSON string
commission_percent_instance = CommissionPercent.from_json(json)
# print the JSON string representation of the object
print CommissionPercent.to_json()

# convert the object into a dict
commission_percent_dict = commission_percent_instance.to_dict()
# create an instance of CommissionPercent from a dict
commission_percent_form_dict = commission_percent.from_dict(commission_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


