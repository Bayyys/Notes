clear;
close all;
%参数设置

for x=1:1
        clearvars -except ratio ratio_each x MF_each MF_each_low MF_each_high MF MF_low MF_high bound ;
        fs=8000;%采样率
        [name,fadd] = uigetfile('*.txt', 'Select an txt file'); %文件名称.后缀 ; 地址 
        rawDATA = load([fadd name],'%f');                          %读取数据文件
%         if x==1 
%             rawDATA = textread('0.txt','%f');%读取数据文件
%             name ='0.txt';
%         end
%         if x==2
%             rawDATA = textread('3.txt','%f');%读取数据文件
%                         name ='3.txt';
%         end  
%         if x==3 
%             rawDATA = textread('7.txt','%f');%读取数据文件
%                         name ='7.txt';
%         end
%         if x==4 
%             rawDATA = textread('4.txt','%f');%读取数据文件
%                         name ='4.txt';
%         end
%         if x==5
%             rawDATA = textread('1.txt','%f');%读取数据文件
%                         name ='1.txt';
%         end
        
        % rawDATA = textread('1-1-16Kch0-decode.txt','%f');%读取数据文件
        ALLDATA = rawDATA';
        dataN = length(ALLDATA);
        chn = 2;%数据中总共的通道数
        actchn = 1;%实际有用的数据通道数
        groupnum = dataN / chn;%一通道数据总共的数据量
        num = 0;%从最开始的数读起
        fnum = 200;%RMS的步长；
        filterdatafile = zeros(actchn,1);
        RMSdatafile = zeros(actchn,1);
        times=dataN/fs;                                    %FFT采样率参数
        N=fs*times;


        for group = 1:chn  %第n通道
            for i = 1:groupnum
            a(group, i) = ALLDATA(num*chn + group);
            num = num + 1;
            end
            if num == groupnum
                num = 0;
                group = group + 1;
            end
        end
% 
        a=a(:, 5 *fs+1 : end) ;%选取时间

        datalength = length(a);
        for chnnum = 1:actchn
            for i = 1:datalength
                singledata(chnnum,i) = a(chnnum,i);
            end
            Rawdata(chnnum,:) = singledata(chnnum,:)- mean(singledata(chnnum,:));  %基线移除
%             Rawdata(chnnum,:) = singledata(chnnum,:);    

        if chnnum == 1

        % 原始数据---------------------------------------------------------------
        figure(1);    
            dcm_obj = datacursormode(gcf);
            set(dcm_obj,'UpdateFcn',@NewCallback);
            
            subplot(1,1,chnnum);
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
%             [b2,b1]=butter(4,[46 50]/(fs/2),'stop');
%             data_filter=filter(b2,b1,data_filter);
%             [b2 b1]=butter(4,[48 52]/(fs/2),'stop');
%             data_filter=filter(b2,b1,data_filter);
%             [b2 b1]=butter(4,[50 54]/(fs/2),'stop');
%             data_filter=filter(b2,b1,data_filter);
%             [b2 b1]=butter(4,[98 102]/(fs/2),'stop');
%             data_filter=filter(b2,b1,data_filter);
%             [b2 b1]=butter(4,[148 152]/(fs/2),'stop');
%            data_filter=filter(b2,b1,data_filter);
%             [b2 b1]=butter(4,500*2/fs,'low');
%             data_filter=filter(b2,b1,data_filter);
            y_filter=fft(data_filter,N);
            abs_y_filter = abs(y_filter);
            Filterdata = data_filter;
% 
%             sum1 = 0;
%             sum2 = 1/N*sum(abs_y_filter);
%             peak = max(abs_y_filter);
%             for i = 1:N
%                 filterdatafile(chnnum,i) = abs_y_filter(1,i);
%             end
%             [L,M]=butter(4,1*2/fs,'high');
%             data_filter7=filter(L,M,data_filter);
%             y_filter=fft(data_filter7,N);
%             abs_y_filter = abs(y_filter);

        %     if name == '1-1-比目鱼.txt'
        %        Filterdata = -Filterdata;
        %     end
        %     Filterdata=Filterdata(1, 5 *fs+1: end);                        %除去前后干扰 默认： (1:chnum, 4 *Fs+1: end)
        %     datalength = length(Filterdata);

            % 滤波后信号图
        %     subplot(2,1,chnnum);
        figure(2); 
            dcm_obj = datacursormode(gcf);
            set(dcm_obj,'UpdateFcn',@NewCallback);
            
            subplot(1,1,chnnum);
            plot((0:(datalength-1))*(1/fs),Filterdata);
            set(gca,'Fontname','Monospaced');
            xlabel ('时间（s）');
            ylabel ('幅值(uV)');
            title(['滤波后信号通道' num2str(chnnum)]);
            axis([0 datalength/fs -inf inf]);
            hold on;
            
            
