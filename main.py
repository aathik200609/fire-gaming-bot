import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)

# ---------------- CONFIGURATION ----------------
BOT_TOKEN = "8829333266:AAEkqlWsZZR1WrF0KjC3jZR33ffwXtXGiJA"
ADMIN_CHAT_ID = 8802337629  # Aathik's Chat ID

# Conversation States
GET_UID, GET_RECEIPT = range(2)

# Price Catalog (LKR)
PRICES = {
    # Diamonds
    "d_25": {"name": "💎 25 Diamonds", "price": "Rs 85.00"},
    "d_50": {"name": "💎 50 Diamonds", "price": "Rs 170.00"},
    "d_100": {"name": "💎 100 Diamonds", "price": "Rs 320.00"},
    "d_200": {"name": "💎 200 Diamonds", "price": "Rs 630.00"},
    "d_310": {"name": "💎 310 Diamonds", "price": "Rs 955.00"},
    "d_520": {"name": "💎 520 Diamonds", "price": "Rs 1,550.00"},
    "d_1060": {"name": "💎 1060 Diamonds", "price": "Rs 3,100.00"},
    "d_2120": {"name": "💎 2120 Diamonds", "price": "Rs 6,200.00"},
    "d_5600": {"name": "💎 5600 Diamonds", "price": "Rs 15,450.00"},
    "d_11500": {"name": "💎 11500 Diamonds", "price": "Rs 31,500.00"},

    # Memberships
    "m_weekly": {"name": "👑 WEEKLY Membership", "price": "LKR 560"},
    "m_monthly": {"name": "👑 MONTHLY Membership", "price": "LKR 2,800"},
    "m_m_w": {"name": "👑 MONTHLY + WEEKLY", "price": "LKR 3,360"},
    "m_m_w4": {"name": "👑 MONTHLY + WEEKLY x4", "price": "LKR 5,040"},
    "m_w_lite": {"name": "👑 WEEKLY LITE", "price": "LKR 130"},

    # Level Up Pass
    "lvl_6": {"name": "📈 Level 6 Pass", "price": "Rs 120.00"},
    "lvl_10": {"name": "📈 Level 10 Pass", "price": "Rs 235.00"},
    "lvl_15": {"name": "📈 Level 15 Pass", "price": "Rs 235.00"},
    "lvl_20": {"name": "📈 Level 20 Pass", "price": "Rs 235.00"},
    "lvl_25": {"name": "📈 Level 25 Pass", "price": "Rs 235.00"},
    "lvl_30": {"name": "📈 Level 30 Pass", "price": "Rs 340.00"},
    "lvl_full": {"name": "📈 Level Up Pass - Full", "price": "Rs 1,390.00"},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Diamond Top-Up", callback_data='menu_diamonds')],
        [InlineKeyboardButton("👑 Membership Packages", callback_data='menu_membership')],
        [InlineKeyboardButton("📈 Level Up Pass", callback_data='menu_levelup')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔥 **Welcome to Fire Gaming Diamond Store** 🔥\n\n"
        "Select a category below to browse packages:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'menu_diamonds':
        keyboard = [
            [InlineKeyboardButton("💎 25 - Rs 85", callback_data='d_25'), InlineKeyboardButton("💎 50 - Rs 170", callback_data='d_50')],
            [InlineKeyboardButton("💎 100 - Rs 320", callback_data='d_100'), InlineKeyboardButton("💎 200 - Rs 630", callback_data='d_200')],
            [InlineKeyboardButton("💎 310 - Rs 955", callback_data='d_310'), InlineKeyboardButton("💎 520 - Rs 1,550", callback_data='d_520')],
            [InlineKeyboardButton("💎 1060 - Rs 3,100", callback_data='d_1060')],
            [InlineKeyboardButton("💎 2120 - Rs 6,200", callback_data='d_2120')],
            [InlineKeyboardButton("💎 5600 - Rs 15,450", callback_data='d_5600')],
            [InlineKeyboardButton("💎 11500 - Rs 31,500", callback_data='d_11500')],
            [InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main_menu')]
        ]
        await query.edit_message_text("💎 **Diamond Top-Up Packages:**", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == 'menu_membership':
        keyboard = [
            [InlineKeyboardButton("👑 WEEKLY - LKR 560", callback_data='m_weekly')],
            [InlineKeyboardButton("👑 MONTHLY - LKR 2,800", callback_data='m_monthly')],
            [InlineKeyboardButton("👑 MONTHLY + WEEKLY - LKR 3,360", callback_data='m_m_w')],
            [InlineKeyboardButton("👑 MONTHLY + WEEKLY x4 - LKR 5,040", callback_data='m_m_w4')],
            [InlineKeyboardButton("👑 WEEKLY LITE - LKR 130", callback_data='m_w_lite')],
            [InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main_menu')]
        ]
        await query.edit_message_text("👑 **Membership Packages:**", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == 'menu_levelup':
        keyboard = [
            [InlineKeyboardButton("📈 Level 6 - Rs 120", callback_data='lvl_6'), InlineKeyboardButton("📈 Level 10 - Rs 235", callback_data='lvl_10')],
            [InlineKeyboardButton("📈 Level 15 - Rs 235", callback_data='lvl_15'), InlineKeyboardButton("📈 Level 20 - Rs 235", callback_data='lvl_20')],
            [InlineKeyboardButton("📈 Level 25 - Rs 235", callback_data='lvl_25'), InlineKeyboardButton("📈 Level 30 - Rs 340", callback_data='lvl_30')],
            [InlineKeyboardButton("📈 Level Up Pass (Full) - Rs 1,390", callback_data='lvl_full')],
            [InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main_menu')]
        ]
        await query.edit_message_text("📈 **Level Up Pass Packages:**", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == 'main_menu':
        keyboard = [
            [InlineKeyboardButton("💎 Diamond Top-Up", callback_data='menu_diamonds')],
            [InlineKeyboardButton("👑 Membership Packages", callback_data='menu_membership')],
            [InlineKeyboardButton("📈 Level Up Pass", callback_data='menu_levelup')],
        ]
        await query.edit_message_text("🔥 **Welcome to Fire Gaming Diamond Store** 🔥\n\nSelect a category below to browse packages:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data in PRICES:
        selected = PRICES.get(data)
        context.user_data['selected_pack'] = selected['name']
        context.user_data['price'] = selected['price']

        await query.edit_message_text(
            f"✅ You selected: **{selected['name']}** ({selected['price']})\n\n"
            "Please enter your **Free Fire Player ID (UID)**:",
            parse_mode="Markdown"
        )
        return GET_UID

async def receive_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_uid = update.message.text
    context.user_data['player_uid'] = user_uid

    payment_info = (
        f"📝 **Order Summary:**\n"
        f"• Package: {context.user_data['selected_pack']}\n"
        f"• Player UID: `{user_uid}`\n"
        f"• Total Price: {context.user_data['price']}\n\n"
        f"💳 **Payment Instructions:**\n"
        f"• **eZ Cash Number:** `0771033703`\n"
        f"• **WhatsApp Support:** `0771033703`\n\n"
        f"Please make the payment and upload your **Payment Receipt / Screenshot** here as an image."
    )
    await update.message.reply_text(payment_info, parse_mode="Markdown")
    return GET_RECEIPT

async def receive_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    user = update.message.from_user

    admin_text = (
        f"🚨 **NEW TOP-UP ORDER** 🚨\n\n"
        f"👤 Customer: @{user.username or user.first_name} (ID: `{user.id}`)\n"
        f"💎 Package: {context.user_data['selected_pack']}\n"
        f"🎯 Player UID: `{context.user_data['player_uid']}`\n"
        f"💰 Price: {context.user_data['price']}"
    )

    admin_keyboard = [
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user.id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user.id}")
        ]
    ]

    await context.bot.send_photo(
        chat_id=ADMIN_CHAT_ID,
        photo=photo_file.file_id,
        caption=admin_text,
        reply_markup=InlineKeyboardMarkup(admin_keyboard),
        parse_mode="Markdown"
    )

    await update.message.reply_text(
        "✅ **Receipt Received!**\n\n"
        "Our admin will verify your payment and process your top-up within 1–5 minutes. Thank you!"
    )
    return ConversationHandler.END

async def admin_action_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.from_user.id != ADMIN_CHAT_ID:
        await query.answer("Unauthorized action.", show_alert=True)
        return

    data = query.data
    action, user_id = data.split("_")
    user_id = int(user_id)

    if action == "approve":
        await context.bot.send_message(
            chat_id=user_id,
            text="🎉 **Order Approved!**\n\nYour diamonds/package have been successfully credited to your Free Fire account. Thank you for buying from Fire Gaming Diamond Store! 🔥",
            parse_mode="Markdown"
        )
        await query.edit_message_caption(
            caption=f"{query.message.caption}\n\n✅ **STATUS: APPROVED**",
            parse_mode="Markdown"
        )
    elif action == "reject":
        await context.bot.send_message(
            chat_id=user_id,
            text="❌ **Order Rejected**\n\nYour payment receipt could not be verified. Please contact support via WhatsApp: `0771033703`.",
            parse_mode="Markdown"
        )
        await query.edit_message_caption(
            caption=f"{query.message.caption}\n\n❌ **STATUS: REJECTED**",
            parse_mode="Markdown"
        )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Operation cancelled.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(menu_handler, pattern="^(menu_|d_|m_|lvl_|main_menu)")],
        states={
            GET_UID: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_uid)],
            GET_RECEIPT: [MessageHandler(filters.PHOTO, receive_receipt)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(CallbackQueryHandler(admin_action_handler, pattern="^(approve_|reject_)"))

    print("Fire Gaming Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
