# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:05:48 2020

@author: sherangagamwasam
"""
import mailchimp_python_function as mpf
import newsletter_template

# =============================================================================
# audience creation
# =============================================================================

audience_creation_dictionary = {
    "audience_name" : "ENTER AUDIENCE NAME",
    "company" : "ENTER COMPANY NAME",
    "address1" : "ENTER ADDRESS",
    "city" :  "ENTER CITY",
    "state" : "ENTER STATE",
    "zip_code" : "ENTER ZIPCODE",
    "country" : "ENTER COUNTRY", # FOR SRI LANKA : USE LK
    "from_name" : "ENTER FROM NAME",
    "from_email" : "ENTER FROM EMAIL",
    "language" : "en"
}    
    
audience_creation = mpf.audience_creation_function(audience_creation_dictionary)

# =============================================================================
# add members to the existing audience 
# =============================================================================

audience_id = audience_creation['id']
# add the email list here
email_list = ['test1@gmail.com',
              'test2@gmail.com']

mpf.add_members_to_audience_function(
    audience_id = audience_creation['id'],
    email_list = email_list)

# =============================================================================
# campaign creation
# =============================================================================

campaign_name = 'ENTER CAMPAIGN NAME'
from_name = 'ENTER YOUR NAME'
reply_to = 'ENTER REPLY EMAIL' # test1@gmail.com

campaign = mpf.campaign_creation_function(campaign_name=campaign_name,
                                      audience_id=audience_creation['id'],
                                      from_name=from_name,
                                      reply_to=reply_to)

# =============================================================================
# news letter tempates creation
# =============================================================================

html_code = newsletter_template.html_code           

mpf.customized_template(html_code=html_code, 
                    campaign_id=campaign['id'])

# =============================================================================
# send the mail campaign
# =============================================================================

mpf.send_mail(campaign_id=campaign['id'])           
