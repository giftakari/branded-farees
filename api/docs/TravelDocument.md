# TravelDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**doc_number** | **str** | Document number value | 
**doc_type** | [**DocTypeCodeEnum**](DocTypeCodeEnum.md) |  | [optional] 
**issue_date** | **date** | Date of Issue | [optional] 
**expire_date** | **date** | Date of expiration | [optional] 
**state_prov_code** | **str** | State Province Code value | [optional] 
**place_of_issue** | **str** | Place of issue value | [optional] 
**issue_country** | **str** | Issue country on Country Code ISO | [optional] 
**birth_date** | **date** | The date of birth of the document holder | [optional] 
**birth_country** | **str** | Birth country on Country Code ISO value | [optional] 
**birth_place** | **str** | Birth place value | [optional] 
**residence** | **str** | Residence value | [optional] 
**id** | **str** | Locally referenced id | [optional] 
**gender** | [**GenderEnum**](GenderEnum.md) |  | 
**nationality** | **str** | Specifies a 2 character country code as defined in ISO3166. | [optional] 
**person_name** | [**PersonName**](PersonName.md) |  | 

## Example

```python
from openapi_client.models.travel_document import TravelDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TravelDocument from a JSON string
travel_document_instance = TravelDocument.from_json(json)
# print the JSON string representation of the object
print TravelDocument.to_json()

# convert the object into a dict
travel_document_dict = travel_document_instance.to_dict()
# create an instance of TravelDocument from a dict
travel_document_form_dict = travel_document.from_dict(travel_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


