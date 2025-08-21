<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Configuration
$to_email = 'irfan@chroniclecraft.tech';
$from_email = 'noreply@chroniclecraft.tech';
$subject_prefix = 'New Creative Brief Submission - ';

// Check if request is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

// Sanitize and validate input
function sanitize_input($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

function validate_email($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

// Required fields
$required_fields = [
    'fullName' => 'Full Name',
    'email' => 'Email Address',
    'projectTitle' => 'Project Title',
    'projectType' => 'Project Type',
    'projectDescription' => 'Project Description',
    'keyObjectives' => 'Key Objectives',
    'targetAudience' => 'Target Audience',
    'mainMessage' => 'Main Message',
    'deliverables' => 'Deliverables'
];

// Validate required fields
$errors = [];
foreach ($required_fields as $field => $label) {
    if (empty($_POST[$field])) {
        $errors[] = "$label is required";
    }
}

// Validate email
if (!empty($_POST['email']) && !validate_email($_POST['email'])) {
    $errors[] = 'Please provide a valid email address';
}

// Check for acknowledgement
if (empty($_POST['acknowledgement'])) {
    $errors[] = 'You must acknowledge the terms to submit the form';
}

if (!empty($errors)) {
    echo json_encode(['success' => false, 'message' => implode(', ', $errors)]);
    exit;
}

// Collect and sanitize form data
$form_data = [];
$all_fields = [
    'fullName' => 'Full Name',
    'companyName' => 'Company/Organization Name',
    'jobTitle' => 'Job Title/Role',
    'email' => 'Email Address',
    'phone' => 'Phone Number',
    'website' => 'Website / Social Media Handles',
    'projectTitle' => 'Project Title',
    'projectType' => 'Type of Project',
    'projectDescription' => 'Project Description',
    'keyObjectives' => 'Key Objectives',
    'targetAudience' => 'Target Audience',
    'preferredStyle' => 'Preferred Style/Tone',
    'designElements' => 'Design Elements to Use',
    'avoidElements' => 'Design Elements to Avoid',
    'inspirations' => 'Inspirations/References',
    'mainMessage' => 'Main Message',
    'contentProvided' => 'Content Provided by Client',
    'deliverables' => 'Final Deliverables Expected',
    'fileFormats' => 'File Formats Required',
    'startDate' => 'Ideal Start Date',
    'deadline' => 'Ideal Completion Date',
    'budget' => 'Budget Range',
    'primaryContact' => 'Primary Contact Person',
    'communicationMethod' => 'Preferred Communication Method',
    'secondaryContact' => 'Secondary Contact',
    'additionalNotes' => 'Additional Notes'
];

foreach ($all_fields as $field => $label) {
    $form_data[$field] = sanitize_input($_POST[$field] ?? '');
}

// Create email content
$email_subject = $subject_prefix . $form_data['projectTitle'];

$email_body = "
<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .header { background: #2c3e50; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .section { margin-bottom: 30px; }
        .section h3 { color: #2c3e50; border-bottom: 2px solid #667eea; padding-bottom: 5px; }
        .field { margin-bottom: 15px; }
        .field-label { font-weight: bold; color: #555; }
        .field-value { margin-top: 5px; padding: 10px; background: #f8f9fa; border-left: 3px solid #667eea; }
        .footer { background: #f1f1f1; padding: 15px; text-align: center; font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <div class='header'>
        <h1>New Creative Brief Submission</h1>
        <p>ChronicleChraft Creative Solutions</p>
    </div>
    
    <div class='content'>
        <div class='section'>
            <h3>Client Information</h3>";

$client_fields = ['fullName', 'companyName', 'jobTitle', 'email', 'phone', 'website'];
foreach ($client_fields as $field) {
    if (!empty($form_data[$field])) {
        $email_body .= "
            <div class='field'>
                <div class='field-label'>{$all_fields[$field]}:</div>
                <div class='field-value'>{$form_data[$field]}</div>
            </div>";
    }
}

$email_body .= "
        </div>
        
        <div class='section'>
            <h3>Project Overview</h3>";

$project_fields = ['projectTitle', 'projectType', 'projectDescription', 'keyObjectives', 'targetAudience'];
foreach ($project_fields as $field) {
    if (!empty($form_data[$field])) {
        $email_body .= "
            <div class='field'>
                <div class='field-label'>{$all_fields[$field]}:</div>
                <div class='field-value'>" . nl2br($form_data[$field]) . "</div>
            </div>";
    }
}

$email_body .= "
        </div>
        
        <div class='section'>
            <h3>Creative Direction</h3>";

$creative_fields = ['preferredStyle', 'designElements', 'avoidElements', 'inspirations'];
foreach ($creative_fields as $field) {
    if (!empty($form_data[$field])) {
        $email_body .= "
            <div class='field'>
                <div class='field-label'>{$all_fields[$field]}:</div>
                <div class='field-value'>" . nl2br($form_data[$field]) . "</div>
            </div>";
    }
}

$email_body .= "
        </div>
        
        <div class='section'>
            <h3>Content & Deliverables</h3>";

$content_fields = ['mainMessage', 'contentProvided', 'deliverables', 'fileFormats'];
foreach ($content_fields as $field) {
    if (!empty($form_data[$field])) {
        $email_body .= "
            <div class='field'>
                <div class='field-label'>{$all_fields[$field]}:</div>
                <div class='field-value'>" . nl2br($form_data[$field]) . "</div>
            </div>";
    }
}

$email_body .= "
        </div>
        
        <div class='section'>
            <h3>Timeline & Budget</h3>";

$timeline_fields = ['startDate', 'deadline', 'budget'];
foreach ($timeline_fields as $field) {
    if (!empty($form_data[$field])) {
        $email_body .= "
            <div class='field'>
                <div class='field-label'>{$all_fields[$field]}:</div>
                <div class='field-value'>{$form_data[$field]}</div>
            </div>";
    }
}

$email_body .= "
        </div>
        
        <div class='section'>
            <h3>Contact & Communication</h3>";

$contact_fields = ['primaryContact', 'communicationMethod', 'secondaryContact'];
foreach ($contact_fields as $field) {
    if (!empty($form_data[$field])) {
        $email_body .= "
            <div class='field'>
                <div class='field-label'>{$all_fields[$field]}:</div>
                <div class='field-value'>{$form_data[$field]}</div>
            </div>";
    }
}

if (!empty($form_data['additionalNotes'])) {
    $email_body .= "
        </div>
        
        <div class='section'>
            <h3>Additional Notes</h3>
            <div class='field'>
                <div class='field-value'>" . nl2br($form_data['additionalNotes']) . "</div>
            </div>";
}

$email_body .= "
        </div>
    </div>
    
    <div class='footer'>
        <p>This creative brief was submitted on " . date('F j, Y \a\t g:i A T') . "</p>
        <p>Submitted from: {$_SERVER['REMOTE_ADDR']}</p>
        <p>ChronicleChraft Creative Solutions - www.chroniclecraft.tech</p>
    </div>
</body>
</html>";

// Email headers
$headers = [
    'MIME-Version: 1.0',
    'Content-type: text/html; charset=UTF-8',
    'From: ' . $from_email,
    'Reply-To: ' . $form_data['email'],
    'X-Mailer: PHP/' . phpversion()
];

// Send email
$mail_sent = mail($to_email, $email_subject, $email_body, implode("\r\n", $headers));

if ($mail_sent) {
    // Send confirmation email to client
    $client_subject = 'Thank you for your Creative Brief submission - ChronicleChraft';
    $client_body = "
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='UTF-8'>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
            .header { background: #2c3e50; color: white; padding: 20px; text-align: center; }
            .content { padding: 20px; }
            .footer { background: #f1f1f1; padding: 15px; text-align: center; font-size: 12px; color: #666; }
        </style>
    </head>
    <body>
        <div class='header'>
            <h1>Thank You!</h1>
            <p>ChronicleChraft Creative Solutions</p>
        </div>
        
        <div class='content'>
            <h2>Dear {$form_data['fullName']},</h2>
            
            <p>Thank you for submitting your creative brief for <strong>{$form_data['projectTitle']}</strong>.</p>
            
            <p>We have received your detailed requirements and our team will review them carefully. We will get back to you within 24-48 hours to discuss your project further.</p>
            
            <p>If you have any urgent questions or need to add additional information, please don't hesitate to contact us directly at <a href='mailto:irfan@chroniclecraft.tech'>irfan@chroniclecraft.tech</a>.</p>
            
            <p>We're excited to work with you on bringing your creative vision to life!</p>
            
            <p>Best regards,<br>
            The ChronicleChraft Team</p>
        </div>
        
        <div class='footer'>
            <p>ChronicleChraft Creative Solutions</p>
            <p>Email: irfan@chroniclecraft.tech | Website: www.chroniclecraft.tech</p>
        </div>
    </body>
    </html>";
    
    $client_headers = [
        'MIME-Version: 1.0',
        'Content-type: text/html; charset=UTF-8',
        'From: ' . $from_email,
        'X-Mailer: PHP/' . phpversion()
    ];
    
    mail($form_data['email'], $client_subject, $client_body, implode("\r\n", $client_headers));
    
    echo json_encode(['success' => true, 'message' => 'Creative brief submitted successfully!']);
} else {
    echo json_encode(['success' => false, 'message' => 'Failed to send email. Please try again or contact us directly.']);
}
?>

