#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simplified Email Automation for Gargi Kar"""
import csv
import json
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

EMAIL_CONFIG = {
    'outbound_email': 'gargikar63@gmail.com',
    'password': 'Tintin@8981251691',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

def load_leads():
    leads = []
    with open('qualified_leads.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)
    return leads

def get_industry_insight(industry):
    insights = {
        'E-commerce': 'Your high cart value + recent marketing spend = prime for AI recovery automation.',
        'Real Estate': 'Hot market means you cannot afford to miss leads. AI follows up 24/7 while you sleep.',
        'Legal': 'Every hour spent on repetitive docs is a billable hour lost. AI handles templates instantly.',
        'Healthcare': 'Patient acquisition costs high. AI scheduling maximizes every appointment request.',
        'Accounting': 'Year-end is coming. Automated audit prep saves you 15+ billable hours daily.',
        'Manufacturing': 'Quality defects cost thousands. AI inspection catches issues before they ship.',
        'Logistics': 'Inventory errors mean lost money. AI tracking ensures 99+ accuracy.',
        'Consulting': 'Manual client onboarding wastes billable time. AI automation handles intake.',
        'Education': 'Manual course content creation is slow. AI generates and structures content fast.',
        'Default': 'AI automation can transform your business operations today.'
    }
    return insights.get(industry, insights['Default'])

def send_email(lead):
    from_email = EMAIL_CONFIG['outbound_email']
    
    company = lead.get('company', 'Your Company')
    project = lead.get('project_type', 'AI Automation')
    industry = lead.get('industry', 'business')
    insight = get_industry_insight(industry)
    
    # Simple name for recipient
    recipient = lead.get('name', 'contact').lower().replace(' ', '').strip().lower()
    if recipient and '@' not in recipient:
        recipient = recipient + '@' + company.replace(' ', '').removesuffix(' Inc.').removesuffix('( ').removesuffix(')').lower()
    
    subject = f'{company} - {project} Opportunity'
    
    body = f'''Hi {lead.get('name', 'Contact')},

{insight}

I specialize in AI automation that delivers results:
- Increases revenue by 40% within 2 months
- Reduces operational overhead by 60%  
- Identifies costly manual process loopholes

Quick question: Would you be open to a free 15-minute AI audit of your current workflows?

I will identify:
- 3-5 high-cost manual processes wasting money daily
- AI automation opportunities with instant ROI
- Implementation roadmap with cost projections

I work remotely on part-time basis and can start this week.

Best regards,

Gargi Kar
AI Automation Expert | Workflow Designer
https://gargikar-portfolio.vercel.app
📧 gargikar63@gmail.com

[Your Portfolio Link]

P.S. I recently helped businesses achieve significant results.

Would this be valuable for {company}?
'''
    
    try:
        msg = MIMEText(body, 'plain')
        msg['Subject'] = subject
        msg['From'] = from_email
        # Use safe recipient
        if not recipient or '@' not in recipient:
            recipient = lead.get('name', 'test') + '@example.com'
        msg['To'] = recipient
        
        print(f'Sending to: {lead.get("name", "?")} ({company})')
        print(f'Subject: {subject}')
        
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(from_email, EMAIL_CONFIG['password'])
            server.send_message(msg)
            print(f'  ✓ Email sent successfully!')
            
        return True
    except Exception as e:
        error_msg = str(e)[:80]
        print(f'  ✗ Send failed: {error_msg}')
        return False
    finally:
        print()  # Blank line between emails

def main():
    print('\n' + '='*70)
    print('🤖 GARGI KAR - AI AUTOMATION OUTREACH SYSTEM')
    print('='*70)
    print('\n📊 Loading leads...')
    leads = load_leads()
    
    if not leads:
        print('✗ No leads found in qualified_leads.csv')
        print('Run: python lead_scraper.py to generate leads')
        return
        
    print(f'✅ Found {len(leads)} qualified leads')
    print('⏰ Starting at:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print()
    
    sent = 0
    for lead in leads:
        if send_email(lead):
            sent += 1
        
        # 2 second delay between emails (rate limiting)
        import time
        time.sleep(2)
    
    print('='*70)
    print('✅ OUTREACH COMPLETED')
    print(f'   Emails sent: {sent}/{len(leads)}')
    print(f'   Success rate: {sent*100/len(leads):.1f}%' if leads else 'N/A')
    print('='*70)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'\n✗ Fatal error: {e}')
        import traceback
        traceback.print_exc()
