%% ================= USER SETTINGS =================
V  = 24;        % supply voltage [V]
Ts = 1/1000;    % sampling time [s]

folder = ...
'C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\final experiment\experiment-fixedbase\mech test\efficiency\Data';

% Arial everywhere (axes, text, legends, titles)
set(groot, 'defaultAxesFontName',   'Arial', ...
           'defaultTextFontName',   'Arial', ...
           'defaultLegendFontName', 'Arial');

%% ================= CASES =================
cases(1).name      = '1kg';
cases(1).title     = 'A: Cumulative energy consumption for 1kg';
cases(1).file_free = fullfile(folder, 'Efficiency4_1kg_motor_0_3Hztrimmed.xlsx');
cases(1).file_vsm  = fullfile(folder, 'Efficiency4_1kg_vsm_0_3Hztrimmed.xlsx');

cases(2).name      = '0.64kg';
cases(2).title     = 'B: Cumulative energy consumption for 0.64kg';
cases(2).file_free = fullfile(folder, 'Efficiency7_05kg_motor_0_3Hztrimmed.xlsx');
cases(2).file_vsm  = fullfile(folder, 'Efficiency7_05kg_vsm_0_3Hztrimmed.xlsx');

%% ================= READ + PROCESS BOTH CASES =================
for k = 1:numel(cases)
    if ~isfile(cases(k).file_free) || ~isfile(cases(k).file_vsm)
        error('One or both files are missing for the %s case.', cases(k).name);
    end

    % ---- Current -> power -> cumulative energy ----
    T_free = readtable(cases(k).file_free);
    T_vsm  = readtable(cases(k).file_vsm);

    I_free = T_free.Var7;   % [A]
    I_vsm  = T_vsm.Var7;    % [A]

    P_free = V * abs(I_free);   % [W]
    P_vsm  = V * abs(I_vsm);    % [W]

    tE_free = (0:length(I_free)-1)' * Ts;
    tE_vsm  = (0:length(I_vsm)-1)'  * Ts;

    cases(k).tE_free = tE_free;
    cases(k).tE_vsm  = tE_vsm;
    cases(k).E_free  = cumtrapz(tE_free, P_free);   % [J]
    cases(k).E_vsm   = cumtrapz(tE_vsm,  P_vsm);    % [J]

    % ---- Tracking signals ----
    data_free = readmatrix(cases(k).file_free);
    data_vsm  = readmatrix(cases(k).file_vsm);

    cases(k).t_free     = data_free(:,1) - data_free(1,1);
    cases(k).y_free     = data_free(:,3);
    cases(k).y_act_free = data_free(:,2);

    cases(k).t_vsm      = data_vsm(:,1) - data_vsm(1,1);
    cases(k).y_vsm      = data_vsm(:,3);
    cases(k).y_act_vsm  = data_vsm(:,2);

    cases(k).err_free = cases(k).y_act_free - cases(k).y_free;
    cases(k).err_vsm  = cases(k).y_act_vsm  - cases(k).y_vsm;

    % ---- Results ----
    Etot_free = cases(k).E_free(end);
    Etot_vsm  = cases(k).E_vsm(end);
    RMSE_free = sqrt(mean(cases(k).err_free.^2));
    RMSE_VSM  = sqrt(mean(cases(k).err_vsm.^2));

    fprintf('\n===== %s =====\n', cases(k).name);
    fprintf('Energy - Free mode      : %.3f J\n', Etot_free);
    fprintf('Energy - VSM assistance : %.3f J\n', Etot_vsm);
    fprintf('Energy reduction        : %.2f %%\n', 100*(Etot_free - Etot_vsm)/Etot_free);
    fprintf('RMSE - Free mode        : %.3f deg\n', RMSE_free);
    fprintf('RMSE - VSM assistance   : %.3f deg\n', RMSE_VSM);
end

