// is this weird to be in the style folder? probably

let total = 1;

function infiniteScrollLines() {
    setInterval(() => {
        total = (total == 0) ? 1 : 0;
        document.documentElement.style.setProperty('--scroll', (total + 1) + 'px'); 
        document.documentElement.style.setProperty('--scroll-second', (total + 2) + 'px');
    }, 100);
}
