# kernel_api_client.UserApi

All URIs are relative to *https://api.kernel.telluslabs.com/api/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get**](UserApi.md#user_get) | **GET** /user | Retrieve User profile information
[**user_put**](UserApi.md#user_put) | **PUT** /user | Update user profile information


# **user_get**
> UserProfile user_get()

Retrieve User profile information

The User endpoint returns profile information such as name, subscription level, and alert preferences for the authorized user.

### Example 
```python
from __future__ import print_function
import time
import kernel_api_client
from kernel_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
kernel_api_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kernel_api_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = kernel_api_client.UserApi()

try: 
    # Retrieve User profile information
    api_response = api_instance.user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_put**
> UserProfile user_put(user_profile)

Update user profile information

Update user profile information and alert preferences

### Example 
```python
from __future__ import print_function
import time
import kernel_api_client
from kernel_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
kernel_api_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kernel_api_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = kernel_api_client.UserApi()
user_profile = kernel_api_client.ExtendedUserProfile() # ExtendedUserProfile | The alert preferences you want to update

try: 
    # Update user profile information
    api_response = api_instance.user_put(user_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**ExtendedUserProfile**](ExtendedUserProfile.md)| The alert preferences you want to update | 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

