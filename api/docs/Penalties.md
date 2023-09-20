# Penalties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**change** | [**List[Change]**](Change.md) |  | [optional] 
**cancel** | [**List[Cancel]**](Cancel.md) |  | [optional] 
**waiver** | [**List[WaiverEnum]**](WaiverEnum.md) |  | [optional] 
**penalty_source_code** | [**PenaltySourceCode**](PenaltySourceCode.md) |  | [optional] 
**passenger_type_codes** | **List[str]** | The passenger type codes that this penalty applies to | [optional] 
**involuntary_ind** | **bool** | Penalties apply for involuntary changes initiated by the airline | [optional] 

## Example

```python
from openapi_client.models.penalties import Penalties

# TODO update the JSON string below
json = "{}"
# create an instance of Penalties from a JSON string
penalties_instance = Penalties.from_json(json)
# print the JSON string representation of the object
print Penalties.to_json()

# convert the object into a dict
penalties_dict = penalties_instance.to_dict()
# create an instance of Penalties from a dict
penalties_form_dict = penalties.from_dict(penalties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


