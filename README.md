# Space Invaders Game

## Overview

**Space Invaders** is a classic arcade game where you control a spaceship to shoot down waves of descending aliens. Your objective is to eliminate all the aliens before they reach the bottom of the screen.

## Features

- **Player Controls:** Move the spaceship left and right with arrow keys and shoot bullets with the space bar.
- **Dynamic Enemies:** Aliens move horizontally and drop down when they hit the screen edges.
- **Scoring System:** Earn points by hitting enemies with bullets.
- **Game Over & Restart:** The game ends if an alien reaches the bottom. Press 'R' to restart.

## Gameplay

1. **Movement:** Use the left and right arrow keys to move your spaceship.
2. **Shooting:** Press the space bar to fire bullets.
3. **Enemy Behavior:** Aliens move left and right, and descend when hitting the screen edges.
4. **Collision Detection:** Bullets that hit aliens will destroy them and update the score.
5. **Game Over:** The game ends if an alien reaches the bottom of the screen. A game over screen will appear, and you can press 'R' to restart.

## Installation

To set up and run the game locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Shreyasingh911/Space-Invaders.git
Navigate to the Project Directory:

bash
Copy code
cd Space-Invaders
Install Dependencies: Make sure you have Python and Pygame installed. Install Pygame with pip:

bash
Copy code
pip install pygame
Run the Game: Start the game by executing the script:

bash
Copy code
python space_invaders.py
Challenges and Solutions
Collision Detection:

Challenge: Ensuring accurate detection of collisions between bullets and enemies.
Solution: Implemented distance calculations for precise collision detection.
Enemy Movement:

Challenge: Achieving smooth and responsive movement with boundary handling.
Solution: Used horizontal movement with edge boundary checks.
Game Over Handling:

Challenge: Managing the game over screen and restart functionality.
Solution: Added a game over screen with a restart option controlled by user input.
Key Learnings
Game Development: Gained hands-on experience with game mechanics and Pygame library.
Problem-Solving: Improved skills in debugging and refining game logic.
Links
Development Video: https://www.youtube.com/watch?v=FfWpgLFMI7w
GitHub Repository: https://github.com/Shreyasingh911
Feel free to explore the game, provide feedback, or contribute to the project!






