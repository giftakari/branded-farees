# DestinationPurpose


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**destination** | [**DestinationEnum**](DestinationEnum.md) |  | 
**purpose** | [**PurposeEnum**](PurposeEnum.md) |  | 

## Example

```python
from openapi_client.models.destination_purpose import DestinationPurpose

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationPurpose from a JSON string
destination_purpose_instance = DestinationPurpose.from_json(json)
# print the JSON string representation of the object
print DestinationPurpose.to_json()

# convert the object into a dict
destination_purpose_dict = destination_purpose_instance.to_dict()
# create an instance of DestinationPurpose from a dict
destination_purpose_form_dict = destination_purpose.from_dict(destination_purpose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


