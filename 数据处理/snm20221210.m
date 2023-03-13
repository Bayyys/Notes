clc;
clear;
close all;

%参数设置
clearvars -except ratio ratio_each x MF_each MF_each_low MF_each_high MF MF_low MF_high bound ;
fs=8000;%采样率
[name,fadd] = uigetfile('*.txt', 'Select an txt file'); %文件名称.后缀 ; 地址
rawDATA = load([fadd name],'%f');                          %读取数据文件

ALLDATA = rawDATA';
dataN = length(ALLDATA);
chn = 2;%数据中总共的通道数
actchn = 2;%实际有用的数据通道数
groupnum = dataN / chn;%一通道数据总共的数据量
num = 0;%从最开始的数读起
% fnum = 200;%RMS的步长；
% filterdatafile = zeros(actchn,1);
% RMSdatafile = zeros(actchn,1);
times=dataN/fs;
% N=fs*times;                                    %FFT采样率参数


for group = 1:chn  %第n通道
    for i = 1:groupnum
        a(group, i) = ALLDATA(group - 2 + 2*i);
%         a(group, i) = ALLDATA(num*chn + group);
%         num = num + 1;
    end
%     if num == groupnum
%         num = 0;
%         group = group + 1;
%     end
end
%
% a=a(:, 5 *fs+1 : end) ;%选取时间
% 
% datalength = length(a);
% for chnnum = 1:actchn
%     for i = 1:datalength
%         singledata(chnnum,i) = a(chnnum,i);
%     end
%     Rawdata(chnnum,:) = singledata(chnnum,:)- mean(singledata(chnnum,:));  %基线移除
%     %             Rawdata(chnnum,:) = singledata(chnnum,:);
%     
%     if chnnum == 1


for i = 1:actchn
    Rawdata(i,:) = a(i,:) - mean(a(i,5*fs+1:end));
end

chnnum = 1;
datalength = groupnum;
        
        % 原始数据---------------------------------------------------------------
        figure(1);
        dcm_obj = datacursormode(gcf);
        set(dcm_obj,'UpdateFcn',@NewCallback);
        
        plot((0:(datalength-1))*(1/fs),Rawdata(chnnum,:));
        xlabel ('时间（s）');
        ylabel ('幅值(uV)');
        title(['滤波前信号通道' num2str(chnnum)]);
        axis([0 datalength/fs -inf inf]);
        hold on;
        
        N=fs*4.096;
        %             N=fs;
        y=fft(Rawdata(chnnum,:), N);
        mag=abs (y);
        f=(0:N-1) /N*fs;
        
        
        %傅里叶变换-------------------------------------------------------------
        
        [b2 b1]=butter(4,5*2/fs,'high');%滤波
        data_filter=filter(b2,b1,Rawdata(chnnum,:));
        
        y_filter=fft(data_filter,N);
        abs_y_filter = abs(y_filter);
        Filterdata = data_filter;
        
        figure(2);
        dcm_obj = datacursormode(gcf);
        set(dcm_obj,'UpdateFcn',@NewCallback);
        
        plot((0:(datalength-1))*(1/fs),Filterdata);
        set(gca,'Fontname','Monospaced');
        xlabel ('时间（s）');
        ylabel ('幅值(uV)');
        title(['滤波后信号通道' num2str(chnnum)]);
        axis([0 datalength/fs -inf inf]);
        hold on;
        
        
        temp = Rawdata(1,:);
        TEMP = fft(temp);
        L = length(temp);
%         P2 = abs(TEMP/L);
%         P1 = P2(1:L/2+1);
%         P1(2:end-1) = 2*P1(2:end-1);
        F = fs*(0:L-1)/L;
        figure(3);
        plot(F,abs(TEMP));
        
