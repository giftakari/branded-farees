# openapi_client.TicketApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ticket**](TicketApi.md#get_ticket) | **GET** /ticket/tickets/{Identifier} | Retrieve a single ticket
[**ticket_get_by_locator**](TicketApi.md#ticket_get_by_locator) | **GET** /ticket/tickets/getbylocator | Retrieve tickets by locator
[**update_ticket**](TicketApi.md#update_ticket) | **PUT** /ticket/tickets/{Identifier} | Void ticket for GDS


# **get_ticket**
> TicketListResponseWrapper get_ticket(identifier, detail_view_ind=detail_view_ind, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Retrieve a single ticket

TicketDisplay returns details for a single ticket.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.ticket_list_response_wrapper import TicketListResponseWrapper
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TicketApi(api_client)
    identifier = '1259900123456' # str | The ticket number
    detail_view_ind = True # bool | If true, TicketDetail will be returned (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Retrieve a single ticket
        api_response = api_instance.get_ticket(identifier, detail_view_ind=detail_view_ind, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of TicketApi->get_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->get_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The ticket number | 
 **detail_view_ind** | **bool**| If true, TicketDetail will be returned | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**TicketListResponseWrapper**](TicketListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_get_by_locator**
> TicketListResponseWrapper ticket_get_by_locator(locator=locator, ticket_number=ticket_number, detail_view_ind=detail_view_ind, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Retrieve tickets by locator

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.ticket_list_response_wrapper import TicketListResponseWrapper
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TicketApi(api_client)
    locator = 'ABC123' # str |  (optional)
    ticket_number = '1231234567890' # str |  (optional)
    detail_view_ind = True # bool | If true, TicketDetail will be returned (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Retrieve tickets by locator
        api_response = api_instance.ticket_get_by_locator(locator=locator, ticket_number=ticket_number, detail_view_ind=detail_view_ind, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of TicketApi->ticket_get_by_locator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_get_by_locator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **ticket_number** | **str**|  | [optional] 
 **detail_view_ind** | **bool**| If true, TicketDetail will be returned | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**TicketListResponseWrapper**](TicketListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket**
> TicketIDResponseWrapper update_ticket(identifier, ticket_query_update_ticket, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Void ticket for GDS

Use the TicketVoid API to void a GDS ticket. Generally a ticket can be voided only within the same day it was issued. See Basic Concepts above for limitations. At this time AirTicketing does not support canceling a GDS itinerary outside the void period.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.ticket_id_response_wrapper import TicketIDResponseWrapper
from openapi_client.models.ticket_query_update_ticket import TicketQueryUpdateTicket
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TicketApi(api_client)
    identifier = '1259900123456' # str | The ticket number
    ticket_query_update_ticket = openapi_client.TicketQueryUpdateTicket() # TicketQueryUpdateTicket | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Void ticket for GDS
        api_response = api_instance.update_ticket(identifier, ticket_query_update_ticket, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of TicketApi->update_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->update_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The ticket number | 
 **ticket_query_update_ticket** | [**TicketQueryUpdateTicket**](TicketQueryUpdateTicket.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**TicketIDResponseWrapper**](TicketIDResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

