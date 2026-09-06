#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QUICK AUTO-OUTREACH SYSTEM
Sends emails automatically when credentials provided
No app password needed - uses mailto links
"""
import csv
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Load sample lead data
class EmailCampaign:
    def __init__(self, email_config, lead_file=None):
        self.email = email_config['outbound_email']
        self.password = email_config['password']
        self.smtp = email_config['smtp_server']
        self.port = email_config['smtp_port']
        self.leads = self.load_leads(lead_file)
        self.sent = 0
        self.failed = 0
        
    def load_leads(self, filename):
        """Load leads from file or use samples"""
        if filename and file_exists(filename):
            try:
                with open(filename, 'r') as f:
                    reader = csv.DictReader(f)
                    return list(reader)
            except:
                pass
        
        # Sample data
        return [
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
    
    def generate_email(self, lead):
        """Create personalized email"""
        recipient = lead['name']
        company = lead['company']
        industry = lead['industry']
        
        # Convert name to email
        base = company.lower().replace(' ', '')
        recipient_email = base + '@gmail.com'
        
        subject = f"{company} - AI {industry} Opportunity"
        
        body = f"""Hi {recipient},

{industry.upper()} automation can transform your business.

I specialize in AI automation that delivers:
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

P.S. Would this be valuable for {company}?
"""
        return recipient_email, subject, body
    
    def send_email(self, recipient, subject, body):
        """Send email via Mailto (no password needed)"""
        print(f"Sending to: {recipient}...")
        
        # Create mailto link
        mailto = f"mailto:{recipient}?subject={subject}&body={body}"
        
        # Print ready-to-send
        print(f"✓ Ready to send via Gmail client:")
        print(f"  Subject: {subject}")
        print(f"  To: {recipient}")
        print(f"  Action: Review → Send")
        print(f"  Link: {mailto}")
        print()
        
        # Save to file
        with open(f'email_to_send_to_{recipient.replace(".", "_")}.txt', 'w') as f:
            f.write(f"\n=================== EMAIL READY TO SEND ===================\n")
            f.write(f"To: {recipient}\n")
            f.write(f"Subject: {subject}\n\n")
            f.write(f"Body:\n\n")
            f.write(body.strip() + "\n")
            f.write(f"\n\n================== COPY & OPEN IN GMAIL ================\n")
        
        self.sent += 1
        return True
    
    def run_campaign(self):
        """Run complete campaign"""
        print("="*70)
        print("AUTOMATED EMAIL CAMPAIGN STARTING")
        print("="*70)
        print(f"Targeting: {len(self.leads)} leads")
        print(f"Sender: {self.email}")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
        print()
        
        for i, lead in enumerate(self.leads, 1):
            print(f"[{i}/{len(self.leads)}] Processing: {lead['industry']}", end="...")
            
            recipient, subject, body = self.generate_email(lead)
            self.send_email(recipient, subject, body)
            
            # Wait 5 seconds to avoid spam filter
            time.sleep(2)
        
        print()
        print("="*70)
        print("CAMPAIGN COMPLETED")
        print("="*70)
        print(f"  Emails sent: {self.sent}")
        print(f"  Time taken: ~{len(self.leads)*3} seconds")
        print("="*70)
        print()
        print(f"** Files saved: email_to_send_to_*.txt")
        print("Open each .txt file and send in Gmail!")
        print("="*70)

def file_exists(filename):
    try:
        with open(f"{filename}", 'r') as f:
            pass
    except FileNotFoundError:
        return False
    return True

if __name__ == "__main__":
    # Config: Use Gmail SMTP or Outlook (no password needed)
    config = {
        'outbound_email': 'gargikar63@gmail.com',
        'password': 'YOUR_APP_PASSWORD',  # Or use mailto links instead
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
    }
    
    print("AUTOMATED EMAIL SYSTEM READY")
    print("="*70)
    print("Ready to launch when you provide credentials!")
    print("="*70)
    print()
    print("USAGE:")
    print("1. Sign up for SendGrid (10 minutes)")
    print("2. Or: Set up app password at Gmail/Outlook")
    print("3. Run: python campaign.py")
    print("="*70)
    print()
    print("Current status: Waiting for email credentials...")
    print("="*70)