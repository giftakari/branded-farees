# GeoPoliticalArea

The location code of the geographical location. Codes from Ref Pub

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**level** | [**GeoPoliticalAreaLevelEnum**](GeoPoliticalAreaLevelEnum.md) |  | [optional] 
**id** | **str** | Optional internally referenced id | [optional] 

## Example

```python
from openapi_client.models.geo_political_area import GeoPoliticalArea

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPoliticalArea from a JSON string
geo_political_area_instance = GeoPoliticalArea.from_json(json)
# print the JSON string representation of the object
print GeoPoliticalArea.to_json()

# convert the object into a dict
geo_political_area_dict = geo_political_area_instance.to_dict()
# create an instance of GeoPoliticalArea from a dict
geo_political_area_form_dict = geo_political_area.from_dict(geo_political_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


