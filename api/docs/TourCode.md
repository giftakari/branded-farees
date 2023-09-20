# TourCode

Tour code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**tour_code_type** | [**TourCodeTypeEnum**](TourCodeTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.tour_code import TourCode

# TODO update the JSON string below
json = "{}"
# create an instance of TourCode from a JSON string
tour_code_instance = TourCode.from_json(json)
# print the JSON string representation of the object
print TourCode.to_json()

# convert the object into a dict
tour_code_dict = tour_code_instance.to_dict()
# create an instance of TourCode from a dict
tour_code_form_dict = tour_code.from_dict(tour_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


