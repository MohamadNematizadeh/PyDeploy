import asyncio
async def fn():
    print("One")
    await asyncio.sleep(1)
    asyncio.create_task(fu2())
    await asyncio.sleep(1)
    print("four")
    await asyncio.sleep(1)
    print("five")

async def fu2():
    print("two")
    await asyncio.sleep(1)
    print("three")

asyncio.run(fn())