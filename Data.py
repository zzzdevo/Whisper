from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}.
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

I ᴀᴍ ᴛʜᴇ Mᴀsᴛᴇʀ ᴏғ Wʜɪsᴘᴇʀᴇʀs (ʟɪᴋᴇ Vᴀʀʏs ɪɴ Gᴀᴍᴇ ᴏғ Tʜʀᴏɴᴇs).

Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ sᴇɴᴅ ᴡʜɪsᴘᴇʀs ᴛᴏ ʏᴏᴜʀ ғʀɪᴇɴᴅ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs (ᴇᴠᴇɴ ɪғ I'ᴍ ɴᴏᴛ ᴛʜᴇʀᴇ).
Oɴʟʏ ᴛʜᴀᴛ ғʀɪᴇɴᴅ ᴀɴᴅ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀʙʟᴇ ᴛᴏ ʀᴇᴀᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴇᴠᴇɴ ᴛʜᴏᴜɢʜ ᴏᴛʜᴇʀs ᴀʀᴇ ɪɴ sᴀᴍᴇ ɢʀᴏᴜᴘ. 

Tᴏ sᴇᴇ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴘʀᴇss 'Hᴏᴡ ᴛᴏ Usᴇ' ʙᴇʟᴏᴡ.

ʙʏ @ZSZZ7
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔐 Sᴇɴᴅ ᴀ Wʜɪsᴘᴇʀ 🔐", switch_inline_query="")],
        [InlineKeyboardButton(text="Rᴇᴛᴜʀɴ Hᴏᴍᴇ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔐 Sᴇɴᴅ ᴀ Wʜɪsᴘᴇʀ 🔐", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("Hᴏᴡ ᴛᴏ Usᴇ ❔", callback_data="help"),
            InlineKeyboardButton("❄️ Aʙᴏᴜᴛ ❄️", callback_data="about")
        ],
        [InlineKeyboardButton("Mᴏʀᴇ Aᴍᴀᴢɪɴɢ ʙᴏᴛs", url="https://t.me/ZSZZ7")],
        [InlineKeyboardButton("💸 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 💸", url="https://t.me/ZSZZ7")],
    ]

    # Help Message
    HELP = """
Jᴜsᴛ ᴛʏᴘᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ ʙᴇʟᴏᴡ ғᴏʀᴍᴀᴛ ɪɴ ᴀɴʏ ᴄʜᴀᴛ.

@zdevobot ʏᴏᴜʀ_ᴍᴇssᴀɢᴇ ғʀɪᴇɴᴅ_ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ
    """

    # About Message
    ABOUT = """
Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ 

Bᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ @ZSZZ7

Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : [Cʟɪᴄᴋ Hᴇʀᴇ](https://github.com/Devansh-Bots/DevXWhisperBot)

Iɴsᴘɪʀᴇᴅ Bʏ : ɴɴʙʙᴏᴛ

Fʀᴀᴍᴇᴡᴏʀᴋ : [Pʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

Lᴀɴɢᴜᴀɢᴇ : [Pʏᴛʜᴏɴ](www.python.org)

Dᴇᴠᴇʟᴏᴘᴇʀ : @ZSZZ7
    """
