# Python Client for the Kernel API (version 0.2)
This library is for accessing Kernel insights programmatically in a Python program.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/telluslabs/kernel-api-python.git
```

You may need to run `pip` with root permission:

```sh
sudo pip install git+https://github.com/telluslabs/kernel-api-python.git
```

Then import the package:

```python
import swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.GeographiesApi()
country_iso = 'USA' # str | 3-letter country code
geo_level = 'level_1' # str | Geographic level of granularity
metric_code = ['TLFCYLMOD1'] # list[str] | Comma-delimited list of metric codes
start_date = '2016-01-01' # date | First date for which metrics are returned
end_date = '2016-01-30' # date | Last date included in the timeseries (optional)
crop = 'soy' # str | Filter response by crop (optional)

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
*MetricsApi* | [**metrics_metadata_get**](docs/MetricsApi.md#metrics_metadata_get) | **GET** /metrics/metadata | All available metric names and descriptions
*MetricsApi* | [**metrics_table_get**](docs/MetricsApi.md#metrics_table_get) | **GET** /metrics/table | Get values for a metric (or group of metrics) for a specific geography, crop, and date (or date range).
*MetricsApi* | [**metrics_timeseries_metric_code_get**](docs/MetricsApi.md#metrics_timeseries_metric_code_get) | **GET** /metrics/timeseries/{metric_code} | Get values for a metric for a specific geography and a specified time period.
*UserApi* | [**user_alerts_put**](docs/UserApi.md#user_alerts_put) | **PUT** /user/alerts | Update alert preferences
*UserApi* | [**user_get**](docs/UserApi.md#user_get) | **GET** /user | User Profile


## Documentation For Models

 - [ColumnDescription](docs/ColumnDescription.md)
 - [Crop](docs/Crop.md)
 - [DateRange](docs/DateRange.md)
 - [Error](docs/Error.md)
 - [Geography](docs/Geography.md)
 - [GeographyLevel](docs/GeographyLevel.md)
 - [Metric](docs/Metric.md)
 - [Profile](docs/Profile.md)
 - [Table](docs/Table.md)
 - [TableRow](docs/TableRow.md)
 - [Timeseries](docs/Timeseries.md)
 - [TimeseriesValue](docs/TimeseriesValue.md)
 - [UserAlertPreferences](docs/UserAlertPreferences.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author
