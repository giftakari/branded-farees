# OrganizationIdentifier

The organization identifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**supplier** | **str** | Supplier code | [optional] 
**organization_code_type** | [**OrganizationCodeTypeEnum**](OrganizationCodeTypeEnum.md) |  | [optional] 
**segment_sequence_list** | **List[int]** | SegmentSequenceList | [optional] 
**product_ref** | **List[str]** | The productRef which the OrganizationIdentifier applies to | [optional] 
**account_code_fares_only_ind** | **bool** | If true, account code only fares will be returned | [optional] 

## Example

```python
from openapi_client.models.organization_identifier import OrganizationIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationIdentifier from a JSON string
organization_identifier_instance = OrganizationIdentifier.from_json(json)
# print the JSON string representation of the object
print OrganizationIdentifier.to_json()

# convert the object into a dict
organization_identifier_dict = organization_identifier_instance.to_dict()
# create an instance of OrganizationIdentifier from a dict
organization_identifier_form_dict = organization_identifier.from_dict(organization_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