% figure(3);                   %%%%% 频谱图 %%%%%
% fA_range=0;
% for i=1
%     data_i=Rawdata;
%     y=abs(fft(data_i,datalength));
%     [m,index]=max(y);
%     fA_range=max(fA_range,m);                           %统一y轴坐标
% end
% for i=1
%     data_i=rawDATA;
%     y=abs(fft(data_i,datalength));
%     md=medfreq(data_i,fs);                              %整体中值频率
%     emg_mf(i,1)=md;
%     subplot(1,1,1);
%     plot((1:datalength/2)/times,y(1:datalength/2));
%     xlabel ('频率(Hz)');
%     ylabel ('幅值');
%     title(['肌电频谱 通道' num2str(i)  ' MF=' num2str(md)]);
%     axis([-inf inf -inf fA_range*1.1]);  
% end
        %     if chnnum == 1  ||   chnnum == 2             %%% 取待用通道进行计算
%             if name == '0.txt'       

%                 second_long = 1;  
%                 starttime=second_long*  53;%%%开始时间
%                 endtime  =second_long*  66;%%%结束时间
% 
%             %     pks_all=zeros(actchn,10);
%             %     locs_all=zeros(actchn,10);
%                 temp(x,:)=Filterdata(starttime*fs:endtime*fs);                
%                 mdwhole(chnnum,:)=medfreq(temp(chnnum,:),fs);   
%                 %找最高点
%                 [pks,locs]= findpeaks(temp(x,:),'minpeakheight',200,'minpeakdistance',50);   %若后面有更多的波需要改这个
%                 len=length(pks);
%                 peaks(x,1:len)=pks;
%                 locations(x,1:len)=locs;
%                 scatter((locations(x,1:len)-2)/fs+starttime,peaks(x,1:len));
%                 hold on;
%                %找最低点
%             for k = 1: len   
%                 dstart(x,k) = locations(x,k)+starttime*fs;
%                 dend(x,k) = dstart(x,k) + 0.006*fs;
%                 dtemp(k,:)=Filterdata(dstart(x,k):dend(x,k));
%                 [oppks,oplocs]= findpeaks(-dtemp(k,:),'minpeakheight',200,'minpeakdistance',70);
%                 oplen=length(oppks);
%                 oppeaks(x,1:oplen)=oppks;
%                 oplocations(x,1:oplen)=oplocs;
%                 scatter((oplocations(x,1:oplen)-2)/fs+dstart(x,k)/fs,-oppeaks(x,1:oplen));
%                 hold on;    
%             end 
%             end
            
