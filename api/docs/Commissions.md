# Commissions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**traveler_identifier_ref** | [**List[TravelerIdentifierRef]**](TravelerIdentifierRef.md) |  | [optional] 
**commission** | [**Commission**](Commission.md) |  | 
**apply_to** | [**CommissionApplyEnum**](CommissionApplyEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.commissions import Commissions

# TODO update the JSON string below
json = "{}"
# create an instance of Commissions from a JSON string
commissions_instance = Commissions.from_json(json)
# print the JSON string representation of the object
print Commissions.to_json()

# convert the object into a dict
commissions_dict = commissions_instance.to_dict()
# create an instance of Commissions from a dict
commissions_form_dict = commissions.from_dict(commissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


