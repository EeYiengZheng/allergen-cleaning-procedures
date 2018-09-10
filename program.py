from os import path, curdir
import csv, tkinter

# procedure output
push = 'push'
rb = 'rinse and breakdown'
wb = 'wash and breakdown'


class AllergenProgram(object):
    def __init__(self, db: str = None) -> None:
        self.current: str = None
        self.next_up: str = None
        self.db = path.join(curdir, db)
        self.mapping: dict = dict()

        with open(self.db) as csv_file:
            records = csv.reader(csv_file, dialect='excel')
            for record in records:
                rec = record[0].strip().lower()
                self.mapping[rec] = record
        if 'frml_nub' in self.mapping:
            self.mapping.pop('frml_nub')

    def execute(self):
        if not self.current or not self.next_up:
            return "product # cannot be empty"
        elif not self.current.isalnum() or not self.next_up.isalnum():
            return "product # cannot contain non-alphanumeric characters"
        elif self.current not in self.mapping or self.next_up not in self.mapping:
            return "at least one product # is not found"
        elif self.current == self.next_up:
            return "product # are the same"
        else:
            row_cur = self.mapping[self.current]
            row_nex = self.mapping[self.next_up]

            alrg_cur = self.filter_row_to_set(row_cur[4:15])
            alrg_nex = self.filter_row_to_set(row_nex[4:15])
            spice_cur = self.filter_row_to_set(row_cur[16].split(','))
            spice_nex = self.filter_row_to_set(row_nex[16].split(','))
            prtcl_cur = self.filter_row_to_set(row_cur[17].split(','))
            prtcl_nex = self.filter_row_to_set(row_nex[17].split(','))
            orga_cur = row_cur[15].strip().lower()
            orga_nex = row_nex[15].strip().lower()

            alrg_match = alrg_cur.issubset(alrg_nex)
            spice_match = spice_cur.issubset(spice_nex)
            prtcl_match = prtcl_cur.issubset(prtcl_nex)

            print(f"allergen:\n{alrg_cur}\n{alrg_nex}\n")
            print(f"spices:\n{spice_cur}\n{spice_nex}\n")
            print(f"particles:\n{prtcl_cur}\n{prtcl_nex}\n")
            print(f"organic or():\n{orga_cur or orga_nex}\n")

            # conditional logic
            if not orga_cur and orga_nex:
                return wb
            else:
                if alrg_match:
                    if spice_match and prtcl_match:
                        return push
                    else:
                        return rb
                return wb

    @staticmethod
    def filter_row_to_set(row):
        st = set(filter(lambda t: t, map(lambda s: s.strip().lower(), row)))
        return st


class GUI(tkinter.Tk):
    def __init__(self, prog=None):
        super().__init__()
        self.program = prog

        from tkinter import N, S, E, W

        # labels and configurations
        self.title("Cleaning Procedure")
        labelfont = ('', 12, '')

        # input boxes
        self.input_current = tkinter.Entry(self, width=10, font=labelfont, takefocus=True, bg='beige')
        self.input_current.grid(row=0, column=1, sticky=W + E + N + S, padx=5, pady=5)

        self.input_next_up = tkinter.Entry(self, width=10, font=labelfont, bg='beige')
        self.input_next_up.grid(row=1, column=1, sticky=W + E + N + S, padx=5, pady=5)

        # execution output box
        self.message = tkinter.Label(self)
        self.message.configure(text='', font=labelfont, wraplength=250, bg='beige', fg='green')
        self.message.grid(row=3, column=0, columnspan=4, sticky=W + E + N + S, padx=10, pady=10)

        # execution button
        self.button = tkinter.Button(self, text="Submit", font=labelfont)
        self.button.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

        # labels
        input_current_label = tkinter.Label(self)
        input_current_label.configure(text='current product #', font=labelfont)
        input_current_label.grid(row=0, sticky=E, padx=5, pady=5)

        input_next_up_label = tkinter.Label(self)
        input_next_up_label.configure(text='next product #', font=labelfont)
        input_next_up_label.grid(row=1, sticky=E)

        # event bindings
        self.button.bind("<Button-1>", self.submission)
        self.bind("<Return>", self.submission)

    def submission(self, event=None):
        program.current = self.input_current.get().strip().lower()
        program.next_up = self.input_next_up.get().strip().lower()
        output = program.execute()
        self.message.configure(text=output)


if __name__ == '__main__':
    program = AllergenProgram(path.join('db', 'db.csv'))

    gui = GUI(program)
    gui.mainloop()
