import asyncio
from bot import bt, dis


async def main():
    await dis.start_polling(bt)


if __name__ == '__main__':
    asyncio.run(main())