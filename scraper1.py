#Upload data to s3 for download from the ODP
##Data Types: Single-table Pdf, Multi-table Pdf, CSV, HTML
#This file is for single-table pdf's

import boto3


# Create an S3 client
s3 = boto3.client('s3')

from tabula import read_pdf

endowment = ['endowment.csv','https://irds.stanford.edu/sites/g/files/sbiybj10071/f/5.2_endowment.pdf']
fac_adm = ['facilities_administration.csv', 'https://irds.stanford.edu/sites/default/files/5.6_facilities-administrative_cost_rates.pdf']
pop17 = ['population_report_FY17.csv', 'https://irds.stanford.edu/sites/g/files/sbiybj10071/f/population_report_fy17.pdf']
pdfs = [endowment, fac_adm, pop17]

for data in pdfs:
	name = data[0]; url = data[1];
	df = read_pdf(url)
	df.to_csv(name)
	s3.upload_file(name, 'open-data-portal', name, ExtraArgs={'ContentType': "text/csv", 'ACL':'public-read'})
