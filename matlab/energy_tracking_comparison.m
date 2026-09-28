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

%% ================= CUMULATIVE ENERGY (HATCHED): A (1kg) & B (0.64kg) =================
col_free = [0.83 0.14 0.14];   % red   - Motor only  (dotted \\\\ lines)
col_vsm  = [0.13 0.60 0.30];   % green - Motor + VSM (solid //// lines)
t_end    = 13.25;              % [s] plotted time span
gap_px   = 9;                  % spacing between hatch lines [pixels]

% Common y-limit so A and B are directly comparable
Emax = 0;
for k = 1:numel(cases)
    Emax = max([Emax; cases(k).E_free(cases(k).tE_free <= t_end); ...
                      cases(k).E_vsm(cases(k).tE_vsm  <= t_end)]);
end
y_top = 1.15*Emax;

figure('Color','w','Position',[100 100 1200 480]);
tiledlayout(1,2,'TileSpacing','compact','Padding','compact');
ax = gobjects(1,numel(cases));
hC = gobjects(numel(cases),2);

% ---- Curves, labels, saving text ----
for k = 1:numel(cases)
    c = cases(k);
    ax(k) = nexttile; hold on;

    hC(k,1) = plot(c.tE_free, c.E_free, '-', 'Color', col_free, 'LineWidth', 2);
    hC(k,2) = plot(c.tE_vsm,  c.E_vsm,  '-', 'Color', col_vsm,  'LineWidth', 2);

    Ef_end = interp1(c.tE_free, c.E_free, min(t_end, c.tE_free(end)));
    Ev_end = interp1(c.tE_vsm,  c.E_vsm,  min(t_end, c.tE_vsm(end)));
    text(0.04, 0.95, sprintf('Energy saving: %.1f %%', 100*(Ef_end - Ev_end)/Ef_end), ...
        'Units','normalized','FontName','Arial','FontSize',14,'FontWeight','bold', ...
        'VerticalAlignment','top','BackgroundColor','w','Margin',1);

    title(c.title, 'FontName','Arial','FontSize',16,'FontWeight','normal');
    xlabel('Time (s)','FontName','Arial','FontSize',16);
    ylabel('Cumulative Energy (J)','FontName','Arial','FontSize',16);
    set(gca,'FontName','Arial','FontSize',16,'LineWidth',1.2,'Layer','top');
    xlim([0 t_end]); ylim([0 y_top]);
    grid off; box on;
end

lgE = legend(ax(end), hC(end,:), {'Motor only','Motor + VSM'}, ...
    'Orientation','horizontal','FontName','Arial','FontSize',16,'AutoUpdate','off');
lgE.Layout.Tile = 'south';
drawnow;   % finalise layout so hatch angles use the real axes size

% ---- Hatching under each curve ----
for k = 1:numel(cases)
    c  = cases(k);
    kf = c.tE_free <= t_end;
    kv = c.tE_vsm  <= t_end;
    hatch_area(ax(k), c.tE_free(kf), zeros(nnz(kf),1), c.E_free(kf), col_free, -45, gap_px, ':', 1.3);
    hatch_area(ax(k), c.tE_vsm(kv),  zeros(nnz(kv),1), c.E_vsm(kv),  col_vsm,   45, gap_px, '-', 1.0);
    uistack(hC(k,:), 'top');
    uistack(findobj(ax(k), 'Type', 'text'), 'top');
end

%% ================= LOCAL FUNCTIONS (must stay at the end of the script) =================
function h = hatch_area(ax, t, y_low, y_up, col, angle_deg, gap_px, ls, lw)
% Fill the region y_low <= y <= y_up with parallel lines at angle_deg (on screen).
t = t(:); y_low = y_low(:); y_up = y_up(:);

p  = getpixelposition(ax);
sx = p(3) / diff(xlim(ax));                  % pixels per second
sy = p(4) / diff(ylim(ax));                  % pixels per joule
m  = tand(angle_deg) * sx / sy;              % data slope giving the on-screen angle
dc = gap_px / (sx * abs(sind(angle_deg)));   % intercept step giving gap_px spacing

cr = [t(1) - [min(y_low) max(y_up)]/m, t(end) - [min(y_low) max(y_up)]/m];
c  = (min(cr) - dc) : dc : (max(cr) + dc);   % line intercepts on the time axis

Y = m * (t - c);                             % one column per hatch line
Y(Y < y_low | Y > y_up) = NaN;               % keep only the part inside the region
Y(:, all(isnan(Y), 1)) = [];
X = repmat(t, 1, size(Y, 2));
X(end+1, :) = NaN;  Y(end+1, :) = NaN;       % break between lines

h = plot(ax, X(:), Y(:), ls, 'Color', col, 'LineWidth', lw, 'HandleVisibility', 'off');
end
