# Minesweeper Project - Python Implementation

## About the Project

This project was developed in Python, using the **pygame** and **sqlite3** libraries. These technologies were chosen for their simplicity and suitability for developing basic games that do not require complex database relationships.

### Important Notes

- This code is not an ideal example for a project, as it contains several decisions that deviate from object-oriented programming principles.
- Python standards and conventions (PEP8) were not strictly followed.
- The code contains comments that may be considered "writing clutter" and are not relevant to the program's functionality.

## Code Structure

### Initial Configurations

Default configurations are defined, such as:

- **Colors**
- **Main variables**
- **Volume**
- **Fonts**
- **Images**
- **Screen settings**

### Main Loop

- The code begins in the main loop at the end, calling the `main_menu()` function.
- In the main menu, "Button" objects are created, receiving parameters such as size, name, and position.
- The loop waits for interactions (collisions) with the buttons, which return an "action" to the main loop.

### Starting the Game

- After selecting the options to play and naming a player, the match (`current_match`) starts.
- Field properties are defined based on the number of bombs and the map size.
- Two matrices are created:
  - **Base matrix**: Contains numbers, bombs, and empty fields.
  - **Game matrix**: Contains unrevealed boxes and flags.
- Flags and the luck counter are loaded on the screen before calling `request_image_rendering_user()`.

### Game Rendering

- Button settings are adjusted according to the difficulty level.
- An internal rendering loop begins:
  - **Main variables**:
    - `count`: Counts the loop iterations to calculate time.
    - `last_render`: Analyzes if the player won after the last click.
  - The loop updates the buttons only when clicks occur.

### Click Management

The `click_manager` function manages the actions performed in the game:

- It receives the matrix, size, and positions of the boxes in play.
- It checks two main actions:
  - **Right-click**: Sets a flag.
  - **Left-click**: Presses and opens the map.

---

## Requirements

- Python 3.x
- Required libraries:
  ```bash
  pip install pygame
