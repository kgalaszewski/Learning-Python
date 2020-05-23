# Next example, the simpliest one
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE
# BEST EXAMPLE BEST EXAMPLE BEST EXAMPLE

# This one actually uses multiprocessing
# You can add reaular methods, async methods and methods requiring multiprocessing to one list and run them and wait for them :)

from unsync import unsync
import colorama
import time
import asyncio


# Needs decorators above the async methods
# @unsync(cpu_bound=True)  if the method is not really async, doesnt have await but takes a long time, can be called on normal methods with normal names
# @unsync  if the method is trully async, has awaits and stuffm requires method to have the async sygnature which is async name()


# lets create 2 methods
@unsync
async def generate_data2(fakeTaskId: int, steps: int, coloramaColor): # 1st diffrence is signature
    print(coloramaColor + f'Processing task wiith id : {fakeTaskId}')
    counter = 0
    while counter < steps:
        counter += 1
        print(coloramaColor + f'Im here ({fakeTaskId})')
        await asyncio.sleep(.25) # 3rd diffrence is that we use asyncio sleep
    print(coloramaColor + f'Finished processing task wiith id : {fakeTaskId}')

@unsync(cpu_bound=True)
def some_regular_long_running_method():
    for a in range(10):
        print(a)
        time.sleep(.25)

@unsync 
def another_regular_method():
    for a in range(10):
        print(f'hereherehere {a}')

# unsync cpu bound will run on multi processing
# unsync with async will run asynchronously
# unsync without async will run on thread

tasks = [
    generate_data2(5, 10, colorama.Fore.LIGHTMAGENTA_EX),
    generate_data2(7, 10, colorama.Fore.LIGHTCYAN_EX),
    some_regular_long_running_method(),
    some_regular_long_running_method(),
    another_regular_method(),
    another_regular_method(),
    generate_data2(9, 10, colorama.Fore.LIGHTGREEN_EX)
]

# Thas how we wait for the results
[t.result() for t in tasks]