# kernel-api-client
Access Kernel insights programmatically

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kernel_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kernel_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = kernel_api_client.GeographiesApi()
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

## Documentation for API Endpoints

All URIs are relative to *https://api.kernel.telluslabs.com/api/v0.2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GeographiesApi* | [**geographies_get**](docs/GeographiesApi.md#geographies_get) | **GET** /geographies | Available geographies
*GeographiesApi* | [**geographies_levels_get**](docs/GeographiesApi.md#geographies_levels_get) | **GET** /geographies/levels | Available geography levels
*MetricsApi* | [**forecasts_metadata_get**](docs/MetricsApi.md#forecasts_metadata_get) | **GET** /forecasts/metadata | Forecast model metadata
*MetricsApi* | [**metrics_metadata_get**](docs/MetricsApi.md#metrics_metadata_get) | **GET** /metrics/metadata | All available metric names and descriptions
*MetricsApi* | [**metrics_table_get**](docs/MetricsApi.md#metrics_table_get) | **GET** /metrics/table | Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).
*TokenApi* | [**token_post**](docs/TokenApi.md#token_post) | **POST** /token | Auth Token
*UserApi* | [**user_get**](docs/UserApi.md#user_get) | **GET** /user | Retrieve User profile information
*UserApi* | [**user_put**](docs/UserApi.md#user_put) | **PUT** /user | Update user profile information


## Documentation For Models

 - [AuthToken](docs/AuthToken.md)
 - [ColumnDescription](docs/ColumnDescription.md)
 - [ForecastMetadata](docs/ForecastMetadata.md)
 - [GeneralError](docs/GeneralError.md)
 - [Geography](docs/Geography.md)
 - [GeographyLevel](docs/GeographyLevel.md)
 - [Metric](docs/Metric.md)
 - [SubscribedCrop](docs/SubscribedCrop.md)
 - [Table](docs/Table.md)
 - [TableRow](docs/TableRow.md)
 - [UserProfile](docs/UserProfile.md)
 - [ExtendedUserProfile](docs/ExtendedUserProfile.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string

## basic_auth

- **Type**: HTTP basic authentication


## Author



