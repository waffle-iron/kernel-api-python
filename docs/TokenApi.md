# kernel_api_client.TokenApi

All URIs are relative to *https://api.kernel.telluslabs.com/api/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_post**](TokenApi.md#token_post) | **POST** /token | Auth Token


# **token_post**
> AuthToken token_post()

Auth Token

The Auth Token endpoint returns an API key for read requests

### Example 
```python
from __future__ import print_function
import time
import kernel_api_client
from kernel_api_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
kernel_api_client.configuration.username = 'YOUR_USERNAME'
kernel_api_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = kernel_api_client.TokenApi()

try: 
    # Auth Token
    api_response = api_instance.token_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

