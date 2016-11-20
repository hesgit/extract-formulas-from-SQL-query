# -*- coding: utf-8 -*-
"""
Created on Thu May 15 10:30:10 2014
program to remove extra \n and \t from SQL containing Vendor formula file

@author: Hes
-----
file1 = KPIname.txt    file inculde KPIs with counter name
file2 = nametoID.txt    file inculde counter_name to counter_ID translation
file3 = KPIID.txt    file to store results ( KPIs with counter_ID)
-----
                        Pseudocode
open file1
open file3
line = readline (file1)
    for counter_name in counter_name_ID list
        if line contains counter_name
            replace counter_name with counter_ID
"""
#!/usr/bin/python
import datetime as dt
# Open a file

#file1 = open("Huawei 3G name.txt", "r") # folder addressing


file1 = open(r"E:\Huawei\3G\FACTS sql\huaweikpi_cell_60.sql", "r")
#file1 = open(r"E:\Huawei\LTE\FACTS imepelmentation\Huawei LTE- cellstats_60.sql", "r")

file3 = open(r"E:\Huawei\3G\FACTS sql\huaweikpi_cell_60-1.sql", "w")
#file3 = open(r"E:\Huawei\LTE\FACTS imepelmentation\Huawei LTE- cellstats_60-1.sql", "w")
print "Name of the file: ", file1.name
print str(dt.datetime.now())
"""
for line in file1:
    # line = fo.readline()
    print line #"Read Line: %s" % (line)
"""    
import re
key1 = '\t'
key2 = ',\n'
key3 = '\n'
key4 = 'UUUU'
key5 = '    '
temp = ''
for line in file1:
    #print line
    #if re.search(key3, line):
    line = line.replace(key1,'')
#    print line
#    name = raw_input(": ")
    line = line.replace(key2,'UUUU')
#    print line
#    name = raw_input(": ")
    while re.search(key5, line) != None:
        line = line.replace(key5,' ') 
      
    if re.search(key3, line):
        #print line
        line = line.replace(key3,' ')        
        temp+= line 
        #print temp
    else:
        if re.search(key4, line):
            line = line.replace(key4,',\n')        
            temp+= line         
       
#            print 'D: ' , temp
#            name = raw_input(": ")
            #print temp 
            file3.write(temp)
            temp = ''    
        
# Close opend file
print str(dt.datetime.now())
file3.close()
file1.close()

file1 = open(r"E:\MTN\Huawei\3G\FACTS sql\huawei-cellstats_60-1.sql", "r")
#file1 = open(r"E:\MTN\Huawei\LTE\FACTS imepelmentation\Huawei LTE- cellstats_60-1.sql", "r")

file3 = open(r"E:\MTN\Huawei\3G\FACTS sql\huawei-cellstats_60-tabed.sql", "w")
#file3 = open(r"E:\MTN\Huawei\LTE\FACTS imepelmentation\Huawei LTE- cellstats_60-2.sql", "w")
print "Name of the file: ", file1.name
print str(dt.datetime.now())
"""
for line in file1:
    # line = fo.readline()
    print line #"Read Line: %s" % (line)
"""    
import re
key1 = ' ,\n'
key2 = '\n'
temp = 0
for line in file1:
    if re.search(key1, line):# and temp<25 :
        #print 'input:',line
        searchObj = re.search( r' (\w*.) ,', line, re.M|re.I)
        #print 'Pattern:', searchObj.group() # found pattern
        
#        print 'Pattern:', searchObj.group(1)
#        print 'Pattern:', searchObj.group(2)
        #r'(.*) are (.*?) .*'
#        print searchObj.string
        if searchObj != None:
#            print len(line)
#            print len(searchObj.group())
            temp_line = searchObj.group().replace(' ,','') + '\t' + line[:(len(line)-len(searchObj.group()))] + '\n'
            #print 'output:', temp_line
            file3.write(temp_line)

    temp += 1   


# Close opened file
print temp
print str(dt.datetime.now())
file3.close()
file1.close()

