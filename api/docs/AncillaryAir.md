# AncillaryAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flight_ref** | **List[str]** | The list of travel segments the ancillary applies to | [optional] 

## Example

```python
from openapi_client.models.ancillary_air import AncillaryAir

# TODO update the JSON string below
json = "{}"
# create an instance of AncillaryAir from a JSON string
ancillary_air_instance = AncillaryAir.from_json(json)
# print the JSON string representation of the object
print AncillaryAir.to_json()

# convert the object into a dict
ancillary_air_dict = ancillary_air_instance.to_dict()
# create an instance of AncillaryAir from a dict
ancillary_air_form_dict = ancillary_air.from_dict(ancillary_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


