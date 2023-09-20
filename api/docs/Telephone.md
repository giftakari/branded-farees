# Telephone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**country_access_code** | **str** | TelephoneCountry AccessCode | [optional] 
**area_city_code** | **str** | Telephone Area CityCode | [optional] 
**phone_number** | **str** | Mobile/Telephone Number | 
**extension** | **str** | Telephone extension number | [optional] 
**id** | **str** | UOptional internally referenced id | [optional] 
**city_code** | **str** | City Code | [optional] 
**role** | [**EnumTelephoneRole**](EnumTelephoneRole.md) |  | [optional] 

## Example

```python
from openapi_client.models.telephone import Telephone

# TODO update the JSON string below
json = "{}"
# create an instance of Telephone from a JSON string
telephone_instance = Telephone.from_json(json)
# print the JSON string representation of the object
print Telephone.to_json()

# convert the object into a dict
telephone_dict = telephone_instance.to_dict()
# create an instance of Telephone from a dict
telephone_form_dict = telephone.from_dict(telephone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


