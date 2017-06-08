# swagger_client.MetricsApi

All URIs are relative to *https://kernel.telluslabs.com/api/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_metadata_get**](MetricsApi.md#metrics_metadata_get) | **GET** /metrics/metadata | All available metric names and descriptions
[**metrics_table_get**](MetricsApi.md#metrics_table_get) | **GET** /metrics/table | Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).
[**metrics_timeseries_metric_code_get**](MetricsApi.md#metrics_timeseries_metric_code_get) | **GET** /metrics/timeseries/{metric_code} | Get values for a metric for a specific geography and a specified time period.


# **metrics_metadata_get**
> list[Metric] metrics_metadata_get(country_iso, metric_category=metric_category, metric_code=metric_code)

All available metric names and descriptions

The Metrics metadata endpoint returns all available metrics, descriptions, UOMs, and other supporting information for a given geography level and crop

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetricsApi()
country_iso = 'country_iso_example' # str | 3-letter country code
metric_category = 'metric_category_example' # str | Metric category (optional)
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes (optional)

try: 
    # All available metric names and descriptions
    api_response = api_instance.metrics_metadata_get(country_iso, metric_category=metric_category, metric_code=metric_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso** | **str**| 3-letter country code | 
 **metric_category** | **str**| Metric category | [optional] 
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes | [optional] 

### Return type

[**list[Metric]**](Metric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_table_get**
> Table metrics_table_get(metric_code, crop, country_iso, geo_level, start_date, geo_id=geo_id, end_date=end_date, collapse=collapse)

Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).

This endpoint returns a table of values, where the rows describe metrics for a specific geography on a specific date for a specific crop.  The list of columns to be included should be specified as a comma delimited list of metric identifiers.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetricsApi()
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes
crop = 'crop_example' # str | Filter response by crop
country_iso = 'country_iso_example' # str | 3-letter country code
geo_level = 'geo_level_example' # str | Geographic level of granularity
start_date = '2013-10-20' # date | First date for which metrics are returned
geo_id = ['geo_id_example'] # list[str] | Comma-delimited list of country-specific geography IDs (optional)
end_date = '2013-10-20' # date | Last date included in the timeseries (optional)
collapse = 'collapse_example' # str | Change the sampling frequency by only returning the last observation for the given time period. (weekly, monthly, annual, none) (optional)

try: 
    # Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).
    api_response = api_instance.metrics_table_get(metric_code, crop, country_iso, geo_level, start_date, geo_id=geo_id, end_date=end_date, collapse=collapse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_table_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes | 
 **crop** | **str**| Filter response by crop | 
 **country_iso** | **str**| 3-letter country code | 
 **geo_level** | **str**| Geographic level of granularity | 
 **start_date** | **date**| First date for which metrics are returned | 
 **geo_id** | [**list[str]**](str.md)| Comma-delimited list of country-specific geography IDs | [optional] 
 **end_date** | **date**| Last date included in the timeseries | [optional] 
 **collapse** | **str**| Change the sampling frequency by only returning the last observation for the given time period. (weekly, monthly, annual, none) | [optional] 

### Return type

[**Table**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_timeseries_metric_code_get**
> Timeseries metrics_timeseries_metric_code_get(metric_code, crop, country_iso, geo_level, start_date, end_date, geo_id=geo_id)

Get values for a metric for a specific geography and a specified time period.

This endpoint returns a timeseries of values for a metric describing a specific geography.  You must provide the crop, the country, geographic level, and the id of the geography, as well as a start and end date.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetricsApi()
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes
crop = 'crop_example' # str | Return metrics pertaining to a specific crop
country_iso = 'country_iso_example' # str | 3-letter country code
geo_level = 'geo_level_example' # str | Geographic level of granularity
start_date = '2013-10-20' # date | Start date of the timeseries
end_date = '2013-10-20' # date | Last date included in the timeseries
geo_id = ['geo_id_example'] # list[str] | Comma-delimited list of country-specific geography IDs (optional)

try: 
    # Get values for a metric for a specific geography and a specified time period.
    api_response = api_instance.metrics_timeseries_metric_code_get(metric_code, crop, country_iso, geo_level, start_date, end_date, geo_id=geo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_timeseries_metric_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes | 
 **crop** | **str**| Return metrics pertaining to a specific crop | 
 **country_iso** | **str**| 3-letter country code | 
 **geo_level** | **str**| Geographic level of granularity | 
 **start_date** | **date**| Start date of the timeseries | 
 **end_date** | **date**| Last date included in the timeseries | 
 **geo_id** | [**list[str]**](str.md)| Comma-delimited list of country-specific geography IDs | [optional] 

### Return type

[**Timeseries**](Timeseries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

