// theme toggle (dark/light)
const toggle = document.getElementById('theme-toggle');
function setTheme(isDark) {
  if (isDark) document.body.classList.add('dark');
  else document.body.classList.remove('dark');
  toggle.textContent = isDark ? '☀️' : '🌙';
  localStorage.setItem('darkMode', isDark ? '1' : '0');
}

// initialize from localStorage
document.addEventListener('DOMContentLoaded', () => {
  const stored = localStorage.getItem('darkMode');
  const isDark = stored === '1' || (stored === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  setTheme(isDark);

  toggle.addEventListener('click', () => {
    setTheme(!document.body.classList.contains('dark'));
  });
});
