import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key-change-in-production')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Email Configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
FROM_EMAIL = os.getenv('FROM_EMAIL', 'noreply@chroniclecraft.tech')
TO_EMAIL = os.getenv('TO_EMAIL', 'irfan@chroniclecraft.tech')
WEBSITE_URL = os.getenv('WEBSITE_URL', 'https://chroniclecraft.tech')

@app.route('/')
def index():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir, 'index.html'), 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error serving index page: {str(e)}")
        return "Application error", 500

@app.route('/styles.css')
def styles():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return send_from_directory(current_dir, 'styles.css', mimetype='text/css')
    except Exception as e:
        logger.error(f"Error serving CSS: {str(e)}")
        return "CSS not found", 404

@app.route('/script.js')
def script():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return send_from_directory(current_dir, 'script.js', mimetype='application/javascript')
    except Exception as e:
        logger.error(f"Error serving JS: {str(e)}")
        return "JS not found", 404

def send_email(to_email, subject, html_body, is_client_email=False):
    """Send email using SMTP configuration"""
    if not all([SMTP_USERNAME, SMTP_PASSWORD]):
        logger.warning("SMTP credentials not configured. Email not sent.")
        return False
    
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        
        # Create HTML part
        html_part = MIMEText(html_body, 'html')
        msg.attach(html_part)
        
        # Connect and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            
        logger.info(f"Email sent successfully to {to_email}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {str(e)}")
        return False

