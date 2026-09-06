#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simplified Email Automation for Gargi Kar - NO UNICODE ISSUES"""
import csv
import smtplib
from email.mime.text import MIMEText
import time

EMAIL_CONFIG = {
    'outbound_email': 'gargikar63@gmail.com',
    'password': 'Tintin@8981251691',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

def get_industry_insight(industry):
    insights = {
        'E-commerce': 'Your high cart abandonment means AI recovery can save 60 percent of lost revenue immediately.',
        'Real Estate': 'Hot market plus manual follow-up equals missed leads. AI follows twenty-four seven while you sleep.',
        'Legal': 'Every hour on documents is billable time lost. AI handles templates in seconds not hours.',
        'Healthcare': 'Patient acquisition costs are high. AI scheduling maximizes every appointment request.',
        'Accounting': 'Year-end is coming. Automated prep saves you fifteen billable hours daily.',
        'Manufacturing': 'Quality defects cost thousands. AI inspection catches issues before they ship.',
        'Logistics': 'Inventory errors mean lost money. AI tracking ensures ninety-nine percent accuracy.',
        'Consulting': 'Manual client onboarding wastes billable time. AI automation handles intake.',
        'Education': 'Manual course content creation is slow. AI generates and structures content fast.',
    }
    return insights.get(industry, 'AI automation can transform your business operations today.')

def send_email(lead):
    from_email = EMAIL_CONFIG['outbound_email']
    
    company = lead.get('company', 'Your Company')
    project = lead.get('project_type', 'AI Automation')
    industry = lead.get('industry', 'business')
    insight = get_industry_insight(industry)
    name = lead.get('name', '')
    
    # Get recipient email safely
    recipient_name = name.lower().replace(' ', '').strip()
    if not recipient_name:
        recipient_name = 'contact'
    recipient = recipient_name + '@example.com'  # Placeholder - replace with real
    
    subject = company + ' - ' + project + ' Opportunity'
    first_name = name.split(',')[0].strip() if name else 'Contact'
    
    body = insight + '''

I specialize in AI automation that delivers results:
- Increases revenue by 40 percent within 2 months
- Reduces operational overhead by 60 percent  
- Identifies costly manual process loopholes

Quick question: Would you be open to a free fifteen-minute AI audit of your current workflows?

I will identify:
- Three to five high-cost manual processes wasting money daily
- AI automation opportunities with instant ROI
- Implementation roadmap with cost projections

I work remotely on part-time basis and can start this week.

Best regards,

Gargi Kar
AI Automation Expert | Workflow Designer
https://gargikar-portfolio.vercel.app
gargikar63@gmail.com

P.S. Would this be valuable for ' + company.replace("'",'') + '?
'''
    
    try:
        msg = MIMEText(body, 'plain')
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = recipient
        
        print('Sending to: ' + lead.get('name', '?') + ' (' + company + ')')
        print('Subject: ' + subject)
        
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(from_email, EMAIL_CONFIG['password'])
            server.send_message(msg)
            print('  Email sent successfully!')
            
        return True
    except Exception as e:
        print('  Send failed: ' + str(e)[:60])
        return False

def main():
    print('GARGI KAR - AI AUTOMATION OUTREACH SYSTEM')
    print('Loading leads...')
    
    leads = []
    try:
        with open('qualified_leads.csv', 'r') as f:
            reader = csv.DictReader(f)
            leads = list(reader)
    except Exception as e:
        print('Error loading leads: ' + str(e)[:60])
        return
    
    print('Found ' + str(len(leads)) + ' qualified leads')
    print('Starting:')
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print()
    
    sent = 0
    for lead in leads:
        if send_email(lead):
            sent += 1
        time.sleep(2)
    
    print('='*60)
    print('OUTREACH COMPLETED')
    print('Emails sent: ' + str(sent) + '/' + str(len(leads)))
    print('='*60)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Fatal error: ' + str(e)[:70])
        import traceback
        traceback.print_exc()
