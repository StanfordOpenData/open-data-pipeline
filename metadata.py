import boto3


# Create an S3 client
s3 = boto3.client('s3')

import csv
import json

filename = 'output.csv'
# Open the CSV
f = open(filename, 'rU' )
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames = ( "name","create_date","source_url","description","tags", "stories"))
# Parse the CSV into JSON
out = json.dumps( [ row for row in reader ] )
print("JSON parsed!")
# Save the JSON
f = open( 'jsonfile.json', 'w')
f.write(out)
print("JSON saved!")
