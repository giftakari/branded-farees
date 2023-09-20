# GSTRegistrationNumber

The GST Registration Number for this Organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**telephone** | **str** | Telephone Number | [optional] 
**address** | **str** | Address of the GST customer | [optional] 
**country** | **str** | Country | 
**company_name** | **str** | Name of the Company | [optional] 
**email** | **str** | E-Mail | [optional] 

## Example

```python
from openapi_client.models.gst_registration_number import GSTRegistrationNumber

# TODO update the JSON string below
json = "{}"
# create an instance of GSTRegistrationNumber from a JSON string
gst_registration_number_instance = GSTRegistrationNumber.from_json(json)
# print the JSON string representation of the object
print GSTRegistrationNumber.to_json()

# convert the object into a dict
gst_registration_number_dict = gst_registration_number_instance.to_dict()
# create an instance of GSTRegistrationNumber from a dict
gst_registration_number_form_dict = gst_registration_number.from_dict(gst_registration_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


