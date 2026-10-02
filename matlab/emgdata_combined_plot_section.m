%% 4. Combined Figure: Angle + EMG + Torque + Force + Current (all Arial)
% Replaces the old "4. Generate Publication-Quality Subplots" section.
% Uses variables already created above in emgdata:
%   timeVec, angle1, angle2, raise_cuts, lower_cuts      (kinematics + events)
%   timeVec_EMG, emg_data                                (raw EMG)
%   dataMatrix  (Excel, rows: 1 time, 2 desired, 3 traced, 4 tau_ff,
%                5 tau_fb, 6 tau total, 7 force, 8 current)

% ====================== SETTINGS ======================
fontName      = 'Arial';
xRange        = [0 65.5];   % time window shown (s)
emgScale      = 1;          % factor to convert EMG to µV (e.g. 1e6 if stored in V)
useForceDelta = true;       % true = force relative to first sample (same as exodata)
fsLabel       = 13;         % right-hand signal names
fsTick        = 11;         % y-tick labels

% ====================== EXO SIGNALS FROM THE EXCEL FILE ======================
if size(dataMatrix, 1) < 8
    error('Excel data has %d rows; expected 8 (time, 2 angles, 3 torques, force, current).', ...
          size(dataMatrix, 1));
end
tau_ff    = dataMatrix(4, :);
tau_fb    = dataMatrix(5, :);
tau_total = dataMatrix(6, :);
force     = dataMatrix(7, :);
current   = dataMatrix(8, :);
if useForceDelta
    force = force - force(find(~isnan(force), 1));
end

% ====================== COLOURS ======================
c.target  = [0.75 0.75 0.75];   % target (desired) angle - light grey
c.tracked = [0.55 0.20 0.85];   % tracked (traced) angle - purple
c.emg     = [0.45 0.45 0.45];   % EMG - grey
c.tau_ff  = [0.20 0.60 0.30];   % feed-forward torque - green
c.tau_fb  = [0.90 0.35 0.35];   % feed-back torque - red
c.tau     = [0.50 0.50 0.50];   % total torque - grey
c.force   = [0.10 0.10 0.60];   % interaction force - dark blue
c.current = [0.60 0.15 0.50];   % current - magenta/purple
c.raise   = [0.90 0.30 0.30];   % upwards motion - red
c.lower   = [0.30 0.50 0.85];   % downwards motion - blue
c.axis    = [0.40 0.40 0.40];   % y-axis lines and tick labels
c.label   = [0.45 0.45 0.45];   % grey right-hand labels

% ====================== AXIS LIMIT HELPER ======================
% Rounds the data range outwards to a multiple of "step"
niceLim = @(v, step) [floor(min(v(:)) / step) * step, ceil(max(v(:)) / step) * step];

% Common symmetric EMG limit (99.9th percentile of |EMG| over all muscles)
emgAll = cellfun(@(e) e * emgScale, emg_data, 'UniformOutput', false);
emgLim = 0;
for i = 1:numel(emgAll)
    s = sort(abs(emgAll{i}(~isnan(emgAll{i}))));
    if ~isempty(s)
        emgLim = max(emgLim, s(ceil(0.999 * numel(s))));
    end
end
if emgLim <= 0
    emgLim = 1;
end
mag    = 10^floor(log10(emgLim));
emgLim = ceil(emgLim / mag) * mag;

% ====================== FIGURE + MANUAL PANEL LAYOUT ======================
fig = figure('Color', 'w', ...
    'Name', [participantID ' ' loadCondition ' - Kinematics, EMG & Exo Signals'], ...
    'Position', [100 40 1000 1050]);
set(fig, 'DefaultAxesFontName', fontName, 'DefaultTextFontName', fontName);

% Panel order (top -> bottom) and relative heights
weights = [1.4 1 1 1 1 1.1 1.1 1];   % angle, AD, MD, PEC, UT, torque, force, current
left    = 0.09;                      % left margin (y-tick labels)
width   = 0.70;                      % plot width (room on the right for labels)
bottom0 = 0.08;                      % bottom margin (motion labels)
top0    = 0.98;
gap     = 0.012;

