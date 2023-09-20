# openapi_client.ReservationReceiptApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_receipts_from_locator**](ReservationReceiptApi.md#build_receipts_from_locator) | **POST** /receipt/reservations/{ReservationResource_Identifier}/receipts/buildfromlocator | ReceiptResource - BuildFromLocator
[**build_receipts_from_payment**](ReservationReceiptApi.md#build_receipts_from_payment) | **POST** /receipt/reservations/{ReservationResource_Identifier}/receipts/buildfrompayment | ReceiptResource - BuildFromPayment
[**cancel_reservation**](ReservationReceiptApi.md#cancel_reservation) | **POST** /receipt/reservations/{ReservationResource_Identifier}/receipts | ReceiptResource - CancelReservation
[**get_receipts**](ReservationReceiptApi.md#get_receipts) | **GET** /receipt/reservations/{ReservationResource_Identifier}/receipts | ReceiptResource - Get


# **build_receipts_from_locator**
> ReceiptListResponseWrapper build_receipts_from_locator(reservation_resource_identifier, view=view, reservation_locator=reservation_locator, issuance=issuance, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

ReceiptResource - BuildFromLocator

Process all unprocessesed offers and create ticket receipts.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.receipt_list_response_wrapper import ReceiptListResponseWrapper
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
    api_instance = openapi_client.ReservationReceiptApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    view = 'view_example' # str | The view. Either detail or summary (optional)
    reservation_locator = 'reservation_locator_example' # str |  (optional)
    issuance = 'issuance_example' # str |  (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # ReceiptResource - BuildFromLocator
        api_response = api_instance.build_receipts_from_locator(reservation_resource_identifier, view=view, reservation_locator=reservation_locator, issuance=issuance, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationReceiptApi->build_receipts_from_locator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationReceiptApi->build_receipts_from_locator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **view** | **str**| The view. Either detail or summary | [optional] 
 **reservation_locator** | **str**|  | [optional] 
 **issuance** | **str**|  | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReceiptListResponseWrapper**](ReceiptListResponseWrapper.md)

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

# **build_receipts_from_payment**
> ReceiptListResponseWrapper build_receipts_from_payment(reservation_resource_identifier, receipt_query_build_from_payment, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

ReceiptResource - BuildFromPayment

Process all un-processesed payments and create a list of payment receipts.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.receipt_list_response_wrapper import ReceiptListResponseWrapper
from openapi_client.models.receipt_query_build_from_payment import ReceiptQueryBuildFromPayment
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
    api_instance = openapi_client.ReservationReceiptApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    receipt_query_build_from_payment = openapi_client.ReceiptQueryBuildFromPayment() # ReceiptQueryBuildFromPayment | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # ReceiptResource - BuildFromPayment
        api_response = api_instance.build_receipts_from_payment(reservation_resource_identifier, receipt_query_build_from_payment, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationReceiptApi->build_receipts_from_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationReceiptApi->build_receipts_from_payment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **receipt_query_build_from_payment** | [**ReceiptQueryBuildFromPayment**](ReceiptQueryBuildFromPayment.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReceiptListResponseWrapper**](ReceiptListResponseWrapper.md)

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

# **cancel_reservation**
> ReceiptListResponseWrapper cancel_reservation(reservation_resource_identifier, offer_identifier=offer_identifier, agency_settlement_not_reported_ind=agency_settlement_not_reported_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

ReceiptResource - CancelReservation

Create a set of offer cancelation receipts for every offer in the reservation.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.receipt_list_response_wrapper import ReceiptListResponseWrapper
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
    api_instance = openapi_client.ReservationReceiptApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    offer_identifier = 'offer_identifier_example' # str |  (optional)
    agency_settlement_not_reported_ind = True # bool | If true, this refund is settled by the agency directly with the traveler. Transaction is not reported to BSP or ARC. Ticket coupon is updated to RFND status (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # ReceiptResource - CancelReservation
        api_response = api_instance.cancel_reservation(reservation_resource_identifier, offer_identifier=offer_identifier, agency_settlement_not_reported_ind=agency_settlement_not_reported_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationReceiptApi->cancel_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationReceiptApi->cancel_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **offer_identifier** | **str**|  | [optional] 
 **agency_settlement_not_reported_ind** | **bool**| If true, this refund is settled by the agency directly with the traveler. Transaction is not reported to BSP or ARC. Ticket coupon is updated to RFND status | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReceiptListResponseWrapper**](ReceiptListResponseWrapper.md)

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

# **get_receipts**
> ReceiptListResponseWrapper get_receipts(reservation_resource_identifier, receipt_type=receipt_type, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

ReceiptResource - Get

Get a list of ticket receipts for a reservation.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.receipt_list_response_wrapper import ReceiptListResponseWrapper
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
    api_instance = openapi_client.ReservationReceiptApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    receipt_type = 'receipt_type_example' # str |  (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # ReceiptResource - Get
        api_response = api_instance.get_receipts(reservation_resource_identifier, receipt_type=receipt_type, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationReceiptApi->get_receipts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationReceiptApi->get_receipts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **receipt_type** | **str**|  | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReceiptListResponseWrapper**](ReceiptListResponseWrapper.md)

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

