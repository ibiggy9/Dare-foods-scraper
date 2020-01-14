# -*- coding: utf-8 -*-
import scrapy
import os as hi
from datetime import datetime


class DarebotSpider(scrapy.Spider):
    name = 'darebot'
    allowed_domains = ['www.darefoods.com']
    start_urls = [
        'https://www.darefoods.com/ca_en/product/bear-paws-sandwich-cookies-chocolate/461/',
        
        'https://www.darefoods.com/ca_en/product/bear-paws-sandwich-cookies-vanilla/462',

        'https://www.darefoods.com/ca_en/product/my-first-bear-paws-vanilla/459',

        'https://www.darefoods.com/ca_en/product/bear-paws-baked-apple/131',
        
        'https://www.darefoods.com/ca_en/product/bear-paws-banana-bread/132',

        'https://www.darefoods.com/ca_en/product/bear-paws-birthday-cake/416',

        'https://www.darefoods.com/ca_en/product/bear-paws-brownie/133',

        'https://www.darefoods.com/ca_en/product/bear-paws-chocolate-chip/134',

        'https://www.darefoods.com/ca_en/product/bear-paws-molasses/136',

        'https://www.darefoods.com/ca_en/product/bear-paws-dipped-granola-caramel/335',

        'https://www.darefoods.com/ca_en/product/bear-paws-dipped-granola-chocolate-chip/334',

        'https://www.darefoods.com/ca_en/product/bear-paws-dipped-granola-smores/359',

        'https://www.darefoods.com/ca_en/product/bear-paws-morning-snack-cereal-and-blueberry-yogourt/141',


        'https://www.darefoods.com/ca_en/product/bear-paws-morning-snack-cereal-and-strawberries/140',

        'https://www.darefoods.com/ca_en/product/bear-paws-morning-snack-cereal-and-vanilla-yogourt/142',
        
        'https://www.darefoods.com/ca_en/product/bear-paws-crackers-mix-cheddar/468',
        'https://www.darefoods.com/ca_en/product/bear-paws-crackers-mix-white-cheddar/469',
        'https://www.darefoods.com/ca_en/product/bear-paws-crackers-cheddar/441',
        'https://www.darefoods.com/ca_en/product/bear-paws-crackers-on-the-go-packs-cheddar/450',
        'https://www.darefoods.com/ca_en/product/bear-paws-crackers-three-cheese/442',
        'https://www.darefoods.com/ca_en/product/my-first-bear-paws-oatmeal/440',
        'https://www.darefoods.com/ca_en/product/my-first-bear-paws-vanilla/459',
        'https://www.darefoods.com/ca_en/product/my-first-bear-paws-vanilla/439',
        'https://www.darefoods.com/ca_en/product/breton-organic-7-grain/425',
        'https://www.darefoods.com/ca_en/product/breton-organic-roasted-garlic/422',
        'https://www.darefoods.com/ca_en/product/breton-original-bites-pouches/457',
        'https://www.darefoods.com/ca_en/product/breton-sprouted-grains-caramelized-onion/414',
        'https://www.darefoods.com/ca_en/product/breton-sprouted-grains-sea-salt/415',
        'https://www.darefoods.com/ca_en/product/breton-veggie-bites-pouches/437',
        'https://www.darefoods.com/ca_en/product/breton-artisanal-cranberry-and-ancient-grains/348',
        'https://www.darefoods.com/ca_en/product/breton-artisanal-sweet-potato-and-ancient-grains/349',
        'https://www.darefoods.com/ca_en/product/breton-cheddar-bites/114',
        'https://www.darefoods.com/ca_en/product/breton-original-bites/115',
        'https://www.darefoods.com/ca_en/product/breton-original-bites-pouches/457',
        'https://www.darefoods.com/ca_en/product/breton-veggie-bites/116',
        'https://www.darefoods.com/ca_en/product/breton-veggie-bites-pouches/437',
        'https://www.darefoods.com/ca_en/product/breton-black-bean-with-onion-and-garlic/327',
        'https://www.darefoods.com/ca_en/product/breton-gluten-free-herb-and-garlic/113',
        'https://www.darefoods.com/ca_en/product/breton-gluten-free-original-with-flax/112',
        'https://www.darefoods.com/ca_en/product/breton-white-bean-with-salt-and-pepper/326',
        'https://www.darefoods.com/ca_en/product/breton-organic-7-grain/425',
        'https://www.darefoods.com/ca_en/product/breton-organic-roasted-garlic/422',
        'https://www.darefoods.com/ca_en/product/breton-sprouted-grains-caramelized-onion/414',
        'https://www.darefoods.com/ca_en/product/breton-sprouted-grains-sea-salt/415',
        'https://www.darefoods.com/ca_en/product/breton-basil-and-olive-oil/106',
        'https://www.darefoods.com/ca_en/product/breton-garden-vegetable/107',
        'https://www.darefoods.com/ca_en/product/breton-multigrain/108',
        'https://www.darefoods.com/ca_en/product/breton-original/109',
        'https://www.darefoods.com/ca_en/product/breton-original-fresh-pack/382',
        'https://www.darefoods.com/ca_en/product/breton-reduced-fat-and-salt/111',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        
     
        ]

    def parse(self, response):
        imageurl = response.css(".six.columns.module-two img::attr(src)").extract()
        title = response.css(".six.columns.module-one H1").extract()
        product_features = response.css(".six.columns.module-one H3").extract()
        reasons_to_believe = response.css(".six.columns.module-one li").getall() 
        concept_statement = response.css(".six.columns.module-one p").extract() 
        product_facts = response.css(".four.columns li").extract()  
        Time_Stamp = ['a', 'b']  
        for item in zip(Time_Stamp, imageurl, title, product_features, reasons_to_believe, concept_statement, product_facts):
            scraped_info = {
                'Time Stamp' : item[0],
                'Image Link' : item[1],
                'Product Title' : item[2],
                'Product Features' : item[3],
                'Reasons to Believe' : item[4],
                'Concept Statement' : item[5],
                'Product Facts' : item[6]
           
            }

            scraped_info['Time Stamp'] = datetime.now().strftime("%m/%d/%Y/ %H:%M:%S")


            yield scraped_info


