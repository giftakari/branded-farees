# openapi_client.WorkbenchManageOffersApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_from_offer**](WorkbenchManageOffersApi.md#build_from_offer) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildfromoffer | Reprice and existing offer in the workbench
[**build_from_offer_list**](WorkbenchManageOffersApi.md#build_from_offer_list) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildfromofferlist | Add an offer with reference to a Price response
[**build_from_shopping_cart_products**](WorkbenchManageOffersApi.md#build_from_shopping_cart_products) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildfromshoppingcartproducts | Create offer from unpriced products in the shopping cart
[**cancel_workbench_offer**](WorkbenchManageOffersApi.md#cancel_workbench_offer) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/canceloffer | Create a cancel offer quote
[**cancel_workbench_offers**](WorkbenchManageOffersApi.md#cancel_workbench_offers) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/canceloffers | Cancel one or more offers within the workbench without refund quote
[**create_manual_offer**](WorkbenchManageOffersApi.md#create_manual_offer) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers | Create refund or passive offer
[**workbench_build_ancillary_offers_from_catalog_offerings**](WorkbenchManageOffersApi.md#workbench_build_ancillary_offers_from_catalog_offerings) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildancillaryoffersfromcatalogofferings | Add ancillary offer (ancillary book)
[**workbench_build_from_catalog_offerings**](WorkbenchManageOffersApi.md#workbench_build_from_catalog_offerings) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildfromcatalogofferings | Add offer to booking - reference payload.
[**workbench_build_from_catalog_product_offerings**](WorkbenchManageOffersApi.md#workbench_build_from_catalog_product_offerings) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildfromcatalogproductofferings | Add offer to booking - reference payload.
[**workbench_build_from_products**](WorkbenchManageOffersApi.md#workbench_build_from_products) | **POST** /book/airoffer/reservationworkbench/{ReservationResource_Identifier}/offers/buildfromproducts | Add offer to booking - full payload


# **build_from_offer**
> OfferResponseWrapper build_from_offer(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_offer=offer_query_build_from_offer)

Reprice and existing offer in the workbench

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_query_build_from_offer import OfferQueryBuildFromOffer
from openapi_client.models.offer_response_wrapper import OfferResponseWrapper
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_build_from_offer = openapi_client.OfferQueryBuildFromOffer() # OfferQueryBuildFromOffer |  (optional)

    try:
        # Reprice and existing offer in the workbench
        api_response = api_instance.build_from_offer(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_offer=offer_query_build_from_offer)
        print("The response of WorkbenchManageOffersApi->build_from_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->build_from_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_build_from_offer** | [**OfferQueryBuildFromOffer**](OfferQueryBuildFromOffer.md)|  | [optional] 

### Return type

[**OfferResponseWrapper**](OfferResponseWrapper.md)

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

# **build_from_offer_list**
> OfferListResponseWrapper build_from_offer_list(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_buildfrom_offer_list=offer_query_buildfrom_offer_list)

Add an offer with reference to a Price response

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_buildfrom_offer_list import OfferQueryBuildfromOfferList
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_buildfrom_offer_list = openapi_client.OfferQueryBuildfromOfferList() # OfferQueryBuildfromOfferList |  (optional)

    try:
        # Add an offer with reference to a Price response
        api_response = api_instance.build_from_offer_list(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_buildfrom_offer_list=offer_query_buildfrom_offer_list)
        print("The response of WorkbenchManageOffersApi->build_from_offer_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->build_from_offer_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_buildfrom_offer_list** | [**OfferQueryBuildfromOfferList**](OfferQueryBuildfromOfferList.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **build_from_shopping_cart_products**
> OfferListResponseWrapper build_from_shopping_cart_products(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_shopping_cart_products=offer_query_build_from_shopping_cart_products)

Create offer from unpriced products in the shopping cart

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_shopping_cart_products import OfferQueryBuildFromShoppingCartProducts
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_build_from_shopping_cart_products = openapi_client.OfferQueryBuildFromShoppingCartProducts() # OfferQueryBuildFromShoppingCartProducts |  (optional)

    try:
        # Create offer from unpriced products in the shopping cart
        api_response = api_instance.build_from_shopping_cart_products(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_shopping_cart_products=offer_query_build_from_shopping_cart_products)
        print("The response of WorkbenchManageOffersApi->build_from_shopping_cart_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->build_from_shopping_cart_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_build_from_shopping_cart_products** | [**OfferQueryBuildFromShoppingCartProducts**](OfferQueryBuildFromShoppingCartProducts.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **cancel_workbench_offer**
> OfferListResponseWrapper cancel_workbench_offer(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_cancel_offer=offer_query_cancel_offer)

Create a cancel offer quote

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_cancel_offer import OfferQueryCancelOffer
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_cancel_offer = openapi_client.OfferQueryCancelOffer() # OfferQueryCancelOffer |  (optional)

    try:
        # Create a cancel offer quote
        api_response = api_instance.cancel_workbench_offer(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_cancel_offer=offer_query_cancel_offer)
        print("The response of WorkbenchManageOffersApi->cancel_workbench_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->cancel_workbench_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_cancel_offer** | [**OfferQueryCancelOffer**](OfferQueryCancelOffer.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **cancel_workbench_offers**
> OfferListResponseWrapper cancel_workbench_offers(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_cancel_offers=offer_query_cancel_offers)

Cancel one or more offers within the workbench without refund quote

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_cancel_offers import OfferQueryCancelOffers
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_cancel_offers = openapi_client.OfferQueryCancelOffers() # OfferQueryCancelOffers |  (optional)

    try:
        # Cancel one or more offers within the workbench without refund quote
        api_response = api_instance.cancel_workbench_offers(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_cancel_offers=offer_query_cancel_offers)
        print("The response of WorkbenchManageOffersApi->cancel_workbench_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->cancel_workbench_offers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_cancel_offers** | [**OfferQueryCancelOffers**](OfferQueryCancelOffers.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **create_manual_offer**
> OfferListResponseWrapper create_manual_offer(reservation_resource_identifier, offer_type_enum=offer_type_enum, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer=offer)

Create refund or passive offer

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer import Offer
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_type_enum import OfferTypeENUM
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    offer_type_enum = openapi_client.OfferTypeENUM() # OfferTypeENUM | Specifies the type of Offer that is being created (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer = openapi_client.Offer() # Offer |  (optional)

    try:
        # Create refund or passive offer
        api_response = api_instance.create_manual_offer(reservation_resource_identifier, offer_type_enum=offer_type_enum, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer=offer)
        print("The response of WorkbenchManageOffersApi->create_manual_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->create_manual_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **offer_type_enum** | [**OfferTypeENUM**](.md)| Specifies the type of Offer that is being created | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer** | [**Offer**](Offer.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **workbench_build_ancillary_offers_from_catalog_offerings**
> OfferListResponseWrapper workbench_build_ancillary_offers_from_catalog_offerings(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_ancillary_offers_from_catalog_offerings=offer_query_build_ancillary_offers_from_catalog_offerings)

Add ancillary offer (ancillary book)

The Ancillary Book request adds a selected ancillary or a paid seat to the new or post-commit workbench. For ancillaries, first send an Ancillary Shop request and an Ancillary Price request (NDC only). After adding an ancillary to the workbench, you must also issue an EMD for the selected ancillary per the Ancillary and EMD Guide. For paid seats, you must first create a workbench and send a Seat Map request.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_ancillary_offers_from_catalog_offerings import OfferQueryBuildAncillaryOffersFromCatalogOfferings
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_build_ancillary_offers_from_catalog_offerings = openapi_client.OfferQueryBuildAncillaryOffersFromCatalogOfferings() # OfferQueryBuildAncillaryOffersFromCatalogOfferings |  (optional)

    try:
        # Add ancillary offer (ancillary book)
        api_response = api_instance.workbench_build_ancillary_offers_from_catalog_offerings(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_ancillary_offers_from_catalog_offerings=offer_query_build_ancillary_offers_from_catalog_offerings)
        print("The response of WorkbenchManageOffersApi->workbench_build_ancillary_offers_from_catalog_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->workbench_build_ancillary_offers_from_catalog_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_build_ancillary_offers_from_catalog_offerings** | [**OfferQueryBuildAncillaryOffersFromCatalogOfferings**](OfferQueryBuildAncillaryOffersFromCatalogOfferings.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **workbench_build_from_catalog_offerings**
> OfferListResponseWrapper workbench_build_from_catalog_offerings(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_catalog_offerings=offer_query_build_from_catalog_offerings)

Add offer to booking - reference payload.

Use the Add Offer reference payload request to add an offer to the reservation workbench as part of the booking workflow. The reference payload request sends identifiers from the Search response instead of full itinerary details. NDC supports only the reference payload. For GDS, you can send either a reference payload or a full payload.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_catalog_offerings import OfferQueryBuildFromCatalogOfferings
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_build_from_catalog_offerings = openapi_client.OfferQueryBuildFromCatalogOfferings() # OfferQueryBuildFromCatalogOfferings |  (optional)

    try:
        # Add offer to booking - reference payload.
        api_response = api_instance.workbench_build_from_catalog_offerings(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_catalog_offerings=offer_query_build_from_catalog_offerings)
        print("The response of WorkbenchManageOffersApi->workbench_build_from_catalog_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->workbench_build_from_catalog_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_build_from_catalog_offerings** | [**OfferQueryBuildFromCatalogOfferings**](OfferQueryBuildFromCatalogOfferings.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **workbench_build_from_catalog_product_offerings**
> OfferListResponseWrapper workbench_build_from_catalog_product_offerings(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_catalog_product_offerings=offer_query_build_from_catalog_product_offerings)

Add offer to booking - reference payload.

Use the Add Offer reference payload request to add an offer to the reservation workbench as part of the booking workflow. The reference payload request sends identifiers from the Search response instead of full itinerary details. NDC supports only the reference payload. For GDS, you can send either a reference payload or a full payload.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_catalog_product_offerings import OfferQueryBuildFromCatalogProductOfferings
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_build_from_catalog_product_offerings = openapi_client.OfferQueryBuildFromCatalogProductOfferings() # OfferQueryBuildFromCatalogProductOfferings |  (optional)

    try:
        # Add offer to booking - reference payload.
        api_response = api_instance.workbench_build_from_catalog_product_offerings(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_catalog_product_offerings=offer_query_build_from_catalog_product_offerings)
        print("The response of WorkbenchManageOffersApi->workbench_build_from_catalog_product_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->workbench_build_from_catalog_product_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_build_from_catalog_product_offerings** | [**OfferQueryBuildFromCatalogProductOfferings**](OfferQueryBuildFromCatalogProductOfferings.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **workbench_build_from_products**
> OfferListResponseWrapper workbench_build_from_products(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_products=offer_query_build_from_products)

Add offer to booking - full payload

Use the Add Offer full payload request to add an offer to the reservation workbench as part of the booking workflow. The full payload request sends full itinerary details instead of identifiers from the Search response as in the reference payload request. Full payload is not supported for NDC; use the reference payload instead. For GDS, you can send either a reference payload or a full payload.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_products import OfferQueryBuildFromProducts
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
    api_instance = openapi_client.WorkbenchManageOffersApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    offer_query_build_from_products = openapi_client.OfferQueryBuildFromProducts() # OfferQueryBuildFromProducts |  (optional)

    try:
        # Add offer to booking - full payload
        api_response = api_instance.workbench_build_from_products(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, offer_query_build_from_products=offer_query_build_from_products)
        print("The response of WorkbenchManageOffersApi->workbench_build_from_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageOffersApi->workbench_build_from_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **offer_query_build_from_products** | [**OfferQueryBuildFromProducts**](OfferQueryBuildFromProducts.md)|  | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

