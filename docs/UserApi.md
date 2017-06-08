# swagger_client.UserApi

All URIs are relative to *https://kernel.telluslabs.com/api/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_alerts_put**](UserApi.md#user_alerts_put) | **PUT** /user/alerts | Update alert preferences
[**user_get**](UserApi.md#user_get) | **GET** /user | User Profile


# **user_alerts_put**
> UserAlertPreferences user_alerts_put(api_key, user_alert_preferences)

Update alert preferences

The alerts endpoint allows the web app to update user alert preference information.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | Authorize request via API key
user_alert_preferences = swagger_client.UserAlertPreferences() # UserAlertPreferences | The alert preferences you want to update

try: 
    # Update alert preferences
    api_response = api_instance.user_alerts_put(api_key, user_alert_preferences)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_alerts_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Authorize request via API key | 
 **user_alert_preferences** | [**UserAlertPreferences**](UserAlertPreferences.md)| The alert preferences you want to update | 

### Return type

[**UserAlertPreferences**](UserAlertPreferences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> Profile user_get(api_key)

User Profile

The User Profile endpoint returns information about the user that has authorized with the application.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | Authorize request via API key

try: 
    # User Profile
    api_response = api_instance.user_get(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Authorize request via API key | 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

