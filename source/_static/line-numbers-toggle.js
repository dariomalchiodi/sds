// Line number toggle functionality with Font Awesome icon
// Check localStorage immediately before DOM loads to prevent flash
(function() {
    const savedState = localStorage.getItem('lineNumbersVisible');
    if (savedState === 'false') {
        // Inject CSS to hide line numbers immediately
        const style = document.createElement('style');
        style.textContent = `
            .highlight td.linenos,
            .highlight span.linenos,
            .highlight pre .linenos {
                display: none !important;
            }
        `;
        document.head.appendChild(style);
    }
})();

document.addEventListener('DOMContentLoaded', function() {
    // Initialize line number toggles
    initializeLineNumberToggles();
    
    // Watch for dynamically revealed code blocks (e.g., from toggle-code functionality)
    setupDynamicObserver();
    
    // Initialize line number toggles for all visible code blocks
    function initializeLineNumberToggles() {
        const codeBlocks = document.querySelectorAll('.highlight');
        
        codeBlocks.forEach(function(codeBlock, index) {
            // Skip if already processed
            if (codeBlock.querySelector('.line-numbers-toggle')) {
                return;
            }
            
            // Check if this code block has line numbers
            const hasLineNumbers = codeBlock.querySelector('td.linenos, span.linenos, pre .linenos');
            
            if (hasLineNumbers) {
                addToggleIcon(codeBlock);
            }
        });
    }
    
    // Add toggle icon to a specific code block
    function addToggleIcon(codeBlock) {
        // Create toggle icon
        const toggleIcon = document.createElement('i');
        toggleIcon.className = 'line-numbers-toggle fas fa-list-ol';
        toggleIcon.setAttribute('aria-label', 'Attiva/disattiva numeri di riga');
        toggleIcon.setAttribute('title', 'Attiva/disattiva numeri di riga');
        
        // Load saved state from localStorage
        const savedState = localStorage.getItem('lineNumbersVisible');
        let lineNumbersVisible = savedState === null ? true : savedState === 'true';
        
        // Apply initial state
        updateLineNumbersDisplay(codeBlock, lineNumbersVisible);
        updateIconState(toggleIcon, lineNumbersVisible);
        
        // Add click event listener
        toggleIcon.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent event bubbling
            lineNumbersVisible = !lineNumbersVisible;
            
            updateLineNumbersDisplay(codeBlock, lineNumbersVisible);
            updateIconState(toggleIcon, lineNumbersVisible);
            
            // Save state to localStorage
            localStorage.setItem('lineNumbersVisible', lineNumbersVisible.toString());
            
            // Update all other code blocks on the page
            updateAllCodeBlocks(lineNumbersVisible);
        });
        
        // Insert the toggle icon into the code block
        codeBlock.appendChild(toggleIcon);
    }
    
    // Set up observer for dynamically revealed code blocks
    function setupDynamicObserver() {
        // Watch for changes in visibility of toggle-code-content elements
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
                    const element = mutation.target;
                    if (element.classList.contains('toggle-code-content')) {
                        // Check if the element became visible
                        const isVisible = element.style.display !== 'none' && 
                                        element.style.visibility !== 'hidden' &&
                                        element.offsetHeight > 0;
                        
                        if (isVisible) {
                            // Re-initialize line number toggles for newly visible code blocks
                            setTimeout(function() {
                                initializeLineNumberToggles();
                            }, 100); // Small delay to ensure DOM is fully updated
                        }
                    }
                }
            });
        });
        
        // Observe all toggle-code-content elements
        document.querySelectorAll('.toggle-code-content').forEach(function(element) {
            observer.observe(element, {
                attributes: true,
                attributeFilter: ['style']
            });
        });
        
        // Also listen for click events on toggle buttons
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('toggle-code-button') || 
                e.target.closest('.toggle-code-button')) {
                // Delay to allow the toggle animation to complete
                setTimeout(function() {
                    initializeLineNumberToggles();
                }, 300);
            }
        });
    }
    
    // Global toggle function to update all code blocks
    function updateAllCodeBlocks(visible) {
        const allCodeBlocks = document.querySelectorAll('.highlight');
        allCodeBlocks.forEach(function(block) {
            const hasLineNumbers = block.querySelector('td.linenos, span.linenos, pre .linenos');
            if (hasLineNumbers) {
                updateLineNumbersDisplay(block, visible);
                
                // Update icon state
                const toggleIcon = block.querySelector('.line-numbers-toggle');
                if (toggleIcon) {
                    updateIconState(toggleIcon, visible);
                }
            }
        });
    }
    
    // Function to update line numbers display
    function updateLineNumbersDisplay(codeBlock, visible) {
        if (visible) {
            codeBlock.classList.remove('hide-line-numbers');
        } else {
            codeBlock.classList.add('hide-line-numbers');
        }
    }
    
    // Function to update icon state
    function updateIconState(icon, visible) {
        if (visible) {
            icon.classList.remove('active');
            icon.setAttribute('title', 'Nascondi numeri di riga');
        } else {
            icon.classList.add('active');
            icon.setAttribute('title', 'Mostra numeri di riga');
        }
    }
    
    // Add global keyboard shortcut (Ctrl+L or Cmd+L)
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'l') {
            e.preventDefault();
            const firstToggleIcon = document.querySelector('.line-numbers-toggle');
            if (firstToggleIcon) {
                firstToggleIcon.click();
            }
        }
    });
});
