import os
import ffmpeg
import subprocess
from liat.service import ffmpeg_dir
from liat import speech
import re

# wav = speech.audio_to_text(r'D:\tts_wav\理想同学.wav')
# # wav = speech.audio_to_text(str(custom_data_path) + "\\" + pcm_name)
# wav_cmd = f"{ffmpeg_dir}\\ffmpeg.exe -f s16le -ar 24000 -ac 1 -i " + r'D:\tts\0c74049957dbba068d96651f7cec644a.pcm' + ' ' + r'D:\tts_wav\0c74049957dbba068d96651f7cec644a.wav'
# wav_cmd2 = (f"{ffmpeg_dir}\\ffmpeg.exe -i " + r'D:\tts_wav\0c74049957dbba068d96651f7cec644a.wav'
#             + " -ar 16000 -ac 1 -f mp3 " + r'D:\audio\tts_wav\out.mp3')
# os.system(wav_cmd)
# file_path = r'D:\audio\tts_wav'
# if not os.path.exists(r'D:\audio\tts_wav\out.mp3'):
#     os.system(wav_cmd2)
# else:
#     print(f'{file_path} already exists.')
# a_to_text = speech.audio_to_text(r'D:\audio\tts_wav\out.mp3')
# print(a_to_text)
# for key, values in a_to_text.items():
#     if key == 'data':
#         # print(values)
#         values = values.split('。')
#         print(values[0])
# # mp3_name = os.path.abspath(r'D:\tts_wav')
# print(mp3_name)
# """
# #获取生成的pcm文件路径
# #pcm文件转换成mp3格式
# #audio_to_text获取mp3的文件名
# #重命名mp3文件，通过上边获取到的文件名
# #把mp3格式文件转换成wav格式，
# """


##获取生成的pcm文件路径
def get_pcm_path(input_folder):
    pcm_path = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            f_path = os.path.join(root, file)
            pcm_path.append(f_path)
    return pcm_path
#
#
input_folder = r'D:\audio\tts_pcm'
mp3_folder = r'D:\audio\tts_mp3'
out_folder = r'D:\audio\tts_wav'
pcm_path = get_pcm_path(input_folder)
# # for i in os.listdir(mp3_folder):
# #     if i.endswith('.mp3'):
# #         print(i)
#
# # print(pcm_path)
# # wav_cmd2 = (f"{ffmpeg_dir}\\ffmpeg.exe -i " + input_file + " -ar 16000 -ac 1 -f mp3 " + mp3_file)
# # wav_cmd2 = f'{ffmpeg_dir}\\ffmpeg.exe -i' + r' D:\audio\tts_pcm\0c74049957dbba068d96651f7cec644a.pcm' + " -f s16le -ar 24000 -ac 1 " + r'D:\audio\tts_mp3\0c74049957dbba068d96651f7cec644a.wav'
# # wav_cmd = f"{ffmpeg_dir}\\ffmpeg.exe -f s16le -ar 24000 -ac 1 -i " + r'D:\audio\tts_pcm\0c74049957dbba068d96651f7cec644a.pcm' + ' ' + r'D:\audio\tts_mp3\0c74049957dbba068d96651f7cec644a.wav'
# # subprocess.run(wav_cmd)
#
#pcm文件转换成mp3格式
def pcm_2_mp3(input_folder, mp3_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.pcm'):
            input_file = os.path.join(input_folder, filename)
            mp3_file = os.path.join(mp3_folder, f'{os.path.splitext(filename)[0]}.mp3')
            # print(input_file, mp3_file)
            wav_cmd2 = (f"{ffmpeg_dir}\\ffmpeg.exe -f s16le -ar 24000 -ac 1 -i " + input_file
                        + " " + mp3_file)
            # os.system(wav_cmd2)
            if not os.path.exists(mp3_file):
                subprocess.run(wav_cmd2)
            else:
                print(f'{mp3_file} already exists.')
    return mp3_folder


pcm_2_mp3(input_folder, mp3_folder)


# print(pcm_2_mp3(input_folder,mp3_folder))
#
# # print(mp3_folder)

#audio_to_text获取mp3的文件名
def audio_2_text(mp3_folder):
    parts = []
    for mp3_file in os.listdir(mp3_folder):
        if mp3_file.endswith('.mp3'):
            mp3_path = os.path.join(mp3_folder,mp3_file)
            a_to_text = speech.audio_to_text(mp3_path)
            # print(type(a_to_text))
            for key, query_name in a_to_text.items():
                if key == 'data':
                    # print(values)
                    # 创建一个正则表达式，匹配任意一个分隔符
                    def split_multiple_delimiters(query_name,delimiters):
                        regex_pattern = '|'.join(map(re.escape, delimiters))
                        return [part.strip() for part in re.split(regex_pattern, query_name) if part.strip()]
                        # query_name = "这是第一句。这是第二句？这是第三句。"
                    delimiters = ['。', '？',' ']
                    parts = split_multiple_delimiters(query_name, delimiters)
                    # query_names = re.split(r'。？',query_name)
                    # print(parts)
                    # parts.append(part)
    return parts


audio_2_text(mp3_folder)
print(audio_2_text(mp3_folder))
#

def sanitize_filename(parts):
    """Sanitize the text to be a valid filename."""
    parts = parts.replace(' ', '_')
    parts = re.sub(r'[<>:"/\\|?*]', '', parts)  # Remove illegal characters
    return parts[:255]  # Limit to 255 characters for filenames

# #重命名mp3文件，通过上边获取到的文件名
def rename_mp3(mp3_folder, new_name):
    """Rename the MP3 file."""
    new_name = sanitize_filename(new_name)
    new_file = f"{new_name}.mp3"
    os.rename(mp3_folder, new_file)
    print(f"Renamed '{mp3_folder}' to '{new_file}'")