clear;
close all;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%读取数据
[name,fadd] = uigetfile('*.txt', 'Select an txt file'); %文件名称.后缀 ; 地址  
data = load(name,'%f');                                 %读取数据文件

% name='li_2.5kg_fali1_p';
% name=[name '.txt'];
% data = load(name,'%f');%读取数据文件
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%输入参数
Fs=8000;                                                %采样率
datalength=size(data,2);                                %数据长度
plot((0:(datalength-1))*(1/Fs),data(1,:));              %绘制第一通道肌电图做参考
xlabel ('时间（s）');    
ylabel ('幅值(uV)');
% dataend = 15;
% datastart = 5;
% dat=data(:,(datastart)*Fs+1:(dataend)*Fs);
dat=data;                                               %数据长度节选

chnum=2;                                                %通道数节选
[chnum,datalength]=size(dat);
times=datalength/Fs;                                    %FFT采样率参数
N=Fs*times;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% 肌电信号幅值图 %%%%%
[m,~]=max(dat');
[m,index]=max(m);
range=1.1*m;                                            %统一y轴坐标
for chnnum = 1:chnum
    rmsd=rms(dat(chnnum,: ));                           %整体RMS值
    subplot(2,chnum/2,chnnum);
    plot((0:(datalength-1))*(1/Fs),dat(chnnum,: ));
    xlabel ('时间（s）');
    ylabel ('幅值(uV)');
    title(['肌电信号 通道' num2str(chnnum) ' RMS=' num2str(rmsd)]);
    axis([0 datalength/Fs -range range]);  
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% 均方根 RMS 图 %%%%%
dat_rms=[];
rms_n=Fs*0.5;                                             %采样窗长
step=1/4;                                               %采样窗重叠比
long=floor(datalength/rms_n);                           %采样窗个数
for chnnum = 1:chnum
   for j=1:(long-1)/step+1     % (L-N)/S+1
    n_start=(j-1)*rms_n*step+1;
    n_end=(j-1)*rms_n*step+rms_n;
    dat_rms(chnnum,j)=rms(dat(chnnum,n_start:n_end));
   end
    subplot(2,chnum/2,chnnum);
    plot((1:(long-1)/step+1)*(rms_n*step/Fs),dat_rms(chnnum,: ));
    xlabel ('时间（s）');
    ylabel ('幅值(uV)');
    title(['RMS 通道' num2str(chnnum)]);
    axis([0 datalength/Fs -inf inf]);  
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(3);                     %%%%% 频谱图 %%%%%
fA_range=0;
for i=1:chnum
    data_i=dat(i,:);
    y=abs(fft(data_i,N));
    [m,index]=max(y);
    fA_range=max(fA_range,m);                           %统一y轴坐标
end
for i=1:chnum
    data_i=dat(i,:);
    y=abs(fft(data_i,N));
    md=medfreq(data_i,Fs);                              %整体中值频率
    emg_mf(i,1)=md;
    subplot(2,chnum/2,i);
    plot((1:N/2)/times,y(1:N/2));
    xlabel ('频率(Hz)');
    ylabel ('幅值');
    title(['肌电频谱 通道' num2str(i)  ' MF=' num2str(md)]);
    axis([-inf inf -inf fA_range*1.1]);  
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% 中值频率 MF 图 %%%%%
dat_MF=[];
% rms_n=Fs*2;                                             %采样窗长
step=1/4;                                               %采样窗重叠比
long=floor(datalength/rms_n);                           %采样窗个数
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
    xlabel ('时间（s）');
    ylabel ('频率(Hz)');
    title(['MF 通道' num2str(chnnum)]);
    axis([0 datalength/Fs -inf 1.01*fA_range]);  
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;                     %%%%% 平均功率频率 MPF 图 %%%%%
dat_mpf=[];
% rms_n=Fs*2;                                             %采样窗长
step=1/4;                                               %采样窗重叠比
long=floor(datalength/rms_n);                           %采样窗个数
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
    xlabel ('时间（s）');
    ylabel ('频率(Hz)');
    title(['MPF 通道' num2str(chnnum)]);
    axis([0 datalength/Fs -inf 1.01*fA_range]);  
end

                             
% dat_MF = dat_MF';
% dat_mpf = dat_mpf';
% dat_rms = dat_rms';
% time = time';                             
                             
