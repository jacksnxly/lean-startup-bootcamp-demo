# Telegram Bot Demo - Task Breakdown

This document outlines the atomic tasks required to build the AI Social Network Telegram Bot Demo, following the PRD (docs/prd.md) and emphasizing a modular structure.

## Phase 1: Project Setup & Configuration

1.  **Initialize Project Structure:**
    *   Create main script file: `bot.py`.
    *   Create data directory: `data/`.
    *   Create templates module: `templates.py`.
    *   Create utility module (optional but recommended for modularity): `utils.py` (or a `utils/` directory).
2.  **Create `requirements.txt`:**
    *   Add dependencies: `python-telegram-bot[ext]==<LATEST_VERSION_SUPPORTED>` (Specify a recent version, e.g., 21.x as mentioned in PRD), `python-dotenv`.
3.  **Configure `.gitignore`:**
    *   Ensure common Python ignores (`__pycache__/`, `*.pyc`, `.env`, `venv/`, etc.) are present.

## Phase 2: Data & Templates

4.  **Create Mock User Data (`data/users.json`):**
    *   Define JSON structures for mock personas (Alex, Lena) including relevant details mentioned in PRD (name, age, location hint, golf details like handicap).
    *   Example structure:
        ```json
        {
          "alex": {"name": "Alex", "location": "Berlin"},
          "lena": {"name": "Lena S.", "age": 29, "handicap": 12, "availability": "09:00-14:00", "telegram_handle": "@lena_swing", "distance_km": 5}
        }
        ```
5.  **Create Data Loader Utility (`utils.py` or `data_loader.py`):**
    *   Implement a function `load_user_data()` to read and parse `users.json`.
6.  **Define Reply Templates (`templates.py`):**
    *   Define constants or functions for all bot replies mentioned in the PRD mock conversation (e.g., welcome message, golf query confirmation, match proposal, introduction confirmation).
    *   Include emojis as specified.

## Phase 3: Bot Logic Implementation

7.  **Basic Bot Setup (`bot.py`):**
    *   Import necessary libraries (`telegram`, `telegram.ext`, `dotenv`, `os`, `logging`, custom modules like `templates`, `utils`).
    *   Load environment variables (`load_dotenv`).
    *   Configure basic logging (`logging.basicConfig`).
    *   Get `TELEGRAM_BOT_TOKEN` from environment variables.
    *   Initialize `telegram.ext.Application.builder().token(TOKEN).build()`.
8.  **Implement `/start` Command (`bot.py`):**
    *   Create an async function `start(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None`.
    *   Use `update.message.reply_text()` to send the welcome message from `templates.py`.
    *   Register it in the main function using `application.add_handler(CommandHandler("start", start))`.
9.  **Implement `/reset` Command (`bot.py`):**
    *   Create an async function `reset(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None`.
    *   Send a simple confirmation message (e.g., "Demo state reset."). Since state is minimal/non-existent, no actual clearing needed.
    *   Register it using `CommandHandler("reset", reset)`.
10. **Implement `/match_golf` Command & Hardcoded Flow (`bot.py`):**
    *   Create an async function `match_golf(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None`.
    *   Load mock user data (Lena's details) using the data loader utility.
    *   Define the sequence of messages based on the PRD mock conversation, using templates from `templates.py`.
    *   Use `await asyncio.sleep(SECONDS)` between messages to simulate conversational pauses.
    *   For the message proposing Lena, create an `InlineKeyboardMarkup` with `InlineKeyboardButton`s for "Introduce 👋" and "Maybe later". Set dummy `callback_data` (e.g., `introduce_lena`, `later_lena`) - no handler needed for these as the flow proceeds automatically in the demo script.
    *   Send the final confirmation message ("Perfect! Here's Lena's contact...").
    *   Register it using `CommandHandler("match_golf", match_golf)`.

## Phase 4: Main Application Logic & Testing

11. **Create Main Execution Block (`bot.py`):**
    *   Define a `main()` async function.
    *   Inside `main()`, set up the application, add all command handlers.
    *   Run the bot using `application.run_polling()`.
    *   Use `if __name__ == "__main__": asyncio.run(main())`.
12. **Local Testing:**
    *   Run `pip install -r requirements.txt`.
    *   Run `python bot.py`.
    *   Interact with the bot in Telegram using `/start`, `/reset`, and the *secret* `/match_golf` command to verify the hardcoded flow.

## Phase 5: Documentation

13. **Update `README.md`:**
    *   Add clear instructions on how to set up the environment (`.env` file, dependencies).
    *   Explain how to run the bot (`python bot.py`).
    *   List the available commands, noting which are secret (`/match_golf`, `/reset`).
    *   Briefly describe the demo flow.
