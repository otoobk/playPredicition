/* Global data */
// Field
const field = document.getElementById("field");

const fieldBounds = field.getBoundingClientRect();
const fieldLeft = fieldBounds.left;
const fieldTop = fieldBounds.top;
const fieldWidth = field.clientWidth;
const fieldHeight = field.clientHeight;

// Line of scrimmage
const footballPosition = {x: 49, y: 69};
const lineOfScrim = footballPosition.y

// Initial player positions
const playerPositions = [
  { x: 68, y: lineOfScrim - 10 },
  { x: 82, y: lineOfScrim - 7},
  { x: 23, y: lineOfScrim - 7},
  { x: 37, y: lineOfScrim - 25},
  { x: 61, y: lineOfScrim - 32},
  { x: 57, y: lineOfScrim - 15},
  { x: 45, y: lineOfScrim - 14},
  { x: 42, y: lineOfScrim - 4},
  { x: 47, y: lineOfScrim - 4},
  { x: 52, y: lineOfScrim - 4},
  { x: 57, y: lineOfScrim - 4},
];

const originalPositions = [...playerPositions]; // Store the original positions

/* Generate dynamic elements */
// Generate 11 players
for (let i = 0; i < 11; i++) {
  const player = document.createElement('div');
  player.classList.add('player');

  // Calculate player positions relative to the field
  const playerX = (fieldWidth * playerPositions[i].x) / 100;
  const playerY = (fieldHeight * playerPositions[i].y) / 100;

  player.style.left = playerX + 'px';
  player.style.top = playerY + 'px';

  makeDraggable(player);

  field.appendChild(player);
};

// Generate football
const football = document.createElement('div');
const marker = document.createElement('div');
football.classList.add('football');
marker.classList.add('marker');

const footballX = (fieldWidth * footballPosition.x) / 100;
const footballY = (fieldHeight * footballPosition.y) / 100;

const markerY = footballY

football.style.left = footballX + 'px';
football.style.top = footballY + 'px';

marker.style.left = 7 + 'px';
marker.style.top = markerY + 'px';

field.appendChild(football);
field.appendChild(marker);

/* Functionality */
// Make element draggable
function makeDraggable(el) {
  let pos = { x: 0, y: 0 };
  let isDragging = false;
  let parent = field;

  el.addEventListener('mousedown', e => {
    e.preventDefault(); // Prevent text selection
    isDragging = true;
    pos = {
      x: e.clientX,
      y: e.clientY
    };

    document.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', stopDrag);
  });

  function drag(e) {
    if (!isDragging) return;

    e.preventDefault(); // Prevent text selection

    let dx = e.clientX - pos.x;
    let dy = e.clientY - pos.y;

    // Calculate the new position
    let newX = el.offsetLeft + dx;
    let newY = el.offsetTop + dy;

    // Calculate the bounds for the player
    let playerWidth = el.clientWidth;
    let playerHeight = el.clientHeight;

    // Limit the player's position to stay within the parent's bounds
    newX = Math.min(Math.max(newX, 0), fieldWidth - playerWidth);
    newY = Math.min(Math.max(newY, 0), (fieldHeight * lineOfScrim) / 100);

    el.style.left = newX + 'px';
    el.style.top = newY + 'px';

    pos = { x: e.clientX, y: e.clientY };
  }

  function stopDrag() {
    isDragging = false;
    document.removeEventListener('mousemove', drag);
    document.removeEventListener('mouseup', stopDrag);
  }
};

// Reset button click event
const resetButton = document.querySelector('.reset-btn');

resetButton.addEventListener('click', () => {
  const players = document.querySelectorAll('.player');

  subheader.textContent = 'A short description of the last play'

  // Iterate through the players and reset their positions
  for (let i = 0; i < players.length; i++) {
    players[i].style.left = playerPositions[i].x + "%";
    players[i].style.top = playerPositions[i].y + "%";
  }
});

// Submit button click event
const submitButton = document.querySelector('.submit-btn');

submitButton.addEventListener('click', () => {
  const players = document.querySelectorAll('.player');

  playerXCoords = []
  playerYCoords = []
  // Iterate through the players and reset their positions
  for (let i = 0; i < players.length; i++) {
    const playerLoc = players[i].getBoundingClientRect();
    const xCoord = playerLoc.left
    const yCoord = fieldHeight - playerLoc.top
    playerXCoords.push(xCoord);
    playerYCoords.push(yCoord);
  }

  const subheader = document.getElementById("subheader");
  let subheaderStr = "("

  // Loop through the array and append values to the div
  for (let i = 0; i < playerXCoords.length; i++) {
    subheaderStr += playerXCoords[i];
    subheaderStr += ", ";
    subheaderStr += playerYCoords[i];

    // Add a comma and space after each value (except the last one)
    if (i < playerXCoords.length - 1) {
      subheaderStr += "), (";
    } else {
      subheaderStr += ")";
    }
  }

  subheader.textContent = subheaderStr;

  const url = "http://localhost:8000/api/data";
  const request_data = {data: subheaderStr};

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    }, 
    body: JSON.stringify(request_data),
  })
    .then(response => response.json())
    .then(result => {
      console.log("Response form backend:", result);
    })
    .catch(error => {
      console.error("Error:", error);
    });
});
