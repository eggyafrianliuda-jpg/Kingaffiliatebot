from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN
from ai import generate

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Selamat datang di KingAffiliateBot!\n\n"
        "Kirim nama produk, misalnya:\n"
        "• Parfum Pria\n"
        "• Dompet Kulit\n"
        "• Jam Tangan\n\n"
        "Saya akan membuat:\n"
        "✅ Ide konten\n"
        "✅ Caption\n"
        "✅ Hook\n"
        "✅ Voice over\n"
        "✅ Prompt gambar AI\n"
        "✅ Hashtag"
    )


@dp.message()
async def process_product(message: Message):
    await message.answer("⏳ Sedang membuat konten, mohon tunggu...")

    prompt = f"""
Kamu adalah ahli TikTok Affiliate.

Produk:
{message.text}

Buat:
1. 10 ide konten
2. 10 caption
3. 10 hook viral
4. 1 script voice over (30 detik)
5. 3 prompt gambar AI
6. 10 hashtag
"""

    hasil = generate(prompt)

    await message.answer(hasil)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
