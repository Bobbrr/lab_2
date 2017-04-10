import os
import glob
import urllib.request
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame



# id =1 
# while id < 28:
#   url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=" + str(id) + "&year1=1981&year2=2017&type=Mean"
#   vhi_url = urllib.request.urlopen(url)
#   x = 'D:/Python/Scripts/srp/1-st lab/vhi_id_' + str(id) + '_' + str(datetime.now().strftime("%Y%m%d-%H%M%S")) + '.csv'
#   out = open(x, 'wb')
#   out.write(vhi_url.read()[:])
#   out.close()

#   df = pd.read_table(x,
#       sep='[ ,]+', engine='python', skipfooter = 1,
#       names = ["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI"], skiprows = [0,1])
#   df1 = DataFrame(df)
#   df1['ind'] = id
#   df1.to_csv(x)
	

#   print ("VHI for id: " + str(id) + " is downloaded...")
#   id += 1




def read_to_frame():
	path = r'D:\Python\Scripts\srp\1-st lab'                     # use your path
	all_files = glob.glob(os.path.join(path, "*.csv"))
	main_frame = DataFrame({'year':[], 'week':[], 'SMN':[], 'SMT':[], 'VCI':[],
		'TCI':[], 'VHI':[], 'ind':[]})
	for f in all_files:
		df = pd.read_table(f, sep='[ ,]+', engine='python', skipfooter = 1,
			names = ["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI","ind"], skiprows = [0,1])
		main_frame = pd.concat([main_frame, df], ignore_index = True)
	print(main_frame)


	print(main_frame.isnull().sum())
	return main_frame

main_frame = read_to_frame()

main_frame['ind'] = main_frame['ind'].map({
	1: 22,
	2: 24,
	3: 23,
	4: 25,
	5: 3,
	6: 4,
	7: 8,
	8: 19,
	9: 20,
	10: 21,
	11: 9,
	12: 26,
	13: 10,
	14: 11,
	15: 12,
	16: 13,
	17: 14,
	18: 15,
	19: 16,
	20: 27,
	21: 17,
	22: 18,
	23: 6,
	24: 1,
	25: 2,
	26: 6,
	27: 5
	})

# print(main_frame) 



def extr(main_frame, year, ind):
	min = main_frame[(main_frame['year'] == year) & (main_frame['ind'] == ind)]['VHI'].min()
	max = main_frame[(main_frame['year'] == year) & (main_frame['ind'] == ind)]['VHI'].max()
	print('Minimum VHI')
	print (main_frame[(main_frame['VHI'] == min) & (main_frame['year'] == year) & (main_frame['ind'] == ind)])
	
	print('Maximum VHI')
	print (main_frame[(main_frame['VHI'] == max) & (main_frame['year'] == year) & (main_frame['ind'] == ind)])
	print ('\n')
	
# # Maximum
# for f in all_files:
# 	df = pd.read_table(f, sep='[ ,]+', engine='python', skipfooter = 1,
# 		names = ["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI","ind"], skiprows = [0,1])
# 	max = df['VHI'].max ()
# 	print(max)
# print('\n')
	
# # Minimum

# for f in all_files:
# 	df = pd.read_table(f, sep='[ ,]+', engine='python', skipfooter = 1,
# 		names = ["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI","ind"], skiprows = [0,1])
# 	min = df['VHI'].min ()
# 	print(min)
# print('\n')


def extreme_drought(main_frame, ind):
    print ('Extreme drought VHI < 15')
    print (main_frame[(main_frame['VHI'] < 15) & (main_frame['ind'] == ind)])
    print ('\n')

def mod_drought(main_frame, ind):
    print ('Av drought 15 <= VHI < 35')
    print (main_frame[(main_frame['VHI'] < 35 ) & (main_frame['VHI'] >= 15 ) & (main_frame['ind'] == ind)])
    print ('\n')



extr(main_frame, 2017, 3)
extreme_drought(main_frame, 3)
mod_drought(main_frame, 3)