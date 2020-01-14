# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.mail import MailSender

mailer = MailSender()
mailer.send(to=['ian.bigford@hotmail.com'], subject="Automated Pull from Dare Website", body="Hi Ian, Here is the pull from the last week")


class DareSitePipeline(object):
    def process_item(self, item, spider):
        return item

