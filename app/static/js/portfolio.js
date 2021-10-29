// alert('JS is working at PORTFOLIO!')

const sixdkbElem = document.querySelector('#proj-sixdkb');
// const cocktailsElem = document.querySelector('#proj-cocktails');
// const marketplaceElem = document.querySelector('#proj-marketplace');
const chartreuseElem = document.querySelector('#proj-chartreuse');
// const codegreenElem = document.querySelector('#proj-code-green');
const djangoflaskElem = document.querySelector('#proj-django-and-flask');

const elemsArray = [sixdkbElem, chartreuseElem, djangoflaskElem]

function handleMouseOver(event) {
    event.target.closest('li').style.boxShadow = '0 0 2px 2px var(--accent-color)'
    event.target.closest('li').firstElementChild.style.opacity = '100%';
}

function handleMouseOut(event) {
    event.target.closest('li').style.boxShadow = 'none'
    event.target.closest('li').firstElementChild.style.opacity = '0%';
}

elemsArray.forEach(item => {
    item.addEventListener('mouseover', handleMouseOver);
    item.addEventListener('mouseout', handleMouseOut)
});
