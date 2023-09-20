# Ancillary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**quantity** | **int** | The quantity value | [optional] 
**description** | [**List[AncillaryDescription]**](AncillaryDescription.md) |  | 

## Example

```python
from openapi_client.models.ancillary import Ancillary

# TODO update the JSON string below
json = "{}"
# create an instance of Ancillary from a JSON string
ancillary_instance = Ancillary.from_json(json)
# print the JSON string representation of the object
print Ancillary.to_json()

# convert the object into a dict
ancillary_dict = ancillary_instance.to_dict()
# create an instance of Ancillary from a dict
ancillary_form_dict = ancillary.from_dict(ancillary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


