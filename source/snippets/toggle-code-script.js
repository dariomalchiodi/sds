// Initialize toggle code functionality after PyScript execution
setTimeout(function() {
    if (typeof window.initializeToggleCode === 'function') {
        window.initializeToggleCode();
    }
}, 100);

