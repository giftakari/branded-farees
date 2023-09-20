# SpecialService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | [**AppliesTo**](AppliesTo.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**service_animal_type** | **str** | The type of service animal accompanying the Traveler. If no service animal leave blank. | [optional] 
**traveler_identifier** | [**TravelerIdentifier**](TravelerIdentifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.special_service import SpecialService

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialService from a JSON string
special_service_instance = SpecialService.from_json(json)
# print the JSON string representation of the object
print SpecialService.to_json()

# convert the object into a dict
special_service_dict = special_service_instance.to_dict()
# create an instance of SpecialService from a dict
special_service_form_dict = special_service.from_dict(special_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


