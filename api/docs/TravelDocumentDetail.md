# TravelDocumentDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issued_for_geo_political_area** | [**GeoPoliticalArea**](GeoPoliticalArea.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from openapi_client.models.travel_document_detail import TravelDocumentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TravelDocumentDetail from a JSON string
travel_document_detail_instance = TravelDocumentDetail.from_json(json)
# print the JSON string representation of the object
print TravelDocumentDetail.to_json()

# convert the object into a dict
travel_document_detail_dict = travel_document_detail_instance.to_dict()
# create an instance of TravelDocumentDetail from a dict
travel_document_detail_form_dict = travel_document_detail.from_dict(travel_document_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


