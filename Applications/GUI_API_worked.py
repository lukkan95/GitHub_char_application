import tkinter as tk

import requests

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import git_token_crypt #This is a module to encrypt user data: email and GitHub token

import matplotlib.ticker as mticker


class GitRepoSigns(object):

    def __init__(self, root=tk.Tk()):

        self.root = root
        self.start_parameters()
        self.upper_frame()
        self.lower_frame()
        self.column_graph()
        self.label1_put_user()
        self.label2_user_not_found()
        self.entry_user_git()
        self.button_check_user()
        # self.root_mainloop()

    def root_mainloop(self):
        self.root.attributes("-topmost", True)
        self.root.mainloop()


    def get_api(self, search_user='OverCookedAgain'):
        self.search_user = search_user
        self.url = f'https://api.github.com/users/{self.search_user}/repos'
        response = requests.get(self.url, auth=(git_token_crypt.code_decrypted('5:hTuk;\a)A)~'),
                                                git_token_crypt.code_decrypted(',o)-uC.W0N48m<G_&>RF^?R.1a<!@?Zmgr9rhaGh')))
        if response.status_code == 200:
            return response

    def convert_data_from_api_to_graph(self, user):
        self.user_not_found['text'] = ''
        master_list = self.get_api(search_user=user)
        if master_list is None:
            self.ax.cla()
            self.chart.draw()
            self.user_not_found['text'] = 'User is not in Github'

        else:
            name_str = []
            for resp in master_list.json():
                name_str.append(resp['name'])
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
        toolbar = NavigationToolbar2Tk(self.chart, self.root)
        toolbar.update()

        self.chart.get_tk_widget().pack(side=tk.TOP, expand=2)
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
        self.root.geometry('800x700')
        self.root.resizable(False, False)
        self.root.title('Character count in GitHub users repositories')

    def entry_user_git(self):
        self.en_user_git = tk.Entry(self.frame_up, bg='white', justify='center')
        self.en_user_git.place(relx=0.05, rely=0.35, relheight=0.25, relwidth=0.65)

    def button_check_user(self):
        but_check_user = tk.Button(self.frame_up, text="Check", font=('Segoe UI', 10),
                             command=lambda: self.convert_data_from_api_to_graph(self.en_user_git.get()))
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
        self.frame_low.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.75)

    def upper_frame(self):
        self.frame_up = tk.Frame(self.root, bg='#ffff66')
        self.frame_up.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)


if __name__ == '__main__':
    view = GitRepoSigns()
    print(git_token_crypt.code_decrypted('5:hTuk;\a)A)~'))
    print(git_token_crypt.code_decrypted(',o)-uC.W0N48m<G_&>RF^?R.1a<!@?Zmgr9rhaGh'))
    if input('Press enter to start GUI: ') == '':
        view.root_mainloop()
    # print(view.get_api())
