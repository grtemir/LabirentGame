# LabirentGame

A level-based maze game developed using Python and the Pygame library.

## ℹ️ Note on AI Usage

This project is part of my learning process for Python and game development logic. **Significant support was received from AI tools** during the writing of the code, debugging, and the implementation of game mechanics (such as the field of view/fog of war and collision detection).

The goal is to create a functional game to understand the underlying code structure and logic.

## 🎮 Features

* **Fog of War:** The player cannot see the entire maze; only a small area around the character is visible. This adds mystery and difficulty to the game.
* **Level System:** Includes 3 different maze designs. Reaching the exit automatically advances the player to the next level.
* **Audio Effects:** Includes background music and movement sound effects.
* **Simple Controls:** Easily playable using arrow keys.

## 🛠️ Installation

To run this project, you need to have Python and the `pygame` library installed.

1.  **Install Requirements:**
    Run the following command in your terminal or command prompt:
    ```bash
    pip install pygame
    ```

2.  **Prepare Assets:**
    Ensure the following sound files are in the same directory as `main.py`:
    * `slow-2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3`
    * `gameboy-pluck-41265-[AudioTrimmer.com].wav`

    *(Note: The game may crash if these files are missing. You might need to remove the audio lines from the code if you don't have them.)*

3.  **Run the Game:**
    ```bash
    python main.py
    ```

## 🕹️ How to Play

* **Blue Box:** Your character.
* **Green Area (G):** The exit point you need to reach.
* **Arrow Keys:** Used to move the character.
* You cannot move through walls (Black areas).

