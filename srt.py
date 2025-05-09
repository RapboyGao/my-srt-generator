time = 4

def generate_srt(filename, duration_minutes=time):
    with open(filename, 'w', encoding='utf-8') as f:
        total_seconds = duration_minutes * 60
        
        for i in range(total_seconds):
            # 计算开始和结束时间（HH:MM:SS,mmm）
            start_h = i // 3600
            start_m = (i % 3600) // 60
            start_s = i % 60
            
            end_i = i + 1
            end_h = end_i // 3600
            end_m = (end_i % 3600) // 60
            end_s = end_i % 60
            
            # 格式化时间显示（MM:SS）
            display_time = f"{start_m:02d}:{start_s:02d}"
            
            # 写入SRT条目
            f.write(f"{i+1}\n")
            f.write(f"{start_h:02d}:{start_m:02d}:{start_s:02d},000 --> {end_h:02d}:{end_m:02d}:{end_s:02d},000\n")
            f.write(f"{display_time}\n\n")

# 生成25分钟的字幕文件
generate_srt(f"{time}min_timer.srt")