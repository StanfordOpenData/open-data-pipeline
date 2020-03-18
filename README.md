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

gspreadsheet.py pulls metada from the google sheet as a csv and converts to JSON. To upload to an S3 bucket in AWS requires configuring S3 with boto3.

```
