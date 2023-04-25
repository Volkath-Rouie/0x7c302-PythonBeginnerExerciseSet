1




































""" # 导入所需的模块
import av
import vulkan
import numpy as np
import os

os.chdir('D:\\Proccess\\TempArea\\')
AUDIO_FILE = "牛佳钰 - 先别说话.flac" # 音频文件名
VIDEO_FILE = "video.mp4" # 视频文件名



# 定义一些常量
WIDTH = 3840 # 视频宽度
HEIGHT = 2160 # 视频高度
FPS = 1 # 视频帧数
BITRATE = 42 * 1024 * 1024 # 视频码率


# 创建一个Vulkan实例和设备
instance = vulkan.VkImageCopy
device = instance.physical_devices[0].create_device()

# 创建一个Vulkan渲染器，用于绘制动效
renderer = vulkan.Renderer(device)

# 打开音频文件，并获取其时长和采样率
audio_input = av.open(AUDIO_FILE)
audio_stream = audio_input.streams.audio[0]
duration = audio_stream.duration / av.time_base # 音频时长（秒）
sample_rate = audio_stream.rate # 音频采样率（赫兹）

# 创建一个音频处理器，用于计算音频的傅里叶变换（FFT）
audio_processor = av.AudioProcessor(sample_rate)

# 创建一个视频输出，并设置其参数和编码器
video_output = av.open(VIDEO_FILE, mode="w")
video_stream = video_output.add_stream("h264_qsv", rate=FPS)
video_stream.width = WIDTH
video_stream.height = HEIGHT
video_stream.bit_rate= BITRATE

# 循环遍历每一帧音频数据，并计算其FFT和动效，并写入视频输出中
for frame in audio_input.decode(audio_stream):
    # 将音频数据转换为numpy数组，并计算其FFT（只取前半部分）
    data = frame.to_ndarray()
    fft_data = np.fft.fft(data)[:len(data)//2]

    # 根据FFT数据的幅度和相位来绘制动效（这里只是一个简单的例子，可以自定义更复杂的动效）
    renderer.clear() # 清空画布
    renderer.set_color(1.0, 1.0, 1.0) # 设置画笔颜色为白色
    
    for i in range(len(fft_data)):
        # 计算每个FFT数据对应的幅度和相位（归一化到[0,1]区间）
        amplitude = np.abs(fft_data[i]) / len(data)
        phase = np.angle(fft_data[i]) / (2 * np.pi)

        # 计算每个FFT数据对应的圆心坐标和半径（根据幅度和相位来映射到画布上）
        x_center = int(phase * WIDTH)
        y_center= int((i / len(fft_data)) * HEIGHT)
        radius= int(amplitude * min(WIDTH, HEIGHT) / 2)

        # 在画布上绘制一个圆形（如果半径大于零）
        if radius > 0:
            renderer.draw_circle(x_center, y_center, radius)

    # 将渲染后的画布转换为numpy数组，并创建一个视频帧对象，并写入视频输出中    
    image_data= renderer.get_image()
    video_frame= av.VideoFrame.from_ndarray(image_data)
    video_output.mux """