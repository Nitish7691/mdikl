from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_MESSAGE = '''๐Hello, {}
๐ ๐๐ฎ๐ป ๐๐ผ๐ป๐๐ฒ๐ฟ๐ ๐๐ถ๐ป๐ธ ๐ง๐ผ ๐ฆ๐ต๐ผ๐ฟ๐๐๐ถ๐ป๐ธ. ๐ฆ๐ฒ๐ป๐ฑ ๐ ๐ฒ ๐๐ป๐ ๐ฃ๐ผ๐๐ ๐ช๐ถ๐๐ต ๐๐ถ๐ป๐ธ๐ ๐๐ป๐ฑ ๐ ๐ช๐ถ๐น๐น ๐ฆ๐ต๐ผ๐ฟ๐๐ฒ๐ป ๐๐น๐น ๐๐ถ๐ป๐ธ๐ ๐๐ป ๐๐ ๐๐ผ๐ป๐๐ฒ๐ฟ๐ ๐๐ผ EarnSpace.

โน๏ธ ๐๐ป๐ฑ ๐ต๐ผ๐ ๐๐ผ ๐๐๐ฒ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐ ๐ฎ๐ป๐ฑ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ ๐๐ผ ๐๐ฎ๐๐ฐ๐ต ๐บ๐ ๐๐ถ๐ฑ๐ฒ๐ผ.
'''


HELP_MESSAGE = '''
๐ค Help and bot not working Then contact me :-@earnspace_bot @nitish7691

โน๏ธ And how to use this bot and command so watch my video.
:-
'''


ABOUT_TEXT = """
๐ My all bot settings in bot command and my most best command list.

/header - set header text and click on command check out more info.

/footer - set footer text and click on command check out more info.

/username - set username and click on command check out more info.

/banner_image - set banner img and click on command check out more info.

/me - your account information and on|off all settings.

โน๏ธ And how to use this bot and command so watch my video.
:-
"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('๐  Home', callback_data='start_command')
    ]
])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('โ Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        
    ],
        [
        InlineKeyboardButton('โ๏ธ Settings', callback_data='about_command'),
        InlineKeyboardButton('โค๏ธ Channel', url='https://t.me/earnspaceofficial')
    ],
            [
        InlineKeyboardButton('โ๏ธ Connect To Earnspace', url='https://earnspace.in/member/tools/api'),
    ],


])


BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('๐ซฅ Back', callback_data=f'start_command')
    ],

])

USER_ABOUT_MESSAGE = """
โณ๏ธ Shortener Website: {base_site}

โณ๏ธ {base_site} API: {shortener_api}

โณ๏ธ Username: @{username}

โณ๏ธ Header Text: {header_text}

โณ๏ธ Footer Text: {footer_text}

โณ๏ธ Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """โTo add or update your Shortner Website API, `/shortener_api api`
            
โณ๏ธEx: `/shortener_api 6LZq851sXofffPHugiKQq`
            
โณ๏ธShortener API of your preferred shortener API.

โณ๏ธCurrent Website: {base_site}

โณ๏ธCurrent Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """โReply to the Header Text You Want

โณ๏ธThis Text will be added to the top of every message caption or text

โณ๏ธTo Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """โReply to the Footer Text You Want

โณ๏ธThis Text will be added to the bottom of every message caption or text

โณ๏ธTo Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """โCurrent Username: {username}

โณ๏ธUsage: `/username your_username`

โณ๏ธFor just removing the username from the post: 
`/username none`

โณ๏ธThis username will be automatically replaced with other usernames in the post

โณ๏ธTo remove current username, `/username remove`"""

BANNER_IMAGE = """โCurrent Banner Image URL: {banner_image}

โณ๏ธUsage: `/banner_image image_url`

โณ๏ธThis image will be automatically replaced with other images in the post

โณ๏ธTo remove custom image, `/banner_image remove`

โณ๏ธEg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

