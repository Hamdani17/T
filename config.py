from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
API_ID = "29097464"
API_HASH = "5b6817dfb42ee608456658b3acd9df09"
BOT_USERNAME = "heloaa_bot"
session = "1AZWarzkBu6hmu1UFuivkJ9hoQq7GAgiLn-4yE8fwvbxgOkSXbWae-D33Ip7d3OBgyHO5PB2gpA-jO9_AmVO-Gv51TVd-S5zFTJHRCzC7qR1SZiujvEMFwXRTOxqJZCG0JjxXjcl4BWbQ6F5s6Gly0IleWMGecNTDvSkAWqwm29_IfobFvhUX2V-LquxUt0OBOWdUqRLRwe_MxQ6c7bPc1Asf7ZlwFdzR4vECjRB8qCTS-3cZg5rV3IwudlpaYIItEZ7o3QVxr_7A4keOIWOFpMwVu9q48zZTtLNZH859Oxo1tNBVqdxe8_Jrrc9tTXNiETxfubU7IfcpaH0YhX3ucaFNFewDFkk="
SESSION = "1AZWarzkBu6hmu1UFuivkJ9hoQq7GAgiLn-4yE8fwvbxgOkSXbWae-D33Ip7d3OBgyHO5PB2gpA-jO9_AmVO-Gv51TVd-S5zFTJHRCzC7qR1SZiujvEMFwXRTOxqJZCG0JjxXjcl4BWbQ6F5s6Gly0IleWMGecNTDvSkAWqwm29_IfobFvhUX2V-LquxUt0OBOWdUqRLRwe_MxQ6c7bPc1Asf7ZlwFdzR4vECjRB8qCTS-3cZg5rV3IwudlpaYIItEZ7o3QVxr_7A4keOIWOFpMwVu9q48zZTtLNZH859Oxo1tNBVqdxe8_Jrrc9tTXNiETxfubU7IfcpaH0YhX3ucaFNFewDFkk="
token = "6026602502:AAHpPpnFlYbWnvMkrV0DWC1oRLXTYMmtTC8"
sofethon = TelegramClient(StringSession(session), API_ID, API_HASH)
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
