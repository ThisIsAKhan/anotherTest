# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from PulllinksdataItem.items import PulllinksdataItem

import sys
import random
from countries import checkLocation


randomSampling = True
samplingProbability = 0.1

filterForUS = True

def striplist(l):
        return ([x.strip().replace('\t',"") for x in l])				


class PulllinksdataSpider(BaseSpider):
	name = "linkedin.com"
	allowed_domains = ["linkedin.com"]
	start_urls = ["http://www.linkedin.com/directory/people-%s" % s
					for s in "abcdefghijklmnopqrstuvwxyz"]

        #start_urls = start_urls[0:1]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
                
                #return


		if not hxs.select('//body[@class="guest directory"]'): #if it is not a directory (its a regular page)
			if hxs.select('//meta[@name="pageImpressionID"]'): 

				item = PulllinksdataItem()		
				item ['url']					= response.url

                                # I found that linkedIn changed around their HTML. Furthermore linkedin seems to have .
                                #item['name'] = striplist(hxs.select('//h1/span/span/text()').extract())
                                item['headlineTitle'] = striplist(hxs.select('//p[@class="headline-title title"]/text()').extract())


                                HTMLtitle = striplist(hxs.select('//title/text()').extract())
                                item['name'] = [HTMLtitle[0].split('|')[0].strip()]
				item['location'] = striplist(hxs.select('//dd/span/text()').extract())			

				#if not checkLocation(item['location']):
					#print item['location']
					#sys.stdout.flush()
				#else:

				if filterForUS and checkLocation(item['location']):
                                        item['industry'] = striplist(hxs.select('//dd[@class="industry"]/text()').extract())		
					item['overviewCurrent'] = striplist(hxs.select('//dd[@class="summary-current"]/ul[@class="current"]/li/text()').extract())
					item['overviewPast'] = striplist(hxs.select('//dd[@class="summary-past"]/ul[@class="past"]/li/text()').extract())
					item['overviewEducation'] = striplist(hxs.select('//dd[@class="summary-education"]/ul/li/text()').extract())
					#item['recommendations'] 		= striplist(hxs.select('').extract())
					item['connections'] 			= striplist(hxs.select('//dd[@class="overview-connections"]/p/strong/text()').extract())
					#item['websites'] 				= striplist(hxs.select('').extract())

					item['descriptionSummary']		= striplist(hxs.select('//p[@class=" description summary"]/text()').extract())
					item['summarySpecialties']		= striplist(hxs.select('//div[@id="profile-specialties"]/p/text()').extract())


					# ------------------------------------------------------------------------------------------------------------------
					# Education
					# ------------------------------------------------------------------------------------------------------------------

					# Education: School Names
					firstEducationSchool	= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/h3[@class="summary fn org"]/text()').extract())
					schoolNames				= striplist(hxs.select('//div[@class="position  education vevent vcard"]/h3[@class="summary fn org"]/text()').extract())

					# Education: Degrees
					firstDegree 			= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/h4/span[@class="degree"]/text()').extract())
					schoolDegrees			= striplist(hxs.select('//div[@class="position  education vevent vcard"]/h4/span[@class="degree"]/text()').extract())

					# Education: Majors
					firstMajor 				= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/h4/span[@class="major"]/text()').extract())
					schoolMajors			= striplist(hxs.select('//div[@class="position  education vevent vcard"]/h4/span[@class="major"]/text()').extract())

					# Education: Time Start
					firstEducationStart		= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/p[@class="period"]/abbr[@class="dtstart"]/text()').extract())
					educationStarts			= striplist(hxs.select('//div[@class="position  education vevent vcard"]/p[@class="period"]/abbr[@class="dtstart"]/text()').extract())

					# Education: Time End
					firstEducationEnd		= striplist(hxs.select('//div[@class="position  first education vevent vcard"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())
					educationEnds			= striplist(hxs.select('//div[@class="position  education vevent vcard"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())


					if firstEducationSchool:
						item['educationSchoolName1']		= firstEducationSchool.pop(0)
						if firstDegree:
							item['educationDegree1']		= firstDegree.pop(0)
						else:
							item['educationDegree1']		= []
						if firstMajor:
							item['educationMajor1']			= firstMajor.pop(0)
						else:
							item['educationMajor1']			= []
						if firstEducationStart:
							item['eduTimeStart1']			= firstEducationStart.pop(0)
						else:
							item['eduTimeStart1']			= []
						if firstEducationEnd:
							item['eduTimeEnd1']				= firstEducationEnd.pop(0)
						else:
							item['eduTimeEnd1']				= []
					elif schoolNames:
						item['educationSchoolName1']		= schoolNames.pop(0)
						if schoolDegrees:
							item['educationDegree1']		= schoolDegrees.pop(0)
						else:
							item['educationDegree1']		= []
						if schoolMajors:
							item['educationMajor1']			= schoolMajors.pop(0)
						else:
							item['educationMajor1']			= []
						if educationStarts:
							item['eduTimeStart1']			= educationStarts.pop(0)
						else:
							item['eduTimeStart1']			= []
						if educationEnds:
							item['eduTimeEnd1']				= educationEnds.pop(0)
						else:
							item['eduTimeEnd1']				= []
					else:
						item['educationSchoolName1']		= []
						item['educationDegree1']			= []
						item['educationMajor1']				= []
						item['eduTimeStart1']				= []
						item['eduTimeEnd1']					= []


					if not schoolNames:
						item['educationSchoolName2']		= []
					else:
						item['educationSchoolName2']		= schoolNames.pop(0)
					if not schoolNames:
						item['educationSchoolName3']		= []
					else:
						item['educationSchoolName3']		= schoolNames.pop(0)



					if not schoolDegrees:
						item['educationDegree2']			= []
					else:
						item['educationDegree2']			= schoolDegrees.pop(0)
					if not schoolDegrees:
						item['educationDegree3']			= []
					else:
						item['educationDegree3']			= schoolDegrees.pop(0)



					if not schoolMajors:
						item['educationMajor2']			= []
					else:
						item['educationMajor2']			= schoolMajors.pop(0)
					if not schoolMajors:
						item['educationMajor3']			= []
					else:
						item['educationMajor3']			= schoolMajors.pop(0)


					if not educationStarts:
						item['eduTimeStart2']			= []
					else:
						item['eduTimeStart2']			= educationStarts.pop(0)
					if not educationStarts:
						item['eduTimeStart3']			= []
					else:
						item['eduTimeStart3']			= educationStarts.pop(0)



					if not educationEnds:
						item['eduTimeEnd2']			= []
					else:
						item['eduTimeEnd2']			= educationEnds.pop(0)
					if not educationEnds:
						item['eduTimeEnd3']			= []
					else:
						item['eduTimeEnd3']			= educationEnds.pop(0)












					#------------------------------------------------------------------------------------------------------------------			
					# Work Experience
					#------------------------------------------------------------------------------------------------------------------


					# Work Experience: title
					experienceHeads					= striplist(hxs.select('//h3[@class="position-title anet"]/span[@class="title"]/text()').extract())
					item['experienceHeads'] 		= striplist(hxs.select('//h3[@class="position-title anet"]/span[@class="title"]/text()').extract())



					# Work Experience: Time started
					currentExpTimeStart				= striplist(hxs.select('//div[@class="position  first experience vevent vcard summary-current"]/p/abbr[@class="dtstart"]/text()').extract())
					if not currentExpTimeStart:
						currentExpTimeStart 		= striplist(hxs.select('//div[@class="position  first experience vevent vcard current-position"]/p/abbr[@class="dtstart"]/text()').extract())

					moreExpTimeStart				= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-current"]/p/abbr[@class="dtstart"]/text()').extract())
					if not moreExpTimeStart:
						moreExpTimeStart			= striplist(hxs.select('//div[@class="position   experience vevent vcard current-position"]/p/abbr[@class="dtstart"]/text()').extract())


					expTimeStarts					= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-past"]/p/abbr[@class="dtstart"]/text()').extract())
					if not expTimeStarts:
						expTimeStarts				= striplist(hxs.select('//div[@class="position   experience vevent vcard past-position"]/p/abbr[@class="dtstart"]/text()').extract())

					item['expTimeStarts']			= currentExpTimeStart + moreExpTimeStart +expTimeStarts


					# Work Experience: Time ended

					present							= striplist(hxs.select('//p[@class="period"]/abbr[@class="dtstamp"]/text()').extract())
					expTimeEnds						= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-past"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())
					if not expTimeEnds:
						expTimeEnds					= striplist(hxs.select('//div[@class="position   experience vevent vcard past-position"]/p[@class="period"]/abbr[@class="dtend"]/text()').extract())

					item['expTimeEnds']				= present + expTimeEnds			



					'''
					print 'experienceHeads'
					print experienceHeads
					
					print 'currentExpTimeStart'
					print currentExpTimeStart
					
					
					print 'moreExpTimeStart'
					print moreExpTimeStart
					
					print 'expTimeStarts'
					print expTimeStarts
					
					
					print 'present'
					print present
					
					print 'expTimeEnds'
					print expTimeEnds
					'''



					# Work Experience: Time duration

					'''		
					currentDuration					= striplist(hxs.select('//div[@class="position  first experience vevent vcard summary-current"]/p/span[@class="duration"]/text()').extract())
					expTimeDurations				= striplist(hxs.select('//div[@class="position   experience vevent vcard summary-past"]/p/span[@class="duration"]/text()').extract())
					'''


					# Work Experience: Description


					#currentDescription				= striplist(hxs.select('//p[@class=" description current-position"]/text()').extract())
					#expDescriptions					= striplist(hxs.select('//p[@class=" description past-position"]/text()').extract())

					#divs = hxs.select('//p[@class=" description past-position"]/text()')
					#for p in divs.select('.//br') :
					#	print p.extract()


		#			if not currentDescription:
		#				if not expDescriptions:
		#					item['expDescription1']	= []
		#				else:
		#					item['expDescription1']	= expDescriptions.pop(0)
		#			else:
		#				item['expDescription1']		= currentDescription.pop(0)
		#			
		#			if not expDescriptions:
		#				item['expDescription2']		= []
		#			else:
		#				item['expDescription2']		= expDescriptions.pop(0)
		#			if not expDescriptions:
		#				item['expDescription3']		= []
		#			else:
		#				item['expDescription3']		= expDescriptions.pop(0)
		#			if not expDescriptions:
		#				item['expDescription4']		= []
		#			else:
		#				item['expDescription4']		= expDescriptions.pop(0)
		#			if not expDescriptions:
		#				item['expDescription5']		= []
		#			else:
		#				item['expDescription5']		= expDescriptions.pop(0)
		#			#item['expDescription2']			= []

					#item['expDescription3']			= []

					#item['expDescription4']			= []

					#item['expDescription5']			= []





					yield item

		else : #if it is a directory
			for url in hxs.select('//ul[@class="directory"]/li/a/@href').extract(): #take all of the subdirectories that show up and request them
				if not randomSampling or random.random() < samplingProbability: #random sampling.
					yield Request('http://www.linkedin.com'+url, callback=self.parse)






