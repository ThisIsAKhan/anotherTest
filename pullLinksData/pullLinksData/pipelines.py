# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import json

import unicodedata
import sys

#handles crazy unicode characters by translating them back into ACII
def unicodeHandle(stuff):
	return unicodedata.normalize('NFKD', stuff).encode('ascii','ignore')


#remove the data from the arrays and store them nicely in formatted strings
def cleanUpBrackets(stuff):
	if isinstance(stuff,str):
		return stuff
	if not stuff:
		return ''
	else:
		string = unicodeHandle(stuff.pop(0))
		for x in stuff:
			if not x == '':
				string = string + ', ' + unicodeHandle(x)
		return string



class LinkedinPipeline(object):
    
    
    
    
    def __init__(self):
    	self.file = open('items.txt','wb')
    
    def process_item(self, item, spider):
        #return item
        
        #line = json.dumps(dict(item)) + "\n"
        
        
        thing = dict(item)
        
        #####################################################################################################
        # Note: I used to use json.dumps... before he wanted me to get rid of the brackets :P. So I cleaned up the brackets.
        # name 				= json.dumps(thing['name'])
        # headlineTitle 	= json.dumps(thing['headlineTitle'])
        # etc
        
        url					= thing['url']
        
        name 				= cleanUpBrackets(thing['name'])
        headlineTitle 		= cleanUpBrackets(thing['headlineTitle'])
        location 			= cleanUpBrackets(thing['location'])
        industry 			= cleanUpBrackets(thing['industry'])        
        connections			= cleanUpBrackets(thing['connections'])
        
        overviewCurrent 	= cleanUpBrackets(thing['overviewCurrent'])        
        overviewEducation 	= cleanUpBrackets(thing['overviewEducation'])
        
        
        
        educationSchool1	= json.dumps(thing['educationSchoolName1']).replace('"','').replace('[','').replace(']','')
        educationDegree1	= json.dumps(thing['educationDegree1']).replace('"','').replace('[','').replace(']','')
        educationMajor1		= json.dumps(thing['educationMajor1']).replace('"','').replace('[','').replace(']','')
        eduTimeStart1		= json.dumps(thing['eduTimeStart1']).replace('"','').replace('[','').replace(']','')
        eduTimeEnd1			= json.dumps(thing['eduTimeEnd1']).replace('"','').replace('[','').replace(']','')
        
        educationSchool2	= json.dumps(thing['educationSchoolName2']).replace('"','').replace('[','').replace(']','')
        educationDegree2	= json.dumps(thing['educationDegree2']).replace('"','').replace('[','').replace(']','')
        educationMajor2		= json.dumps(thing['educationMajor2']).replace('"','').replace('[','').replace(']','')
        eduTimeStart2		= json.dumps(thing['eduTimeStart2']).replace('"','').replace('[','').replace(']','')
        eduTimeEnd2			= json.dumps(thing['eduTimeEnd2']).replace('"','').replace('[','').replace(']','')
        
        educationSchool3	= json.dumps(thing['educationSchoolName3']).replace('"','').replace('[','').replace(']','')
        educationDegree3	= json.dumps(thing['educationDegree3']).replace('"','').replace('[','').replace(']','')
        educationMajor3		= json.dumps(thing['educationMajor3']).replace('"','').replace('[','').replace(']','')
        eduTimeStart3		= json.dumps(thing['eduTimeStart3']).replace('"','').replace('[','').replace(']','')
        eduTimeEnd3			= json.dumps(thing['eduTimeEnd3']).replace('"','').replace('[','').replace(']','')
        
        
        experienceHeads		= thing['experienceHeads']
        expTimeStarts		= thing['expTimeStarts']
        expTimeEnds			= thing['expTimeEnds']
        
        
        
        
        
#        experienceHead1		= json.dumps(thing['experienceHead1'])
#        expTimeStart1		= json.dumps(thing['expTimeStart1'])
#        expTimeEnd1			= json.dumps(thing['expTimeEnd1'])
#        expTimeDuration1	= json.dumps(thing['expTimeDuration1'])
        
#        experienceHead2		= json.dumps(thing['experienceHead2'])
#        expTimeStart2		= json.dumps(thing['expTimeStart2'])
#        expTimeEnd2			= json.dumps(thing['expTimeEnd2'])
#        expTimeDuration2	= json.dumps(thing['expTimeDuration2'])
        
