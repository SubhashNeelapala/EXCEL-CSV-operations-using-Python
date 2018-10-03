import csv 

# with open('data.csv','r+') as csv_file:
# 	d=csv.writer(csv_file)
# 	file=d.writerow(['10','Pavan','23','pavan@gmail.com','10000'])
	
with open('data.csv') as csv_file:
	d=csv.reader(csv_file)
	for each in d:
		print each
