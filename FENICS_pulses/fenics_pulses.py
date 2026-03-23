import pandas as pd
import matplotlib.pyplot as plt

occ = 121

if occ == 25:
    data = pd.read_csv('iladata_occ25.csv')
elif occ == 121:
    data = pd.read_csv('iladata_occ121.csv')


pedestal_in           = pd.to_numeric(data['pedestal_in_reg[12:0]'] , errors='coerce')
pedestal_compensation = pd.to_numeric(data['pedestal_out_reg[12:0]'], errors='coerce')
adc_signal            = pd.to_numeric(data['adc_out_reg[11:0]']     , errors='coerce')
bt_mask               = pd.to_numeric(data['bt_mask_out_reg']       , errors='coerce')
eng_truth             = pd.to_numeric(data['event_bt_reg[12:0]']    , errors='coerce')
pzc_output            = pd.to_numeric(data['pzc_out_reg[28:0]']     , errors='coerce') / 455
occupancy             = pd.to_numeric(data['occupancy_reg[6:0]']    , errors='coerce')

wiener_normal         = pd.to_numeric(data['wiener_normal_out_reg[32:0]'], errors='coerce').iloc[6:] / 450
wiener_pzc            = pd.to_numeric(data['wiener_pzc_out_reg[32:0]']   , errors='coerce').iloc[7:] / (450*455)

# =========================
# === PLOTS ==============
# =========================

xlim1 = 5000
xlim2 = 5100

# Truth + ADC
plt.figure()
plt.plot(eng_truth.values[xlim1:xlim2], drawstyle='steps-post', label="Amp. Truth")
plt.plot(adc_signal.values[xlim1:xlim2], drawstyle='steps-post', label="ADC Signal")
plt.xlabel("Samples")
plt.ylabel("Amplitude [ADC Counts]")
plt.legend()
plt.title('Shaper')
plt.grid()

# ADC + PZC + Pedestals
plt.figure()
plt.plot(adc_signal.values[xlim1:xlim2], drawstyle='steps-post', label="ADC Signal")
plt.plot(pzc_output.values[xlim1:xlim2], drawstyle='steps-post', label="PZC Output")
plt.plot(pedestal_in.values[xlim1:xlim2], drawstyle='steps-post', label="Pedestal Input")
plt.plot(pedestal_compensation.values[xlim1:xlim2], drawstyle='steps-post', label="Pedestal Compensation")
plt.xlabel("Samples")
plt.ylabel("Amplitude [ADC Counts]")
plt.legend()
plt.title('PZC')
plt.grid()

# Wiener normal
# plt.figure()
# plt.plot(eng_truth.values, drawstyle='steps-post', label="Amp. Truth")
# plt.plot(wiener_normal.values, drawstyle='steps-post', label="WIENER")
# plt.xlabel("Samples")
# plt.ylabel("Amplitude [ADC Counts]")
# plt.legend()
# plt.grid()

# Wiener + PZC
plt.figure()
plt.plot(eng_truth.values[xlim1:xlim2], drawstyle='steps-post', label="Amp. Truth")
plt.plot(wiener_pzc.values[xlim1:xlim2], drawstyle='steps-post', label="WIENER+PZC")
plt.xlabel("Samples")
plt.ylabel("Amplitude [ADC Counts]")
plt.legend()
plt.grid()
plt.title('Energy Reconstruction')

plt.show()
