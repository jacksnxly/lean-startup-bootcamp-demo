import logging
import os
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters
)

# Import project modules
import templates
import utils

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Get Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

# --- Conversation States ---
(WAITING_REPLY_1, WAITING_REPLY_2, WAITING_REPLY_3, WAITING_REPLY_4, WAITING_REPLY_5) = range(5)

# --- Command Handlers --- 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the AI avatar image and the initial prompt with a button when /start is issued."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    logger.info(f"Received /start command from user {user_id} in chat {chat_id}")

    # Send the avatar image first
    avatar_path = '/Users/jacksonly/Projects/lean-startup-bootcamp-demo/assets/images/Avatar-20.png'
    try:
        logger.info(f"Sending avatar image {avatar_path} to chat {chat_id}")
        await context.bot.send_photo(chat_id=chat_id, photo=open(avatar_path, 'rb'))
        logger.info(f"Successfully sent avatar image to chat {chat_id}")
    except FileNotFoundError:
        logger.error(f"Avatar image not found at {avatar_path}")
        # Optionally send a fallback message if image fails
        # await update.message.reply_text("Could not load avatar image.")
    except Exception as e:
        logger.error(f"Error sending avatar image to chat {chat_id}: {e}", exc_info=True)

    # Then send the prompt with the button
    keyboard = [
        [InlineKeyboardButton(templates.START_CHAT_BUTTON, callback_data='start_chat')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(templates.START_PROMPT, reply_markup=reply_markup)

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a confirmation message when the /reset command is issued."""
    logger.info(f"Received /reset command from user {update.effective_user.id}")
    await update.message.reply_text(templates.RESET_CONFIRMATION)
    # Potentially clear user_data if needed: context.user_data.clear()
    # For ConversationHandler, returning END is usually done within the conversation

# --- Conversation Handler Functions ---

async def start_chat_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation when the 'Start Chat' button is pressed."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    await query.answer()
    logger.info(f"'{templates.START_CHAT_BUTTON}' clicked by user {user_id}. Starting conversation.")

    try:
        # Remove the button from the original message
        await query.edit_message_reply_markup(reply_markup=None)
        # Send Imane's first line
        await context.bot.send_message(chat_id=chat_id, text=templates.START_CHAT_FOLLOW_UP)
        # Transition to the state waiting for the user's first reply
        return WAITING_REPLY_1
    except Exception as e:
        logger.error(f"Error starting conversation for user {user_id}: {e}", exc_info=True)
        await context.bot.send_message(chat_id=chat_id, text="Sorry, couldn't start the chat properly.")
        return ConversationHandler.END

async def reply_1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles user's first reply, sends Imane's second line."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    user_text = update.message.text
    logger.info(f"User {user_id} (state WAITING_REPLY_1) said: {user_text}")
    await asyncio.sleep(2.5) # Simulate thinking time
    await context.bot.send_message(chat_id=chat_id, text=templates.IMANE_LINE_2)
    return WAITING_REPLY_2

async def reply_2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles user's second reply, sends Imane's third line."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    user_text = update.message.text
    logger.info(f"User {user_id} (state WAITING_REPLY_2) said: {user_text}")
    await asyncio.sleep(2.5)
    await context.bot.send_message(chat_id=chat_id, text=templates.IMANE_LINE_3)
    return WAITING_REPLY_3

async def reply_3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles user's third reply, sends Imane's fourth line."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    user_text = update.message.text
    logger.info(f"User {user_id} (state WAITING_REPLY_3) said: {user_text}")
    await asyncio.sleep(3)
    await context.bot.send_message(chat_id=chat_id, text=templates.IMANE_LINE_4)
    return WAITING_REPLY_4

async def reply_4_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles user's fourth reply, sends Imane's fifth line."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    user_text = update.message.text
    logger.info(f"User {user_id} (state WAITING_REPLY_4) said: {user_text}")
    await asyncio.sleep(2.5)
    await context.bot.send_message(chat_id=chat_id, text=templates.IMANE_LINE_5)
    return WAITING_REPLY_5

async def reply_5_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles user's fifth reply, sends Imane's final line and contact card."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    user_text = update.message.text
    logger.info(f"User {user_id} (state WAITING_REPLY_5) said: {user_text}")
    await asyncio.sleep(3)

    # Send final intro line
    await context.bot.send_message(chat_id=chat_id, text=templates.IMANE_LINE_6)
    await asyncio.sleep(1.5)

    # Load Fabio Data
    try:
        users = utils.load_user_data()
        fabio_data = users.get('fabio', {})
        if not fabio_data:
            raise ValueError("Fabio data not found in users.json")

        # Prepare contact card caption
        contact_caption = templates.CONTACT_CARD_CAPTION.format(
            name=fabio_data.get('name', 'N/A'),
            hcp=fabio_data.get('hcp', 'N/A'),
            distance_km=fabio_data.get('distance_km', 'N/A'),
            loves_match_play=fabio_data.get('loves_match_play', '')
        ).strip()
        
        # Prepare Contact Card Buttons
        fabio_name = fabio_data.get('name', 'Fabio')
        keyboard = [
            [InlineKeyboardButton(templates.CHAT_BUTTON.format(name=fabio_name), callback_data='chat_fabio')],
            [InlineKeyboardButton(templates.DISMISS_BUTTON, callback_data='dismiss_fabio')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send Fabio Contact Card Image with Caption and Buttons
        fabio_image_path = '/Users/jacksonly/Projects/lean-startup-bootcamp-demo/assets/images/fabio.jpg'
        logger.info(f"Sending Fabio contact image {fabio_image_path} with buttons to chat {chat_id}")
        await context.bot.send_photo(
            chat_id=chat_id, 
            photo=open(fabio_image_path, 'rb'), 
            caption=contact_caption, 
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=reply_markup
        )
        logger.info(f"Successfully sent Fabio contact image with buttons to chat {chat_id}")

    except FileNotFoundError:
        logger.error(f"Fabio contact image not found at {fabio_image_path}. Cannot proceed with contact card.")
        await context.bot.send_message(chat_id=chat_id, text="Oops, I couldn't find the contact card image.")
    except ValueError as ve:
         logger.error(f"Data error for Fabio contact card: {ve}")
         await context.bot.send_message(chat_id=chat_id, text="Oops, couldn't load the contact details correctly.")
    except Exception as e:
        logger.error(f"Error sending Fabio contact card for user {user_id}: {e}", exc_info=True)
        await context.bot.send_message(chat_id=chat_id, text="Sorry, something went wrong showing the contact card.")

    # End the conversation
    logger.info(f"Ending conversation for user {user_id}")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info(f"User {user.id} canceled the conversation.")
    await update.message.reply_text(
        "Okay, cancelling our current chat flow. You can start again with /start if you like."
    )
    return ConversationHandler.END

# --- Standalone Button Handlers (for after conversation ends) ---
async def fabio_chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles 'Chat with Fabio' button click."""
    query = update.callback_query
    await query.answer()
    logger.info(f"'Chat with Fabio' button clicked by user {query.from_user.id}")
    await query.message.reply_text("Great! Connecting you... (Feature not implemented yet)")
    await query.edit_message_reply_markup(reply_markup=None) # Remove buttons

async def fabio_dismiss_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles 'Dismiss Fabio' button click."""
    query = update.callback_query
    await query.answer()
    logger.info(f"'Dismiss Fabio' button clicked by user {query.from_user.id}")
    await query.message.reply_text("Okay, dismissed.")
    await query.edit_message_reply_markup(reply_markup=None) # Remove buttons


# --- Main Function --- 
async def main() -> None:
    """Start the bot."""
    logger.info("Building application...")
    application = Application.builder().token(TOKEN).build()

    logger.info("Registering handlers...")
    # Conversation handler for the main chat flow
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(start_chat_callback, pattern='^start_chat$')],
        states={
            WAITING_REPLY_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, reply_1_handler)],
            WAITING_REPLY_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, reply_2_handler)],
            WAITING_REPLY_3: [MessageHandler(filters.TEXT & ~filters.COMMAND, reply_3_handler)],
            WAITING_REPLY_4: [MessageHandler(filters.TEXT & ~filters.COMMAND, reply_4_handler)],
            WAITING_REPLY_5: [MessageHandler(filters.TEXT & ~filters.COMMAND, reply_5_handler)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)

    # Standard command handlers (outside conversation)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reset", reset))

    # Handlers for Fabio buttons (after conversation ends)
    application.add_handler(CallbackQueryHandler(fabio_chat_handler, pattern='^chat_fabio$'))
    application.add_handler(CallbackQueryHandler(fabio_dismiss_handler, pattern='^dismiss_fabio$'))

    logger.info("Starting bot polling...")
    await application.initialize() 
    await application.start()
    await application.updater.start_polling()
    logger.info("Bot is running. Press Ctrl-C to stop.")
    while True:
        await asyncio.sleep(3600) 

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.critical(f"Bot encountered critical error: {e}", exc_info=True)
