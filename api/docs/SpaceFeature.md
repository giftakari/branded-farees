# SpaceFeature

Discriptive information about the seat.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**context** | **str** | The source of the code | [optional] 
**seat_type** | **str** | The type of object that occupies the space | [optional] 
**description** | **str** | The description of the space feature | [optional] 
**power** | **str** | The type of power provided, if any | [optional] 
**video** | **str** | The type of video provided, if any | [optional] 
**rating** | **str** | The seat guru rating of the seat | [optional] 

## Example

```python
from openapi_client.models.space_feature import SpaceFeature

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceFeature from a JSON string
space_feature_instance = SpaceFeature.from_json(json)
# print the JSON string representation of the object
print SpaceFeature.to_json()

# convert the object into a dict
space_feature_dict = space_feature_instance.to_dict()
# create an instance of SpaceFeature from a dict
space_feature_form_dict = space_feature.from_dict(space_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


