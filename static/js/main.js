// Active nav highlighting
(function() {
    const path = location.pathname;
    const map = {
        '/':           'nav-dashboard',
        '/predictions':'nav-predictions',
        '/analytics':  'nav-analytics',
        '/attendance': 'nav-attendance',
        '/planner':    'nav-planner',
        '/timetable':  'nav-timetable',
        '/lifestyle':  'nav-lifestyle',
    };
    const id = map[path];
    if (id) {
        const el = document.getElementById(id);
        if (el) el.classList.add('active');
    }
})();

// Sidebar toggle
document.getElementById('menu-toggle').addEventListener('click', function() {
    const sidebar = document.getElementById('sidebar-wrapper');
    const content = document.getElementById('page-content-wrapper');
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('full-width');
});

// Animate all progress bars on page load
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.progress-slim .bar[data-width]').forEach(bar => {
        const w = bar.getAttribute('data-width');
        setTimeout(() => { bar.style.width = w + '%'; }, 300);
    });
    
    // Animate attendance rings
    document.querySelectorAll('.ring-val[data-pct]').forEach(ring => {
        const pct = parseFloat(ring.getAttribute('data-pct'));
        const offset = 251 - (251 * pct / 100);
        setTimeout(() => { ring.style.strokeDashoffset = offset; }, 400);
    });
});
