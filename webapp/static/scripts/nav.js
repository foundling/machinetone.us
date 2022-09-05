const header = document.getElementById('nav-dropdown-target')
const nav = document.getElementById('nav-dropdown')

header.addEventListener('mouseover', () => {
    nav.classList.remove('hidden');
});
