from flask import Flask, render_template_string, request, jsonify, send_from_directory
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
TO_EMAIL = 'irfan@chroniclecraft.tech'
FROM_EMAIL = 'noreply@chroniclecraft.tech'
SUBJECT_PREFIX = 'New Creative Brief Submission - '

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css', mimetype='text/css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js', mimetype='application/javascript')

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
            return jsonify({'success': False, 'message': '; '.join(errors)})
        
        # Collect form data
        form_data = {}
        all_fields = {
            'fullName': 'Full Name',
            'companyName': 'Company/Organization Name',
            'jobTitle': 'Job Title/Role',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'website': 'Website / Social Media Handles',
            'projectTitle': 'Project Title',
            'projectType': 'Type of Project',
            'projectDescription': 'Project Description',
            'keyObjectives': 'Key Objectives',
            'targetAudience': 'Target Audience',
            'preferredStyle': 'Preferred Style/Tone',
            'designElements': 'Design Elements to Use',
            'avoidElements': 'Design Elements to Avoid',
            'inspirations': 'Inspirations/References',
            'mainMessage': 'Main Message',
            'contentProvided': 'Content Provided by Client',
            'deliverables': 'Final Deliverables Expected',
            'fileFormats': 'File Formats Required',
            'startDate': 'Ideal Start Date',
            'deadline': 'Ideal Completion Date',
            'budget': 'Budget Range',
            'primaryContact': 'Primary Contact Person',
            'communicationMethod': 'Preferred Communication Method',
            'secondaryContact': 'Secondary Contact',
            'additionalNotes': 'Additional Notes'
        }
        
        for field in all_fields:
            form_data[field] = request.form.get(field, '').strip()
        
        # Create email content
        email_subject = SUBJECT_PREFIX + form_data['projectTitle']
        
        # Create HTML email body
        email_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset='UTF-8'>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; }}
                .section {{ margin-bottom: 30px; }}
                .section h3 {{ color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px; }}
                .field {{ margin-bottom: 15px; }}
                .field-label {{ font-weight: bold; color: #555; }}
                .field-value {{ margin-top: 5px; padding: 10px; background: #f8f9fa; border-left: 3px solid #667eea; }}
                .footer {{ background: #f1f1f1; padding: 15px; text-align: center; font-size: 12px; color: #666; }}
            </style>
        </head>
        <body>
            <div class='header'>
                <h1>New Creative Brief Submission</h1>
                <p>ChronicleChraft Creative Solutions</p>
            </div>
            
            <div class='content'>
                <div class='section'>
                    <h3>Client Information</h3>
        """
        
        # Add client information
        client_fields = ['fullName', 'companyName', 'jobTitle', 'email', 'phone', 'website']
        for field in client_fields:
            if form_data[field]:
                email_body += f"""
                    <div class='field'>
                        <div class='field-label'>{all_fields[field]}:</div>
                        <div class='field-value'>{form_data[field]}</div>
                    </div>"""
        
        # Add project overview
        email_body += """
                </div>
                <div class='section'>
                    <h3>Project Overview</h3>"""
        
        project_fields = ['projectTitle', 'projectType', 'projectDescription', 'keyObjectives', 'targetAudience']
        for field in project_fields:
            if form_data[field]:
                newline_to_br = '\n'
                value = form_data[field].replace(newline_to_br, '<br>')
                email_body += f"""
                    <div class='field'>
                        <div class='field-label'>{all_fields[field]}:</div>
                        <div class='field-value'>{value}</div>
                    </div>"""
        
        # Add other sections similarly
        sections = [
            ('Creative Direction', ['preferredStyle', 'designElements', 'avoidElements', 'inspirations']),
            ('Content & Deliverables', ['mainMessage', 'contentProvided', 'deliverables', 'fileFormats']),
            ('Timeline & Budget', ['startDate', 'deadline', 'budget']),
            ('Contact & Communication', ['primaryContact', 'communicationMethod', 'secondaryContact'])
        ]
        
        for section_name, fields in sections:
            email_body += f"""
                </div>
                <div class='section'>
                    <h3>{section_name}</h3>"""
            
            for field in fields:
                if form_data[field]:
                    newline_to_br = '\n'
                    value = form_data[field].replace(newline_to_br, '<br>')
                    email_body += f"""
                        <div class='field'>
                            <div class='field-label'>{all_fields[field]}:</div>
                            <div class='field-value'>{value}</div>
                        </div>"""
        
        # Add additional notes if present
        if form_data['additionalNotes']:
            email_body += f"""
                </div>
                <div class='section'>
                    <h3>Additional Notes</h3>
                    <div class='field'>
                        <div class='field-value'>{form_data['additionalNotes'].replace(chr(10), '<br>')}</div>
                    </div>"""
        
        # Close email body
        email_body += f"""
                </div>
            </div>
            
            <div class='footer'>
                <p>This creative brief was submitted on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
                <p>Submitted from: {request.remote_addr}</p>
                <p>ChronicleChraft Creative Solutions - www.chroniclecraft.tech</p>
            </div>
        </body>
        </html>"""
        
        # For now, we'll just log the submission since we don't have SMTP configured
        print(f"Form submission received from {form_data['email']}")
        print(f"Project: {form_data['projectTitle']}")
        print("Email would be sent to:", TO_EMAIL)
        
        # Send confirmation email content (would be sent in production)
        client_body = f"""
        Dear {form_data['fullName']},
        
        Thank you for submitting your creative brief for {form_data['projectTitle']}.
        
        We have received your detailed requirements and our team will review them carefully. 
        We will get back to you within 24-48 hours to discuss your project further.
        
        If you have any urgent questions, please contact us at irfan@chroniclecraft.tech.
        
        Best regards,
        The ChronicleChraft Team
        """
        
        print("Confirmation email content:", client_body)
        
        return jsonify({'success': True, 'message': 'Creative brief submitted successfully!'})
        
    except Exception as e:
        print(f"Error processing form: {str(e)}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

