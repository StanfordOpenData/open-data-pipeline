#Try out scraping functionality


import boto3


# Create an S3 client
s3 = boto3.client('s3')

from tabula import read_pdf

df = read_pdf('https://irds.stanford.edu/sites/g/files/sbiybj10071/f/5.2_endowment.pdf')
df.to_csv('endowment.csv')
s3.upload_file('endowment.csv', 'open-data-portal', 'endowment.csv', ExtraArgs={'ContentType': "text/csv", 'ACL':'public-read'})
