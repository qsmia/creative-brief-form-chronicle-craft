# ChronicleChraft Creative Brief Form

## Overview
A professional, responsive HTML/CSS/JavaScript form designed for collecting detailed creative project requirements from clients. Perfect for LinkedIn ad campaigns and client onboarding.

## Live Website
**Deployed URL:** https://kkh7ikcydxd1.manus.space

## Features

### Form Sections
1. **Client Information** - Contact details and company information
2. **Project Overview** - Project type, description, objectives, and target audience
3. **Creative Direction** - Style preferences, design elements, and inspirations
4. **Content & Deliverables** - Main message, content provided, and expected deliverables
5. **Timeline & Budget** - Project dates and budget range
6. **Approval & Contact** - Communication preferences and contacts
7. **Additional Notes** - Extra details and requirements
8. **Acknowledgement** - Terms confirmation

### Technical Features
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
- **Form Validation** - Real-time validation with visual feedback
- **Character Counters** - For long text fields to guide users
- **Professional Styling** - Modern gradient design with ChronicleChraft branding
- **Email Integration** - Form submissions are sent to irfan@chroniclecraft.tech
- **Confirmation Emails** - Automatic confirmation emails sent to clients

### Email Functionality
- **Primary Email:** All form submissions are sent to `irfan@chroniclecraft.tech`
- **Confirmation Email:** Clients receive automatic confirmation emails
- **HTML Format:** Professional HTML email templates with structured data
- **Complete Data:** All form fields are included in the email with proper formatting

## Form Fields

### Required Fields (*)
- Full Name
- Email Address
- Project Title/Name
- Type of Project
- Project Description
- Key Objectives/Goals
- Target Audience
- Main Message/Core Idea
- Final Deliverables Expected
- Acknowledgement checkbox

### Optional Fields
- Company/Organization Name
- Job Title/Role
- Phone Number
- Website/Social Media Handles
- Preferred Style/Tone
- Design Elements to Use/Avoid
- Inspirations/References
- Content Provided by Client
- File Formats Required
- Project Start/End Dates
- Budget Range
- Contact Preferences
- Additional Notes

## Technical Stack
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Backend:** Python Flask
- **Styling:** Custom CSS with gradient backgrounds and animations
- **Fonts:** Inter font family from Google Fonts
- **Deployment:** Manus hosting platform

## File Structure
```
creative-brief-form/
├── index.html          # Main form page
├── styles.css          # CSS styling
├── script.js           # JavaScript functionality
├── app.py             # Flask backend (local development)
├── src/
│   ├── main.py        # Production Flask app
│   ├── index.html     # Production HTML
│   ├── styles.css     # Production CSS
│   └── script.js      # Production JavaScript
├── requirements.txt    # Python dependencies
└── README.md          # This documentation
```

## Usage Instructions

### For LinkedIn Ad Campaigns
1. Use the deployed URL: https://kkh7ikcydxd1.manus.space
2. Direct potential clients to fill out the form
3. All submissions will be sent to irfan@chroniclecraft.tech
4. Clients receive automatic confirmation emails

### For Your Own Domain (chroniclecraft.tech)
To use this form on your own domain, you have several options:

1. **Redirect/Frame:** Point a subdomain to the deployed URL
2. **Download & Upload:** Download the files and upload to your hosting
3. **Custom Deployment:** Use the source files to deploy on your preferred platform

## Customization Options

### Branding
- Update company name in `index.html`
- Modify colors in `styles.css` (search for color values)
- Change email addresses in the backend configuration

### Form Fields
- Add/remove fields by editing `index.html`
- Update validation in `script.js`
- Modify email template in the backend

### Styling
- Colors: Modify CSS variables for consistent theming
- Fonts: Change font family in CSS
- Layout: Adjust grid and spacing in CSS

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance
- Fast loading with optimized CSS and JavaScript
- Responsive images and efficient animations
- Form validation prevents unnecessary submissions

## Security Features
- Input sanitization and validation
- CSRF protection through Flask
- Secure email handling
- No sensitive data stored locally

## Support
For technical support or customization requests, contact: irfan@chroniclecraft.tech

---

**Created for ChronicleChraft Creative Solutions**  
**Deployment Date:** August 20, 2025  
**Version:** 1.0

