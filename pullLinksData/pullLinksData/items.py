# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PulllinksdataItem(Item):
    # define the fields for your item here like:
    
    url							= Field()
    
    name 						= Field()
    headlineTitle 				= Field()
    location 					= Field()
    industry 					= Field()
    overviewCurrent 			= Field()
    overviewPast 				= Field()
    overviewEducation 			= Field()
    #recommendations 			= Field()
    connections 				= Field()
    #websites 					= Field()
    
    descriptionSummary 			= Field()
    summarySpecialties 			= Field()
    
    
    experienceHeads				= Field()
    expTimeStarts				= Field()
    expTimeEnds					= Field()
    #expDescriptions				= Field()
    
    
#    experienceHead1			 	= Field()
#    expTimeStart1				= Field()
#    expTimeEnd1					= Field()
#    expTimeDuration1			= Field()
#    expDescription1				= Field()
    
#    experienceHead2	 			= Field()
#    expTimeStart2				= Field()
#    expTimeEnd2					= Field()
#    expTimeDuration2			= Field()
#    expDescription2				= Field()
    
#    experienceHead3			 	= Field()
#    expTimeStart3				= Field()
#    expTimeEnd3					= Field()
 #   expTimeDuration3			= Field()
 #   expDescription3				= Field()
    
#    experienceHead4			 	= Field()
#    expTimeStart4				= Field()
#    expTimeEnd4					= Field()
#    expTimeDuration4			= Field()
#    expDescription4				= Field()
    
#    experienceHead5			 	= Field()
#    expTimeStart5				= Field()
#    expTimeEnd5					= Field()
#    expTimeDuration5			= Field()
#    expDescription5				= Field()
    
    
    
    
    
    
    educationSchoolName1		= Field()
    educationMajor1				= Field()
    educationDegree1			= Field()
    eduTimeStart1				= Field()
    eduTimeEnd1					= Field()
    
    educationSchoolName2		= Field()
    educationMajor2				= Field()
    educationDegree2			= Field()
    eduTimeStart2				= Field()
    eduTimeEnd2					= Field()
    
    educationSchoolName3		= Field()
    educationMajor3				= Field()
    educationDegree3			= Field()
    eduTimeStart3				= Field()
    eduTimeEnd3					= Field()
    


    #descriptionEducation 		= Field()
    
    additionalInterests			= Field()
    #additionalGroups			= Field()
    additionalAwards			= Field()
    
    #contactFor					= Field()
    
