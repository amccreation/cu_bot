# from pyrogram import Client, filters
# import os
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# # Get the channel ids from environment variables
# PENDING = os.environ.get("PENDING")
# AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL")
#
# # Define the inline keyboard buttons
# accept_button = InlineKeyboardButton("Accept", callback_data="accept")
# reject_button = InlineKeyboardButton("Reject", callback_data="reject")
# keyboard = InlineKeyboardMarkup([[accept_button, reject_button]])
#
#
# # Create a handler for documents and photos
# @Client.on_message(filters.document | filters.photo)
# def forward_file(client, message):
#     # Forward the file to the pending channel with the keyboard
#     message.forward(PENDING).reply_markup(keyboard)
#
#
# # Create a handler for callback queries
# @Client.on_callback_query()
# def handle_callback(client, callback_query):
#     # Get the data from the callback query
#     data = callback_query.data
#
#     # If accept button is clicked
#     if data == "accept":
#         # Forward the file to the auth channel
#         callback_query.message.forward(AUTH_CHANNEL)
#         # Edit the message to show that it was accepted
#         callback_query.edit_message_text("Accepted!")
#
#     # If reject button is clicked
#     elif data == "reject":
#         # Edit the message to show that it was rejected
#         callback_query.edit_message_text("Rejected!")
#
#