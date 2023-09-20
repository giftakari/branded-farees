# DocumentTicketRefund


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_number** | **str** | The control number assigned to the TicketRefund | 
**partial_refund_ind** | **bool** | if true, the ticket has been partially refunded | [optional] 
**refund_guaranteed_ind** | **bool** | if true, this refund amount is guaranteed by Travelport JSON API automated refunds | [optional] 
**historic_ind** | **bool** | if true this document refund has been cancelled/voided | [optional] 
**agency_settlement_not_reported_ind** | **bool** | If true, this refund is settled by the agency directly with the traveler. Transaction is not reported to BSP or ARC. Ticket coupon is updated to RFND status | [optional] 
**fare_guarantee_policy** | [**FareGuaranteePolicy**](FareGuaranteePolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_ticket_refund import DocumentTicketRefund

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTicketRefund from a JSON string
document_ticket_refund_instance = DocumentTicketRefund.from_json(json)
# print the JSON string representation of the object
print DocumentTicketRefund.to_json()

# convert the object into a dict
document_ticket_refund_dict = document_ticket_refund_instance.to_dict()
# create an instance of DocumentTicketRefund from a dict
document_ticket_refund_form_dict = document_ticket_refund.from_dict(document_ticket_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


