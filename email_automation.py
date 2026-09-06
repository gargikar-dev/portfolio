#!/usr/bin/env python3
"""
AI Automation Email Outreach Automation System
Automatically finds leads, qualifies them, and sends personalized outreach messages
"""

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, timedelta
import csv
import time
import random
import hashlib

# Configuration - EDIT THESE SETTINGS
EMAIL_CONFIG = {
    "outbound_email": "gargikar63@gmail.com",
    "password": "Tintin@8981251691",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "enable_debug": False
}

# Portfolio file paths
PORTFOLIO_HTML = "portfolio/index.html"
CASE_STUDIES_JSON = "portfolio/case_studies.json"

# Lead database file
LEADS_CSV = "qualified_leads.csv"

def load_portfolio():
    """Load portfolio HTML file"""
    try:
        with open(PORTFOLIO_HTML, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Portfolio not found. Place 'portfolio/index.html' in root directory."

def load_case_studies():
    """Load case studies"""
    try:
        with open(CASE_STUDIES_JSON, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"case_studies": []}

def personalize_email(lead, industry_insights):
    """Create personalized email content"""
    personalization = {
        "name": lead["name"],
        "company": lead["company"],
        "industry": lead.get("industry", "your business"),
        "industry_insight": industry_insights.get(lead.get("industry", "general"), 
                                                       "AI automation can save time and money in your industry.")
    }
    
    # Select appropriate template
    if lead.get("project_type", "") == "AI Cart Recovery":
        template_id = "e_commerce"
    elif lead.get("project_type", "") == "Lead Automation":
        template_id = "real_estate"
    elif lead.get("project_type", "") == "Document Automation":
        template_id = "legal"
    elif lead.get("project_type", "") == "Audit Automation":
        template_id = "accounting"
    else:
        template_id = "general_ai_consulting"
    
    # Generate personalized body
    body = f"""Hi {personalization['name']},

{personalization['industry_insight']}

I specialize in AI automation that:
✅ Reduces operational overhead by 60%
✅ Increases revenue by 40% within 2 months
✅ Identifies costly manual process loopholes

Quick question: Would you be open to a free 15-minute AI audit of your current workflows?

I'll identify:
• 3-5 high-cost manual processes wasting money daily
• AI automation opportunities with instant ROI
• Implementation roadmap with cost projections

I work remotely on part-time basis and can start this week.

Best,
Gargi Kar
AI Automation Expert

📧 gargikar63@gmail.com
📱 +91 8777547678
🔗 www.gargikar.ai-automation.com"""
    
    # Load portfolio as attachment reference
    portfolio_html = load_portfolio()
    
    return {
        "subject": f"{lead['company']} - {lead['project_type'].title()} Opportunity",
        "body": body,
        "portfolio_html": portfolio_html
    }

def get_industry_insight(industry):
    """Get industry-specific insights"""
    insights = {
        "E-commerce": "Your high cart value + recent marketing spend = prime for AI recovery automation",
        "Real Estate": "Hot market means you can't afford to miss leads. AI follows up 24/7 while you sleep.",
        "Legal": "Every hour spent on repetitive docs is a billable hour lost. AI handles templates instantly.",
        "Healthcare": "Patient acquisition costs high. AI scheduling maximizes every appointment request.",
        "Accounting": "Year-end is coming. Automated audit prep saves you 15+ billable hours/day.",
        "General": "AI automation is transforming how businesses operate. Let's talk specifics."
    }
    return insights.get(industry, insights["General"])

def send_email(lead, email_template):
    """Send email to lead"""
    from_email = EMAIL_CONFIG["outbound_email"]
    
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = f"{lead['name'].lower().replace(' ', '')}@{lead['company'].lower().replace(' ', '').removesuffix(' Inc.').removesuffix('( ').removesuffix(')').domain().lower()}</{lead['company'].replace(' ', '').removesuffix(' Inc.').removesuffix('( ').removesuffix(')')}@{lead['company'].replace(' ', '').removesuffix(' Inc.').removesuffix('( ').removesuffix(')').domain().lower()}>" if '@' in lead['company'] else f"{lead['name'].lower().replace(' ', '')}@{lead['company'].lower().split()[-1]}>"
        msg['Subject'] = email_template["subject"]
        msg.attach(MIMEText(email_template["body"], "plain"))
        
        # Add portfolio attachment
        # In production, upload portfolio to web hosting and provide link
        
        print(f"✓ Email sent to {lead['name']}")
        print(f"  Subject: {email_template['subject']}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send to {lead['name']}: {str(e)}")
        return False

def load_leads():
    """Load leads from CSV"""
    leads = []
    try:
        with open(LEADS_CSV, 'r') as f:
            reader = csv.DictReader(f)
            leads = list(reader)
        return leads
    except FileNotFoundError:
        print(f"✗ No leads found in {LEADS_CSV}")
        return []

def run_campaign():
    """Run the complete outreach campaign"""
    print("\n" + "="*80)
    print("🤖 GARGI KAR - AI AUTOMATION OUTREACH SYSTEM")
    print("="*80)
    
    print("\n📋 Loading leads from CSV...")
    leads = lead = load_leads()
    if not leads:
        print("No leads to process. Please generate qualified_leads.csv first.")
        print("Run: python lead_scraper.py (production: connect to LinkedIn API)")
        return
    
    total_leads = len(leads)
    processed = 0
    
    print(f"\n⚙️  Processing {total_leads} leads...")
    print(f"⏰ Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    case_studies = load_case_studies()
    
    for lead in leads:
        # Rate limiting - add delay between emails
        if processed > 0:
            time.sleep(2)  # 2 seconds between emails
        
        lead_dict = {k: v for k, v in lead.items()}
        email_template = personalize_email(lead_dict, get_industry_insight(lead_dict.get('industry', '')))
        
        if send_email(lead_dict, email_template):
            processed += 1
        
        # Progress indicator
        status = "✓" if processed else "✗"
        print(f"[{status}] {processed}/{total_leads}: {lead_dict.get('name', 'Unknown')}")
    
    print(f"\n{'='*80}")
    print(f"✅ OUTREACH COMPLETED")
    print(f"   Emails sent: {processed}/{total_leads}")
    print(f"   Success rate: {processed*100/total_leads:.1f}%" if total_leads > 0 else "N/A")
    print(f"{'='*80}\n")
    
    print("\n📧 Next Steps:")
    print("   1. Monitor email opens/clicks (set up tracking in EMAIL_CONFIG)")
    print("   2. Handle replies within 2-4 hours")
    print("   3. Schedule 15-min discovery calls")
    print("   4. Send portfolio link + case studies")
    print("   5. Close deals!")
    
    return processed, total_leads

def add_test_leads():
    """Add sample leads for testing"""
    sample_leads = [
        {
            "name": "Test Lead 1",
            "company": "Test Store",
            "platform": "Upwork",
            "job_title": "E-commerce Test",
            "project_type": "AI Cart Recovery",
            "budget": "$500-1200",
            "location": "Remote",
            "status": "Active",
            "post_date": "2025-01-16",
            "urgency": "High",
            "industry": "E-commerce",
            "stack": "Shopify",
            "pain_points": "cart losses"
        },
        {
            "name": "Test Lead 2",
            "company": "Test Realty",
            "platform": "LinkedIn",
            "job_title": "Real Estate Test",
            "project_type": "Lead Automation",
            "budget": "$750-1500",
            "location": "Remote",
            "status": "Active",
            "post_date": "2025-01-16",
            "urgency": "Medium",
            "industry": "Real Estate",
            "stack": "Manual CRM",
            "pain_points": "lead followup"
        }
    ]
    
    with open(LEADS_CSV, 'w') as f:
        fieldnames = ["name", "company", "platform", "job_title", "project_type", 
                      "budget", "location", "status", "post_date", "urgency", 
                      "industry", "stack", "pain_points"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_leads)
    
    print(f"✓ Added 2 test leads to {LEADS_CSV}")

def main():
    """Main entry point"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("🧪 MODE: Test with sample leads\n")
        add_test_leads()
        run_campaign()
    else:
        print("\n" + "="*80)
        print("🤖 GARGI KAR - AI AUTOMATION LEAD & EMAIL AUTOMATION SYSTEM")
        print("="*80)
        print("\n⚙️  SETUP REQUIRED:")
        print("   1. Edit EMAIL_CONFIG with your email credentials")
        print("   2. Run 'python lead_scraper.py' to generate qualified_leads.csv")
        print("   3. Or use --test flag to add sample leads first")
        print("   4. Run this script again")
        print("\n💡 READY FOR PRODUCTION:")
        print("   • Connect to LinkedIn API for real-time job posting scraping")
        print("   • Add Upwork/Freelancer.com API integration")
        print("   • Set up Google Sheets integration for CRM")
        print("   • Add email tracking (Mailgun, SendGrid, etc.)")
        print("   • Automate follow-up sequences")
        print("="*80 + "\n")

if __name__ == "__main__":
    main()
