// Define the toggle code initialization function
window.initializeToggleCode = function() {
    const allButtons = document.querySelectorAll('.toggle-code-button');
    
    console.log(`Total toggle buttons found: ${allButtons.length}`);
    
    // Get labels from Sphinx config
    const showLabel = window.sphinxConfig?.showCodeLabel || 'Mostra codice';
    const hideLabel = window.sphinxConfig?.hideCodeLabel || 'Nascondi codice';
    
    allButtons.forEach((button, index) => {
        // Remove any existing event listeners by cloning
        const newButton = button.cloneNode(true);
        button.parentNode.replaceChild(newButton, button);
        
        // Remove the processed attribute
        newButton.removeAttribute('data-toggle-processed');
        
        // Get elements
        const buttonText = newButton.querySelector('.button-text');
        const triangle = newButton.querySelector('.triangle');
        const content = newButton.nextElementSibling;
        
        // Set initial state based on whether content is expanded
        const isExpanded = content && content.classList.contains('expanded');
        
        if (buttonText) {
            buttonText.textContent = ` ${isExpanded ? hideLabel : showLabel}`;
        }
        if (triangle) {
            triangle.textContent = '▶';
        }
        
        newButton.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            console.log(`Button ${index} clicked`);
            
            if (!content || !content.classList.contains('toggle-code-content')) {
                console.error('No valid content element found for button', index);
                return;
            }
            
            // Toggle expanded class
            this.classList.toggle('expanded');
            content.classList.toggle('expanded');
            
            console.log('Content classes after toggle:', content.className);
            
            // Update button text and triangle
            if (content.classList.contains('expanded')) {
                buttonText.textContent = ` ${hideLabel}`;
            } else {
                buttonText.textContent = ` ${showLabel}`;
                triangle.textContent = '▶'
            }
        });
        
        newButton.setAttribute('data-toggle-processed', 'true');
    });
};

// Initialize immediately
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', window.initializeToggleCode);
} else {
    window.initializeToggleCode();
}

// Re-initialize after delays for dynamic content
setTimeout(window.initializeToggleCode, 500);
setTimeout(window.initializeToggleCode, 1000);