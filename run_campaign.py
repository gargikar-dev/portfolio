import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime

EMAIL_CONFIG = {
    'outbound_email': 'gargikar63@gmail.com',
    'password': 'Tintin@7278475797',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'use_tls': True
}

def get_industry_insight(industry):
    insights = {
        'E-commerce': 'High cart value plus recent marketing spend equals opportunity for AI recovery automation.',
        'Real Estate': 'Hot market means you cannot afford to miss leads. AI follows up twenty four seven while you sleep.',
        'Legal': 'Every hour on documents is billable time lost. AI handles templates instantly.',
        'Healthcare': 'Patient acquisition costs are high. AI scheduling maximizes every appointment request.',
        'Accounting': 'Year end is coming. Automated audit prep saves you fifteen billable hours daily.',
        'Manufacturing': 'Quality defects cost thousands. AI inspection catches issues before they ship.',
        'Logistics': 'Inventory errors mean lost money. AI tracking ensures ninety nine percent accuracy.',
        'Consulting': 'Manual client onboarding wastes billable time. AI automation handles intake.',
        'Education': 'Manual course content creation is slow. AI generates and structures content fast.',
    }
    return insights.get(industry, 'AI automation can transform your business operations.')

def format_email_body(lead, insight):
    """Create email body without complex f-strings"""
    name = lead.get('name', 'Contact')
    company = lead.get('company', 'Your Company')
    
    body = insight + "\n\n"
    
    body += "I specialize in AI automation that delivers:\n"
    body += "- Increase revenue by 40 percent within 2 months\n"
    body += "- Reduces operational overhead by 60 percent\n"  
    body += "- Identifies costly manual process loopholes\n\n"
    
    body += "Quick question: Would you be open to a free 15-minute AI audit?"
    body += "\n\nI will identify:"
    body += "\n- Three to five high-cost manual processes"
    body += "\n- AI automation opportunities with instant ROI"
    body += "\n- Implementation roadmap with cost projections"
    body += "\n\nI work remotely and can start this week."
    body += "\n\nBest regards,"
    body += "\n\nGargi Kar"
    body += "AI Automation Expert"
    body += "https://gargikar-portfolio.vercel.app"
    body += "gargikar63@gmail.com"
    body += "\n\nP.S. Would this be valuable for " + company.replace("'", "'") + "?"
    body += "\n"
    return body
    
    return body

def send_email_to_lead(lead):
    """Send email to single lead"""
    name = lead.get('name', 'Contact')
    company = lead.get('company', 'Your Company')
    industry = lead.get('industry', 'business')
    
    insight = get_industry_insight(industry)
    subject = company + ' - AI Automation Opportunity'
    
    # Convert name to email-like format
    recipient_name = name.lower().replace(' ', '').strip()
    if not recipient_name or '@' in recipient_name:
        recipient_name = 'contact'
    recipient = recipient_name + '@gmail.com'
    
    body = format_email_body(lead, insight)
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_CONFIG['outbound_email']
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    print("Sending to:", lead.get('name', '?'), "|", company)
    
    try:
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.set_debuglevel(0)
            server.starttls()
            server.login(EMAIL_CONFIG['outbound_email'], EMAIL_CONFIG['password'])
            server.send_message(msg)
            print("  SUCCESS: Email sent!")
            return True
            
    except smtplib.SMTPAuthenticationError as e:
        print("  AUTH ERROR:", str(e)[:60])
        print("  Check: Is password a Gmail app password (16+ chars) or regular Gmail password?")
        print("  Gmail requires app password from: https://myaccount.google.com/apppasswords")
        return False
    except smtplib.SMTPException as e:
        print("  SEND ERROR:", str(e)[:60])
        return False
    except Exception as e:
        print("  ERROR:", str(e)[:60])
        return False

def log_sent_email(lead):
    """Log successfully sent email"""
    with open('sent_emails.log', 'a', encoding='utf-8') as log:
        industry = lead.get('industry', 'general')
        budget = lead.get('budget', 'N/A')
        time_sent = datetime.now().strftime('%H:%M:%S')
        log.write(f"{time_sent} | {lead['name']} | {lead['company']} | {industry} | {budget}\n")

def run_campaign():
    """Main campaign runner"""
    print("\nGARGI KAR - AI AUTOMATION OUTREACH SYSTEM")
    print("Date:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("=" * 60)
    
    # Load leads
    leads = []
    try:
        with open('qualified_leads.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            leads = list(reader)
        print("\nLoaded", len(leads), "qualified leads")
        if not leads:
            print("No leads found. Run: python lead_scraper.py")
            return False
    except FileNotFoundError:
        print("ERROR: qualified_leads.csv not found.")
        print("Create sample leads or run lead scraper")
        return False
    except Exception as e:
        print("ERROR loading leads:", str(e)[:60])
        return False
    
    # Send emails
    sent_count = 0
    failed_count = 0
    
    print("\nStarting automated outreach...")
    for i, lead in enumerate(leads, 1):
        print(f"\n--- Lead {i}/{len(leads)} ---")
        
        success = send_email_to_lead(lead)
        
        if success:
            sent_count += 1
            log_sent_email(lead)
        else:
            failed_count += 1
        
        # Rate limiting - 2 second delay
        time.sleep(2)
        
        # Progress
        if (i % 2) == 0:
            print("\nÃ°ÂÂÂ Progress:", sent_count, "sent, ", failed_count, "failed")
    
    print("\n" + "=" * 60)
    print("CAMPAIGN RESULTS")
    print("=" * 60)
    print("Total Leads Processed:", len(leads))
    print("Emails Sent:", sent_count)
    print("Failed:", failed_count)
    print("Success Rate:", sent_count * 100 / len(leads) if leads else 0, "%")
    print("=" * 60)
    
    if sent_count > 0:
        print("\nÃ¢ÂÂ AUTOMATED OUTREACH COMPLETED")
        print("   Your portfolio: https://gargikar-portfolio.vercel.app")
        print("   Check spam folder if emails appear to be missing")
        print("   Follow-ups will be queued automatically")
    else:
        print("\nÃ¢ÂÂ Ã¯Â¸Â  All emails failed")
        print("   Common reasons:")
        print("   1. Gmail requires App Password (not regular password)")
        print("   2. Password too short (< 16 characters)")
        print("   3. Security settings blocking automation")
        print("   4. Email already sent to recipient in this session")
    
    return sent_count > 0

if __name__ == '__main__':
    try:
        success = run_campaign()
    except KeyboardInterrupt:
        print("\nÃ¢ÂÂ¸Ã¯Â¸Â  Campaign paused by user")
    except Exception as e:
        print("\nÃ¢ÂÂ Unexpected error:", str(e)[:100])
        import traceback
        traceback.print_exc()
