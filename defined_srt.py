class SubtitleItem:
    def __init__(self, timeMinute: int, timeSecond: float, text: str):
        """
        定义字幕项的数据结构
        :param timeMinute: 分钟数（整数，如0表示0分）
        :param timeSecond: 秒数（可含小数，如2.35表示2秒350毫秒）
        :param text: 字幕文本内容
        """
        self.timeMinute = timeMinute  # 分钟数
        self.timeSecond = timeSecond  # 秒数（支持小数）
        self.text = text              # 字幕文本

    def __repr__(self) -> str:
        """方便调试的字符串表示"""
        return f"SubtitleItem(timeMinute={self.timeMinute}, timeSecond={self.timeSecond}, text='{self.text}')"


def generate_srt(subtitles: list[SubtitleItem]) -> str:
    """
    将字幕对象数组转换为SRT格式字符串
    :param subtitles: SubtitleItem实例列表
    :return: SRT格式的字幕字符串
    """
    if not subtitles:
        return ''
    
    srt_content = []
    
    for index, item in enumerate(subtitles):
        # 计算当前字幕的开始时间（总秒数）
        start_total = item.timeMinute * 60 + item.timeSecond
        
        # 计算结束时间：下一条的开始时间（最后一条默认持续2秒）
        if index < len(subtitles) - 1:
            next_item = subtitles[index + 1]
            end_total = next_item.timeMinute * 60 + next_item.timeSecond
        else:
            end_total = start_total + 2

        def format_time(total: float) -> str:
            """将总秒数转换为SRT要求的HH:MM:SS,mmm格式"""
            hours, remainder = divmod(total, 3600)
            minutes, remainder = divmod(remainder, 60)
            seconds = int(remainder)
            milliseconds = int(round((remainder - seconds) * 1000))
            return (
                f"{int(hours):02d}:{int(minutes):02d}:{seconds:02d},"
                f"{milliseconds:03d}"
            )

        # 拼接SRT块
        srt_content.append(
            f"{index + 1}\n"
            f"{format_time(start_total)} --> {format_time(end_total)}\n"
            f"{item.text}\n"
        )
    
    # 合并并移除末尾多余空行
    return '\n'.join(srt_content).rstrip() + '\n'


def write_srt_to_file(file_path: str, subtitles: list[SubtitleItem]) -> None:
    """
    将字幕对象数组写入SRT文件
    :param file_path: 目标文件路径（如"./subtitles.srt"）
    :param subtitles: SubtitleItem实例列表
    """
    try:
        srt_content = generate_srt(subtitles)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        print(f"SRT文件已成功写入：{file_path}")
    except Exception as e:
        print(f"写入文件失败: {str(e)}")
        raise  # 向上抛出异常以便调用方处理



    