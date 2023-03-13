clear;
close all;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%��ȡ����
[name,fadd] = uigetfile('*.txt', 'Select an txt file'); %�ļ�����.��׺ ; ��ַ  
data = load(name,'%f');                                 %��ȡ�����ļ�

% name='li_2.5kg_fali1_p';
% name=[name '.txt'];
% data = load(name,'%f');%��ȡ�����ļ�
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%�������
Fs=8000;                                                %������
datalength=size(data,2);                                %���ݳ���
plot((0:(datalength-1))*(1/Fs),data(1,:));              %���Ƶ�һͨ������ͼ���ο�
xlabel ('ʱ�䣨s��');    
ylabel ('��ֵ(uV)');
% dataend = 15;
% datastart = 5;
% dat=data(:,(datastart)*Fs+1:(dataend)*Fs);
dat=data;                                               %���ݳ��Ƚ�ѡ

chnum=2;                                                %ͨ������ѡ
[chnum,datalength]=size(dat);
times=datalength/Fs;                                    %FFT�����ʲ���
N=Fs*times;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% �����źŷ�ֵͼ %%%%%
[m,~]=max(dat');
[m,index]=max(m);
range=1.1*m;                                            %ͳһy������
for chnnum = 1:chnum
    rmsd=rms(dat(chnnum,: ));                           %����RMSֵ
    subplot(2,chnum/2,chnnum);
    plot((0:(datalength-1))*(1/Fs),dat(chnnum,: ));
    xlabel ('ʱ�䣨s��');
    ylabel ('��ֵ(uV)');
    title(['�����ź� ͨ��' num2str(chnnum) ' RMS=' num2str(rmsd)]);
    axis([0 datalength/Fs -range range]);  
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% ������ RMS ͼ %%%%%
dat_rms=[];
rms_n=Fs*0.5;                                             %��������
step=1/4;                                               %�������ص���
long=floor(datalength/rms_n);                           %����������
for chnnum = 1:chnum
   for j=1:(long-1)/step+1     % (L-N)/S+1
    n_start=(j-1)*rms_n*step+1;
    n_end=(j-1)*rms_n*step+rms_n;
    dat_rms(chnnum,j)=rms(dat(chnnum,n_start:n_end));
   end
    subplot(2,chnum/2,chnnum);
    plot((1:(long-1)/step+1)*(rms_n*step/Fs),dat_rms(chnnum,: ));
    xlabel ('ʱ�䣨s��');
    ylabel ('��ֵ(uV)');
    title(['RMS ͨ��' num2str(chnnum)]);
    axis([0 datalength/Fs -inf inf]);  
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(3);                     %%%%% Ƶ��ͼ %%%%%
fA_range=0;
for i=1:chnum
    data_i=dat(i,:);
    y=abs(fft(data_i,N));
    [m,index]=max(y);
    fA_range=max(fA_range,m);                           %ͳһy������
end
for i=1:chnum
    data_i=dat(i,:);
    y=abs(fft(data_i,N));
    md=medfreq(data_i,Fs);                              %������ֵƵ��
    emg_mf(i,1)=md;
    subplot(2,chnum/2,i);
    plot((1:N/2)/times,y(1:N/2));
    xlabel ('Ƶ��(Hz)');
    ylabel ('��ֵ');
    title(['����Ƶ�� ͨ��' num2str(i)  ' MF=' num2str(md)]);
    axis([-inf inf -inf fA_range*1.1]);  
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% ��ֵƵ�� MF ͼ %%%%%
dat_MF=[];
% rms_n=Fs*2;                                             %��������
step=1/4;                                               %�������ص���
long=floor(datalength/rms_n);                           %����������
fA_range=0;
for chnnum = 1:chnum
    for j=1:(long-1)/step+1     % (L-N)/S+1
    n_start=(j-1)*rms_n*step+1;
    n_end=(j-1)*rms_n*step+rms_n;
    dat_MF(chnnum,j)=medfreq(dat(chnnum,n_start:n_end),Fs);
    end
%     dat_MF(chnnum,:) = dat_MF(chnnum,:)-mean(dat_MF(chnnum,:))
    [m,index]=max(dat_MF(chnnum,:));
    fA_range=max(fA_range,m);
end
  for chnnum = 1:chnum 
    subplot(2,chnum/2,chnnum);
    time = ((1:(long-1)/step+1)*(rms_n*step/Fs));
    plot((1:(long-1)/step+1)*(rms_n*step/Fs),dat_MF(chnnum,: ));
    xlabel ('ʱ�䣨s��');
    ylabel ('Ƶ��(Hz)');
    title(['MF ͨ��' num2str(chnnum)]);
    axis([0 datalength/Fs -inf 1.01*fA_range]);  
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% ƽ������Ƶ�� MPF ͼ %%%%%
dat_mpf=[];
% rms_n=Fs*2;                                             %��������
step=1/4;                                               %�������ص���
long=floor(datalength/rms_n);                           %����������
fA_range=0;
for chnnum = 1:chnum
   for  j=1:(long-1)/step+1 
    n_start=(j-1)*rms_n*step+1;
    n_end=(j-1)*rms_n*step+rms_n;
    dat_mpf(chnnum,j)=getmpffeat(dat(chnnum,n_start:n_end)',Fs);
   end
    [m,index]=max(dat_mpf(chnnum,:));
    fA_range=max(fA_range,m);
end
for chnnum = 1:chnum
    subplot(2,chnum/2,chnnum);
    plot((1:(long-1)/step+1)*(rms_n*step/Fs),dat_mpf(chnnum,: ));
    xlabel ('ʱ�䣨s��');
    ylabel ('Ƶ��(Hz)');
    title(['MPF ͨ��' num2str(chnnum)]);
    axis([0 datalength/Fs -inf 1.01*fA_range]);  
end

                             
% dat_MF = dat_MF';
% dat_mpf = dat_mpf';
% dat_rms = dat_rms';
% time = time';                             
                             
