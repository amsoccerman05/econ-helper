def calculate_npv(cash_flows, discount_rate):
    npv = 0
    for year, cash_flow in cash_flows.items():
        npv += cash_flow / ((1 + discount_rate) ** year)
    return npv

def calculate_pvr(cash_flows, discount_rate):
    inflows = sum(cf for year, cf in cash_flows.items() if cf > 0)
    outflows = sum(cf for year, cf in cash_flows.items() if cf < 0)
    pv_inflows = calculate_npv({year: cf for year, cf in cash_flows.items() if cf > 0}, discount_rate)
    pv_outflows = calculate_npv({year: cf for year, cf in cash_flows.items() if cf < 0}, discount_rate)
    return pv_inflows / abs(pv_outflows)

def main():
    num_cash_flows = int(input("Enter the number of cash flows: "))
    cash_flows = {}
    for i in range(num_cash_flows):
        year = int(input(f"Enter year for cash flow {i + 1}: "))
        cash_flow = float(input(f"Enter cash flow for year {year}: "))
        cash_flows[year] = cash_flow
    
    discount_rate = float(input("Enter the discount rate (as a decimal): "))

    npv = calculate_npv(cash_flows, discount_rate)
    pvr = calculate_pvr(cash_flows, discount_rate)

    print(f"NPV: {npv}")
    print(f"PVR: {pvr}")

if __name__ == "__main__":
    main()
