import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hi {}!!</b>
<b>I'm Simple Auto file Forward Bot
This Bot forward all files to One Public channel to Your Personal channel
More details /help</b>"""
  CAPTION = "**{}**"
  HELP_TXT = """<b>Follow These Steps!!</b>
<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /forward command in your bot</b>

<b><u>Available Command</b></u>

<b>* /start - <b>Bot Alive</b>
* /help - <b>more help</b>
* /forward - <b>start forward</b>
* /about - About Me</b>"""
  ABOUT_TXT = """<b><u>My Info</b></u>

<b>Name :</b> <code>Auto Forward Bot</code>
<b>Credit :</b> <b>@Star_Bots_Tamil</b>
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Server :</b> <code>Heroku</code>
<b>Build :</b><code>V2.0</code>"""