nP     = numel(weights);
usable = (top0 - bottom0) - gap * (nP - 1);
h      = usable * weights / sum(weights);

ax   = gobjects(1, nP);
yPos = top0;
for p = 1:nP
    yPos  = yPos - h(p);
    ax(p) = axes(fig, 'Position', [left yPos width h(p)]);
    styleAxis(ax(p), c.axis, fsTick, fontName);
    yPos  = yPos - gap;
end

% ====================== PANEL 1: JOINT ANGLES ======================
a = ax(1);
plot(a, timeVec, angle1, '-', 'LineWidth', 3.0, 'Color', c.target);
plot(a, timeVec, angle2, '-', 'LineWidth', 2.0, 'Color', c.tracked);

if ~isempty(raise_cuts)
    scatter(a, raise_cuts, interp1(timeVec, angle2, raise_cuts), 70, c.raise, ...
        'filled', 'MarkerEdgeColor', 'w', 'LineWidth', 1.2);
end
if ~isempty(lower_cuts)
    scatter(a, lower_cuts, interp1(timeVec, angle2, lower_cuts), 70, c.lower, ...
        'filled', 'MarkerEdgeColor', 'w', 'LineWidth', 1.2);
end

setEndTicks(a, [40 110], '%g°', 0.08);
sideLabel(a, 'Target angle',  c.target,  0.75, fsLabel, fontName);
sideLabel(a, 'Tracked angle', c.tracked, 0.40, fsLabel, fontName);

% ====================== PANELS 2-5: RAW EMG ======================
muscleLabels = {{'Anterior', 'Deltoid'}, {'Medial', 'Deltoid'}, ...
                {'Pectoralis', 'Major'}, {'Upper', 'Trapezius'}};

for i = 1:4
    a = ax(1 + i);
    plot(a, timeVec_EMG, emgAll{i}, '-', 'LineWidth', 0.5, 'Color', c.emg);
    a.YLim = [-emgLim emgLim];

    if i == 1
        % Only the top EMG panel carries the amplitude scale (shared by all)
        setEndTicks(a, [-emgLim emgLim], '%g µV', 0);
    else
        a.YColor = 'none';
    end
    sideLabel(a, muscleLabels{i}, c.label, 0.5, fsLabel, fontName);
end

% ====================== PANEL 6: TORQUES ======================
a = ax(6);
plot(a, timeVec, tau_total, '-', 'LineWidth', 1.8, 'Color', c.tau);
plot(a, timeVec, tau_ff,    '-', 'LineWidth', 1.8, 'Color', c.tau_ff);
plot(a, timeVec, tau_fb,    '-', 'LineWidth', 1.8, 'Color', c.tau_fb);

setEndTicks(a, niceLim([tau_ff tau_fb tau_total], 1), '%g Nm', 0.05);
sideLabel(a, 'Feed-forward torque', c.tau_ff, 0.80, fsLabel, fontName);
sideLabel(a, 'Feed-back torque',    c.tau_fb, 0.50, fsLabel, fontName);
sideLabel(a, 'Total torque',        c.tau,    0.20, fsLabel, fontName);

% ====================== PANEL 7: INTERACTION FORCE ======================
a = ax(7);
plot(a, timeVec, force, '-', 'LineWidth', 2.0, 'Color', c.force);

setEndTicks(a, niceLim(force, 10), '%g N', 0.05);
sideLabel(a, {'Interaction', 'Force'}, c.force, 0.5, fsLabel, fontName);

% ====================== PANEL 8: MOTOR CURRENT ======================
a = ax(8);
plot(a, timeVec, current, '-', 'LineWidth', 2.0, 'Color', c.current);

setEndTicks(a, niceLim(current, 1), '%g A', 0.05);
sideLabel(a, 'Current', c.current, 0.5, fsLabel, fontName);

