// INTERVALS are in milliseconds. 
// NOTE: related css transition times are also used to control the time over which this change is made. 
const WIDTH_LIMIT_UPPER = 105;
const WIDTH_LIMIT_LOWER = 115;
const SIZE_INTERVAL = 8000;
// css transition for size: 10s

const ROTATION_LIMIT_UPPER = 4;
const ROTATION_LIMIT_LOWER = 0;
const ROTATION_INTERVAL = 3000;
// css transition for rotation: 6s

const OPACITY_LIMIT_UPPER = .5;
const OPACITY_LIMIT_LOWER = .2; 
const OPACITY_INTERVAL = 7000;
// css transition for opacity: 8s

const portrait = document.querySelector('#portrait');
portrait.style.width = "110%";
portrait.style.transform = "rotate(3deg)";
portrait.style.opacity = .35;

// IMAGE SIZE
setInterval(()=>{
  const options = ['same', 'bigger', 'smaller'];
  const randNum = Math.floor(Math.random() * 3);
  const randChoice = options[randNum];
  let oldWidth = portrait.style.width.replace('%', '');
  oldWidth = Number(oldWidth);
  let newWidth = oldWidth;

  switch (randChoice) {
    case 'same':
      break;
    case 'bigger':
      if (oldWidth < WIDTH_LIMIT_UPPER) {
        newWidth = oldWidth + 1;
        newWidth += "%";
        portrait.style.width = newWidth;

      }
      break;
    case 'smaller':
      if (oldWidth > WIDTH_LIMIT_LOWER) {
        newWidth = oldWidth - 1;
        newWidth += "%";
        portrait.style.width = newWidth;
      }
      break;
    default:
      console.log('unknown choice');
  }
}, SIZE_INTERVAL);

// IMAGE ROTATION
setInterval(()=>{
  const options = ['same', 'bigger', 'smaller'];
  const randNum = Math.floor(Math.random() * 3);
  const randChoice = options[randNum];
  let oldRotation = portrait.style.transform;
  oldRotation = oldRotation[7];
  oldRotation = Number(oldRotation);
  let newRotation;

  switch (randChoice) {
    case 'same':
      break;
    case 'bigger':
      if (oldRotation < ROTATION_LIMIT_UPPER) {
        newRotation = oldRotation + 1;
        newRotation = `rotate(${newRotation}deg)`;
        portrait.style.transform = newRotation;

      }
      break;
    case 'smaller':
      if (oldRotation > ROTATION_LIMIT_LOWER) {
        newRotation = oldRotation - 1;
        newRotation = `rotate(${newRotation}deg)`;
        portrait.style.transform = newRotation;
      }
      break;
    default:
      console.log('unknown choice');
  }
}, ROTATION_INTERVAL);

// IMAGE OPACITY
setInterval(()=>{
  const options = ['same', 'bigger', 'smaller'];
  const randNum = Math.floor(Math.random() * 3);
  const randChoice = options[randNum];
  let oldOpacity = portrait.style.opacity;
  oldOpacity = Number(oldOpacity);
  let newOpacity;

  switch (randChoice) {
    case 'same':
      break;
    case 'bigger':
      if (oldOpacity < OPACITY_LIMIT_UPPER) {
        newOpacity = oldOpacity + .05;
        portrait.style.opacity = newOpacity;
      }
      break;
    case 'smaller':
      if (oldOpacity > OPACITY_LIMIT_LOWER) {
        newOpacity = oldOpacity - .05;
        portrait.style.opacity = newOpacity;
      }
      break;
    default:
      console.log('unknown choice');
  }
}, OPACITY_INTERVAL);
