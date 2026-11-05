import time
import asyncio

async def function1():
    await asyncio.sleep(2)
    print("hello from function 1")

async def function2():
    await asyncio.sleep(5)
    print("hello from function 2")

async def function3():
    await asyncio.sleep(5)
    print("hello form function 3 ")

async def main():
    L = await asyncio.gather(
            function1(),
            function2(),
            function3(),
        )
    print(L)
asyncio.run(main())