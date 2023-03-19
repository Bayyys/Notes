function y = doFilter(x)
%DOFILTER 对输入 x 进行滤波并返回输出 y。

% MATLAB Code
% Generated by MATLAB(R) 9.8 and DSP System Toolbox 9.10.
% Generated on: 09-Sep-2020 15:18:18

%#codegen

% 要通过此函数生成 C/C++ 代码，请使用 codegen 命令。有关详细信息，请键入 'help codegen'。

persistent Hd;

if isempty(Hd)
    
    % 设计滤波器系数时使用了以下代码:
    %
    % Fpass1 = 47;    % First Passband Frequency
    % Fstop1 = 49;    % First Stopband Frequency
    % Fstop2 = 51;    % Second Stopband Frequency
    % Fpass2 = 53;    % Second Passband Frequency
    % Apass1 = 1;     % First Passband Ripple (dB)
    % Astop  = 60;    % Stopband Attenuation (dB)
    % Apass2 = 1;     % Second Passband Ripple (dB)
    % Fs     = 1000;  % Sampling Frequency
    %
    % h = fdesign.bandstop('fp1,fst1,fst2,fp2,ap1,ast,ap2', Fpass1, Fstop1, ...
    %                      Fstop2, Fpass2, Apass1, Astop, Apass2, Fs);
    %
    % Hd = design(h, 'butter', ...
    %     'MatchExactly', 'stopband', ...
    %     'SystemObject', true);
    
    Hd = dsp.BiquadFilter( ...
        'Structure', 'Direct form II', ...
        'SOSMatrix', [1 -1.90245099848081 1 1 -1.88608648330375 ...
        0.993465262659601; 1 -1.90245099848081 1 1 -1.90602134053192 ...
        0.994067066302791; 1 -1.90245099848081 1 1 -1.87648329471124 ...
        0.981629395420204; 1 -1.90245099848081 1 1 -1.89417229611244 ...
        0.983066831334135; 1 -1.90245099848081 1 1 -1.87117335356578 ...
        0.972981424573822; 1 -1.90245099848081 1 1 -1.88338962812532 ...
        0.974407951845028; 1 -1.90245099848081 1 1 -1.87080217126322 ...
        0.968747216337919; 1 -1.90245099848081 1 1 -1.8751666387667 ...
        0.969335792499314], ...
        'ScaleValues', [0.996759863158372; 0.996759863158372; ...
        0.99108588096696; 0.99108588096696; 0.98680806985864; 0.98680806985864; ...
        0.984515913911964; 0.984515913911964; 1]);
end

s = double(x);
y = step(Hd,s);

