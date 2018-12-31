import csv

locations={}
timestamps={}
def extract_csv(filename):
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		next(reader, None)
		counter = 1
		for row in reader:
			#print(row)
			if row[0] not in locations:
				locations[row[0]] = counter
				timestamps[row[0]] = row
				counter += 1
			print(row[0])

	result = []
	#print(timestamps)
	
		

	with open('2018_week39_staff_hourly.tsv', 'w') as tsvfile:
	    writer = csv.writer(tsvfile, delimiter='\t')
	    writer.writerow(['day','hour','value'])
	    for key, value in sorted(locations.items(), key=lambda x:x[1]):
	    	#print(key, value)
	    	counter = 1
	    	while counter < 25:
	    		#print([locations[row[0]], counter, timestamps[key][counter]])
	        	writer.writerow([locations[key], counter, timestamps[key][counter]])
	        	counter+=1
	        
	print(sorted(locations.keys()))
extract_csv('2018_week39_staff_hourly.csv')

