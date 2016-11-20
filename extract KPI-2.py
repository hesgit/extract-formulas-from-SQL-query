# -*- coding: utf-8 -*-
"""
Created on Thu May 15 10:30:10 2014
program to replace counter_name with counter_ID for Huawei KPI

@author: Hesam.mo
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


file1 = open(r"E:\MTN\Huawei\3G\FACTS sql\huaweikpi_cell_60-1.sql", "r")
#file1 = open(r"E:\MTN\Huawei\LTE\FACTS imepelmentation\Huawei LTE- cellstats_60-1.sql", "r")

file3 = open(r"E:\MTN\Huawei\3G\FACTS sql\huaweikpi_cell_60-tabed.sql", "w")
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
#            temp_line_1 = re.sub( r' (.*.) ,','', line, re.M|re.I)
            
            
#            reline[:(len(line)-len(searchObj.string))]
#            print 
    temp += 1   
#        modfied_line = line.replace(key1,str('ID_'+ temp_dict[key]))
#        line = line.replace(key,str('ID_'+ temp_dict[key])) 
##            print line
#           # print (key,temp_dict[key])
#            modfied_line = line.replace(key,str('ID_'+ temp_dict[key]))
#            line = line.replace(key,str('ID_'+ temp_dict[key])) 
#       
##    for val in temp_dict.itervalues():  
##        print val
#        
#    for key in temp_dict.iterkeys(): 
#        # print line
#        # print key
#        if re.search(key, line):
##            print line
#           # print (key,temp_dict[key])
#            modfied_line = line.replace(key,str('ID_'+ temp_dict[key]))
#            line = line.replace(key,str('ID_'+ temp_dict[key]))
##            print modfied_line
#          #  file3.write(modfied_line)
#            
#          #  line = modfied_line
#                           
#            # temp +=1
#    file3.write(line)   

        
# print temp
#        if line contains val:
#            line.replace(val,temp_dict['val'])
#        
##        if re.search(val.upper(),line) and ((re.search("^R",line) or re.search("^C",line))):
##            print "value found!"
#
#for key in aDict.keys():
#...     print 'A %s is %s.' % (key, aDict[key])

# Close opend file
print temp
print str(dt.datetime.now())
file3.close()
file1.close()