%% ================= TRACKING ENVELOPE PLOTS (one figure per case) =================
color_free = [0.121 0.235 0.498];   % Navy
color_vsm  = [0.890 0.690 0.106];   % Mustard / Goldenrod
opacity1   = 0.4;
opacity2   = 0.5;

for k = 1:numel(cases)
    c = cases(k);

    y_free_smooth = smoothdata(c.y_free, 'movmean', 200);
    y_vsm_smooth  = smoothdata(c.y_vsm,  'movmean', 100);

    t_f   = c.t_free(:)';
    y_f_u = (y_free_smooth + c.err_free)';
    y_f_l = (y_free_smooth - c.err_free)';

    t_v   = c.t_vsm(:)';
    y_v_u = (y_vsm_smooth + c.err_vsm)';
    y_v_l = (y_vsm_smooth - c.err_vsm)';

    figure;
    tl = tiledlayout(2,1,'TileSpacing','compact','Padding','compact');
    title(tl, sprintf('Tracking for %s', c.name), 'FontName','Arial','FontSize',16);

    % ---------------- Free condition envelope ----------------
    nexttile;
    hFree = fill([t_f, fliplr(t_f)], [y_f_u, fliplr(y_f_l)], color_free, ...
        'FaceAlpha', opacity1, 'EdgeColor', 'none');
    hold on;
    hRef = plot(c.t_free, c.y_act_free, 'k--', 'LineWidth', 1.2);
    hold off;
    xlabel('Time (s)','FontName','Arial','FontSize',16);
    ylabel('θ (°)','FontName','Arial','FontSize',16);
    xlim([0 13.5]); ylim([20 80]);
    set(gca,'FontName','Arial','FontSize',16,'LineWidth',1.2);
    grid off; box on;

    % ---------------- VSM condition envelope ----------------
    nexttile;
    hVSM = fill([t_v, fliplr(t_v)], [y_v_u, fliplr(y_v_l)], color_vsm, ...
        'FaceAlpha', opacity2, 'EdgeColor', 'none');
    hold on;
    plot(c.t_free, c.y_act_free, 'k--', 'LineWidth', 1.2);
    hold off;
    xlabel('Time (s)','FontName','Arial','FontSize',16);
    ylabel('θ (°)','FontName','Arial','FontSize',16);
    xlim([0 13.5]); ylim([20 80]);
    set(gca,'FontName','Arial','FontSize',16,'LineWidth',1.2);
    grid off; box on;

    % ---------------- Single shared legend ----------------
    lg = legend([hFree, hVSM, hRef], {'Motor Only','Motor + VSM','Reference'}, ...
        'Orientation','horizontal','FontName','Arial','FontSize',16);
    lg.Layout.Tile = 'south';
end

%% ================= CUMULATIVE ENERGY: SUBPLOTS A (1kg) & B (0.64kg) =================
newcolors = [0.83 0.14 0.14;   % red
             1.00 0.54 0.00;   % orange
             0.47 0.25 0.80;   % purple
             0.25 0.80 0.54];  % green

figure;
tlE = tiledlayout(1,2,'TileSpacing','compact','Padding','compact');

for k = 1:numel(cases)
    c = cases(k);
    nexttile;
    h1 = plot(c.tE_free, c.E_free, ':',  'LineWidth', 2, 'Color', newcolors(1,:)); hold on;
    h2 = plot(c.tE_vsm,  c.E_vsm,  '-.', 'LineWidth', 2, 'Color', newcolors(4,:));
    hold off;

    title(c.title, 'FontName','Arial','FontSize',16,'FontWeight','normal');
    xlabel('Time (s)','FontName','Arial','FontSize',16);
    ylabel('Cumulative Energy (J)','FontName','Arial','FontSize',16);
    set(gca,'FontName','Arial','FontSize',16);
    xlim([0 13.25]);
    grid off; box on;
end

lgE = legend([h1 h2], {'Motor only','Motor+VSM'}, ...
    'Orientation','horizontal','FontName','Arial','FontSize',16);
lgE.Layout.Tile = 'south';