def create_admin_email_body(form_data):
    """Create HTML email body for admin notification"""
    email_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='UTF-8'>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
            .header {{ background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 30px; text-align: center; }}
            .header h1 {{ margin: 0; font-size: 28px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; }}
            .content {{ padding: 30px; max-width: 800px; margin: 0 auto; }}
            .section {{ margin-bottom: 30px; }}
            .section h3 {{ color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 8px; margin-bottom: 15px; }}
            .field {{ margin-bottom: 15px; }}
            .field-label {{ font-weight: bold; color: #555; margin-bottom: 5px; }}
            .field-value {{ 
                padding: 12px; 
                background: #f8f9fa; 
                border-left: 4px solid #667eea; 
                border-radius: 0 4px 4px 0;
                word-wrap: break-word;
            }}
            .footer {{ 
                background: #f1f1f1; 
                padding: 20px; 
                text-align: center; 
                font-size: 14px; 
                color: #666; 
                margin-top: 30px;
            }}
            .priority {{ background: #fff3cd; border-left-color: #ffc107; }}
            .highlight {{ background: #e8f4fd; border-left-color: #2196f3; }}
        </style>
    </head>
    <body>
        <div class='header'>
            <h1>New Creative Brief Submission</h1>
            <p>ChronicleChraft Creative Solutions</p>
        </div>
        
        <div class='content'>
    """
    
    # Field mappings with sections
    sections = [
        ("Client Information", {
            'fullName': 'Full Name',
            'companyName': 'Company/Organization Name',
            'jobTitle': 'Job Title/Role',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'website': 'Website / Social Media Handles'
        }),
        ("Project Overview", {
            'projectTitle': 'Project Title',
            'projectType': 'Type of Project',
            'projectDescription': 'Project Description',
            'keyObjectives': 'Key Objectives',
            'targetAudience': 'Target Audience'
        }),
        ("Creative Direction", {
            'preferredStyle': 'Preferred Style/Tone',
            'designElements': 'Design Elements to Use',
            'avoidElements': 'Design Elements to Avoid',
            'inspirations': 'Inspirations/References'
        }),
        ("Content & Deliverables", {
            'mainMessage': 'Main Message',
            'contentProvided': 'Content Provided by Client',
            'deliverables': 'Final Deliverables Expected',
            'fileFormats': 'File Formats Required'
        }),
        ("Timeline & Budget", {
            'startDate': 'Ideal Start Date',
            'deadline': 'Ideal Completion Date',
            'budget': 'Budget Range'
        }),
        ("Contact & Communication", {
            'primaryContact': 'Primary Contact Person',
            'communicationMethod': 'Preferred Communication Method',
            'secondaryContact': 'Secondary Contact'
        })
    ]
    
    # Add each section
    for section_name, fields in sections:
        email_body += f"""
            <div class='section'>
                <h3>{section_name}</h3>
        """
        
        for field_key, field_label in fields.items():
            if form_data.get(field_key):
                value = form_data[field_key].replace('\n', '<br>')
                css_class = 'highlight' if field_key in ['projectTitle', 'email', 'deliverables'] else ''
                email_body += f"""
                    <div class='field'>
                        <div class='field-label'>{field_label}:</div>
                        <div class='field-value {css_class}'>{value}</div>
                    </div>
                """
        
        email_body += "</div>"
    
    # Add additional notes if present
    if form_data.get('additionalNotes'):
        additional_notes = form_data['additionalNotes'].replace('\n', '<br>')
        email_body += f"""
            <div class='section'>
                <h3>Additional Notes</h3>
                <div class='field'>
                    <div class='field-value priority'>{additional_notes}</div>
                </div>
            </div>
        """
    
    # Close email body
    email_body += f"""
        </div>
        
        <div class='footer'>
            <p><strong>Submission Details:</strong></p>
            <p>Submitted on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
            <p>From IP: {request.remote_addr if request else 'Unknown'}</p>
            <p>ChronicleChraft Creative Solutions | {WEBSITE_URL}</p>
        </div>
    </body>
    </html>
    """
    
    return email_body

def create_client_confirmation_email(form_data):
    """Create HTML confirmation email for the client"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='UTF-8'>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; }}
            .content {{ padding: 30px; max-width: 600px; margin: 0 auto; }}
            .highlight {{ background: #f0f8ff; padding: 15px; border-radius: 8px; border-left: 4px solid #667eea; }}
            .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #666; }}
            .button {{ 
                display: inline-block; 
                padding: 12px 24px; 
                background: #667eea; 
                color: white; 
                text-decoration: none; 
                border-radius: 6px; 
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class='header'>
            <h1>Thank You!</h1>
            <p>Your Creative Brief Has Been Received</p>
        </div>
        
        <div class='content'>
            <p>Dear {form_data.get('fullName', 'Valued Client')},</p>
            
            <p>Thank you for submitting your creative brief for <strong>"{form_data.get('projectTitle', 'your project')}"</strong>.</p>
            
            <div class='highlight'>
                <h3>What happens next?</h3>
                <ul>
                    <li>Our team will review your detailed requirements within 24-48 hours</li>
                    <li>We'll prepare a customized proposal based on your specifications</li>
                    <li>You'll receive a follow-up email with project timeline and next steps</li>
                </ul>
            </div>
            
            <p>We're excited to work with you on this project and bring your vision to life!</p>
            
            <p>If you have any urgent questions or need to add additional information, please don't hesitate to contact us:</p>
            
            <ul>
                <li><strong>Email:</strong> {TO_EMAIL}</li>
                <li><strong>Website:</strong> <a href="{WEBSITE_URL}">{WEBSITE_URL}</a></li>
            </ul>
            
            <a href="{WEBSITE_URL}" class="button">Visit Our Website</a>
            
            <p>Best regards,<br>
            <strong>The ChronicleChraft Team</strong><br>
            Creative Solutions</p>
        </div>
        
        <div class='footer'>
            <p>This email was sent in response to your creative brief submission on {datetime.now().strftime('%B %d, %Y')}</p>
            <p>ChronicleChraft Creative Solutions | {WEBSITE_URL}</p>
        </div>
    </body>
    </html>
    """

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Required fields validation
        required_fields = {
            'fullName': 'Full Name',
            'email': 'Email Address',
            'projectTitle': 'Project Title',
            'projectType': 'Project Type',
            'projectDescription': 'Project Description',
            'keyObjectives': 'Key Objectives',
            'targetAudience': 'Target Audience',
            'mainMessage': 'Main Message',
            'deliverables': 'Deliverables'
        }
        
        # Check required fields
        errors = []
        for field, label in required_fields.items():
            if not request.form.get(field, '').strip():
                errors.append(f"{label} is required")
        
        # Check acknowledgement
        if not request.form.get('acknowledgement'):
            errors.append('You must acknowledge the terms to submit the form')
        
        if errors:
            logger.warning(f"Form validation errors: {'; '.join(errors)}")
            return jsonify({'success': False, 'message': '; '.join(errors)})
        
        # Collect form data
        form_data = {}
        all_fields = [
            'fullName', 'companyName', 'jobTitle', 'email', 'phone', 'website',
            'projectTitle', 'projectType', 'projectDescription', 'keyObjectives', 'targetAudience',
            'preferredStyle', 'designElements', 'avoidElements', 'inspirations',
            'mainMessage', 'contentProvided', 'deliverables', 'fileFormats',
            'startDate', 'deadline', 'budget',
            'primaryContact', 'communicationMethod', 'secondaryContact',
            'additionalNotes'
        ]
        
        for field in all_fields:
            form_data[field] = request.form.get(field, '').strip()
        
        # Log submission
        logger.info(f"New form submission from {form_data['email']} for project: {form_data['projectTitle']}")
        
        # Send admin notification email
        admin_subject = f"New Creative Brief Submission - {form_data['projectTitle']}"
        admin_body = create_admin_email_body(form_data)
        admin_sent = send_email(TO_EMAIL, admin_subject, admin_body)
        
        # Send client confirmation email
        client_subject = f"Creative Brief Received - {form_data['projectTitle']}"
        client_body = create_client_confirmation_email(form_data)
        client_sent = send_email(form_data['email'], client_subject, client_body, is_client_email=True)
        
        # Response message based on email sending success
        if admin_sent and client_sent:
            message = 'Creative brief submitted successfully! You should receive a confirmation email shortly.'
        elif admin_sent:
            message = 'Creative brief submitted successfully! There was an issue sending the confirmation email, but we have received your submission.'
        else:
            message = 'Creative brief submitted successfully! We have received your submission and will contact you soon.'
        
        return jsonify({'success': True, 'message': message})
        
    except Exception as e:
        logger.error(f"Error processing form submission: {str(e)}")
        return jsonify({
            'success': False, 
            'message': 'An error occurred while processing your submission. Please try again or contact us directly.'
        })

@app.route('/health')
def health_check():
    """Health check endpoint for deployment platforms"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'smtp_configured': bool(SMTP_USERNAME and SMTP_PASSWORD)
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
