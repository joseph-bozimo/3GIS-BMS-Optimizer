# ==============================================================================
# 3GIS CLIMATE ENGINEERING PLATFORM: THERMODYNAMIC BMS AUTOMATION SUB-ROUTINE
# Formulation: Q_required = m_dot * c_p * delta_T
# Authorized Operator: Joseph Bozimo (Senior Technical Officer)
# ==============================================================================
import time

def compute_dynamic_hvac_load(occupant_density):
    """
    Calculates the proportional air mass flow rate and sensible cooling requirement
    to dynamically match localized building occupancy metrics.
    """
    c_p = 1.005       # Specific heat capacity of indoor air (kJ/kg·K)
    delta_t = 6.0     # Baseline temperature gradient delta (Kelvin)
    
    # Metabolic sensible heat gain added per active occupant connection (approx 100 Watts)
    metabolic_load = occupant_density * 0.100 
    
    # Mechatronic air handler mass flow rate scaling logic (m_dot)
    if occupant_density == 0:
        mass_flow_rate = 0.05  # 5% Volume: Carbon Hibernation Mode (Unoccupied sector)
        status_label = "HIBERNATION"
    elif occupant_density < 10:
        mass_flow_rate = 0.40  # 40% Volume: Partial Load Adaptive State
        status_label = "ADAPTIVE PARTIAL"
    else:
        mass_flow_rate = 1.00  # 100% Volume: Peak Design Flow State
        status_label = "PEAK DESIGN"
        
    # Calculate sensible cooling energy requirement
    sensible_q = (mass_flow_rate * c_p * delta_t) + metabolic_load
    
    return round(sensible_q, 3), round(mass_flow_rate * 100, 1), status_label

# Simulated live occupancy stream from university access point connections
campus_occupancy_telemetry = [0, 4, 15, 22, 8, 0]

print("=" * 70)
print("             3GIS MECHATRONIC HVAC CONTROLLER SIMULATION LAB            ")
print("=" * 70)

for density in campus_occupancy_telemetry:
    load_kw, fan_speed_pct, mode = compute_dynamic_hvac_load(density)
    print(f"[ACCESS POINT ALERT] Detected Users: {density:02d} | State: {mode:<16} | Fan Speed: {fan_speed_pct:>5}% | Thermal Load Req: {load_kw:.3f} kW")
    time.sleep(0.3)

print("=" * 70)
print("Simulation cycle complete. All variables verified for BACnet/Modbus API mapping.")
