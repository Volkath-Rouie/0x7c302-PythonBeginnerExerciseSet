""" # 导入所需的库
import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import matplotlib.animation as animation
import simpleaudio as sa

# 读取音频文件并获取采样率和数据
rate, data = wavfile.read("test.wav")

# 播放音频文件
play_obj = sa.play_buffer(data, 1, 2, rate)

# 计算每帧的时间间隔和总帧数
dt = 1/rate # 时间间隔
N = len(data) # 总帧数

# 创建一个画布和子图对象
fig = plt.figure()
ax = fig.add_subplot(111)

# 设置子图的标题，标签和范围
ax.set_title("Audio Spectrum")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")
ax.set_xlim(0, 2000) # 设置频率范围为0-2000Hz

# 初始化一个空的线条对象，用于绘制频谱曲线
line, = ax.plot([], [], lw=2)

# 定义一个函数，用于更新每一帧的数据和线条对象
def animate(i):
    # 计算当前帧对应的时间点和数据点
    t = i * dt # 时间点
    y = data[i] # 数据点
    
    # 对数据点进行快速傅里叶变换，并获取幅度和频率值
    Y_k = fft(y) / N # FFT结果（复数列表）
    Y_k[1:] = 2 * Y_k[1:] # 乘以2（除去直流分量）
    Pxx = np.abs(Y_k) # 取模（幅度值）
    f = rate * np.arange(N) / N # 频率值
    
    # 更新线条对象的数据源，并返回线条对象作为元组
    line.set_data(f, Pxx)
    return line,

# 创建一个动画对象，指定画布，更新函数，帧数，时间间隔等参数，并保存为mp4格式的视频文件    
ani = animation.FuncAnimation(fig, animate, frames=N,
                              interval=dt*1000)
ani.save('test_spec.mp4') """

""" # 导入device-manager 模块
import device_manager
# 导入os 模块
import os

# 创建一个DeviceManager 对象
dm = device_manager.DeviceManager()

# 查找连接的设备，并将它们存储到一个字典中
devices = dm.search()

# 获取本地组策略编辑器的地址
gpedit = dm.get_device("gpedit")

# 重新启动本地组策略编辑器
os.execv(gpedit, []) """

""" # 导入需要的库
import librosa
import matplotlib.pyplot as plt
import numpy as np

os.chdir('D:\\Proccess\\TempArea\\')

# 读取音频文件并获取采样率
audio_file = "牛佳钰 - 先别说话" # 音频文件路径
y, sr = librosa.load(audio_file) # y 是音频信号数组，sr 是采样率

# 计算音频时长（秒）
duration = librosa.get_duration(y=y, sr=sr)

# 计算短时傅里叶变换（STFT）并获取幅度谱
D = np.abs(librosa.stft(y)) # D 是幅度谱矩阵

# 设置视频参数
fps = 1 # 帧数
bitrate = "42M" # 码率
width = 3840 # 宽度（像素）
height = 2160 # 高度（像素）
dpi = 100 # 分辨率（每英寸点数）

# 设置柱状图参数
bins = 50 # 柱子数量
color = "blue" # 柱子颜色

# 创建一个空白的画布，并设置大小和分辨率
fig, ax = plt.subplots()
fig.set_size_inches(width / dpi, height / dpi)
fig.set_dpi(dpi)

# 循环遍历每一帧，并绘制柱状图
for i in range(int(duration * fps)):
    # 获取当前帧对应的幅度谱切片，并计算平均值
    slice = D[:, i * (D.shape[1] // (duration * fps)) : (i + 1) * (D.shape[1] // (duration * fps))]
    mean_slice = np.mean(slice, axis=1)

    # 绘制柱状图，并设置标题、坐标轴等属性
    ax.clear()
    ax.bar(np.arange(bins), mean_slice[:bins], color=color)
    ax.set_title("Spectrogram Animation")
    ax.set_xlabel("Frequency Bin")
    ax.set_ylabel("Amplitude")

    # 将当前帧保存为图片文件，命名格式为 frame_000.png 等
    fig.savefig(f"frame_{i:03d}.png")

# 使用 ffmpeg 将图片序列转换为视频文件，并设置视频参数
import os 
os.system(f"ffmpeg -hide_banner -hwaccel vulkan -r {fps} -f image2 -s {width}x{height} -i frame_%03d.png -vcodec h264_qsv -crf 25 -pix_fmt yuv420p -b:v {bitrate} output.mp4") """