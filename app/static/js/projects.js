// alert('JS Working!');

const gameButton = document.querySelector('#btn-game');
const projectButton = document.querySelector('#btn-project');
const techButton = document.querySelector('#btn-tech');

const gameSect = document.querySelector('#the-game');
const projectSect = document.querySelector('#the-project');
const techSect = document.querySelector('#the-techs');

const img1 = document.querySelector('#image1');
const img2 = document.querySelector('#image2');
const img3 = document.querySelector('#image3');


gameButton.addEventListener('click',  handleClick);
projectButton.addEventListener('click', handleClick);
techButton.addEventListener('click', handleClick);

function handleClick(event) {
    // console.log(event.target.innerHTML);
    if (event.target.innerHTML === "The Game" || event.target.innerHTML === "The App") {
        gameButton.classList.add('proj-btn-current');
        projectButton.classList.remove('proj-btn-current');
        techButton.classList.remove('proj-btn-current');

        gameButton.classList.remove('proj-btn-active');
        projectButton.classList.add('proj-btn-active');
        techButton.classList.add('proj-btn-active');
  
        gameSect.classList.remove('hidden');
        projectSect.classList.add('hidden');
        techSect.classList.add('hidden');

        img1.classList.add('current-image');
        img1.classList.remove('hidden-image');
        img2.classList.add('hidden-image');
        img2.classList.remove('current-image');
        img3.classList.add('hidden-image');
        img3.classList.remove('current-image');

    } else if (event.target.innerHTML === "The Project") {
        gameButton.classList.remove('proj-btn-current');
        projectButton.classList.add('proj-btn-current');
        techButton.classList.remove('proj-btn-current');

        gameButton.classList.add('proj-btn-active');
        projectButton.classList.remove('proj-btn-active');
        techButton.classList.add('proj-btn-active');
     
        gameSect.classList.add('hidden');
        projectSect.classList.remove('hidden');
        techSect.classList.add('hidden');

        img1.classList.add('hidden-image');
        img1.classList.remove('current-image');
        img2.classList.add('current-image');
        img2.classList.remove('hidden-image');
        img3.classList.add('hidden-image');
        img3.classList.remove('current-image');

    } else {
        gameButton.classList.remove('proj-btn-current');
        projectButton.classList.remove('proj-btn-current');
        techButton.classList.add('proj-btn-current');

        gameButton.classList.add('proj-btn-active');
        projectButton.classList.add('proj-btn-active');
        techButton.classList.remove('proj-btn-active');

        gameSect.classList.add('hidden');
        projectSect.classList.add('hidden');
        techSect.classList.remove('hidden');

        img1.classList.add('hidden-image');
        img1.classList.remove('current-image');
        img2.classList.add('hidden-image');
        img2.classList.remove('current-image');
        img3.classList.add('current-image');
        img3.classList.remove('hidden-image');
    }
}
