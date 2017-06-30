# kernel_api_client.MetricsApi

All URIs are relative to *https://api.kernel.telluslabs.com/api/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecasts_metadata_get**](MetricsApi.md#forecasts_metadata_get) | **GET** /forecasts/metadata | Forecast model metadata
[**metrics_metadata_get**](MetricsApi.md#metrics_metadata_get) | **GET** /metrics/metadata | All available metric names and descriptions
[**metrics_table_get**](MetricsApi.md#metrics_table_get) | **GET** /metrics/table | Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).


# **forecasts_metadata_get**
> ForecastMetadata forecasts_metadata_get(active=active, primary=primary, secondary=secondary, crop=crop, metric_code=metric_code, model_type=model_type)

Forecast model metadata

The Forecasts Metadata endpoint returns supporting contextual information about a given forecast model.

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
api_instance = kernel_api_client.MetricsApi()
active = true # bool | Flag designating whether or not the model is active. (optional) (default to true)
primary = true # bool | Flag designating the primary forecast model (optional)
secondary = true # bool | Flag designating the secondary forecast model (optional)
crop = 'crop_example' # str | Filter models by a particular crop (optional)
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes (optional)
model_type = ['model_type_example'] # list[str] | Comma-delimited list of model types (optional)

try: 
    # Forecast model metadata
    api_response = api_instance.forecasts_metadata_get(active=active, primary=primary, secondary=secondary, crop=crop, metric_code=metric_code, model_type=model_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->forecasts_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Flag designating whether or not the model is active. | [optional] [default to true]
 **primary** | **bool**| Flag designating the primary forecast model | [optional] 
 **secondary** | **bool**| Flag designating the secondary forecast model | [optional] 
 **crop** | **str**| Filter models by a particular crop | [optional] 
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes | [optional] 
 **model_type** | [**list[str]**](str.md)| Comma-delimited list of model types | [optional] 

### Return type

[**ForecastMetadata**](ForecastMetadata.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_metadata_get**
> list[Metric] metrics_metadata_get(dropdown_visible=dropdown_visible, crop=crop, metric_category=metric_category, metric_type=metric_type, metric_source=metric_source, metric_code=metric_code)

All available metric names and descriptions

The Metrics metadata endpoint returns all available metrics, descriptions, UOMs, and other supporting information for a given geography level and crop

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
api_instance = kernel_api_client.MetricsApi()
dropdown_visible = true # bool | Metric used for dropdowns (optional) (default to true)
crop = 'crop_example' # str | Filter response by crop (optional)
metric_category = 'metric_category_example' # str | Metric category (optional)
metric_type = ['metric_type_example'] # list[str] | Comma-delimited list of metric types (optional)
metric_source = ['metric_source_example'] # list[str] | Comma-delimited list of metric sources (optional)
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes (optional)

try: 
    # All available metric names and descriptions
    api_response = api_instance.metrics_metadata_get(dropdown_visible=dropdown_visible, crop=crop, metric_category=metric_category, metric_type=metric_type, metric_source=metric_source, metric_code=metric_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropdown_visible** | **bool**| Metric used for dropdowns | [optional] [default to true]
 **crop** | **str**| Filter response by crop | [optional] 
 **metric_category** | **str**| Metric category | [optional] 
 **metric_type** | [**list[str]**](str.md)| Comma-delimited list of metric types | [optional] 
 **metric_source** | [**list[str]**](str.md)| Comma-delimited list of metric sources | [optional] 
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes | [optional] 

### Return type

[**list[Metric]**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_table_get**
> Table metrics_table_get(metric_code, crop, country_iso, geo_level, start_date, end_date=end_date, geo_id=geo_id)

Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).

This endpoint returns a table of values, where the rows describe metrics for a specific geography on a specific date for a specific crop.  The list of columns to be included should be specified as a comma delimited list of metric identifiers.

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
api_instance = kernel_api_client.MetricsApi()
metric_code = ['metric_code_example'] # list[str] | Comma-delimited list of metric codes
crop = 'crop_example' # str | Filter response by crop
country_iso = ['country_iso_example'] # list[str] | 3-letter country code
geo_level = 'geo_level_example' # str | Geographic level of granularity
start_date = '2013-10-20' # date | First date for which metrics are returned
end_date = '2013-10-20' # date | Last date included in the timeseries (optional)
geo_id = ['geo_id_example'] # list[str] | Comma-delimited list of country-specific geography IDs (optional)

try: 
    # Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).
    api_response = api_instance.metrics_table_get(metric_code, crop, country_iso, geo_level, start_date, end_date=end_date, geo_id=geo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_table_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_code** | [**list[str]**](str.md)| Comma-delimited list of metric codes | 
 **crop** | **str**| Filter response by crop | 
 **country_iso** | [**list[str]**](str.md)| 3-letter country code | 
 **geo_level** | **str**| Geographic level of granularity | 
 **start_date** | **date**| First date for which metrics are returned | 
 **end_date** | **date**| Last date included in the timeseries | [optional] 
 **geo_id** | [**list[str]**](str.md)| Comma-delimited list of country-specific geography IDs | [optional] 

### Return type

[**Table**](Table.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

