// Form handling and validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('creativeBriefForm');
    const submitBtn = document.querySelector('.submit-btn');
    
    // Add smooth scrolling for better UX
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Form submission handling
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading state
        submitBtn.textContent = 'Submitting...';
        submitBtn.disabled = true;
        form.classList.add('loading');
        
        // Remove any existing messages
        removeMessages();
        
        // Collect form data
        const formData = new FormData(form);
        
        // Submit form via fetch API
        fetch('/submit', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showSuccessMessage('Thank you! Your creative brief has been submitted successfully. We will contact you soon.');
                form.reset();
                // Scroll to top to show success message
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                showErrorMessage(data.message || 'There was an error submitting your form. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showErrorMessage('There was an error submitting your form. Please try again or contact us directly at irfan@chroniclecraft.tech');
        })
        .finally(() => {
            // Reset button state
            submitBtn.textContent = 'Submit Creative Brief';
            submitBtn.disabled = false;
            form.classList.remove('loading');
        });
    });

    // Real-time validation
    const requiredFields = form.querySelectorAll('[required]');
    requiredFields.forEach(field => {
        field.addEventListener('blur', validateField);
        field.addEventListener('input', clearFieldError);
    });

    function validateField(e) {
        const field = e.target;
        const value = field.value.trim();
        
        if (!value) {
            showFieldError(field, 'This field is required');
        } else if (field.type === 'email' && !isValidEmail(value)) {
            showFieldError(field, 'Please enter a valid email address');
        } else {
            clearFieldError(field);
        }
    }

    function clearFieldError(e) {
        const field = e.target;
        const errorMsg = field.parentNode.querySelector('.field-error');
        if (errorMsg) {
            errorMsg.remove();
        }
        field.classList.remove('error');
    }

    function showFieldError(field, message) {
        clearFieldError({ target: field });
        field.classList.add('error');
        
        const errorDiv = document.createElement('div');
        errorDiv.className = 'field-error';
        errorDiv.textContent = message;
        errorDiv.style.color = '#e74c3c';
        errorDiv.style.fontSize = '0.875rem';
        errorDiv.style.marginTop = '0.25rem';
        
        field.parentNode.appendChild(errorDiv);
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function showSuccessMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'success-message';
        messageDiv.textContent = message;
        messageDiv.style.display = 'block';
        
        const formHeader = document.querySelector('.form-header');
        formHeader.appendChild(messageDiv);
    }

    function showErrorMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'error-message';
        messageDiv.textContent = message;
        messageDiv.style.display = 'block';
        
        const formHeader = document.querySelector('.form-header');
        formHeader.appendChild(messageDiv);
    }

    function removeMessages() {
        const messages = document.querySelectorAll('.success-message, .error-message');
        messages.forEach(msg => msg.remove());
    }

    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    });

    // Add animation delay to form sections
    const formSections = document.querySelectorAll('.form-section');
    formSections.forEach((section, index) => {
        section.style.animationDelay = `${index * 0.1}s`;
    });

    // Character counter for textareas
    const longTextareas = document.querySelectorAll('textarea[rows="4"], textarea[rows="5"]');
    longTextareas.forEach(textarea => {
        const maxLength = 1000;
        textarea.setAttribute('maxlength', maxLength);
        
        const counter = document.createElement('div');
        counter.className = 'char-counter';
        counter.style.textAlign = 'right';
        counter.style.fontSize = '0.8rem';
        counter.style.color = '#666';
        counter.style.marginTop = '0.25rem';
        
        textarea.parentNode.appendChild(counter);
        
        function updateCounter() {
            const remaining = maxLength - textarea.value.length;
            counter.textContent = `${remaining} characters remaining`;
            
            if (remaining < 50) {
                counter.style.color = '#e74c3c';
            } else {
                counter.style.color = '#666';
            }
        }
        
        textarea.addEventListener('input', updateCounter);
        updateCounter();
    });
});

