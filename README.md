# OpenDataPipeline
Extract structured datasets for the Stanford Open Data Project

Use Python 3.

```
pip3 install awscli boto3
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
aws configure
# enter access key id and secret access key
```

```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 gspreadsheet.py
# This will query the google sheet API, bring in the file as csv, convert to JSON, and upload to AWS
```

https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types

```
