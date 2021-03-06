# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Python package `playwright` is a Python library to automate Chromium,
Firefox and WebKit with a single API. Playwright is built to enable cross-browser
web automation that is ever-green, capable, reliable and fast.
For more information you'll find the documentation for the sync API [here](sync_api.html)
and for the async API [here](async_api.html).
"""

import playwright._api_structures as api_structures
import playwright._api_types as api_types
from playwright._main import AsyncPlaywrightContextManager, SyncPlaywrightContextManager

DeviceDescriptor = api_types.DeviceDescriptor
Error = api_types.Error
FilePayload = api_types.FilePayload
FloatRect = api_types.FloatRect
Geolocation = api_types.Geolocation
HttpCredentials = api_types.HttpCredentials
PdfMargins = api_types.PdfMargins
ProxySettings = api_types.ProxySettings
RecordHarOptions = api_types.RecordHarOptions
RecordVideoOptions = api_types.RecordVideoOptions
RequestFailure = api_types.RequestFailure
OptionSelector = api_types.OptionSelector
SourceLocation = api_types.SourceLocation
TimeoutError = api_types.TimeoutError

Cookie = api_structures.Cookie
ResourceTiming = api_structures.ResourceTiming
StorageState = api_structures.StorageState


def async_playwright() -> AsyncPlaywrightContextManager:
    return AsyncPlaywrightContextManager()


def sync_playwright() -> SyncPlaywrightContextManager:
    return SyncPlaywrightContextManager()


__all__ = [
    "async_playwright",
    "sync_playwright",
    "Cookie",
    "HttpCredentials",
    "DeviceDescriptor",
    "Error",
    "FilePayload",
    "FloatRect",
    "Geolocation",
    "PdfMargins",
    "ProxySettings",
    "RecordHarOptions",
    "RecordVideoOptions",
    "RequestFailure",
    "ResourceTiming",
    "OptionSelector",
    "SourceLocation",
    "StorageState",
    "TimeoutError",
]

__pdoc__ = {
    "_accessibility": False,
    "_async_base": False,
    "_browser": False,
    "_browser_context": False,
    "_browser_type": False,
    "_cdp_session": False,
    "_chromium_browser_context": False,
    "_connection": False,
    "_console_message": False,
    "_dialog": False,
    "_download": False,
    "_element_handle": False,
    "_event_context_manager": False,
    "_file_chooser": False,
    "_frame": False,
    "_helper": False,
    "_impl_to_api_mapping": False,
    "_input": False,
    "_js_handle": False,
    "_main": False,
    "_network": False,
    "_object_factory": False,
    "_page": False,
    "_path_utils": False,
    "_playwright": False,
    "_selectors": False,
    "_sync_base": False,
    "_transport": False,
    "_wait_helper": False,
    "_async_playwright": False,
    "_sync_playwright": False,
}
