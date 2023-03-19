function y = doFilter(x)
%DOFILTER 对输入 x 进行滤波并返回输出 y。

% MATLAB Code
% Generated by MATLAB(R) 9.8 and DSP System Toolbox 9.10.
% Generated on: 24-Aug-2020 10:11:00

%#codegen

% 要通过此函数生成 C/C++ 代码，请使用 codegen 命令。有关详细信息，请键入 'help codegen'。

persistent Hd;

if isempty(Hd)
    
    % 设计滤波器系数时使用了以下代码:
    %
    % Fstop = 0.5;   % Stopband Frequency
    % Fpass = 0.8;   % Passband Frequency
    % Astop = 80;    % Stopband Attenuation (dB)
    % Apass = 1;     % Passband Ripple (dB)
    % Fs    = 1000;  % Sampling Frequency
    %
    % h = fdesign.highpass('fst,fp,ast,ap', Fstop, Fpass, Astop, Apass, Fs);
    %
    % Hd = design(h, 'butter', ...
    %     'MatchExactly', 'stopband', ...
    %     'SystemObject', true);
    
    Hd = dsp.BiquadFilter( ...
        'Structure', 'Direct form II', ...
        'SOSMatrix', [1 -2 1 1 -1.99929616225198 0.999318954461862; 1 -2 1 1 ...
        -1.99794931769147 0.997972094547163; 1 -2 1 1 -1.99664547185903 ...
        0.996668233850725; 1 -2 1 1 -1.99541095206814 0.995433699986172; 1 -2 1 ...
        1 -1.99427059106548 0.99429332598326; 1 -2 1 1 -1.99324724579097 ...
        0.99326996904249; 1 -2 1 1 -1.99236136098417 0.992384074136501; 1 -2 1 1 ...
        -1.99163058418943 0.991653289010825; 1 -2 1 1 -1.99106943750609 ...
        0.991092135930341; 1 -2 1 1 -1.99068905030999 0.990711744397786; 1 -2 1 ...
        1 -1.99049695615576 0.990519648053659], ...
        'ScaleValues', [0.999653779178461; 0.998980353059658; ...
        0.998328426427438; 0.997711163013579; 0.997140979262185; ...
        0.996629303708364; 0.996186358780167; 0.995820968300064; ...
        0.995540393359107; 0.995350198676944; 0.995254151052354; 1]);
end

s = double(x);
y = step(Hd,s);

