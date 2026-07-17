# 🐍 Snake Game

A modern implementation of the classic **Snake** game built in **Python** using **Object-Oriented Programming (OOP)** principles. Navigate the snake around the board, collect food to grow longer, and avoid colliding with the walls or yourself to achieve the highest score possible.

## Features

* 🐍 Smooth snake movement
* 🍎 Randomly generated food
* 📈 Live score tracking
* 🚀 Increasing challenge as the snake grows
* 💥 Collision detection with walls and the snake's body
* 🔄 Game over and restart functionality
* 🎮 Keyboard controls for intuitive gameplay
* 🧱 Clean object-oriented code structure

## How to Play

1. Run the game.
2. Control the snake using the arrow keys.
3. Eat food to increase your score and grow longer.
4. Avoid running into:

   * The walls
   * Your own tail
5. Try to achieve the highest score before the game ends!

## Controls

| Key | Action     |
| --- | ---------- |
| ↑   | Move Up    |
| ↓   | Move Down  |
| ←   | Move Left  |
| →   | Move Right |

## Technologies Used

* **Python**
* **Turtle Graphics**
* **Object-Oriented Programming (OOP)**

## Project Structure

```text
Snake-Game/
│
├── main.py          # Starts the game loop
├── snake.py         # Snake class and movement logic
├── food.py          # Food generation
├── scoreboard.py    # Score tracking and game over screen
└── README.md
```

## Object-Oriented Design

The project is organized into separate classes to keep the code modular and maintainable:

* **Snake** – Handles movement, growth, and body segments.
* **Food** – Randomly generates food across the game board.
* **Scoreboard** – Displays the current score and handles the game-over message.
* **Main** – Runs the game loop and coordinates interactions between all classes.

## Future Improvements

* 🎵 Sound effects and background music
* 🏆 High score saving
* ⚡ Multiple difficulty levels
* 🌈 Custom snake colors and themes
* 🍏 Special bonus food
* ⏸️ Pause and resume functionality
* 🖥️ Start menu and settings screen
* 🌍 Online leaderboard

## Example Gameplay

```text
Score: 12

🐍⬜⬜⬜⬜
⬜🍎⬜⬜⬜
⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜

↓

Snake eats the food...

↓

Score: 13
Snake grows longer!
```

## Purpose

This project was created to practice **Python programming** and **Object-Oriented Programming** by recreating one of the most iconic arcade games. It demonstrates concepts such as class design, event handling, collision detection, game loops, and state management in a fun and interactive application.
