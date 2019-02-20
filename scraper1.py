#Try out scraping functionality

from tabula import read_pdf

df = read_pdf('https://irds.stanford.edu/sites/g/files/sbiybj10071/f/5.2_endowment.pdf')
print(df)
