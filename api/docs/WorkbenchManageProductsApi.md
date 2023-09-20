# openapi_client.WorkbenchManageProductsApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product**](WorkbenchManageProductsApi.md#delete_product) | **DELETE** /book/products/reservationworkbench/{ReservationResource_Identifier}/Products/{id} | Delete unpriced products
[**get_product**](WorkbenchManageProductsApi.md#get_product) | **GET** /book/products/reservationworkbench/{ReservationResource_Identifier}/Products/{id} | Retrieve unpriced products
[**product_build_from_catalog_product_offerings**](WorkbenchManageProductsApi.md#product_build_from_catalog_product_offerings) | **POST** /book/products/reservationworkbench/{ReservationResource_Identifier}/shoppingcart/products/buildfromcatalogproductofferings | Add unpriced products to the workbench by reference to an availability
[**product_build_from_products**](WorkbenchManageProductsApi.md#product_build_from_products) | **POST** /book/products/reservationworkbench/{ReservationResource_Identifier}/shoppingcart/products/buildfromproducts | Add unpriced products to the workbench using full payload


# **delete_product**
> delete_product(reservation_resource_identifier, id, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Delete unpriced products

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.WorkbenchManageProductsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    id = 'id_example' # str | Local indentifier within a given message for this object.
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Delete unpriced products
        api_instance.delete_product(reservation_resource_identifier, id, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
    except Exception as e:
        print("Exception when calling WorkbenchManageProductsApi->delete_product: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **id** | **str**| Local indentifier within a given message for this object. | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

void (empty response body)

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

# **get_product**
> ProductListResponseWrapper get_product(reservation_resource_identifier, id, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Retrieve unpriced products

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.product_list_response_wrapper import ProductListResponseWrapper
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
    api_instance = openapi_client.WorkbenchManageProductsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    id = 'id_example' # str | Local indentifier within a given message for this object.
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Retrieve unpriced products
        api_response = api_instance.get_product(reservation_resource_identifier, id, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of WorkbenchManageProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageProductsApi->get_product: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **id** | **str**| Local indentifier within a given message for this object. | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**ProductListResponseWrapper**](ProductListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_build_from_catalog_product_offerings**
> ProductListResponseWrapper product_build_from_catalog_product_offerings(reservation_resource_identifier, product_query_build_from_catalog_product_offerings, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Add unpriced products to the workbench by reference to an availability

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.product_list_response_wrapper import ProductListResponseWrapper
from openapi_client.models.product_query_build_from_catalog_product_offerings import ProductQueryBuildFromCatalogProductOfferings
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
    api_instance = openapi_client.WorkbenchManageProductsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    product_query_build_from_catalog_product_offerings = openapi_client.ProductQueryBuildFromCatalogProductOfferings() # ProductQueryBuildFromCatalogProductOfferings | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Add unpriced products to the workbench by reference to an availability
        api_response = api_instance.product_build_from_catalog_product_offerings(reservation_resource_identifier, product_query_build_from_catalog_product_offerings, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of WorkbenchManageProductsApi->product_build_from_catalog_product_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageProductsApi->product_build_from_catalog_product_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **product_query_build_from_catalog_product_offerings** | [**ProductQueryBuildFromCatalogProductOfferings**](ProductQueryBuildFromCatalogProductOfferings.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**ProductListResponseWrapper**](ProductListResponseWrapper.md)

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

# **product_build_from_products**
> ProductListResponseWrapper product_build_from_products(reservation_resource_identifier, product_query_build_from_products, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Add unpriced products to the workbench using full payload

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.product_list_response_wrapper import ProductListResponseWrapper
from openapi_client.models.product_query_build_from_products import ProductQueryBuildFromProducts
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
    api_instance = openapi_client.WorkbenchManageProductsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    product_query_build_from_products = openapi_client.ProductQueryBuildFromProducts() # ProductQueryBuildFromProducts | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Add unpriced products to the workbench using full payload
        api_response = api_instance.product_build_from_products(reservation_resource_identifier, product_query_build_from_products, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of WorkbenchManageProductsApi->product_build_from_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageProductsApi->product_build_from_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **product_query_build_from_products** | [**ProductQueryBuildFromProducts**](ProductQueryBuildFromProducts.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**ProductListResponseWrapper**](ProductListResponseWrapper.md)

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

