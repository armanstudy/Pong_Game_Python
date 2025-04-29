# Pong Game

This is a step-by-step implementation of the classic Pong game using Python and the Turtle module.

## Game Features
The game consists of the following stages:
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with walls and bounce
6. Detect collision with paddles
7. Detect when a paddle misses the ball
8. Keep score

---

## Implementation Details

### 1. Create the Screen
- **Screen Size**: 800 (width) x 600 (height)
- **Title**: "PONG GAME"
- **Background Color**: Black

### 2. Create and Move a Paddle
- **Paddle Size**: 20 (width) x 100 (height)
- **Initial Position**: 
  - Paddle 1: (350, 0)
  - Paddle 2: (-350, 0)
- **Controls**:
  - Paddle 1: Arrow keys (`Up` to move up, `Down` to move down)
  - Paddle 2: `W` to move up, `S` to move down

### 3. Create Another Paddle
- The second paddle is created at position (-350, 0) and moves similarly to the first paddle.

### 4. Create the Ball and Make It Move
- The ball starts at the center of the screen (0, 0).
- It moves diagonally by default, with an initial speed of 0.1 seconds per frame.

### 5. Detect Collision with Walls and Bounce
- The ball bounces off the top and bottom walls by reversing its vertical direction.

### 6. Detect Collision with Paddles
- The ball bounces off the paddles by reversing its horizontal direction.
- Each paddle collision increases the ball's speed by 10%.

### 7. Detect When a Paddle Misses
- If the ball crosses the right boundary, the left paddle scores a point.
- If the ball crosses the left boundary, the right paddle scores a point.
- The ball resets to the center after a miss.

### 8. Keep Score
- The score is displayed at the top of the screen:
  - Left Paddle Score: Left side
  - Right Paddle Score: Right side
- The score updates dynamically as the game progresses.

---

## How to Run the Game
1. Ensure you have Python installed on your system.
2. Install the Turtle module (if not already installed).
3. Run the `main.py` file:
   ```bash
   python main.py