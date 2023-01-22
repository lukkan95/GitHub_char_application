import asyncio

import re

import tkinter as tk

import aiohttp as aiohttp

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from Applications import git_token_crypt


import matplotlib.ticker as mticker


class GitRepoSigns(object):

    def __init__(self, root=tk.Tk()):

        self.root = root
        self.start_parameters()
        self.upper_frame()
        self.lower_frame()
        self.left_frame()
        self.column_graph()
        self.label1_put_user()
        self.label2_user_not_found()
        self.entry_user_git()
        self.button_check_user()
        self.search_queue = [None]
        self.searching_queue_tool()



    def root_mainloop(self):
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def unpack_users(self, many):
        list_split = re.split('[;|,*.\n\s/:_]', many)
        list_unpacked = [i for i in list_split if i != '']

        return list_unpacked

    def get_tasks(self, session, search_users):
        tasks = []
        self.search_user = None

        self.search_user = self.unpack_users(search_users)
        for user in self.search_user:
            random_url = f'https://api.github.com/users/{user}/repos'
            tasks.append(asyncio.create_task(session.get(random_url, auth=aiohttp.BasicAuth(git_token_crypt.username,

                                                                            git_token_crypt.user_token))))
        # print(tasks)
        return tasks

    async def get_api_async_way(self, users):
        results = []
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session, users)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                if response.status == 200:
                    results.append(await response.json())
            print(results)
            return results



    def convert_data_from_api_to_graph(self, users):
        self.user_not_found['text'] = ''
        master_list = asyncio.run(self.get_api_async_way(users))
        if len(master_list) == 0:
            self.ax.cla()
            self.chart.draw()
            self.user_not_found['text'] = 'User is not in Github'

        else:
            name_str = []
            for n in range(len(master_list[0])):
                name_str.append(master_list[0][n]['name'])
            whole_signs = ''.join(name_str)
            self.graph_data(self.char_frequency(whole_signs))

    def char_frequency(self, str1):
        dict_of_chars = {}
        for n in str1.upper():
            keys = dict_of_chars.keys()
            if n in keys:
                dict_of_chars[n] += 1
            else:
                dict_of_chars[n] = 1
        return dict_of_chars

    def column_graph(self):
        self.fig = Figure(figsize=(7.5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.chart = FigureCanvasTkAgg(self.fig, master=self.frame_low)
        self.chart.draw()

        self.chart.get_tk_widget().pack(side=tk.TOP, expand=1)
        toolbar = NavigationToolbar2Tk(self.chart, self.frame_low)
        toolbar.update()

        self.chart.get_tk_widget().pack(side=tk.TOP, expand=1)
        self.ax.set_xlabel('Signs')
        self.ax.set_ylabel('Ammount of sign')

    def graph_data(self, data):
        self.ax.cla()
        for key, value in data.items():
            self.ax.bar(key, value, width=0.1, color='blue')
            data_label = '{:.0f}'.format(value)
            self.ax.annotate(data_label, (key, value), textcoords='offset points', xytext=(0, 4), ha='center')
            self.fig.gca().yaxis.set_major_locator(mticker.MultipleLocator(round(max(data.values()) / 5)))
        self.chart.get_tk_widget().pack(side=tk.TOP, expand=2)
        self.ax.set_xlabel('Signs')
        self.ax.set_ylabel('Ammount of sign')
        self.ax.set_title(f'Frequencies of signs in {self.search_user}\'s repositories.')
        self.chart.draw()

    def start_parameters(self):
        self.root.geometry('1200x800')
        self.root.resizable(False, False)
        self.root.title('Character count in GitHub users repositories')

    def entry_user_git(self):
        self.en_user_git = tk.Entry(self.frame_up, bg='white', justify='center')
        self.en_user_git.place(relx=0.05, rely=0.35, relheight=0.25, relwidth=0.65)

    def button_check_user(self):
        but_check_user = tk.Button(self.frame_up, text="Check", font=('Segoe UI', 10),
                             command = lambda: self.convert_data_from_api_to_graph(self.en_user_git.get()))
        but_check_user.place(relx=0.75, rely=0.35, relheight=0.25, relwidth=0.2)

    def label1_put_user(self):
        self.put_user = tk.Label(self.frame_up, bg='#ffff66', font=('Segoe UI', 10, 'bold'), text='GitHub user:',
                                 anchor='w')
        self.put_user.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.9)

    def label2_user_not_found(self):
        self.user_not_found = tk.Label(self.frame_up, bg='#ffff66', font=('Segoe UI', 10, 'bold'), fg='red', anchor='w')
        self.user_not_found.place(relx=0.05, rely=0.65, relheight=0.2, relwidth=0.9)

    def lower_frame(self):
        self.frame_low = tk.Frame(self.root, bg='#ffff66')
        self.frame_low.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

    def upper_frame(self):
        self.frame_up = tk.Frame(self.root, bg='#ffff66')
        self.frame_up.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=0.2)

    def left_frame(self):
        self.frame_left = tk.Frame(self.root, bg='white')
        self.frame_left.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1)

    def new_frame(self):
        self.frame_new = tk.Frame(self.root, bg='#ffff66')
        self.frame_new.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1)
        self.lb_new_frame = tk.Label(self.frame_new, bg='#ffff66', font=('Segoe UI', 10, 'bold'), text='elo',
                                     anchor='w')
        self.lb_new_frame.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.9)


    def searching_queue_tool(self):
        self.clicked = tk.StringVar()
        self.clicked.set('Searching queue')
        self.favourites = tk.OptionMenu(self.frame_left, self.clicked, *self.search_queue)
        self.favourites.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.05)

    def fav_list_remove_None(self):
        if None in self.search_queue:
            self.search_queue.remove(None)

    def fav_list_add(self, city):
        if city in self.search_queue:
            pass
        else:
            self.search_queue.append(city)

    def fav_list_remove_city(self, city):
        if len(self.search_queue) > 1:
            self.search_queue.remove(city)
            self.searching_queue_tool()
        else:
            self.search_queue.append(None)
            self.search_queue.remove(city)
            self.searching_queue_tool()


if __name__ == '__main__':
    view = GitRepoSigns()
    view.root_mainloop()
    # asyncio.run(view.get_api_async_way('Trickest, OverCookedAgain'))