% ====================== EVENT LINES ACROSS ALL PANELS ======================
% A transparent overlay axes spanning from the bottom panel up to the top of
% the first EMG panel, so each event is one continuous dashed line.
ovBottom = ax(end).Position(2);
ovTop    = ax(2).Position(2) + ax(2).Position(4);
axOv = axes(fig, 'Position', [left ovBottom width ovTop - ovBottom], ...
    'Color', 'none', 'XLim', xRange, 'YLim', [0 1], ...
    'Visible', 'off', 'HitTest', 'off', 'PickableParts', 'none');
hold(axOv, 'on');

for x = raise_cuts(:)'
    plot(axOv, [x x], [0 1], '--', 'Color', c.raise, 'LineWidth', 1.2);
end
for x = lower_cuts(:)'
    plot(axOv, [x x], [0 1], '--', 'Color', c.lower, 'LineWidth', 1.2);
end

% "Upwards / Downwards motion" labels under the first event of each type
if ~isempty(raise_cuts)
    text(axOv, raise_cuts(1), -0.01, {'Upwards', 'motion'}, ...
        'Color', c.raise, 'FontName', fontName, 'FontSize', fsLabel, ...
        'HorizontalAlignment', 'center', 'VerticalAlignment', 'top', 'Clipping', 'off');
end
if ~isempty(lower_cuts)
    text(axOv, lower_cuts(1), -0.01, {'Downwards', 'motion'}, ...
        'Color', c.lower, 'FontName', fontName, 'FontSize', fsLabel, ...
        'HorizontalAlignment', 'center', 'VerticalAlignment', 'top', 'Clipping', 'off');
end

% ====================== SYNC TIME AXES + FORCE ARIAL ======================
linkaxes([ax axOv], 'x');
xlim(ax(1), xRange);

set(findall(fig, '-property', 'FontName'), 'FontName', fontName);

fprintf('Plotted: %d Raise | %d Lower events\n', length(raise_cuts), length(lower_cuts));

%% 5. Save Figure + Data
figBase = [participantID '_' loadCondition '_combined'];

% ---- Live figure for supervisor ----
savefig(fig, [figBase '.fig']);

% ---- 300 dpi image ----
exportgraphics(fig, [figBase '.png'], 'Resolution', 300);

% ---- Underlying data so he can iterate ----
save([figBase '_figdata.mat'], ...
     'timeVec', 'angle1', 'angle2', ...
     'timeVec_EMG', 'emg_data', ...
     'tau_ff', 'tau_fb', 'tau_total', 'force', 'current', ...
     'raise_cuts', 'lower_cuts', ...
     'EMG_SF', 'EXO_SF');

fprintf('Saved .fig, .png and .mat to: %s\n', pwd);


%% ====================== LOCAL HELPER FUNCTIONS ======================
% (Must stay at the very END of the script file.)

function styleAxis(a, axCol, fs, fn)
    % Clean panel: no box, no x-axis, thin grey y-axis only
    hold(a, 'on');
    set(a, 'Color', 'none', 'Box', 'off', ...
        'FontName', fn, 'FontSize', fs, ...
        'XColor', 'none', 'YColor', axCol, ...
        'TickDir', 'out', 'TickLength', [0.005 0.005], ...
        'LineWidth', 0.8, 'TickLabelInterpreter', 'none');
end

function setEndTicks(a, ticks, fmt, pad)
    % Two ticks (min and max) with units, e.g. '40°' / '110°'
    if ticks(1) == ticks(2)
        ticks = ticks + [-1 1];
    end
    r = ticks(2) - ticks(1);
    a.YLim       = [ticks(1) - pad * r, ticks(2) + pad * r];
    a.YTick      = ticks;
    a.YTickLabel = {sprintf(fmt, ticks(1)), sprintf(fmt, ticks(2))};
end

function sideLabel(a, str, col, yPos, fs, fn)
    % Coloured signal name to the right of a panel
    text(a, 1.02, yPos, str, 'Units', 'normalized', ...
        'Color', col, 'FontName', fn, 'FontSize', fs, ...
        'HorizontalAlignment', 'left', 'VerticalAlignment', 'middle', ...
        'Clipping', 'off');
end
