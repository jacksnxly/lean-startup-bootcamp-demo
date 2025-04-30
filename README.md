# AI Social Network Telegram Bot Demo

This project is a proof-of-concept Telegram bot that simulates an AI social network where users can find activity partners through their personal "AI Friend". This version demonstrates a hardcoded flow for finding a golf partner.

Based on the PRD in `docs/prd.md`.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd lean-startup-bootcamp-demo
    ```

2.  **Create environment file:**
    *   Create a file named `.env` in the project root.
    *   Add your Telegram Bot Token to it:
        ```
        TELEGRAM_BOT_TOKEN=YOUR_ACTUAL_BOT_TOKEN
        ```

3.  **Install dependencies:**
    *   It's recommended to use a virtual environment:
        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```
    *   Install the required packages:
        ```bash
        pip install -r requirements.txt
        ```

## Running the Bot

1.  Make sure your `.env` file is configured and dependencies are installed.
2.  Run the bot script:
    ```bash
    python bot.py
    ```
3.  The bot will start polling for messages. You can stop it by pressing `Ctrl+C` in the terminal.

## Interacting with the Bot

Open Telegram and find your bot.

*   **/start**: Initiates the conversation and shows the welcome message.
*   **/reset** (Secret): Resets any minimal bot state (mostly for demo purposes, as state is not really stored).
*   **/match_golf** (Secret): Triggers the hardcoded golf matchmaking demo flow, simulating a user request and the AI finding a match (Lena).

## Project Structure

```
.env                  # Environment variables (TELEGRAM_BOT_TOKEN)
.gitignore            # Git ignore rules
README.md             # This file
requirements.txt      # Python dependencies
bot.py                # Main bot script with command handlers
templates.py          # Bot reply message templates
utils.py              # Utility functions (e.g., data loading)
data/
└── users.json        # Mock user data for the demo
docs/
├── TASK.md           # Development task breakdown
└── prd.md            # Product Requirements Document
```
