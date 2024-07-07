import CoolProp.CoolProp as CP

# Given data
p = 1e5  # pressure in Pa (1 bar)
m_dot = 2  # mass flow rate in kg/s
L = 2257 * 1e3  # latent heat of steam in J/kg
heating_demand = 5000  # heating demand in kW
temperature_inlet = 100 + 273.15  # 100°C in Kelvin
temperature_outlet = 120 + 273.15  # 120°C in Kelvin

# Calculate the heat recovery rate using latent heat
Q = m_dot * L / 1e3  # in kW
print(f"Heat recovery rate: {Q} kW")

# Get specific enthalpies from CoolProp
h_inlet = CP.PropsSI('H', 'P', p, 'T', temperature_inlet, 'Water')  # J/kg
h_outlet = CP.PropsSI('H', 'P', p, 'T', temperature_outlet, 'Water')  # J/kg

print(f"Specific enthalpy at inlet: {h_inlet / 1000} kJ/kg")
print(f"Specific enthalpy at outlet: {h_outlet / 1000} kJ/kg")

# Calculate the required heat input using the specific enthalpies and mass flow rate
required_heat_input = m_dot * (h_outlet - h_inlet) / 1e3  # Convert to kW
print(f"Required heat input: {required_heat_input:.2f} kW")

# Calculate COP based on heating demand
COP = heating_demand / required_heat_input
print(f"COP: {COP:.2f}")

# Check if the heat recovery rate meets the heat demand
if Q >= required_heat_input:
    print("The heat recovery system meets the heat demand.")
else:
    print("The heat recovery system does not meet the heat demand. Additional heat source required.")

