# swagger_client.GeographiesApi

All URIs are relative to *https://api.kernel.telluslabs.com/api/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geographies_get**](GeographiesApi.md#geographies_get) | **GET** /geographies | Available geographies
[**geographies_levels_get**](GeographiesApi.md#geographies_levels_get) | **GET** /geographies/levels | Available geography levels


# **geographies_get**
> list[Geography] geographies_get(country_iso, geo_level, metric_code, start_date, end_date=end_date, crop=crop)

Available geographies

The Geographies endpoint returns information about the available geographies for a given country, geography level, metric, & date combination.

### Example
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeographiesApi()
country_iso = 'country_iso_example' # str | 3-letter country code
geo_level = 'geo_level_example' # str | Geographic level of granularity
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes
start_date = '2013-10-20' # date | First date for which metrics are returned
end_date = '2013-10-20' # date | Last date included in the timeseries (optional)
crop = 'crop_example' # str | Filter response by crop (optional)

try:
    # Available geographies
    api_response = api_instance.geographies_get(country_iso, geo_level, metric_code, start_date, end_date=end_date, crop=crop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographiesApi->geographies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso** | **str**| 3-letter country code |
 **geo_level** | **str**| Geographic level of granularity |
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes |
 **start_date** | **date**| First date for which metrics are returned |
 **end_date** | **date**| Last date included in the timeseries | [optional]
 **crop** | **str**| Filter response by crop | [optional]

### Return type

[**list[Geography]**](Geography.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geographies_levels_get**
> list[GeographyLevel] geographies_levels_get(country_iso, metric_code, start_date, end_date=end_date, crop=crop)

Available geography levels

The Geography Levels endpoint returns information about the available geography levels for a given country, metric, & date combination.

### Example
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeographiesApi()
country_iso = 'country_iso_example' # str | 3-letter country code
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes
start_date = '2013-10-20' # date | First date for which metrics are returned
end_date = '2013-10-20' # date | Last date included in the timeseries (optional)
crop = 'crop_example' # str | Filter response by crop (optional)

try:
    # Available geography levels
    api_response = api_instance.geographies_levels_get(country_iso, metric_code, start_date, end_date=end_date, crop=crop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographiesApi->geographies_levels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso** | **str**| 3-letter country code |
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes |
 **start_date** | **date**| First date for which metrics are returned |
 **end_date** | **date**| Last date included in the timeseries | [optional]
 **crop** | **str**| Filter response by crop | [optional]

### Return type

[**list[GeographyLevel]**](GeographyLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
