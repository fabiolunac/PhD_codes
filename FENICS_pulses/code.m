close all
clear all

// % Path to the CSV archive exported from Vivado ILA
filename = 'iladata_occ25.csv';

// % Read the archive (Automatically detects the header)
opts = detectImportOptions(filename);
data = readtable(filename, opts);

// % Show the name of the available columns
disp('Imported Signals:');
disp(data.Properties.VariableNames);

// % Create workspace variables wht column names
for i = 1:numel(data.Properties.VariableNames)
    varName = data.Properties.VariableNames{i};
    assignin('base', varName, data.(varName));
end

disp('Variables created in  workspace.');


pedestal_in = pedestal_in_reg_12_0_;
pedestal_compensation = pedestal_out_reg_12_0_;
adc_signal = adc_out_reg_11_0_;
bt_mask = bt_mask_out_reg;
eng_truth = event_bt_reg_12_0_;
pzc_output = pzc_out_reg_28_0_/(455); 
occupancy = occupancy_reg_6_0_;
wiener_normal = wiener_normal_out_reg_32_0_(7:end)/(450);
wiener_pzc = wiener_pzc_out_reg_32_0_(8:end)/(450*455);


// %% Plots

// % Truth and ADC Signal
figure('DefaultAxesFontSize',24)
hold on;
stairs(eng_truth);
stairs(adc_signal);
hold off;
xlabel("Samples");
ylabel("Amplitude [ADC Counts]");
legend("Amp. Truth","ADC Signal");

// % PZC and ADC Signal
figure('DefaultAxesFontSize',24)
hold on;
stairs(adc_signal);
stairs(pzc_output);
stairs(pedestal_in);
stairs(pedestal_compensation);
hold off;
xlabel("Samples");
ylabel("Amplitude [ADC Counts]");
legend("ADC Signal","PZC Output","Pedestal Input","Pedestal Compensation");

// % Estimations
figure('DefaultAxesFontSize',24)
hold on;
stairs(eng_truth);
// %stairs(wiener_pzc);
stairs(wiener_normal);
hold off;
xlabel("Samples");
ylabel("Amplitude [ADC Counts]");
legend("Amp. Truth","WIENER+PZC","WIENER");

figure('DefaultAxesFontSize',24)
hold on;
stairs(eng_truth);
stairs(wiener_pzc);
hold off;
xlabel("Samples");
ylabel("Amplitude [ADC Counts]");
legend("Amp. Truth","WIENER+PZC");


