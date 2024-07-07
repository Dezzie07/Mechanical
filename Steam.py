import CoolProp.CoolProp as CP

# Given data
p = 1e5  # pressure [Pa] (1 bar)
m_dot = 2  # mass flow rate [kg/s]
L = 2257 * 1e3  # latent heat steam [J/kg]
heating_demand = 5000  # heating demand [kW]
temperature_in = 100 + 273.15  # 100°C in Kelvin
temperature_out = 120 + 273.15  # 120°C in Kelvin

# Heat recovery rate with latent heat
Q = m_dot * L / 1e3  # [kW]
print(f"Heat recovery rate: {Q} kW")

# Enthalpies from given temperature
h_in = CP.PropsSI('H', 'P', p, 'T', temperature_in, 'Water')  # J/kg
h_out = CP.PropsSI('H', 'P', p, 'T', temperature_out, 'Water')  # J/kg

print(f"Specific enthalpy at inlet: {h_in / 1000} kJ/kg")
print(f"Specific enthalpy at outlet: {h_out / 1000} kJ/kg")

# The required heat input using enthalpies and mass flow rate. ( Q = m\delta(H))
required_heat_input = m_dot * (h_out - h_in) / 1e3  # Also conversion to kW
print(f"Required heat input: {required_heat_input:.2f} kW")

# Calculate COP using heat demand
COP = heating_demand / required_heat_input
print(f"COP: {COP:.2f}")


if Q >= required_heat_input:
    print("The heat recovery system meets the heat demand.")
else:
    print("The heat recovery system does not meet the given heat demand. Additional heat source is required.")

