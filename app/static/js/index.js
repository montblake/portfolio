// alert('Index JS is ALIVE');

const introEl = document.querySelector('#btn-intro');
const bootcampEl = document.querySelector('#btn-boot');
const fullstackEl = document.querySelector('#btn-full');
const prevEl = document.querySelector('#btn-theater');
const currentEl = document.querySelector('#btn-current');
const aboutButtons = [introEl, bootcampEl, fullstackEl, prevEl, currentEl];


const bootcampTagEl = document.querySelector('#tag-boot');
const fullstackTagEl = document.querySelector('#tag-full');
const prevTagEl = document.querySelector('#tag-theater');
const currentTagEl = document.querySelector('#tag-current');


const introInfoEl = document.querySelector('#info-intro');
const bootcampInfoEl = document.querySelector('#info-boot');
const fullstackInfoEl = document.querySelector('#info-full');
const prevInfoEl = document.querySelector('#info-theater');
const currentInfoEl = document.querySelector('#info-current');
const aboutParas = [introInfoEl, bootcampInfoEl, fullstackInfoEl, prevInfoEl, currentInfoEl];


function regulate_click(event) {
    let clickedButton;
    console.log(event.target);
    if (event.target  === introEl ||
        event.target === bootcampEl ||
        event.target === fullstackEl ||
        event.target === prevEl ||
        event.target === currentEl) {
            clickedButton = event.target;
        }
    else {
        if (event.target === bootcampTagEl) {
            clickedButton = bootcampEl;
        }
        if (event.target === fullstackTagEl) {
            clickedButton = fullstackEl;
        }
        if (event.target === prevTagEl) {
            clickedButton = prevEl;
        }
        if (event.target === currentTagEl) {
            clickedButton = currentEl;
        }
    }
    return clickedButton;
}

function handleClick(event) {
    const clickedButton = regulate_click(event);
    let chosenPara;
    if (clickedButton === introEl) {
        chosenPara = introInfoEl
    } 
    if (clickedButton === bootcampEl) {
        chosenPara = bootcampInfoEl
    } 
    if (clickedButton === fullstackEl) {
        chosenPara = fullstackInfoEl
    } 
    if (clickedButton === prevEl) {
        chosenPara = prevInfoEl
    } 
    if (clickedButton === currentEl) {
        chosenPara = currentInfoEl
    }

    const buttonsNotChosen = aboutButtons.filter(button => button !== clickedButton);
    const parasNotChosen = aboutParas.filter(para => para != chosenPara);  
    clickedButton.classList.add('btn-current-subject');
    clickedButton.classList.remove('btn-active');
    buttonsNotChosen.forEach(button => {
        button.classList.remove('btn-current-subject');
        button.classList.add('btn-active');
    });
    chosenPara.classList.remove('hidden');
    chosenPara.classList.add('para-current-subject');
    // console.log(chosenPara);
    parasNotChosen.forEach(para => {
        para.classList.remove('para-current-subject');
        para.classList.add('hidden');
    });

}

introEl.addEventListener('click', handleClick)
bootcampEl.addEventListener('click', handleClick);
fullstackEl.addEventListener('click', handleClick);
prevEl.addEventListener('click', handleClick);
currentEl.addEventListener('click', handleClick);

bootcampTagEl.addEventListener('click', handleClick);
fullstackTagEl.addEventListener('click', handleClick);
prevTagEl.addEventListener('click', handleClick);
currentTagEl.addEventListener('click', handleClick);