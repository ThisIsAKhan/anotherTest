# Scrapy settings for linkedIn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pullLinksData'
 
SPIDER_MODULES = ['pullLinksData.spiders']
NEWSPIDER_MODULE = 'pullLinksData.spiders'
DEFAULT_ITEM_CLASS = 'linkedIn.items.linkedinDataItem'
