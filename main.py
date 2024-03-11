import tkinter as tk
from tkinter import messagebox

class CashFlowInput(tk.Toplevel):
    def __init__(self, master, option_name, callback):
        super().__init__(master)
        self.title(f"Cash Flows for {option_name}")
        self.option_name = option_name
        self.callback = callback
        self.cash_flows = {}

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"Enter cash flows for {self.option_name}").grid(row=0, columnspan=3, padx=5, pady=5)

        self.num_years_entry = tk.Entry(self)
        self.num_years_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Number of years:").grid(row=1, column=0, padx=5, pady=5)

        tk.Button(self, text="Submit", command=self.submit_years).grid(row=1, column=2, padx=5, pady=5)

    def submit_years(self):
        try:
            num_years = int(self.num_years_entry.get())
            self.enter_cash_flows(num_years)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of years.")

    def enter_cash_flows(self, num_years):
        for year in range(1, num_years + 1):
            tk.Label(self, text=f"Year {year}:").grid(row=year + 1, column=0, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=year + 1, column=1, padx=5, pady=5)
            self.cash_flows[year] = entry
        
        tk.Button(self, text="Submit", command=self.submit).grid(row=num_years + 2, columnspan=2, padx=5, pady=10)

def submit(self):
    for year, entry in self.cash_flows.items():
        if isinstance(entry, float):
            self.cash_flows[year] = entry
        else:
            try:
                cash_flow = float(entry.get())
                self.cash_flows[year] = cash_flow
            except ValueError:
                messagebox.showerror("Error", "Invalid input for cash flow.")
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

        self.results_label = tk.Label(self, text="")
        self.results_label.pack(pady=10)

    def enter_options(self):
        try:
            self.num_options = int(self.num_options_entry.get())
            self.enter_cash_flows()
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of options.")

    def enter_cash_flows(self):
        if self.current_option_index < self.num_options:
            option_num = self.current_option_index + 1
            option_name = f"Option {option_num}"
            cash_flow_window = CashFlowInput(self, option_name, self.receive_cash_flows)
            cash_flow_window.grab_set()

    def receive_cash_flows(self, option_name, cash_flows):
        self.options[option_name] = cash_flows
        self.current_option_index += 1
        if self.current_option_index < self.num_options:
            self.enter_cash_flows()
        else:
            self.calculate_results()

    def calculate_results(self):
        npvs = {}
        pvrs = {}
        results_text = ""
        for option, cash_flows in self.options.items():
            npv = sum(cf / (1 + 0.1) ** year for year, cf in cash_flows.items())
            pvr = sum(cf for year, cf in cash_flows.items() if cf > 0) / abs(sum(cf for year, cf in cash_flows.items() if cf < 0))
            npvs[option] = npv
            pvrs[option] = pvr
            results_text += f"{option}:\nNPV: {npv}\nPVR: {pvr}\n\n"

        best_option = max(npvs, key=npvs.get)
        best_option_text = f"Best Option: {best_option} (NPV: {npvs[best_option]}, PVR: {pvrs[best_option]})"
        self.results_label.config(text=best_option_text)

        messagebox.showinfo("Results", results_text)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
