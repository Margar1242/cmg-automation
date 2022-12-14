import os

BASE = os.environ.get('URL')
GAMES_DATA_URL = f'{BASE}/sites/default/files/cmatgame_games_with_levels.json'
GAME_NODE_JSON_URL = f'{BASE}/sites/default/files/likedislike/thumbsuplike_cmatgame_games_v1.json'

GAME_WITH_DIFFERENT_INSTRUCTIONS_SECTION = {
    '10x10 instructions': f'{BASE}/0-10x10',
    '2048 instructions': f'{BASE}/0-2048',
    '4 in a row instructions': f'{BASE}/0-4-in-a-row',
    'backgammon instructions': f'{BASE}/0-backgammon',
    'ball lines instructions': f'{BASE}/0-balllines',
    'how to play 8 ball pool': f'{BASE}/0-8-ball-pool',
    'beach soccer instructions': f'{BASE}/0-beach-soccer',
    'bouncing balls instructions': f'{BASE}/0-bouncingballs',
    'candy word instructions': f'{BASE}/0-candy-word',
    'checkers instructions': f'{BASE}/0-checkers',
    'chess instructions': f'{BASE}/0-chess',
    'chinese checkers instructions': f'{BASE}/0-chinesecheckers',
    'clicker heroes instructions': f'{BASE}/0-clicker-heroes',
    'copter royale instructions': f'{BASE}/0-copter-royale',
    'crazy eights instructions': f'{BASE}/0-crazy-eights',
    'crazy taxi m-12 instructions': f'{BASE}/0-crazy-taxi-m12',
    'daily crossword instructions': f'{BASE}/0-daily-crossword',
    'dominoes instructions': f'{BASE}/0-dominoes',
    'duck life instructions': f'{BASE}/0-duck-life',
    'factory balls instructions': f'{BASE}/0-factory-balls',
    'hangman instructions': f'{BASE}/0-hangman',
    'hearts instructions': f'{BASE}/0-hearts',
    'hidden objects instructions': f'{BASE}/0-hidden-objects-pirate-adventures',
    'how to play magic solitaire': f'{BASE}/0-magic-solitaire',
    'how to play snake': f'{BASE}/0-snake',
    'how to play tic tac toe': f'{BASE}/0-tic-tac-toe',
    'ludo instructions': f'{BASE}/0-ludo',
    'math man instructions': f'{BASE}/0-math-man',
    'minesweeper instructions': f'{BASE}/0-minesweeper',
    'misspelled instructions': f'{BASE}/0-misspelled',
    'nonogram instructions': f'{BASE}/0-nonogram',
    'puzzle blocks instructions': f'{BASE}/0-puzzle-blocks-ancient',
    'red ball instructions': f'{BASE}/0-red-ball-4',
    'retro ping pong instructions': f'{BASE}/0-retro-ping-pong',
    'reversi instructions': f'{BASE}/0-reversi',
    'run 3 instructions': f'{BASE}/0-run-3',
    'solitaire instructions': f'{BASE}/0-solitaire',
    'spider solitaire instructions': f'{BASE}/0-spider-solitaire',
    'sudoku instructions': f'{BASE}/0-sudoku',
    'sugar, sugar instructions': f'{BASE}/0-sugar-sugar',
    'swing monkey instructions': f'{BASE}/0-swing-monkey',
    'tingly bubble shooter instructions': f'{BASE}/0-tingly-bubble-shooter',
    'unolingo instructions': f'{BASE}/0-unolingo',
    'word detector instructions': f'{BASE}/0-word-detector',
    'word scramble instructions': f'{BASE}/0-wordscramble',
    'word search instructions': f'{BASE}/0-word-search',
    'word surge instructions': f'{BASE}/0-word-surge',
    'word worm instructions': f'{BASE}/0-word-worm',
    "word's party instructions": f'{BASE}/0-words-party',
    'words family instructions': f'{BASE}/0-words-family',
    'z-type instructions': f'{BASE}/0-z-type'
}
