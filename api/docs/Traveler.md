# Traveler


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** | Date of Birth YYYY-MM-DD | [optional] 
**gender** | [**GenderEnum**](GenderEnum.md) |  | [optional] 
**person_name** | [**PersonName**](PersonName.md) |  | 
**address** | [**List[Address]**](Address.md) |  | [optional] 
**telephone** | [**List[Telephone]**](Telephone.md) |  | [optional] 
**email** | [**List[Email]**](Email.md) |  | [optional] 
**passenger_type_code** | **str** | Passenger type code | [optional] 
**nationality** | **str** | Nationality on country code ISO | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 
**alternate_contact** | [**List[AlternateContact]**](AlternateContact.md) |  | [optional] 
**travel_document** | [**List[TravelDocument]**](TravelDocument.md) |  | [optional] 
**comments** | [**Comments**](Comments.md) |  | [optional] 
**rail_discount_card** | [**List[RailDiscountCard]**](RailDiscountCard.md) |  | [optional] 
**accompanied_by_infant_ind** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.traveler import Traveler

# TODO update the JSON string below
json = "{}"
# create an instance of Traveler from a JSON string
traveler_instance = Traveler.from_json(json)
# print the JSON string representation of the object
print Traveler.to_json()

# convert the object into a dict
traveler_dict = traveler_instance.to_dict()
# create an instance of Traveler from a dict
traveler_form_dict = traveler.from_dict(traveler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


