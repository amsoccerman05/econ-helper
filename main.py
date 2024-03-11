import tkinter as tk

class CashFlowInput(tk.Toplevel):
    def __init__(self, master, option_name, num_years, callback):
        super().__init__(master)
        self.title(f"Cash Flows for Option {option_name}")
        self.option_name = option_name
        self.num_years = num_years
        self.callback = callback
        self.cash_flows = {}

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"Enter cash flows for Option {self.option_name}").grid(row=0, columnspan=2, padx=5, pady=5)

        self.entries = {}
        for year in range(1, self.num_years + 1):
            tk.Label(self, text=f"Year {year}:").grid(row=year, column=0, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=year, column=1, padx=5, pady=5)
            self.entries[year] = entry
        
        tk.Button(self, text="Submit", command=self.submit).grid(row=self.num_years + 1, columnspan=2, padx=5, pady=10)

    def submit(self):
        for year, entry in self.entries.items():
            try:
                cash_flow = float(entry.get())
                self.cash_flows[year] = cash_flow
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid input for cash flow.")
                return
        self.callback(self.option_name, self.cash_flows)
        self.destroy()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Engineering Economics Helper")
        self.options = {}
        self.current_option_index = 0
        self.num_options = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter the number of options to analyze:").pack(pady=5)
        self.num_options_entry = tk.Entry(self)
        self.num_options_entry.pack()

        tk.Button(self, text="Enter", command=self.enter_options).pack(pady=5)

    def enter_options(self):
        try:
            self.num_options = int(self.num_options_entry.get())
            self.enter_cash_flows()
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input for number of options.")

    def enter_cash_flows(self):
        if self.current_option_index < self.num_options:
            option_num = self.current_option_index + 1
            option_name = f"Option {option_num}"
            cash_flow_window = CashFlowInput(self, option_name, 5, self.receive_cash_flows)
            cash_flow_window.grab_set()

    def receive_cash_flows(self, option_name, cash_flows):
        self.options[option_name] = cash_flows
        self.current_option_index += 1
        if self.current_option_index < self.num_options:
            self.enter_cash_flows()
        else:
            self.calculate_results()

    def calculate_results(self):
        # Implement NPV and PVR calculation using self.options
        # Display results
        print("Calculation completed.")
        print(self.options)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
