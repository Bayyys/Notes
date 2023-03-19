clc;
clear;
close all;

%参数设置%参数设置
fs=8000;%采样率
[name,fadd] = uigetfile('*.txt', 'Select an txt file'); %文件名称.后缀 ; 地址
rawDATA = load([fadd name],'%f');                          %读取数据文件

ALLDATA = rawDATA';
dataN = length(ALLDATA);
chn = 2;%数据中总共的通道数
actchn = 2;%实际有用的数据通道数

groupnum = dataN / chn;%一通道数据总共的数据量
times=([1:groupnum]-1)/fs;%时间戳

for group = 1:chn  %第n通道
    for i = 1:groupnum
        a(group, i) = ALLDATA(group - chn + chn*i);
    end
end

%基线移除
for i = 1:actchn
     Rawdata(i,:) = a(i,:);
     for j = (fs/2+1):(groupnum-fs/2)
         Rawdata(i,j) =  a(i,j) - mean(a(i,(j-fs/2):(j+fs/2)));
     end
     
     Rawdata(i,1:fs/2) = zeros(1,fs/2);
     Rawdata(i,j+1:end) = zeros(1,fs/2);
%      Rawdata(i,:) = a(i,:) - mean(a(i,10*fs+1:end));
end

chnnum = 1;
datalength = groupnum;

% 原始数据(基线移除前)---------------------------------------------------------------
figure(1);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(times,a(chnnum,:));
xlabel ('时间（s）');   ylabel ('幅值(uV)');
title(['滤波前信号通道' num2str(chnnum)]);
hold on;

% 原始数据(基线移除后)---------------------------------------------------------------
figure(2);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(times,Rawdata(chnnum,:));
xlabel ('时间（s）');   ylabel ('幅值(uV)');
title(['滤波前信号通道' num2str(chnnum)]);
hold on;


%频谱图
N = groupnum;
%直接使用fft
y = fft(Rawdata(chnnum,:));
%fftshift()调整0频位置
y1 = fftshift(y);
%将横坐标转化，频率范围 0Hz - fs/2
f =(N/2:N-1)*fs/N - fs/2 ;
%幅值修正得到真实幅值
y2 = abs(y1);
y3 =  2*y2(N/2:N-1)/N;
figure(3);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(f,y3);
xlabel('Frequency');    ylabel('Amplitude');    hold on;


%傅里叶变换-------------------------------------------------------------

% [b2 b1]=butter(4,[20*2/fs, 1000*2/fs]);%滤波
[b2 b1]=butter(4,1*2/fs,'high');%滤波
% [b2 b1]=butter(6,1500*2/fs,'low');%滤波
% [b2 b1]=butter(4,[1*2/fs, 1000*2/fs]);%滤波
data_filter=filter(b2,b1,Rawdata(chnnum,:));

% [c2 c1] = butter(4,[45*2/fs, 55*2/fs]);%滤波
% data_filter2 = filter(c2,c1,Rawdata(chnnum,:));
% 
% Filterdata = data_filter - data_filter2;

[c2 c1] = butter(4,1000*2/fs,'low');
Filterdata = filter(c2,c1,data_filter);

figure(4);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot((0:(datalength-1))*(1/fs),Filterdata);
set(gca,'Fontname','Monospaced');
xlabel ('时间（s）');
ylabel ('幅值(uV)');
title(['滤波后信号通道' num2str(chnnum)]);
axis([0 datalength/fs -inf inf]);
hold on;


%频谱图
N = groupnum;
%直接使用fft
y = fft(Filterdata);
%fftshift()调整0频位置
y1 = fftshift(y);
%将横坐标转化，频率范围 0Hz - fs/2
f =(N/2:N-1)*fs/N - fs/2 ;
%幅值修正得到真实幅值
y2 = abs(y1);
y3 =  2*y2(N/2:N-1)/N;
figure(5);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(f,y3);
xlabel('Frequency');    ylabel('Amplitude');    hold on;