#        experienceHead3		= json.dumps(thing['experienceHead3'])
#        expTimeStart3		= json.dumps(thing['expTimeStart3'])
#        expTimeEnd3			= json.dumps(thing['expTimeEnd3'])
#        expTimeDuration3	= json.dumps(thing['expTimeDuration3'])
        
#        experienceHead4		= json.dumps(thing['experienceHead4'])
#        expTimeStart4		= json.dumps(thing['expTimeStart4'])
#        expTimeEnd4			= json.dumps(thing['expTimeEnd4'])
#        expTimeDuration4	= json.dumps(thing['expTimeDuration4'])
        
#        experienceHead5		= json.dumps(thing['experienceHead5'])
#        expTimeStart5		= json.dumps(thing['expTimeStart5'])
#        expTimeEnd5			= json.dumps(thing['expTimeEnd5'])
#        expTimeDuration5	= json.dumps(thing['expTimeDuration5'])
        
        
        
        
        #additionalAwards	= json.dumps(thing['additionalAwards'])
        #contactFor			= json.dumps(thing['contactFor'])
        
        #####################################################################################################
        delimiter = " # "
        
        
        
        line = url + delimiter + name + delimiter + headlineTitle + delimiter + location + delimiter + industry + delimiter
        line = line + overviewCurrent + delimiter + overviewEducation + delimiter + connections + delimiter
        
        line = line + educationSchool1 + delimiter + educationDegree1 + delimiter + educationMajor1 + delimiter + eduTimeStart1 + delimiter + eduTimeEnd1 + delimiter
        
        line = line + educationSchool2 + delimiter + educationDegree2 + delimiter + educationMajor2 + delimiter + eduTimeStart2 + delimiter + eduTimeEnd2 + delimiter
        
        line = line + educationSchool3 + delimiter + educationDegree3 + delimiter + educationMajor3 + delimiter + eduTimeStart3 + delimiter + eduTimeEnd3 + delimiter
        
        
                
        #handling the arbitrary number of work experiences
        while experienceHeads and expTimeStarts and expTimeEnds: 
        	line = line + experienceHeads.pop(0) + delimiter + expTimeStarts.pop(0) + delimiter + expTimeEnds.pop(0) + delimiter
        
 
#        line = line + experienceHead1 + delimiter + expTimeStart1 + delimiter + expTimeEnd1 + delimiter + expTimeDuration1 + delimiter       
#        line = line + experienceHead2 + delimiter + expTimeStart2 + delimiter + expTimeEnd2 + delimiter + expTimeDuration2 + delimiter
#        line = line + experienceHead3 + delimiter + expTimeStart3 + delimiter + expTimeEnd3 + delimiter + expTimeDuration3 + delimiter
#        line = line + experienceHead4 + delimiter + expTimeStart4 + delimiter + expTimeEnd4 + delimiter + expTimeDuration4 + delimiter
#        line = line + experienceHead5 + delimiter + expTimeStart5 + delimiter + expTimeEnd5 + delimiter + expTimeDuration5 + delimiter
        
        
        
        
        #line = line + additionalAwards + " ## "
        
        #####################################################################################################
        
        exampleLine = "URL" + delimiter + "Name" + delimiter + "Headline Title" + delimiter + "Location" + delimiter + "Industry" + delimiter + "Overview Current" + delimiter + "Overview Education" + delimiter + "Connections" + delimiter + "School Name 1" + delimiter + "Education Degree 1" + delimiter + "Education Major 1" + delimiter + "Education Time Start 1" + delimiter + "Education Time End 1" + delimiter + "School Name 2" + delimiter + "Education Degree 2" + delimiter + "Education Major 2" + delimiter + "Education Time Start 2" + delimiter + "Education Time End 2" + delimiter + "School Name 3" + delimiter + "Education Degree 3" + delimiter + "Education Major 3" + delimiter + "Education Time Start 3" + delimiter + "Education Time End 3" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter+ "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter + "Work Experience Title" + delimiter + "Work Experience Time Began" + delimiter + "Work Experience Time Ended" + delimiter
        
        #self.file.write(exampleLine)
        
        
        
        
        #self.file.write(line)
        
        print line
        sys.stdout.flush()
        
        #for x,y in dict(item).iteritems():
        #	print json.dumps(x) + "\t\t\t = " +json.dumps(y)
        
        #for x,y in dict(item).iteritems():
        #	print json.dumps(x) +": "
        #	for z in y:
        #		print "\t"+json.dumps(z)
        		
       	
        
        
        #self.file.write(line)
        return item
