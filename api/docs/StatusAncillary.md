# StatusAncillary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**OfferStatusEnum**](OfferStatusEnum.md) |  | [optional] 
**code** | **str** | Assigned Type: c-1100:StringTiny | [optional] 

## Example

```python
from openapi_client.models.status_ancillary import StatusAncillary

# TODO update the JSON string below
json = "{}"
# create an instance of StatusAncillary from a JSON string
status_ancillary_instance = StatusAncillary.from_json(json)
# print the JSON string representation of the object
print StatusAncillary.to_json()

# convert the object into a dict
status_ancillary_dict = status_ancillary_instance.to_dict()
# create an instance of StatusAncillary from a dict
status_ancillary_form_dict = status_ancillary.from_dict(status_ancillary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


