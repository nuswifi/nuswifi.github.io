import pandas as pd
import csv
import extract_to_tsv

day='2018-09-03.csv'

df = pd.read_csv("2018_week36_student.csv",infer_datetime_format=True, parse_dates=['start_time','end_time'])
locations = ['ARTS-AS1-01', 'ARTS-AS1-02', 'ARTS-AS1-03', 'ARTS-AS1-04', 'ARTS-AS1-05', 'ARTS-AS2-02', 'ARTS-AS2-03', 'ARTS-AS2-04', 'ARTS-AS2-05', 'ARTS-AS2-06', 'ARTS-AS3-01', 'ARTS-AS3-02', 'ARTS-AS3-03', 'ARTS-AS3-04', 'ARTS-AS3-05','ARTS-AS3-06', 'ARTS-AS4-01', 'ARTS-AS4-02', 'ARTS-AS4-03', 'ARTS-AS4-04', 'ARTS-AS4-05', 'ARTS-AS4-06', 'ARTS-AS4-B1', 'ARTS-AS5-02', 'ARTS-AS5-03', 'ARTS-AS5-04', 'ARTS-AS5-05', 'ARTS-AS5-06', 'ARTS-AS6-01', 'ARTS-AS6-02', 'ARTS-AS6-03', 'ARTS-AS7-01', 'ARTS-AS7-02', 'ARTS-AS7-03', 'ARTS-AS7-04', 'ARTS-AS7-05', 'ARTS-AS7-06', 'ARTS-CTN-02', 'ARTS-LT10', 'ARTS-LT11', 'ARTS-LT12', 'ARTS-LT13', 'ARTS-LT14', 'ARTS-LT15', 'ARTS-LT8', 'ARTS-LT9', 'ARTS-Ventus-01','ARTS-Ventus-02', 'ARTS-Ventus-03','ARTS-Ventus-B1', 'CCELIB-CL-01', 'CCELIB-CL-03', 'CCELIB-CL-04', 'CCELIB-CL-05', 'CCELIB-CL-06']
results = {}
for loc in locations:
	#print(row.start_time.hour
	time = {}
	i = 0
	#trajectory =row.origin + '-' + row.destination
	while i < 24:
		time[pd.to_datetime(day[:-4] + " " + str(i) + ":00")] = 0
		i += 1
	results[loc] = time		
	#print(results[item[0]])

for row in df.itertuples():
	try:
		for key in results[row.location].keys():

			if key.hour >= row.start_time.hour and key.hour <= row.end_time.hour:
				#start:2:30, end:4:30
				#print(key, item[1], item[2])
				results[row.location][key] += 1  
				#print(item[1], item[2])
	except KeyError:
		break

with open("2018_week36_student" + "_hourly.csv",'w') as csvfile:
	writer = csv.writer(csvfile)
	#writer.writerow(['journey','count'])
	#writer.writerow(['origin','destination','start_time','end_time', 'start_x','start_y','end_x','end_y'])
	# for location, times in result.items():
	# 	writer.writerow([location] + [times])
	writer.writerow(['journey', '00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'])
	for location, times in results.items():
		writer.writerow([location] + list(times.values()))

print(extract_to_tsv.extract_csv("2018_week36_student_hourly.csv"))

