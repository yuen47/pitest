#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anthony
#
# Created:     21/05/2017
# Copyright:   (c) Anthony 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#
#def main():
#    pass
#
#if __name__ == '__main__':
#    main()
#
#
import os
import time
import datetime
import csv

var = 1

while var == 1:
    timeStamp = time.time()
    temperature = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()

    date = datetime.datetime.fromtimestamp(timeStamp).strftime('%d/%m/%y   %H: %M: %S')

#    text_file = open('TempLog.log', 'a')
#    text_file.write(str(temperature) + '      ' + str(date) + '\n' )
#    text_file.close()
#    time.sleep(60)

#    print(str(temperature) + '      ' + str(date) + '\n' )
#    time.sleep(1)

    with open('TempLog.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)
#        filewriter.writerow(['Temperature', 'Time'])
        filewriter.writerow([str(temperature), str(date)])
        time.sleep(300)