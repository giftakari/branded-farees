# openapi_client.ReservationApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_reservation**](ReservationApi.md#build_reservation) | **POST** /book/reservation/reservations/build | Single payload booking request
[**cancel_reservation_offer**](ReservationApi.md#cancel_reservation_offer) | **PUT** /book/reservation/reservations/{reservationIdentifier}/canceloffer | Cancel an Offer within a Reservation
[**commit_reservation**](ReservationApi.md#commit_reservation) | **POST** /book/reservation/reservations/{Identifier} | Commit workbench
[**create_reservation**](ReservationApi.md#create_reservation) | **POST** /book/reservation/reservations | Create a reservation
[**divide**](ReservationApi.md#divide) | **POST** /book/reservation/reservations/divide | Divide a reservation
[**find_reservation**](ReservationApi.md#find_reservation) | **POST** /book/reservation/reservations/find | Find a reservation
[**get_reservation_by_locator**](ReservationApi.md#get_reservation_by_locator) | **GET** /book/reservation/reservations/getbylocator | Retrieve a reservation by locator
[**retrieve_reservation**](ReservationApi.md#retrieve_reservation) | **GET** /book/reservation/reservations/{Identifier} | Retrieve a Reservation
[**update_reservation**](ReservationApi.md#update_reservation) | **PUT** /book/reservation/reservations/{Identifier} | Update a reservation


# **build_reservation**
> ReservationResponseWrapper build_reservation(reservation_query_build_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Single payload booking request

As an alternative to the booking workflow that takes place in a workbench session, you can send all booking details and commit a single payload to create a booking. The single payload book request does not support any of the optional steps in the booking workflow, such as adding seats or ancillaries.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_query_build_wrapper import ReservationQueryBuildWrapper
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_query_build_wrapper = openapi_client.ReservationQueryBuildWrapper() # ReservationQueryBuildWrapper | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Single payload booking request
        api_response = api_instance.build_reservation(reservation_query_build_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->build_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->build_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_query_build_wrapper** | [**ReservationQueryBuildWrapper**](ReservationQueryBuildWrapper.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_reservation_offer**
> ReservationResponseWrapper cancel_reservation_offer(reservation_identifier, supplier_locator=supplier_locator, offer_id=offer_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Cancel an Offer within a Reservation

Cancel an Offer by modifying the Reservation

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_identifier = 'reservation_identifier_example' # str | 
    supplier_locator = 'supplier_locator_example' # str |  (optional)
    offer_id = 'offer_id_example' # str |  (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Cancel an Offer within a Reservation
        api_response = api_instance.cancel_reservation_offer(reservation_identifier, supplier_locator=supplier_locator, offer_id=offer_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->cancel_reservation_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->cancel_reservation_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_identifier** | **str**|  | 
 **supplier_locator** | **str**|  | [optional] 
 **offer_id** | **str**|  | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request - 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | Payment Required - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_reservation**
> ReservationResponseWrapper commit_reservation(identifier, auto_delete_date=auto_delete_date, issuance=issuance, document_value=document_value, pay_later_ind=pay_later_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, reservation_query_commit_reservation=reservation_query_commit_reservation)

Commit workbench

After all required and any optional steps in a booking workbench session, send a POST request with the workbench identifier to commit the workbench. The resulting actions depend on whether payment is present in the workbench. If no Add Payment request has been sent, committing the workbench books the itinerary and generates a PNR. If an Add Payment request has not been sent, committing the workbench tickets the itinerary and generates ticket number/s.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_query_commit_reservation import ReservationQueryCommitReservation
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    identifier = 'identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    auto_delete_date = '2013-10-20' # date | Acts as a retention segment to hold the reservation open past the last date of travel purge date. Sending a new autoDeleteDate at commit step will update the existing autoDeleteDate. Sending 000/00/00 will delete an existing autoDeleteDate. (optional)
    issuance = 'issuance_example' # str | Indicates the type of issuance that should be performed at commit. (Ticket, BackOffice (MIR/TAIR)) (optional)
    document_value = 'document_value_example' # str | Indicates of the value of the document should be refunded or retained following a CancelOffer action (optional)
    pay_later_ind = True # bool | If true, the Reservation will be fulfilled at a later date (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    reservation_query_commit_reservation = openapi_client.ReservationQueryCommitReservation() # ReservationQueryCommitReservation |  (optional)

    try:
        # Commit workbench
        api_response = api_instance.commit_reservation(identifier, auto_delete_date=auto_delete_date, issuance=issuance, document_value=document_value, pay_later_ind=pay_later_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, reservation_query_commit_reservation=reservation_query_commit_reservation)
        print("The response of ReservationApi->commit_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->commit_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **auto_delete_date** | **date**| Acts as a retention segment to hold the reservation open past the last date of travel purge date. Sending a new autoDeleteDate at commit step will update the existing autoDeleteDate. Sending 000/00/00 will delete an existing autoDeleteDate. | [optional] 
 **issuance** | **str**| Indicates the type of issuance that should be performed at commit. (Ticket, BackOffice (MIR/TAIR)) | [optional] 
 **document_value** | **str**| Indicates of the value of the document should be refunded or retained following a CancelOffer action | [optional] 
 **pay_later_ind** | **bool**| If true, the Reservation will be fulfilled at a later date | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **reservation_query_commit_reservation** | [**ReservationQueryCommitReservation**](ReservationQueryCommitReservation.md)|  | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reservation**
> ReservationResponseWrapper create_reservation(reservation_detail_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Create a reservation

Create a reservation on the core or with the vendor/provider.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_detail_wrapper import ReservationDetailWrapper
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_detail_wrapper = openapi_client.ReservationDetailWrapper() # ReservationDetailWrapper | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Create a reservation
        api_response = api_instance.create_reservation(reservation_detail_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->create_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->create_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_detail_wrapper** | [**ReservationDetailWrapper**](ReservationDetailWrapper.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**201** | Created - 201 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **divide**
> ReservationListResponseWrapper divide(reservation_query_divide, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Divide a reservation

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_list_response_wrapper import ReservationListResponseWrapper
from openapi_client.models.reservation_query_divide import ReservationQueryDivide
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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_query_divide = openapi_client.ReservationQueryDivide() # ReservationQueryDivide | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Divide a reservation
        api_response = api_instance.divide(reservation_query_divide, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->divide:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->divide: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_query_divide** | [**ReservationQueryDivide**](ReservationQueryDivide.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationListResponseWrapper**](ReservationListResponseWrapper.md)

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

# **find_reservation**
> ReservationListResponseWrapper find_reservation(reservation_query_search_criteria_reservation, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Find a reservation

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_list_response_wrapper import ReservationListResponseWrapper
from openapi_client.models.reservation_query_search_criteria_reservation import ReservationQuerySearchCriteriaReservation
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
    api_instance = openapi_client.ReservationApi(api_client)
    reservation_query_search_criteria_reservation = openapi_client.ReservationQuerySearchCriteriaReservation() # ReservationQuerySearchCriteriaReservation | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Find a reservation
        api_response = api_instance.find_reservation(reservation_query_search_criteria_reservation, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->find_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->find_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_query_search_criteria_reservation** | [**ReservationQuerySearchCriteriaReservation**](ReservationQuerySearchCriteriaReservation.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationListResponseWrapper**](ReservationListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - 201 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservation_by_locator**
> ReservationResponseWrapper get_reservation_by_locator(locator=locator, creation_date=creation_date, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Retrieve a reservation by locator

To be deprecated and replaced by Get by Identifier using identifier Type \"Locator\"

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    locator = 'locator_example' # str |  (optional)
    creation_date = '2013-10-20' # date | PNR creation Date (optional)
    detail_view_ind = True # bool | If true, ReservationDetail will be returned (optional)
    view_brand_complete_info_ind = True # bool | If true, Brand complete information will be returned in Reservation Response (optional)
    view_baggage_detail_ind = True # bool | if true, full baggage information will be returned in Reservation Response (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Retrieve a reservation by locator
        api_response = api_instance.get_reservation_by_locator(locator=locator, creation_date=creation_date, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->get_reservation_by_locator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->get_reservation_by_locator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **creation_date** | **date**| PNR creation Date | [optional] 
 **detail_view_ind** | **bool**| If true, ReservationDetail will be returned | [optional] 
 **view_brand_complete_info_ind** | **bool**| If true, Brand complete information will be returned in Reservation Response | [optional] 
 **view_baggage_detail_ind** | **bool**| if true, full baggage information will be returned in Reservation Response | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

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

# **retrieve_reservation**
> ReservationResponseWrapper retrieve_reservation(identifier, authority, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, identifier_type=identifier_type, document_type=document_type, view_shopping_cart_products_ind=view_shopping_cart_products_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Retrieve a Reservation

Retrieve details about a held booking, or PNR. While a PNR refers to a held booking that has not been ticketed, the PNR code persists after ticketing to provide the booking records. Once a PNR has been ticketed, you can still use PNR Retrieve to return both booking and ticketing details. A Ticket Display request can also be used to retrieve any ticketed itinerary.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.document_type_enum import DocumentTypeEnum
from openapi_client.models.identifier_type_enum import IdentifierTypeENUM
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    identifier = 'identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    authority = 'authority_example' # str | The authorising entity creating the identifier
    detail_view_ind = True # bool | If true, ReservationDetail will be returned. (optional)
    view_brand_complete_info_ind = True # bool | If true, Brand complete information will be returned in Reservation Response (optional)
    view_baggage_detail_ind = True # bool | if true, full baggage information will be returned in Reservation Response (optional)
    identifier_type = openapi_client.IdentifierTypeENUM() # IdentifierTypeENUM | The type of identifier key used to retrieve the reservation (optional)
    document_type = openapi_client.DocumentTypeEnum() # DocumentTypeEnum | When document is selected in IdentifierType, use documentType to identify the type of document (optional)
    view_shopping_cart_products_ind = True # bool | If true, Unfinished Offers will be returned as ShoppingCartProducts (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Retrieve a Reservation
        api_response = api_instance.retrieve_reservation(identifier, authority, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, identifier_type=identifier_type, document_type=document_type, view_shopping_cart_products_ind=view_shopping_cart_products_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->retrieve_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->retrieve_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **authority** | **str**| The authorising entity creating the identifier | 
 **detail_view_ind** | **bool**| If true, ReservationDetail will be returned. | [optional] 
 **view_brand_complete_info_ind** | **bool**| If true, Brand complete information will be returned in Reservation Response | [optional] 
 **view_baggage_detail_ind** | **bool**| if true, full baggage information will be returned in Reservation Response | [optional] 
 **identifier_type** | [**IdentifierTypeENUM**](.md)| The type of identifier key used to retrieve the reservation | [optional] 
 **document_type** | [**DocumentTypeEnum**](.md)| When document is selected in IdentifierType, use documentType to identify the type of document | [optional] 
 **view_shopping_cart_products_ind** | **bool**| If true, Unfinished Offers will be returned as ShoppingCartProducts | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

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

# **update_reservation**
> ReservationResponseWrapper update_reservation(identifier, reservation_detail_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Update a reservation

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_detail_wrapper import ReservationDetailWrapper
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.ReservationApi(api_client)
    identifier = 'identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    reservation_detail_wrapper = openapi_client.ReservationDetailWrapper() # ReservationDetailWrapper | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Update a reservation
        api_response = api_instance.update_reservation(identifier, reservation_detail_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of ReservationApi->update_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationApi->update_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **reservation_detail_wrapper** | [**ReservationDetailWrapper**](ReservationDetailWrapper.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

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

