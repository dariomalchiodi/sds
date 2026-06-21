document.addEventListener("DOMContentLoaded", function() {
    
  // Function to get localized labels - with fallback support
  function getLabels() {
    // console.log('getLabels called');
    
    // Try to get labels from Sphinx config first
    if (window.sphinxConfig && window.sphinxConfig.showCodeLabel && window.sphinxConfig.hideCodeLabel) {
      return {
        showCode: window.sphinxConfig.showCodeLabel,
        hideCode: window.sphinxConfig.hideCodeLabel
      };
    }
    
    // Fallback to Italian (hardcoded)
    console.log('Using fallback Italian labels');
    return {
      showCode: 'Mostra codice',
      hideCode: 'Nascondi codice'
    };
  }

  // Set localized splash loading message
  function setLocalizedSplashMessage() {
    const splashMessage = window.sphinxConfig && window.sphinxConfig.pyscriptWaitLabel 
      ? window.sphinxConfig.pyscriptWaitLabel 
      : 'Attendi il caricamento di PyScript'; // fallback to Italian
    
    // Create a style element to override the CSS ::after content
    const style = document.createElement('style');
    style.textContent = `
      .splash::after {
        content: ' ${splashMessage}';
        color: var(--visited-link-color);
      }
    `;
    document.head.appendChild(style);
  }

  // Set the splash message immediately
  setLocalizedSplashMessage();

  const openDetails = document.querySelectorAll("li:not(.current) > details[open]");
  openDetails.forEach(details => {
    // Chiudi il dettaglio rimuovendo l'attributo open
    details.removeAttribute("open");
  });

  
  // JavaScript for toggle-code functionality on pre-generated buttons
  function initializeToggleCode() {
    const toggleButtons = document.querySelectorAll('.toggle-code-button');
    
    toggleButtons.forEach(function(button, index) {
      
      // Skip if already processed
      if (button.dataset.toggleProcessed) {
        // console.log('Button', index + 1, 'already processed');
        return;
      }
      
      // Find the content div
      const wrapper = button.closest('.toggle-code-wrapper');
      if (!wrapper) {
        console.log('No wrapper found for button', index + 1);
        return;
      }
      
      const content = wrapper.querySelector('.toggle-code-content');
      if (!content) {
        console.log('No content found for button', index + 1);
        return;
      }
      
      // Add click event listener to the toggle button
      button.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        // console.log('Current content classes:', content.className);
        
        const textSpan = button.querySelector('.button-text');
        const labels = getLabels();
        
        if (content.classList.contains('expanded')) {
          // Hide the content
          content.classList.remove('expanded');
          button.classList.remove('expanded');
          // Only update the text, triangle rotates via CSS
          textSpan.textContent = ' ' + labels.showCode;
          console.log('Code collapsed for button', index + 1);
        } else {
          // Show the content
          content.classList.add('expanded');
          button.classList.add('expanded');
          // Only update the text, triangle rotates via CSS
          textSpan.textContent = ' ' + labels.hideCode;
          // console.log('Code expanded for button', index + 1);
        }
      });
      
      // Mark as processed
      button.dataset.toggleProcessed = 'true';
    });
  }
  
  // Make the function globally available
  window.initializeToggleCode = initializeToggleCode;

  // Initialize immediately
  initializeToggleCode();

  // Expose myproof subtitle: when the admonition title is not the placeholder
  // '_', set data-proof-subtitle so CSS can append it in parentheses after the
  // localized "Dimostrazione / Proof / ..." label via attr().
  document.querySelectorAll('.myproof.admonition').forEach(function(proof) {
    var title = proof.querySelector('.admonition-title');
    if (!title) return;
    var text = title.textContent.trim();
    if (text && text !== '_') {
      proof.setAttribute('data-proof-subtitle', text);
    }
  });

  // Prevent focus ring on exercise/solution title clicks by blocking the
  // mousedown default (which is what causes the browser to focus the element).
  // The click event still fires, so togglebutton.js works normally.
  document.querySelectorAll(
    '.exercise.admonition > .admonition-title, ' +
    '.exercise.admonition + .solution.admonition > .admonition-title'
  ).forEach(function(title) {
    title.addEventListener('mousedown', function(e) {
      e.preventDefault();
    });
  });

  // Solution toggle hint: swap data-toggle-hint between show/hide strings so the
  // CSS ::before always reflects the current state (library only sets it once at init).
  document.querySelectorAll('.exercise.admonition + .solution.admonition').forEach(function(solution) {
    var title = solution.querySelector('.admonition-title');
    if (!title) return;
    title.addEventListener('click', function() {
      setTimeout(function() {
        var btn = solution.querySelector('.toggle-button');
        if (!btn) return;
        btn.setAttribute('data-toggle-hint',
          solution.classList.contains('toggle-hidden') ? toggleHintShow : toggleHintHide
        );
      }, 0);
    });
  });

  // Chapter chevron toggle: clicking the rightmost ~36px of a chapter-collapsible
  // link toggles its sub-items without navigating.
  document.querySelectorAll('.chapter-collapsible').forEach(function(link) {
    link.addEventListener('click', function(e) {
      var subItems = link.parentElement.querySelector('.chapter-sub-items');
      if (!subItems) return;
      var rect = link.getBoundingClientRect();
      if (e.clientX >= rect.right - 36) {
        e.preventDefault();
        e.stopPropagation();
        link.classList.toggle('collapsed');
        subItems.classList.toggle('collapsed');
      }
    });
  });

  // Wrap section numbers in <span class="sec-num"> so CSS can style them
  // separately from the heading title text.
  (function styleHeadingNumbers() {
    document.querySelectorAll(
      '.bd-article-container h1, .bd-article-container h2, .bd-article-container h3'
    ).forEach(function(h) {
      var node = h.childNodes[0];
      if (!node || node.nodeType !== 3) return;
      var m = node.textContent.match(/^(\d+(?:\.\d+)*\.\s+)([\s\S]*)/);
      if (!m) return;
      var numSpan = document.createElement('span');
      numSpan.className = 'sec-num';
      numSpan.textContent = m[1];
      var titleSpan = document.createElement('span');
      titleSpan.className = 'sec-title';
      titleSpan.textContent = m[2];
      h.replaceChild(titleSpan, node);
      h.insertBefore(numSpan, titleSpan);
    });
  })();

  // Function to detect and mark appendices
  function detectAppendices() {
    const currentPath = window.location.pathname;
    const currentPageTitle = document.title;
    
    // console.log('Current path:', currentPath);
    // console.log('Current title:', currentPageTitle);
    
    // Check if current page is an appendix
    if (currentPath.includes('references.html') || 
        currentPath.includes('appendix') || 
        currentPath.includes('bibliography') ||
        currentPageTitle.includes('References') ||
        currentPageTitle.includes('Bibliografia')) {
      
      document.body.classList.add('appendix-page');
      // console.log('Detected appendix page, added appendix-page class');
    } else {
      document.body.classList.add('chapter-page');
      // console.log('Detected chapter page, added chapter-page class');
    }
  }

  // Comprehensive function to handle sidebar appendix numbering
  function setupSidebarAppendixNumbering() {
    const sidebar = document.querySelector('.bd-sidebar nav.bd-links');
    if (!sidebar) {
      console.log('Sidebar not found');
      return false;
    }
    
    // Find all caption elements
    const captions = sidebar.querySelectorAll('.caption-text');
    let appendiciFound = false;
    
    for (let caption of captions) {
      if (caption.textContent.includes('Appendici')) {
        appendiciFound = true;
        // console.log('Found Appendici caption');
        
        // Get the parent paragraph
        const captionParagraph = caption.closest('p');
        if (captionParagraph) {
          // Find all following ul elements (they should be appendices)
          let nextElement = captionParagraph.nextElementSibling;
          while (nextElement) {
            if (nextElement.tagName === 'UL') {
              nextElement.classList.add('appendix-list');
              // console.log('Added appendix-list class to ul');
              
              // Add specific class to each li within this ul
              const appendixItems = nextElement.querySelectorAll('li.toctree-l1');
              appendixItems.forEach((item, index) => {
                item.classList.add('appendix-item');
                item.setAttribute('data-appendix-index', index + 1);
              });
              
              break; // Assuming only one ul follows the Appendici caption
            }
            nextElement = nextElement.nextElementSibling;
          }
        }
        break;
      }
    }
    
    if (!appendiciFound) {
      console.log('Appendici caption not found');
      return false;
    }
    
    return true;
  }

  // Call the detection functions
  detectAppendices();
  
  // DISABLED: Add section numbers to cross-references
  // addSectionNumbersToReferences();

  // Try immediately; if the sidebar isn't in the DOM yet, watch for it.
  if (!setupSidebarAppendixNumbering()) {
    const sidebarObserver = new MutationObserver(function(mutations, obs) {
      if (setupSidebarAppendixNumbering()) {
        obs.disconnect();
      }
    });
    sidebarObserver.observe(document.body, { childList: true, subtree: true });
  }
  
  // Function to add section numbers to cross-references
  function addSectionNumbersToReferences() {
    console.log('Adding section numbers to cross-references');
    
    // Find all internal reference links
    const refLinks = document.querySelectorAll('a.reference.internal');
    
    refLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      
      // Check if this is a section reference (has # anchor)
      if (href.includes('#')) {
        const targetId = href.split('#')[1];
        
        // Try to find the target element
        let targetElement = null;
        
        // First try in current document
        targetElement = document.getElementById(targetId);
        
        // If not found in current document, it might be in another document
        // We need to handle this differently
        if (!targetElement && href.includes('.html#')) {
          // This is a reference to another document
          // We'll need to extract section info differently
          handleCrossDocumentReference(link, href);
          return;
        }
        
        if (targetElement) {
          // Find the section number
          const sectionNumber = getSectionNumber(targetElement);
          if (sectionNumber) {
            updateReferenceText(link, sectionNumber);
          }
        }
      }
    });
  }
  
  function handleCrossDocumentReference(link, href) {
    // For cross-document references, we'll use a mapping approach
    // Based on our CSS numbering system
    const sectionMappings = {
      'approccio.html#chap-approccio': '2',
      'presentazione.html#presentazione': '1',
      // Add more mappings as needed
    };
    
    const key = href.replace('../', '').replace('./', '');
    if (sectionMappings[key]) {
      updateReferenceText(link, sectionMappings[key]);
    }
  }
  
  function getSectionNumber(element) {
    // Try to get section number from various possible parent elements
    let current = element;
    while (current && current !== document.body) {
      if (current.tagName && current.tagName.match(/^H[1-6]$/)) {
        // This is a heading element, try to get its number
        const computedStyle = window.getComputedStyle(current, '::before');
        const content = computedStyle.content;
        if (content && content !== 'none' && content !== '""') {
          // Extract number from content
          const match = content.match(/(\d+)/);
          if (match) {
            return match[1];
          }
        }
      }
      current = current.parentElement;
    }
    return null;
  }
  
  function updateReferenceText(link, sectionNumber) {
    const spanElement = link.querySelector('span.std.std-ref');
    if (spanElement) {
      const currentText = spanElement.textContent;
      if (!currentText.match(/^\d+\./)) { // Only add if not already numbered
        spanElement.textContent = `${sectionNumber}. ${currentText}`;
      }
    }
  }

  // True/false (Vero o falso) question cards — rendered by the {tf-item}
  // directive. The HTML structure is pre-built: div.tf-item > (div.tf-question
  // + div.tf-verdict). JS only wires the click toggle and detects the verdict.
  document.querySelectorAll('.tf-item').forEach(function(item) {
    var question = item.querySelector('.tf-question');
    var verdict  = item.querySelector('.tf-verdict');
    if (!question || !verdict) return;

    question.addEventListener('click', function() {
      item.classList.toggle('tf-open');
      item.classList.add('tf-seen'); // permanent once revealed; drives badge colour
    });

    // Detect vera/falsa from the first <strong> in the answer.
    // Accept all four languages: it=Vera/Falsa, en=True/False, fr=Vrai/Faux,
    // es=Verdadero/Verdadera/Falso/Falsa.
    var strong = verdict.querySelector('p:first-child > strong:first-child');
    if (!strong) return;
    var v = strong.textContent.trim().toLowerCase();
    var isVera  = v === 'vera'  || v === 'vrai'  || v === 'vraie'  || v === 'true'
               || v === 'verdadero' || v === 'verdadera';
    var isFalsa = v === 'falsa' || v === 'faux'  || v === 'fausse' || v === 'false'
               || v === 'falso';
    if (isVera)  item.classList.add('tf-vera');
    if (isFalsa) item.classList.add('tf-falsa');
  });

  // Keyword reveal grid for {sds-wordcloud} containers.
  // Cells start visually empty; a button above the grid reveals all terms
  // with a staggered fade-in. Clicking again re-hides them.
  document.querySelectorAll('.sds-wordcloud').forEach(function(container) {
    var raw = container.getAttribute('data-words');
    if (!raw) return;
    var words;
    try { words = JSON.parse(raw); } catch(e) { return; }
    if (!words.length) return;

    var allCells = [];

    // Render a term string: backtick spans → <code>, plain text HTML-escaped.
    function renderTerm(text) {
      var html = '';
      var parts = text.split('`');
      for (var i = 0; i < parts.length; i++) {
        var escaped = parts[i]
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;');
        if (i % 2 === 0) {
          html += escaped;
        } else {
          html += '<code>' + escaped + '</code>';
        }
      }
      return html;
    }

    words.forEach(function(w, idx) {
      var cell = document.createElement('div');
      cell.className            = 'sds-ptable-cell';
      cell.style.animationDelay = (idx * 0.04) + 's';

      var name = document.createElement('span');
      name.className = 'sds-ptable-name';
      name.innerHTML = renderTerm(w.term);

      cell.appendChild(name);
      container.appendChild(cell);
      allCells.push(cell);
    });

    // Button label by document language
    var lang = (document.documentElement.lang || 'it').slice(0, 2).toLowerCase();
    var LBLS = {
      it: ['Scopri i termini',      'Nascondi i termini'],
      en: ['Reveal terms',          'Hide terms'],
      fr: ['Révéler les termes',    'Masquer les termes'],
      es: ['Revelar los términos',  'Ocultar los términos']
    };
    var lbls = LBLS[lang] || LBLS['it'];

    var wrap = document.createElement('div');
    wrap.className = 'sds-reveal-wrap';

    var btn = document.createElement('button');
    btn.className   = 'sds-reveal-btn';
    btn.textContent = lbls[0];
    wrap.appendChild(btn);
    container.parentNode.insertBefore(wrap, container);

    var revealed = false;

    btn.addEventListener('click', function() {
      if (!revealed) {
        revealed = true;
        btn.textContent = lbls[1];
        btn.classList.add('sds-reveal-btn--reset');
        allCells.forEach(function(cell, i) {
          setTimeout(function() {
            cell.classList.add('sds-ptable-cell--revealed');
          }, i * 60);
        });
      } else {
        revealed = false;
        btn.textContent = lbls[0];
        btn.classList.remove('sds-reveal-btn--reset');
        allCells.forEach(function(cell) {
          cell.classList.remove('sds-ptable-cell--revealed');
        });
      }
    });
  });

  // Prevent line break between inline math spans and adjacent brackets/punctuation.
  // Handles: "( math", "math )", and combined "( math )".
  document.querySelectorAll('span.math').forEach(function(span) {
    var prev = span.previousSibling;
    var next = span.nextSibling;
    var leadChar  = (prev && prev.nodeType === 3 && /\($/.test(prev.textContent)) ? '(' : null;
    var trailChar = (next && next.nodeType === 3 && /^[,\.;:!?…\)]/.test(next.textContent))
                    ? next.textContent[0] : null;

    if (!leadChar && !trailChar) return;

    var wrapper = document.createElement('span');
    wrapper.style.whiteSpace = 'nowrap';
    span.parentNode.insertBefore(wrapper, span);

    if (leadChar) {
      prev.textContent = prev.textContent.slice(0, -1);
      wrapper.appendChild(document.createTextNode(leadChar));
      if (prev.textContent === '') prev.parentNode.removeChild(prev);
    }

    wrapper.appendChild(span);

    if (trailChar) {
      next.textContent = next.textContent.slice(1);
      wrapper.appendChild(document.createTextNode(trailChar));
      if (next.textContent === '') next.parentNode.removeChild(next);
    }
  });

  // Sidebar uses display:grid so the outer sidebar cannot scroll (scrollTop always 0).
  // PyData's active-link scroll targets the outer sidebar and is therefore a no-op.
  // We replicate it here, targeting the inner scroll area instead.
  (function scrollTocToActiveLink() {
    var scrollArea = document.querySelector('.bd-sidebar-scroll-area');
    if (!scrollArea) return;
    var docsNav = scrollArea.querySelector('.bd-docs-nav');
    if (!docsNav) return;
    var activeLinks = docsNav.querySelectorAll('.active');
    if (!activeLinks.length) return;
    var lastActive = activeLinks[activeLinks.length - 1];
    if (lastActive.getBoundingClientRect().y > 0.5 * window.innerHeight) {
      var r = lastActive.getBoundingClientRect().y - scrollArea.getBoundingClientRect().y;
      scrollArea.scrollTop = r - scrollArea.clientHeight * 0.25;
    }
  })();

});