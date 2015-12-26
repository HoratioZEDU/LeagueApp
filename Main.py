from RiotAPI import RiotAPI
from tkinter import *


class App(object):

    def __init__(self, master):

        self.master = master
        self.current_game(master)

    def current_game(self, master):

        #Defining/Packing frames
        menu_buttons = Frame(master, width=75, height=450, bg='#0f0')
        menu_buttons.pack(side=LEFT)
        namely = Frame(master, width=600, height=25, bg='#0aa', padx=30, pady=15)
        namely.pack(side=TOP)
        global meaty
        meaty = Frame(master, width=600, height=350)
        meaty.pack(side=RIGHT)
        meaty.grid_propagate(0)

        #Defining/Gridding buttons
        current_game_button = Button(menu_buttons, width=10, height=10, bg='#5153B5')
        current_game_button.grid(row=1)
        ranked_stats_button = Button(menu_buttons, width=10, height=10, bg='#5153B5')
        ranked_stats_button.grid(row=2)
        match_history_button = Button(menu_buttons, width=10, height=10, bg='#5153B5')
        match_history_button.grid(row=3)

        #Defining/Gridding summoner name field
        summoner_name_entry = Entry(namely)
        summoner_name_entry.grid(row=0, pady=10)
        summoner_name_button = Button(namely,
                                      text="Get Summoner Game",
                                      bg='#5aa',
                                      command=lambda: self.get_summoner_data(summoner_name_entry.get(), meaty))
        summoner_name_button.grid(row=1)

    def get_summoner_data(self, name, region, meaty):
        api = RiotAPI('47fb4460-e2bd-47b5-9136-8c146d4e1ebb')
        summoner_id = api.get_summoner_by_name(name)[name.lower()]['id']
        print(summoner_id)
        #Label(meaty, text=summoner_id).grid()
        current_game = api.get_current_game(summoner_id)["participants"]
        for i in range(len(current_game)):
            if i < 5:
                print(current_game[i]["summonerName"])
                Label(meaty, text=current_game[i]["summonerName"], fg='blue').grid(column=i, row=0, padx=30, pady=20)
            else:
                print(current_game[i]["summonerName"])
                Label(meaty, text=current_game[i]["summonerName"], fg='red').grid(column=i-5, row=1, pady=130)
        meaty.pack(side=RIGHT)
        print(current_game)



root = Tk()
root.title("League of Legends Application")
if __name__ == '__main__':
    app = App(root)
    root.mainloop()
"""
def main(name):
    api = RiotAPI('df1f6f80-2c8b-48f2-99f8-59ac1e0e7b65')
    summoner_id = api.get_summoner_by_name(name)[name.lower()]['id']
    print(summoner_id)

if __name__ == '__main__':
    main('Seqond')

"""