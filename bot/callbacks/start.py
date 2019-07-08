from telegram import Update, ParseMode
from telegram.ext import CallbackContext


def handle_start(update: Update, context: CallbackContext):
    del context
    update.effective_chat.send_message(
        "Здравствуй! Я помогу распознать QR и другие баркоды.\n\n"
        "*Для распознования отправьте мне фотографию.*",
        parse_mode=ParseMode.MARKDOWN,
    )
