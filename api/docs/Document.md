# Document


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**number** | **str** | The identifying number of the document | [optional] 
**traveler_identifier_ref** | [**TravelerIdentifierRef**](TravelerIdentifierRef.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**waiver_code** | [**WaiverCode**](WaiverCode.md) |  | [optional] 
**commission** | [**Commission**](Commission.md) |  | [optional] 
**cumulative_value** | [**CumulativeValue**](CumulativeValue.md) |  | [optional] 
**issuing_pcc** | **str** | Document issuing pcc | [optional] 
**issuing_iata** | **str** | Document issuing IATA | [optional] 
**issuing_city** | **str** | Document issuing city | [optional] 
**filed_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