%             if name == '3.txt'       
% 
%                 second_long = 1;  
%                 starttime=second_long*  10;%%%开始时间
%                 endtime  =second_long*  23.5;%%%结束时间
% 
%             %     pks_all=zeros(actchn,10);
%             %     locs_all=zeros(actchn,10);
%                 temp(x,:)=Filterdata(starttime*fs:endtime*fs);
%                                 mdwhole(chnnum,:)=medfreq(temp(chnnum,:),fs);   
%                 [pks,locs]= findpeaks(temp(x,:),'minpeakheight',1000,'minpeakdistance',50);   %若后面有更多的波需要改这个
%                 len=length(pks);
%                 peaks(x,1:len)=pks;
%                 locations(x,1:len)=locs;
%                 scatter((locations(x,1:len)-2)/fs+starttime,peaks(x,1:len));
%                 hold on;
% 
%             for k = 1: len   
%                 dstart(x,k) = locations(x,k)+starttime*fs;
%                 dend(x,k) = dstart(x,k) + 0.006*fs;
%                 dtemp(k,:)=Filterdata(dstart(x,k):dend(x,k));
%                 [oppks,oplocs]= findpeaks(-dtemp(k,:),'minpeakheight',1000,'minpeakdistance',50);
%                 oplen=length(oppks);
%                 oppeaks(x,1:oplen)=oppks;
%                 oplocations(x,1:oplen)=oplocs;
%                 scatter((oplocations(x,1:oplen)-2)/fs+dstart(x,k)/fs,-oppeaks(x,1:oplen));
%                 hold on;    
%             end 
%             end
%             if name == '7.txt'       
% 
%                 second_long = 1;  
%                 starttime=second_long*  10;%%%开始时间
%                 endtime  =second_long*  25;%%%结束时间
% 
%             %     pks_all=zeros(actchn,10);
%             %     locs_all=zeros(actchn,10);
%                 temp(x,:)=Filterdata(starttime*fs:endtime*fs);
%                                 mdwhole(chnnum,:)=medfreq(temp(chnnum,:),fs);   
%                 [pks,locs]= findpeaks(temp(x,:),'minpeakheight',2000,'minpeakdistance',50);   %若后面有更多的波需要改这个
%                 len=length(pks);
%                 peaks(x,1:len)=pks;
%                 locations(x,1:len)=locs;
%                 scatter((locations(x,1:len)-2)/fs+starttime,peaks(x,1:len));
%                 hold on;
% 
%             for k = 1: len   
%                 dstart(x,k) = locations(x,k)+starttime*fs;
%                 dend(x,k) = dstart(x,k) + 0.006*fs;
%                 dtemp(k,:)=Filterdata(dstart(x,k):dend(x,k));
%                 [oppks,oplocs]= findpeaks(-dtemp(k,:),'minpeakheight',2000,'minpeakdistance',50);
%                 oplen=length(oppks);
%                 oppeaks(x,1:oplen)=oppks;
%                 oplocations(x,1:oplen)=oplocs;
%                 scatter((oplocations(x,1:oplen)-2)/fs+dstart(x,k)/fs,-oppeaks(x,1:oplen));
%                 hold on;    
%             end 
%             end
        
