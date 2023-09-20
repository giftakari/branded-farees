# GeographicRestriction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**geographic_restriction_type** | [**GeographicRestrictionTypeEnum**](GeographicRestrictionTypeEnum.md) |  | 

## Example

```python
from openapi_client.models.geographic_restriction import GeographicRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of GeographicRestriction from a JSON string
geographic_restriction_instance = GeographicRestriction.from_json(json)
# print the JSON string representation of the object
print GeographicRestriction.to_json()

# convert the object into a dict
geographic_restriction_dict = geographic_restriction_instance.to_dict()
# create an instance of GeographicRestriction from a dict
geographic_restriction_form_dict = geographic_restriction.from_dict(geographic_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


