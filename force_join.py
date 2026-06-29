"""
=========================================
Gezx Downloader
force_join.py
=========================================
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatMemberStatus

from config import FORCE_JOIN, CHANNEL_USERNAME
from constants import (
    FORCE_JOIN_TEXT,
    BTN_JOIN
)


async def is_user_joined(bot, user_id: int) -> bool:
    """
    Check whether a user has joined the required channel.
    """

    if not FORCE_JOIN:
        return True

    try:
        member = await bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=user_id
        )

        return member.status in (
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.MEMBER
        )

    except Exception:
        return False


async def check_force_join(update, context):
    """
    Returns True if the user is allowed to continue.
    Returns False after sending the join message.
    """

    if not FORCE_JOIN:
        return True

    joined = await is_user_joined(
        context.bot,
        update.effective_user.id
    )

    if joined:
        return True

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                BTN_JOIN,
                url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"
            )
        ]
    ])

    if update.message:
        await update.message.reply_text(
            FORCE_JOIN_TEXT,
            reply_markup=keyboard
        )

    elif update.callback_query:
        await update.callback_query.answer()

        await update.callback_query.message.reply_text(
            FORCE_JOIN_TEXT,
            reply_markup=keyboard
        )

    return False
