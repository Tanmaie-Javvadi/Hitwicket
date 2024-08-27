const socket = io('http://localhost:3000');

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('update_board', (board) => {
    renderBoard(board);
});

function renderBoard(board) {
    const boardDiv = document.getElementById('game-board');
    boardDiv.innerHTML = '';
    
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            let cell = document.createElement('div');
            cell.classList.add('cell');
            cell.innerText = board[row][col] || '';
            boardDiv.appendChild(cell);
        }
    }
}
