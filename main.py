def calculate_npv(cash_flows, discount_rate):
    npvs = {}
    for option, flows in cash_flows.items():
        if isinstance(flows, dict):
            npv = 0
            for year, cash_flow in flows.items():
                npv += cash_flow / ((1 + discount_rate) ** year)
            npvs[option] = npv
        else:
            npvs["Single Option"] = flows / (1 + discount_rate)
    return npvs

def calculate_pvr(cash_flows, discount_rate):
    pvrs = {}
    for option, flows in cash_flows.items():
        if isinstance(flows, dict):
            inflows = sum(cf for year, cf in flows.items() if cf > 0)
            outflows = sum(cf for year, cf in flows.items() if cf < 0)
            pv_inflows = calculate_npv({year: cf for year, cf in flows.items() if cf > 0}, discount_rate)[option]
            pv_outflows = calculate_npv({year: cf for year, cf in flows.items() if cf < 0}, discount_rate)[option]
            pvrs[option] = pv_inflows / abs(pv_outflows)
        else:
            pvrs["Single Option"] = "Cannot calculate PVR for single cash flow"
    return pvrs

def input_cash_flows(option_name):
    num_years = int(input(f"Enter the number of years for option {option_name}: "))
    flows = {}
    for year in range(1, num_years + 1):
        cash_flow = float(input(f"Enter cash flow for year {year} of option {option_name}: "))
        flows[year] = cash_flow
    return flows

def main():
    num_options = int(input("Enter the number of options to analyze: "))
    cash_flows = {}
    for i in range(num_options):
        option_name = input(f"Enter name for option {i + 1}: ")
        cash_flows[option_name] = input_cash_flows(option_name)
    
    discount_rate = float(input("Enter the discount rate (as a decimal): "))

    npvs = calculate_npv(cash_flows, discount_rate)
    pvrs = calculate_pvr(cash_flows, discount_rate)

    print("\nNPVs:")
    for option, npv in npvs.items():
        print(f"{option}: {npv}")
    
    print("\nPVRs:")
    for option, pvr in pvrs.items():
        print(f"{option}: {pvr}")

if __name__ == "__main__":
    main()

