clc;
clear;
close all;

%��������
clearvars -except ratio ratio_each x MF_each MF_each_low MF_each_high MF MF_low MF_high bound ;
fs=8000;%������
[name,fadd] = uigetfile('*.txt', 'Select an txt file'); %�ļ�����.��׺ ; ��ַ
rawDATA = load([fadd name],'%f');                          %��ȡ�����ļ�

ALLDATA = rawDATA';
dataN = length(ALLDATA);
chn = 2;%�������ܹ���ͨ����
actchn = 2;%ʵ�����õ�����ͨ����
groupnum = dataN / chn;%һͨ�������ܹ���������
num = 0;%���ʼ��������
% fnum = 200;%RMS�Ĳ�����
% filterdatafile = zeros(actchn,1);
% RMSdatafile = zeros(actchn,1);
times=dataN/fs;
% N=fs*times;                                    %FFT�����ʲ���


for group = 1:chn  %��nͨ��
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
% a=a(:, 5 *fs+1 : end) ;%ѡȡʱ��
% 
% datalength = length(a);
% for chnnum = 1:actchn
%     for i = 1:datalength
%         singledata(chnnum,i) = a(chnnum,i);
%     end
%     Rawdata(chnnum,:) = singledata(chnnum,:)- mean(singledata(chnnum,:));  %�����Ƴ�
%     %             Rawdata(chnnum,:) = singledata(chnnum,:);
%     
%     if chnnum == 1


for i = 1:actchn
    Rawdata(i,:) = a(i,:) - mean(a(i,5*fs+1:end));
end

chnnum = 1;
datalength = groupnum;
        
        % ԭʼ����---------------------------------------------------------------
        figure(1);
        dcm_obj = datacursormode(gcf);
        set(dcm_obj,'UpdateFcn',@NewCallback);
        
        plot((0:(datalength-1))*(1/fs),Rawdata(chnnum,:));
        xlabel ('ʱ�䣨s��');
        ylabel ('��ֵ(uV)');
        title(['�˲�ǰ�ź�ͨ��' num2str(chnnum)]);
        axis([0 datalength/fs -inf inf]);
        hold on;
        
        N=fs*4.096;
        %             N=fs;
        y=fft(Rawdata(chnnum,:), N);
        mag=abs (y);
        f=(0:N-1) /N*fs;
        
        
        %����Ҷ�任-------------------------------------------------------------
        
        [b2 b1]=butter(4,5*2/fs,'high');%�˲�
        data_filter=filter(b2,b1,Rawdata(chnnum,:));
        
        y_filter=fft(data_filter,N);
        abs_y_filter = abs(y_filter);
        Filterdata = data_filter;
        
        figure(2);
        dcm_obj = datacursormode(gcf);
        set(dcm_obj,'UpdateFcn',@NewCallback);
        
        plot((0:(datalength-1))*(1/fs),Filterdata);
        set(gca,'Fontname','Monospaced');
        xlabel ('ʱ�䣨s��');
        ylabel ('��ֵ(uV)');
        title(['�˲����ź�ͨ��' num2str(chnnum)]);
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
        
