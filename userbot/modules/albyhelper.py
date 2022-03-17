""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke @albyaja atau tag admin di @ruangdiskusikami:\n"
        "\n[Telegram](t.me/Punya_Alby)"
        "\n[Repo](https://github.com/PunyaAlby/ALBY-Userbot/)"
        "\n[Instagram](instagram.com/fadzkuruuniialmuttaqiin/)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/PunyaAlby/ALBY-Userbot/ALBY-Userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : **`helper`\
        \n\n  **𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `.lhelp`\
        \n  **Usage : **Lakukan ketika ingin OFF.\nSiapapun Yang Balas, Tag, Atau Chat Kamu \
Mereka Akan Tau Alasan Kamu OFF.
        \n\nAFK Bisa Dilakukan Dan Dibatalkan Dimanapun.\
        \n\n  **𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `.vars`\
        \n  **Usage : **Melihat Daftar Vars. \
    "
    }
)
