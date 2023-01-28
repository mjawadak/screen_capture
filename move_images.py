'''
Code to move images from one folder to another periodically
'''
import os
import time

while(1):
	file_names = os.listdir("/media/jawad-drive/sky_stream02_processed")
	file_names.sort()
	dates = map(lambda x:x[4:4+8], file_names)
	dates = list(set(dates))
	dates.sort()

	base_url = "/media/jawad-drive/sky_stream02_processed_final/"
	from_url = "/media/jawad-drive/sky_stream02_processed/"
	for d in dates:
		date_url = base_url+d
		if os.path.exists(date_url) == False:
			os.mkdir(date_url)

	for f in file_names:
		f_date = f[4:4+8]
		os.replace(from_url+f,base_url+f_date+"/"+f)

	time.sleep(90000)


