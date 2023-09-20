# FareSelection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**fare_type** | [**FaresFilterEnum**](FaresFilterEnum.md) |  | [optional] 
**refund_options** | [**RefundOptions**](RefundOptions.md) |  | [optional] 
**change_options** | [**ChangeOptions**](ChangeOptions.md) |  | [optional] 
**fare_qualifier** | [**FareQualifierENUM**](FareQualifierENUM.md) |  | [optional] 

## Example

```python
from openapi_client.models.fare_selection import FareSelection

# TODO update the JSON string below
json = "{}"
# create an instance of FareSelection from a JSON string
fare_selection_instance = FareSelection.from_json(json)
# print the JSON string representation of the object
print FareSelection.to_json()

# convert the object into a dict
fare_selection_dict = fare_selection_instance.to_dict()
# create an instance of FareSelection from a dict
fare_selection_form_dict = fare_selection.from_dict(fare_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


