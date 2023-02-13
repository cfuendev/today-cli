import urllib3
from bs4 import BeautifulSoup
import keyboard
from colorama.ansi import Cursor
from colorama import just_fix_windows_console
from shutil import get_terminal_size

# CONTROLLER + VIEW
# 0:5 --> First page (5 items) | [page*5:(page+1)*5] [0*5:1*5]
# 5:10 --> Second page (5 items) | [1*5:2*5] .. You get the idea
# ===============================================================

def render(state, dayElms):
    for line in range(-1,state['lines']-2):
        print(Cursor.UP(), end='')
        print(" "*get_terminal_size()[0], end='')
        print(Cursor.BACK(get_terminal_size()[0]), end='')
    state['lines'] = 1
    print(f"{len(dayElms)} results\n"); state['lines'] = 3
    for elm in dayElms[state['page']*5:(state['page']+1)*5]:
        print(f"{elm.h3.string}\n{elm.p.string}\n"); state['lines'] += 3
    print(f"\u00AB {state['page']+1} \u00BB"); state['lines'] += 1


def prevPage(state, dayElms):
    if(len(dayElms[(state['page']-1)*5:(state['page'])*5]) != 0):
        state['page'] -= 1
        render(state, dayElms)


def nextPage(state, dayElms):
    if(len(dayElms[(state['page']+1)*5:(state['page']+2)*5]) != 0):
        state['page'] += 1
        render(state, dayElms)


def main():

    # SETUP
    # ===============================================================

    http = urllib3.PoolManager()
    html = http.request("GET", "https://nationaltoday.com/what-is-today/").data.decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")
    dayElms = soup.find_all("div", class_="day-card")
    state = {"page": 0, "lines": 0}

    just_fix_windows_console()

    for key in ["left", 'h', 'j', 'b']:
        keyboard.add_hotkey(key, prevPage, args=(state, dayElms))

    for key in ["right", 'k', 'l', 'e']:
        keyboard.add_hotkey(key, nextPage, args=(state, dayElms))

    render(state, dayElms)

    keyboard.wait()

if __name__ == "__main__":
    main()