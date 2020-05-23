# Python has a memory management feature called the GIL - Global Interpreter Lock. Because of that threading in python is not the same as real threading in C# or C++
# For real threading you can use CPython and multiprocessing module 
# For Asynchronous programming you can use for example asyncio


import colorama
import time
import asyncio

# # Synchronous 
# def generate_data(fakeTaskId: int, steps: int, coloramaColor):
#     print(coloramaColor + f'Processing task wiith id : {fakeTaskId}')
#     counter = 0
#     while counter < steps:
#         counter += 1
#         print(coloramaColor + f'Im here ({fakeTaskId})')
#         time.sleep(.25)
#     print(coloramaColor + f'Finished processing task wiith id : {fakeTaskId}')

# generate_data(1, 10, colorama.Fore.CYAN) # Synchronous call


# Asynchronous
loop = asyncio.get_event_loop()
data = asyncio.Queue() # we are using it because thats the asynchronous queue so that we can something to await for


async def generate_data(fakeTaskId: int, steps: int, coloramaColor, data: asyncio.Queue): # 1st diffrence is signature
    print(coloramaColor + f'Processing task wiith id : {fakeTaskId}')
    counter = 0
    while counter < steps:
        counter += 1
        print(coloramaColor + f'Im here ({fakeTaskId})')
        await data.put(fakeTaskId) # 2nd diffrence is that we need to await for something
        await asyncio.sleep(.25) # 3rd diffrence is that we use asyncio sleep
    print(coloramaColor + f'Finished processing task wiith id : {fakeTaskId}')


# Inside the method we would just invoke it using await generate_data(params)
task = asyncio.gather(generate_data(1, 10, colorama.Fore.CYAN, data)) # 4th diffrence is how to invoke this, something like Task.Wait in C#
loop.run_until_complete(task)

# To samo ale wywolanie dla kilku "taskow"
task = asyncio.gather(
    generate_data(1, 10, colorama.Fore.CYAN, data),
    generate_data(2, 10, colorama.Fore.GREEN, data),
    generate_data(3, 10, colorama.Fore.YELLOW, data)) # 4th diffrence is how to invoke this, something like Task.Wait in C#
loop.run_until_complete(task)

# Powyzszy przyklad mozna zrobic podobnie jak w C# uzywajac List<Task> tasks
tasks = []
tasks.append(loop.create_task(generate_data(4, 10, colorama.Fore.CYAN, data)))
tasks.append(loop.create_task(generate_data(5, 10, colorama.Fore.GREEN, data)))
tasks.append(loop.create_task(generate_data(6, 10, colorama.Fore.YELLOW, data)))

async def do_something_with_tasks():
    for task in tasks:
        result = await task
        del result # just to use the variable
    print(f'done something with task')

task = asyncio.gather(do_something_with_tasks())
loop.run_until_complete(task)

# Nastepny przyklad, troche latwiej niz poprzednio
loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(generate_data(5, 10, colorama.Fore.LIGHTMAGENTA_EX, data)),
    loop.create_task(generate_data(7, 10, colorama.Fore.LIGHTCYAN_EX, data)),
    loop.create_task(generate_data(9, 10, colorama.Fore.LIGHTGREEN_EX, data))
]

loop.run_until_complete(asyncio.gather(*tasks))



# Yield return is not async, but at the same time it's doing pretty similar job
# To check the Yield example, go to Yield.py


