#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate mailto links for outreach"""
import csv
from urllib.parse import quote
from datetime import datetime

leads = [
    {'name': 'Acme E-Commerce', 'company': 'Acme Store', 'industry': 'E-commerce'},
    {'name': 'Ridge Realty Group', 'company': 'Ridge Realty Inc.', 'industry': 'Real Estate'},
    {'name': 'LegalFlow Docs', 'company': 'LegalFlow LLC', 'industry': 'Legal'},
    {'name': 'MetroHealth AI', 'company': 'MetroHealth Group', 'industry': 'Healthcare'},
    {'name': 'Apex Manufacturing', 'company': 'Apex Corp', 'industry': 'Manufacturing'},
    {'name': 'Trend Accounting', 'company': 'Trend Solutions', 'industry': 'Accounting'},
    {'name': 'Bloom Consulting', 'company': 'Bloom Advisors', 'industry': 'Consulting'},
    {'name': 'Swift Logistics', 'company': 'Swift Transport', 'industry': 'Logistics'},
    {'name': 'Prime Fitness', 'company': 'Fitness Centers', 'industry': 'Fitness'},
    {'name': 'CulinaryChef AI', 'company': 'Chef Master Class', 'industry': 'Education'},
]

outbound_email = 'gargikar63@gmail.com'

print('='*70)
print('GARGI KAR - 10 MAILTO LINKS GENERATED')
print('='*70)
print('Generated:', datetime.now().strftime('%H:%M:%S'))
print()

for i, lead in enumerate(leads, 1):
    name = lead['name']
    company = lead['company']
    industry = lead['industry']
    
    # Convert name to email-like format
    email_name = name.lower().replace(' ', '').strip()
    if '@' not in email_name:
        email_name = email_name + '@gmail.com'
    
    # Create subject
    subject = f'{company} - AI {industry} Opportunity'
    subject_url = quote(subject)
    
    # Create email body
    body = f'''Hi {name},

{industry.upper()} automation can transform your business.

AI solutions that I implement:
- Increase revenue by 40% within 2 months
- Reduce operational overhead by 60%
- Identify costly manual process loopholes

Quick question: Would you be open to a 15-minute free AI audit?

I will identify:
- 3-5 high-cost manual processes
- AI automation opportunities with instant ROI
- Implementation roadmap with cost projections

I work remotely and can start this week.

Best regards,

Gargi Kar
AI Automation Expert
https://gargikar-dev.github.io/portfolio/
gargikar63@gmail.com

P.S. Would this be valuable for {company}?
'''

    body_url = quote(body, safe=' \n')
    
    # Create mailto URL
    mailto = f'mailto:{email_name}?subject={subject_url}&body={body_url}'
    
    # Print link info
    print(f'== Link #{i}: {lead["industry"].upper()} ==')
    print('To:', email_name)
    print('Subject:', subject)
    print('Click to open:')
    print(mailto)
    print()
    
    # Save to file
    with open(f'link_{i}.txt', 'w', encoding='utf-8') as f:
        f.write(mailto + '\n')

print('='*70)
print('All 10 mailto links saved to:')
print('  .\\link_1.txt through .\\link_10.txt')
print('='*70)
print()
print('USAGE:')
print('1. Open each .txt file')
print('2. Copy the mailto link')
print('3. Paste in your browser (Google Mail, Outlook, etc.)')
print('4. Review email → HIT SEND')
print('='*70)