%             if name == '4.txt'       
% 
%                 second_long = 1;  
%                 starttime=second_long*  11;%%%开始时间
%                 endtime  =second_long*  25;%%%结束时间
% 
%             %     pks_all=zeros(actchn,10);
%             %     locs_all=zeros(actchn,10);
%                 temp(x,:)=Filterdata(starttime*fs:endtime*fs);
%                 mdwhole(chnnum,:)=medfreq(temp(chnnum,:),fs);   
%                 [pks,locs]= findpeaks(temp(x,:),'minpeakheight',4000,'minpeakdistance',50);   %若后面有更多的波需要改这个
%                 len=length(pks);
%                 peaks(x,1:len)=pks;
%                 locations(x,1:len)=locs;
%                 scatter((locations(x,1:len)-2)/fs+starttime,peaks(x,1:len));
%                 hold on;
% 
%             for k = 1: len   
%                 dstart(x,k) = locations(x,k)+starttime*fs;
%                 dend(x,k) = dstart(x,k) + 0.006*fs;
%                 dtemp(k,:)=Filterdata(dstart(x,k):dend(x,k));
%                 [oppks,oplocs]= findpeaks(-dtemp(k,:),'minpeakheight',2000,'minpeakdistance',50);
%                 oplen=length(oppks);
%                 oppeaks(x,1:oplen)=oppks;
%                 oplocations(x,1:oplen)=oplocs;
%                 scatter((oplocations(x,1:oplen)-2)/fs+dstart(x,k)/fs,-oppeaks(x,1:oplen));
%                 hold on;    
%             end 
%             end
% 
%             if name == '1.txt'       
% 
%                 second_long = 1;  
%                 starttime=second_long*  15;%%%开始时间
%                 endtime  =second_long*  20;%%%结束时间
% 
%             %     pks_all=zeros(actchn,10);
%             %     locs_all=zeros(actchn,10);
%                 temp(x,:)=Filterdata(starttime*fs:endtime*fs);
%                 mdwhole(chnnum,:)=medfreq(temp(chnnum,:),fs);   
%                 [pks,locs]= findpeaks(temp(x,:),'minpeakheight',500,'minpeakdistance',50);   %若后面有更多的波需要改这个
%                 len=length(pks);
%                 peaks(x,1:len)=pks;
%                 locations(x,1:len)=locs;
%                 scatter((locations(x,1:len)-2)/fs+starttime,peaks(x,1:len));
%                 hold on;
% 
%             for k = 1: len   
%                 dstart(x,k) = locations(x,k)+starttime*fs;
%                 dend(x,k) = dstart(x,k) + 0.006*fs;
%                 dtemp(k,:)=Filterdata(dstart(x,k):dend(x,k));
%                 [oppks,oplocs]= findpeaks(-dtemp(k,:),'minpeakheight',500,'minpeakdistance',50);
%                 oplen=length(oppks);
%                 oppeaks(x,1:oplen)=oppks;
%                 oplocations(x,1:oplen)=oplocs;
%                 scatter((oplocations(x,1:oplen)-2)/fs+dstart(x,k)/fs,-oppeaks(x,1:oplen));
%                 hold on;    
%             end 
%             end
        %         峰后找零点
        %         for k = 1:len
        %             dstart(chnnum,k) = locations(chnnum,k)/fs+starttime;
        %             dend(chnnum,k) = dstart(chnnum,k) + 0.0011;
        %             dtemp(k,:)=Filterdata(dstart(chnnum,k)*fs:dend(chnnum,k)*fs);
        %             dlen(k,:) = length(dtemp(k,:));
        %         end
        %         for k = 1:len
        %             for i = 1:dlen(k,:)-1
        %                if dtemp(k,i)*dtemp(k,i+1)<0
        %                   ddd = i;
        %                end
        %             end
        % %             scatter(ddd/fs+dstart(chnnum,k),dtemp(k,i),[],'b');                
        %         end


                %峰后找10ms内的max峰作为肌电峰值        
        %         for k = 1:len
        %             myostart(chnnum,k) = locations(chnnum,k)/fs+starttime+0;
        %             myoend(chnnum,k) = myostart(chnnum,k) + 0.05;
        %             myotemp(k,:)=Filterdata(myostart(chnnum,k)*fs:myoend(chnnum,k)*fs);
        %             ave_elecpeak = mean(peaks(chnnum,:));
        %         end
        %         for k = 1:len
        %             [myopks,myolocs]= findpeaks(myotemp(k,:),'minpeakdistance',0);
        %             lengthofpks = length(myopks);
        %             if myopks(1)>60 
        %                 myopks(1)=[];
        %                 myolocs(1)=[];
        %             end        
        %             if myopks(1)<20
        %                 myopks(1)=[];
        %                 myolocs(1)=[];
        %             end   
        %             End_of_electrical_pks(chnnum,k) = myopks(1);
        %             End_of_electrical_locs(chnnum,k)= myolocs(1);
        % 
        %             myopeaks(chnnum,k) = max(myopks(:));
        %             M1 = find(myopks()==myopeaks(chnnum,k));
        %             myolocations(chnnum,k) = myolocs(M1);
        %             
        %             End_of_electrical_pks(chnnum,k) = myopks(M1-1);
        %             End_of_electrical_locs(chnnum,k)= myolocs(M1-1);
        %             
        %             scatter((End_of_electrical_locs(chnnum,k))/fs+myostart(chnnum,k),End_of_electrical_pks(chnnum,k),[],'r');
        % 
        %             scatter(((myolocations(chnnum,k))-2)/fs+myostart(chnnum,k),myopeaks(chnnum,k),[],'b');    
        %         end  

                %统计大于0的肌电峰值与潜伏期

%                 total_delay_time = zeros(actchn,1);
%                 total_amp = zeros(actchn,1);
%                 count = 0;
%                 for k = 1:len
%                     if  peaks(x,k) > 0 
%         %                 delay_time_each(chnnum,k)=(locations(chnnum,2*k)-locations(chnnum,2*k-1));
%                         amp_each(x,k) = peaks(x,k);
%         %                 delay_time_each(chnnum,k)=(myolocations(chnnum,k));    
%         % %                 if  delay_time_each(chnnum,k)>20 && delay_time_each(chnnum,k)<80
%         %                 if  delay_time_each(chnnum,k)< 1000          
%         %                 total_delay_time(chnnum,1) = total_delay_time(chnnum,1) + (delay_time_each(chnnum,k));
%                         total_amp(x,1) = total_amp(x,1)+ (peaks(x,k));
%         %                     delay_time_each1(chnnum,k) =  delay_time_each(chnnum,k);
%         %                     myopeaks1(chnnum,k) = myopeaks(chnnum,k);
%                         count =count+1;
%         %                 end
%                     end
%                 end
%         %         delay_time_each2 =  nonzeros(delay_time_each1)/fs*1000;
%         %         myopeaks2 = nonzeros(myopeaks1);
%         %         std_delay_time = std(delay_time_each,1);
%                 std_amp = std(amp_each(x,:),1);
%         %         delay_time(chnnum,1) =  (total_delay_time(chnnum,1)/count)/fs*1000;
%                 amp(x,1) =  total_amp(x,1)/count;

        %      end



            %肌电峰前后一个完整的波形作为肌电响应算持续时间+面积+做频谱分析 
