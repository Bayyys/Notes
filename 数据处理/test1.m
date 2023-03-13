clc;
clear;
close all;

%��������%��������
fs=8000;%������
[name,fadd] = uigetfile('*.txt', 'Select an txt file'); %�ļ�����.��׺ ; ��ַ
rawDATA = load([fadd name],'%f');                          %��ȡ�����ļ�

ALLDATA = rawDATA';
dataN = length(ALLDATA);
chn = 2;%�������ܹ���ͨ����
actchn = 2;%ʵ�����õ�����ͨ����

groupnum = dataN / chn;%һͨ�������ܹ���������
times=([1:groupnum]-1)/fs;%ʱ���

for group = 1:chn  %��nͨ��
    for i = 1:groupnum
        a(group, i) = ALLDATA(group - chn + chn*i);
    end
end

%�����Ƴ�
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

% ԭʼ����(�����Ƴ�ǰ)---------------------------------------------------------------
figure(1);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(times,a(chnnum,:));
xlabel ('ʱ�䣨s��');   ylabel ('��ֵ(uV)');
title(['�˲�ǰ�ź�ͨ��' num2str(chnnum)]);
hold on;

% ԭʼ����(�����Ƴ���)---------------------------------------------------------------
figure(2);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(times,Rawdata(chnnum,:));
xlabel ('ʱ�䣨s��');   ylabel ('��ֵ(uV)');
title(['�˲�ǰ�ź�ͨ��' num2str(chnnum)]);
hold on;


%Ƶ��ͼ
N = groupnum;
%ֱ��ʹ��fft
y = fft(Rawdata(chnnum,:));
%fftshift()����0Ƶλ��
y1 = fftshift(y);
%��������ת����Ƶ�ʷ�Χ 0Hz - fs/2
f =(N/2:N-1)*fs/N - fs/2 ;
%��ֵ�����õ���ʵ��ֵ
y2 = abs(y1);
y3 =  2*y2(N/2:N-1)/N;
figure(3);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(f,y3);
xlabel('Frequency');    ylabel('Amplitude');    hold on;


%����Ҷ�任-------------------------------------------------------------

% [b2 b1]=butter(4,[20*2/fs, 1000*2/fs]);%�˲�
[b2 b1]=butter(4,1*2/fs,'high');%�˲�
% [b2 b1]=butter(6,1500*2/fs,'low');%�˲�
% [b2 b1]=butter(4,[1*2/fs, 1000*2/fs]);%�˲�
data_filter=filter(b2,b1,Rawdata(chnnum,:));

% [c2 c1] = butter(4,[45*2/fs, 55*2/fs]);%�˲�
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
xlabel ('ʱ�䣨s��');
ylabel ('��ֵ(uV)');
title(['�˲����ź�ͨ��' num2str(chnnum)]);
axis([0 datalength/fs -inf inf]);
hold on;


%Ƶ��ͼ
N = groupnum;
%ֱ��ʹ��fft
y = fft(Filterdata);
%fftshift()����0Ƶλ��
y1 = fftshift(y);
%��������ת����Ƶ�ʷ�Χ 0Hz - fs/2
f =(N/2:N-1)*fs/N - fs/2 ;
%��ֵ�����õ���ʵ��ֵ
y2 = abs(y1);
y3 =  2*y2(N/2:N-1)/N;
figure(5);
% dcm_obj = datacursormode(gcf);
% set(dcm_obj,'UpdateFcn',@NewCallback);

plot(f,y3);
xlabel('Frequency');    ylabel('Amplitude');    hold on;

