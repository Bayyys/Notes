clear;
close all;
%%  set information
fs=8000;    % samplerate //  采样率
chn = 2;    % chn number //  通道数

%%  read data
%filename = "F:\EEG32\组会\2020.8.24\7T_Plexon电极测试\330-280-220-160-79-30processed_2020-08-22[15-55-36]-ch4-sample1000\330-280-220-160-79-30processed_2020-08-22[15-55-36]-ch4-sample1000.txt";
% [name,fadd] = uigetfile('*.txt', 'Select an txt file'); 
% 
% [name,fadd] = uigetfile('*.txt', 'Select an txt file'); %文件名称.后缀 ; 地址 
% rawdata = load([fadd name],'%f%f');




filename = uigetfile('*.txt', 'Select an txt file')
fid = fopen(filename);
rawdata = textscan(fid,'%f%f');

% for i = 1:4
%     rawdata{i} = rawdata{i};
% end

%%   *************************************  Data Analyze  ******************************************    %%
%%   DC filter
channel = 1;
data_DC = doFilter_DC(rawdata{channel});
data_50Hz= doFilter_50Hz(data_DC);
scan_pedot(1,:)=data_50Hz;


%% synchronization begin=15.462  32 volumes
% pp_synchronization = zeros(N,1);
% for i= 0:31
%     for j =0:24
%         for k = 0:1
%             pp_synchronization(15.462*1000+i*1000*3+j*0.1*1000+k) = 20000;
%         end
%     end
% end

%% IAR Time&FFT domain
figure(1)
N = length(scan_pedot(1,:));    
plot((0:(N-1))*(1/fs),data_50Hz);xlabel ('time/s');ylabel ('Amplitude(uV)');title(['Time-domain of raw signal collected by Pedot-Pss electrodes']);hold on;
mark_revise(1,:) = zeros(1,N);
%for i=7.415e4:1:N
%    if(scan_pedot(1,i)-scan_pedot(1,i-1)>500 && scan_pedot(1,i-1)<500)
%        mark_revise(1,i)=500;
%    end
%end

%j_post = 7.415e4
%j_pre = 0
%for i=7.415e4+1:1:N
 %   if(mark_revise(1,i))
  %      j_pre = j_post
   %     j_post = i
    %    j_int = j_post-j_pre
     %   if(j_int<100)
      %      mark_revise(1,j_post) = 0;
       % end
    %end
%end

for i=1:32 
    for j=1:31
       if(j-1<25)
       mark_revise(1,1.06184e5+(j-1)*10+(i-1)*300) = 1000;
       end
    end
end   

%pp_synchronization = mark_revise;
% plot( mark_revise(1,:));

figure(2);
y_f_sta = fft(data_50Hz,N);
y_f_sta = abs(y_f_sta);
y_f_sta = y_f_sta/(N);
x_f_sta =([1:N]-1)*fs/N;
plot(x_f_sta(1:N/2),y_f_sta(1:N/2),'blue');xlabel('Hz');ylabel('uV');title(['Frequency-domain of raw signal collected by Pedot-Pss electrodes']);grid on;


%EEGdata = zeros(1,N);
%EEGdata(1,1:N) = data_50Hz;
%EEGdata(2,1:N) = pp_synchronization;


% figure;
% subplot(3,1,1);
% plot((0:(N-1))*(1/fs),pp_synchronization_slice);xlabel ('时间/s');ylabel ('标记Mark');title(['手动添加slice同步信号']);hold on;
% subplot(3,1,2);
% plot((0:(N-1))*(1/fs),pp_synchronization_volume,'r');xlabel ('时间/s');ylabel ('标记Mark');title(['手动添加slice同步信号']);hold on;
% subplot(3,1,3);
% plot((0:(N-1))*(1/fs),markdata,'m');xlabel ('时间/s');ylabel ('标记Mark');title(['同步光纤采集模块采集volume同步信号']);hold on;