%             for k = 1:len             %找零点1
%                 count = 1;
%                 zerostart(x,k) = (locations(x,k)-100)+starttime*fs;
%                 zeroend(x,k) = locations(x,k)+starttime*fs;
%                 zerotemp(k,:)=Filterdata(zerostart(x,k):zeroend(x,k));  
%                 zerolength(k,:)=length(zerotemp(k,:));
%                 for i = 1 : zerolength(k,:)-10
%                    if (zerotemp(k,i) * zerotemp(k,i+1)<0) || (zerotemp(k,i) >= zerotemp(k,i+1))
%                        zeroset(k,count)= find(zerotemp(k,:)==zerotemp(k,i+1));
%                    end
%                 end        
%                 scatter((zerostart(x,k)+zeroset(k,count)-2)/fs,zerotemp(k,zeroset(k,1)));
%                 hold on;
%             end
% 
%                 for k = 1:len       %找零点2
%                     count = 1;
%                     zerostart2(x,k) = (oplocations(x,1)-2)+dstart(x,k);
%                     zeroend2(x,k) = zerostart2(x,k)+300;
%                     zerotemp2(k,:)=Filterdata(zerostart2(x,k):zeroend2(x,k));  
%                     zerolength2(k,:)=length(zerotemp2(k,:));
%                     for i = 1 : zerolength2(k,:)-1
%                          if (zerotemp2(k,i) >= 0)
% %                        if (zerotemp2(k,i) >= 0) || (zerotemp2(k,i) * zerotemp2(k,i+1)<0)
%             %            if  (zerotemp2(k,i) * zerotemp2(k,i+1)<0)             
%                            zeroset2(k,count)= find(zerotemp2(k,:)==zerotemp2(k,i));
%                            count = count+1;
%                        end
%                     end
%                     scatter((zerostart2(x,k)+zeroset2(k,1)-2)/fs,zerotemp2(k,zeroset2(k,1)));
%                     hold on;
%                 end   
% 
%             for k = 1:len
%                 durationeach(1,k) =  1000*((zerostart2(x,k)+(zeroset2(k,1)-2))/fs-(zerostart(x,k)+(zeroset(k,1)-2))/fs);
%                 areaeach(1,k) = sum(abs(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2)))))/fs;
%             end   
%             area = sum(areaeach)/length(areaeach);
%             std_area = std(areaeach,1);       %标准差
%             duration = sum(durationeach)/length(durationeach);
%             std_duration = std(durationeach,1);   
% 
% 
%             %频谱图        
%         figure(3); 
%             subplot(2,1,chnnum);
%             for bound = 150:150
%                     for k = 1:len
%                 %         subplot(len,1,k);
%                         clearvars fil;
%                         fil(1,:)=(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))));
%                         N=length(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))));
% %                         N=length(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart(x,k+1)+(zeroset(k+1,1)-2))));
%                         times=N*N/fs;
% 
%                 %         y=abs(fft(Filterdata((zerostart(chnnum,k)+(zeroset(k,1)-2)):(zerostart2(chnnum,k)+(zeroset2(k,1)-2))),N));
%                 %         plot((0:N/2-1)/times,y(1:N/2));
%                         y=abs(fft(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))),N*N));
% %                         y=abs(fft(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart(x,k+1)+(zeroset(k+1,1)-2))),N*N));
% %                         [pxx1(k,:),f1(k,:)]=pwelch(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))),hamming(N-1),20,N-1,'onesided',N-1);
% %                         plot(f1(k,:)/(2*pi)*N,10*log10(pxx1(k,:)));
% %                         axis([0 250 -inf inf]); 
% %                         clearvars pxx1  f1;
%                         
%                         plot((0:(N+1)*N/2-1)/times,y(1:(N+1)*N/2));
%                         axis([0 1000 -inf inf]); 
% %                         ymax(x,k)=max(y(1:N*N/2));
% %                         PF=find(y==ymax(x,k))/times;
% %                         PF_each(x,k)=PF(1);
% % 
% %                         [b2 b1]=butter(4,1*2/fs,'high');
% %                         data_filter=filter(b2,b1,Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))));
% %                         [b2 b1]=butter(4,200*2/fs,'low');
% %                         data_filter=filter(b2,b1,data_filter);
% %                         y1=abs(fft(data_filter,N*N));
% % 
% %                         [b2 b1]=butter(4,200*2/fs,'high');
% %                         data_filter2=filter(b2,b1,Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))));
% %                         [b2 b1]=butter(4,500*2/fs,'low');
% %                         data_filter2=filter(b2,b1,data_filter2);
% %                         y2=abs(fft(data_filter2,N*N));
% % 
% %                         [b2 b1]=butter(4,20*2/fs,'high');
% %                         data_filter=filter(b2,b1,Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))));
% %                         [b2 b1]=butter(4,500*2/fs,'low');
% %                         data_filter=filter(b2,b1,data_filter);
% %                         y=abs(fft(data_filter,N*N));       
% % 
% %                         plot((0:N*N/2-1)/times,y1(1:N*N/2));
% %                         ymax1=max(y1(1:N*N/2));
% %                         PF1=find(y1==ymax1)/times;
% %                         PF_each(chnnum,k)=PF1(1);
% % 
% %                         plot((0:N*N/2-1)/times,y2(1:N*N/2));
% %                         ymax2=max(y2(1:N*N/2));
% %                         PF2=find(y2==ymax2)/times;
% %                         PF_each(chnnum,k)=PF2(1);
% % 
% % %                         y=abs(fft(Filterdata((zerostart(chnnum,k)+(zeroset(k,1)-2)):(zerostart2(chnnum,k)+(zeroset2(k,1)-2))),N*N));
% % %                         plot((0:N*N/2-1)/times,y(1:N*N/2));
% % %                         ymax=max(y(1:N*N/2));
% % %                         PF=find(y==ymax)/times;
% % %                         PF_each(chnnum,k)=PF(1);
% % 
% %                         MF_each(x,k)=medfreq(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))),fs,[20 500]);                              %整体中值频率
% %                         MF_each_low(x,k)=medfreq(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))),fs,[20 bound]);                             
% %                         MF_each_high(x,k)=medfreq(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))),fs,[bound 500]);       
% %                         MPF_each(chnnum,k)=getmpffeat((Filterdata((zerostart(chnnum,k)+(zeroset(k,1)-2)):(zerostart2(chnnum,k)+(zeroset2(k,1)-2))))',fs); 
% % 
% %                         
% % %                         ratiop(1:5,1) = [0.81439 0.69948 0.59266 0.57186 0.55913];
% % %                         ratiop(1:5,2) = [0.18561 0.30052 0.40734 0.42814 0.44087];
% %                         
% %                         ratio_each(x,k) = MF_each_low(x,k);
% % 
% %                         Freq_area_low_each(chnnum,k)=sum((1:1/times:PF_each(chnnum,k)).*y((1*times+1):( PF_each(chnnum,k)*times+1)))/sum(y((1*times+1):( PF_each(chnnum,k)*times+1)));
% %                         Freq_area_high_each(chnnum,k)=sum((PF_each(chnnum,k):1/times:500).*y(( PF_each(chnnum,k)*times+1):(500*times+1)))/sum(y(( PF_each(chnnum,k)*times+1):(500*times+1)));        
% % 
% %                         FFR_each(chnnum,k)= Freq_area_low_each(chnnum,k)/(Freq_area_low_each(chnnum,k)+Freq_area_high_each(chnnum,k));
% % 
% %                         twenty(x,k)=sum(y(round((20*times+1)):round(( bound*times+1))));
% %                         twen(x,k)=sum(y(round(( bound*times+1)):round((500*times+1))));
% % 
% % %                         ratio_each(x,k)= twenty(x,k)*+twen(x,k)*;
% %                 %         FFR_each(chnnum,k)= sum(y(( PF_each(1,k)*times+1):(500*times+1)))/(sum(y(( PF_each(1,k)*times+1):(500*times+1)))+sum(y((1*times+1):( PF_each(1,k)*times+1))));
% % 
%                         xlabel ('频率(Hz)');
%                         ylabel ('幅值');
%                         title(['FFT 通道' num2str(1)]);
%                         axis([0 1000 -inf inf]);  
%                         hold on;
%                     end
% %                     Freq_area_low(chnnum,:)=sum(Freq_area_low_each(chnnum,:))/length(Freq_area_low_each(chnnum,:));
% %                     std_low(chnnum,:)=std(Freq_area_low_each(chnnum,:),1);
% %                     Freq_area_high(chnnum,:)=sum(Freq_area_high_each(chnnum,:))/length(Freq_area_high_each(chnnum,:));
% %                     std_high(chnnum,:)=std(Freq_area_high_each(chnnum,:),1);
% %                     FFR(chnnum,:)=sum(FFR_each(chnnum,:))/length(FFR_each(chnnum,:));
% %                     std_FFR(chnnum,:)=std(FFR_each(chnnum,:),1);
% %                     FFR2(chnnum,:)=sum(FFR_each2(chnnum,:))/length(FFR_each2(chnnum,:));
% %                     std_FFR2=std(FFR_each2(chnnum,:),1);
% 
% %                     ratio(x,bound) = sum(ratio_each(x,1:10))/length(ratio_each(x,1:10));
% %                     std_ratio(x,bound)=std(ratio_each(x,1:10),1);
% %                                         
% %                     low(x,1)=sum(twenty(chnnum,:))/length(twenty(chnnum,:));
% %                     std_lower(x,1)=std(twenty(chnnum,:),1);
% %                     high(x,1)=sum(twen(chnnum,:))/length(twen(chnnum,:));
% %                     std_higher(x,1)=std(twen(chnnum,:),1);    
% %                     summary = [low(x,1) std_lower(x,1) high(x,1) std_higher(x,1)];
% %                     
% %                     
% %                     PeakFreq(x,:) = sum(PF_each(x,:))/length(PF_each(x,:));
% %                     std_PeakFreq(x,:)= std(PF_each(x,:) ,1);
% %                     MF(x,:) = sum(MF_each(x,5:9))/length(MF_each(x,5:9));
% %                     std_MF (x,:)= std(MF_each(x,5:9),1);
% %                     MFF=[MF_each(x,3),MF_each(x,7),MF_each(x,9),MF_each(x,6),MF_each(x,8)];
% %                     MF(x,:) = mean(MFF);
% %                     std_MF (x,:)=  std(MFF,1);
% %                     
% %                     MF_low(x,:) = sum(MF_each_low(x,1:5))/length(MF_each_low(x,1:5));
% %                     std_MF_low (x,:)= std(MF_each_low(x,1:5),1);
% %                     MF_high(x,:) = sum(MF_each_high(x,1:5))/length(MF_each_high(x,1:5));
% %                     std_MF_high(x,:)= std(MF_each_high(x,1:5),1);
% %                     MPF (chnnum,:)= sum(MPF_each(chnnum,:))/length(MPF_each(chnnum,:));
% %                     std_MPF (chnnum,:)= std(MPF_each(chnnum,:),1);
%                     
% %                     scatter(bound,ratio(x,bound));           
%             end
% 
%             %两点波峰阈值检测算法滤除刺激信号
%         % figure;
%         %     for k = 1:len
%         %         
%         %         elecstart(chnnum,k) = (locations(chnnum,k)-10)+starttime*fs;
%         %         elecend(chnnum,k) = zerostart(chnnum,k)*fs+(zeroset(k,1)-1);
%         % %         electemp(k,:)=Filterdata(elecstart(chnnum,k)*fs:elecend(chnnum,k)*fs);  
%         % %         eleclength(k,:)=length(electemp(k,:));
%         % %         Filterdata(elecstart(chnnum,k):elecstart(chnnum,k)+1) = [500 -500];
%         %         Filterdata(elecstart(chnnum,k):elecend(chnnum,k))=random('Normal',0,2,1,round(elecend(chnnum,k)-elecstart(chnnum,k)));
%         %         xlswrite('single wave',Filterdata(elecstart(chnnum,k)-0.004*fs:elecstart(chnnum,k)+0.008*fs),'sheet1',[char('A'),num2str(k)]);
%         %     end
%         %     plot((0:(datalength-1))*(1/fs),Filterdata);
% 
%         end      
% 
%             dlength = length(Filterdata);
%             for i = 1:dlength
%                 RMSdatafile(chnnum,i) = Filterdata(i);
%             end
% 
% %             stat(1,:)=[amp(chnnum,1) duration area MF(chnnum,1)  MF_low(chnnum,1) MF_high(chnnum,1) ratio(chnnum,1) MPF(chnnum,1) Freq_area_low(chnnum,1) Freq_area_high(chnnum,1) PeakFreq(chnnum,1) ];
% %             stat(2,:)=[std_amp std_duration std_area std_MF(chnnum,1)  std_MF_low(chnnum,1) std_MF_high(chnnum,1) std_ratio(chnnum,1) std_MPF(chnnum,1) std_low(chnnum,1) std_high(chnnum,1) std_PeakFreq(chnnum,1) ];
% 
%         end 
% %             [pxx1(x,:),f1(x,:)]=pwelch(Filterdata((zerostart(x,k)+(zeroset(k,1)-2)):(zerostart2(x,k)+(zeroset2(k,1)-2))),hamming(N-1),20,N+128,'onesided',N);
% %             plot(f1(x,:)/(2*pi)*N,10*log10(pxx1(x,:)));
% %             axis([0 250 -inf inf]); 
% %             clearvars pxx1  f1;
% 
%         end
% 
% 
% 
% 
%         % A = zeros(2,10);
%         % A(1,:) = [amp duration area MF MPF Freq_area_low Freq_area_high low high FFR];
%         % A(2,:) = [std_amp std_duration std_area std_MF std_MPF std_low std_high std_lower std_higher std_FFR];
%         % xlswrite('name.xls',A);
% 
%         % 四阶巴特沃斯滤波器（10Hz高通）（50Hz，100Hz限波）滤波，第二幅图像——第一次滤波后图像
%         % figure;
%         % 
%         %      Smoothdata=(smooth(Filterdata,30,'sgolay',3))';			%利用sgolay方法
%         %     plot((0:(datalength-1))*(1/fs),Smoothdata);
%         %     xlabel ('时间（s）');
%         %     ylabel ('幅值(uV)');
%         %     title(['平滑处理后信号通道' num2str(j)]);
%         %     subplot(4,actchn/4,1i);
%         %     axis([0 datalength/fs -100 100]);
% 
%         %smooth函数，第四幅图像——平滑后图像----------------------------------------
% 
%         %       Jdata = Smoothdata;
%         %       Adata = Smoothdata - Smoothdata;
%         %       Qdata=smooth(Jdata,30,'sgolay',3);			%利用sgolay方法
%         %       Cdata = Qdata;
%         %       Ddata = Qdata - Qdata;
%         %       jnum = 20;
%         %          for i = jnum + 1:datalength-jnum
%         %              for j = 1:jnum * 2
%         %                  Ddata(i) = Ddata(i)+(Cdata(i-j+jnum).^2);
%         %              end
%         %              RMSdata(i) = sqrt(Ddata(i)/jnum/2);
%         %          end
%         %         RMSlength = length(RMSdata);    
% 
% 
% 
% 
%         % figure;
%         % for i = 1:actchn
%         %         subplot(2,1,chnnum);
%         %         plot((1:N/2)/4,filterdatafile(i,1:N/2));
%         %         xlabel ('频率(Hz)');
%         %         ylabel ('幅值');
%         %         title(['肌电幅频信号通道' num2str(i)]);
%         %         axis([0 500 -inf inf]);
%         %         set(gca,'Fontname','Monospaced');
% % end
% 
% % xlswrite('A.xlsx',ratio);
% %         cir=[1.000000003	0.969737778	1.027068727	0.972627136	1.028133228 0.943012171	0.90195287	0.982246614	0.9049943	0.988633616 0.894039335	0.871228612	0.915633485	0.867274753	0.912287913 0.82968191	0.802765257	0.855838205	0.802309043	0.860096207 0.787991579	0.760618712	0.816581018	0.759097997	0.818405876 1	0.976718714	1.028384034	0.971297045	1.02950026 0.983923138	0.96399053	1.005928737	0.952349887	1.013423398 0.96402366	0.93643693	0.994799607	0.916185401	1.011861919 0.954306456	0.925284579	0.974239064	0.925603501	0.986198629 0.922890523	0.896101098	0.950477252	0.892592959	0.954782695]; 
% % 
% %         for i =1:5    
% %             total(1,5*(i-1)+1:5*(i-1)+5) = MF_each_low(i,5:9)/MF_each_low(1,5);
% %         end
% % 
% %         for i =1:5    
% %             total(1,5*(i+4)+1:5*(i+4)+5) = MF_each_high(i,5:9)/MF_each_high(1,5);
% %         end
% %         
% %         figure(4);
% %         r1=corr(cir',total');
% %         r(count2,:)=r1(1,2);
% %         scatter(count2,r(count2,:));
% %         hold on;

        end
        end
end





