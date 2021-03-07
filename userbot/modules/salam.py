from platform import uname
from time import sleep

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ppp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("salam biar ~~ganteng~~ berkah")
    sleep(1)
    await typew.edit("assalamu'alaikum")


@register(outgoing=True, pattern="^.lll(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam")


@register(outgoing=True, pattern="^.lll(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam")


CMD_HELP.update(
    {
        "salam": "`.ppp`\
\nUsage: Untuk Memberi salam.\
\n\n`.lll`\
\nUsage: Untuk Menjawab Salam."
    }
)
