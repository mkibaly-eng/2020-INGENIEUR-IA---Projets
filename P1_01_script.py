#!/usr/bin/env python
# coding: utf-8

# In[3]:


# This simple app uses the '/detect' resource to identify the language of
# the provided text or texts.

import os, requests, uuid, json

key1_var_name     = 'COGNITIVE_SERVICE_KEY'
key2_var_name     = 'COGNITIVE_SERVICE_REGION'
endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'

if not key1_var_name in os.environ:
    raise Exception('Please set/export the environment variable 1: {}'.format(key1_var_name))
subscription_key = os.environ[key1_var_name]

if not key2_var_name in os.environ:
    raise Exception('Please set/export the environment variable 2: {}'.format(key2_var_name))
region_key = os.environ[key2_var_name]


if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable 3: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]


# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-detect
path = '/detect?api-version=3.0'
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': region_key,    
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# Text to translate or to detect the language.
body = [{
    'text': '未幾離異。四年，撰《金石錄後序》。晚年表上《金石錄》於朝。卒年七十餘。'
      }]


request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))


# In[ ]:





# In[ ]:




