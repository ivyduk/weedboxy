const navbar = document.querySelector('.header');

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 50;

    if (scrolled) {
        navbar.classList.add('scrolled');
        changeTitleColor('green-text');
    } else {
        navbar.classList.remove('scrolled');
        changeTitleColor('white-text');
    }

    if (scrolled) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    
    const isTransparent = navbar.classList.contains('transparent');
    if (scrolled && isTransparent) {
        navbar.classList.remove('transparent');
    } else if (!scrolled && !isTransparent) {
        navbar.classList.add('transparent');
    }
});


function changeTitleColor(colorClass) {
    const titles = document.querySelectorAll('.navbar-nav a');
    titles.forEach(title => {
        title.classList.remove('green-text', 'white-text');
        title.classList.add(colorClass);
    });
}