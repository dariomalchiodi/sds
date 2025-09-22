document.addEventListener('DOMContentLoaded', function() {
    // Find all part titles with collapsible class
    const partTitles = document.querySelectorAll('.part-collapsible');
    partTitles.forEach(function(title) {
        // Find the chapters container more reliably
        let chapters = title.nextElementSibling;
        
        // Skip any non-ul elements (like whitespace nodes)
        while (chapters && chapters.nodeType !== 1) {
            chapters = chapters.nextSibling;
        }
        while (chapters && !chapters.classList.contains('part-chapters')) {
            chapters = chapters.nextElementSibling;
        }
        
        if (!chapters) {
            console.log('No chapters container found for part:', title.textContent.trim());
            return;
        }
        
        // Check if this part contains the current page
        let containsCurrentPage = false;
        const currentItems = chapters.querySelectorAll('.current, .active');
        containsCurrentPage = currentItems.length > 0;
        
        // console.log('Part:', title.textContent.trim(), 'contains current page:', containsCurrentPage);
        
        // Initialize parts as collapsed by default, but expand if it contains current page
        if (!containsCurrentPage) {
            title.classList.add('collapsed');
            chapters.classList.add('collapsed');
        }
        
        title.addEventListener('click', function(e) {
            // Make click work on the entire element, not just chevron area
            e.preventDefault();
            console.log('Clicked on part:', title.textContent.trim());
            
            title.classList.toggle('collapsed');
            chapters.classList.toggle('collapsed');
        });
    });
    
    // Find all chapter titles with collapsible class
    const chapterTitles = document.querySelectorAll('.chapter-collapsible');
    
    chapterTitles.forEach(function(title) {
        // Initialize chapters as collapsed by default (except current page)
        const parentLi = title.closest('li');
        const isCurrentPage = parentLi && (parentLi.classList.contains('current') || parentLi.classList.contains('active'));
        
        if (!isCurrentPage) {
            title.classList.add('collapsed');
        }
        
        const subItems = title.parentElement.querySelector('.chapter-sub-items');
        if (subItems) {
            if (!isCurrentPage) {
                subItems.classList.add('collapsed');
            }
        }
        
        title.addEventListener('click', function(e) {
            console.log('Clicked on chapter:', title.textContent.trim());
            
            // Check if the click was specifically on the chevron (right side of the element)
            const rect = title.getBoundingClientRect();
            const clickX = e.clientX;
            const chevronArea = rect.right - 40; // Chevron is positioned 30px + padding from right
            
            if (clickX >= chevronArea) {
                // Click was on chevron area - only handle collapse/expand
                e.preventDefault();
                if (subItems) {
                    title.classList.toggle('collapsed');
                    subItems.classList.toggle('collapsed');
                }
            } else {
                // Click was on the main title area - allow navigation AND handle collapse
                // Don't prevent default - let the link navigate
                if (subItems) {
                    title.classList.toggle('collapsed');
                    subItems.classList.toggle('collapsed');
                }
                // Navigation will happen naturally due to the link
            }
        });
    });
    
    // Remove any remaining details elements that might not have been converted
    const remainingDetails = document.querySelectorAll('details');
    remainingDetails.forEach(function(detail) {
        detail.style.display = 'none';
    });
});
