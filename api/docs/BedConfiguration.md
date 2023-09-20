# BedConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The number of bed of this type and size in the room | [optional] 
**bed_type** | **str** | Configuration of bed(s) in room. | [optional] 
**size** | **str** | Size of bed(s) in the room. | [optional] 

## Example

```python
from openapi_client.models.bed_configuration import BedConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of BedConfiguration from a JSON string
bed_configuration_instance = BedConfiguration.from_json(json)
# print the JSON string representation of the object
print BedConfiguration.to_json()

# convert the object into a dict
bed_configuration_dict = bed_configuration_instance.to_dict()
# create an instance of BedConfiguration from a dict
bed_configuration_form_dict = bed_configuration.from_dict(bed_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


