import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons


class SphericalIntegralVisualizer:
    def __init__(self):
        # 创建图形和3D坐标轴
        self.fig = plt.figure(figsize=(12, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

        # 初始参数
        self.r_max = 2.0  # 最大半径
        self.n_r = 5  # r方向的分割数
        self.n_theta = 8  # θ方向的分割数
        self.n_phi = 8  # φ方向的分割数
        self.animation_speed = 50  # 动画速度（毫秒）
        self.current_frame = 0
        self.total_frames = 100
        self.show_grid = True
        self.show_volume_element = True
        self.integration_mode = 'radial'  # 'radial', 'angular', 'full'

        # 动画对象
        self.anim = None

        # 设置坐标轴
        self.setup_axes()

        # 创建控制面板
        self.setup_controls()

        # 初始化可视化
        self.initialize_visualization()

    def setup_axes(self):
        # 设置坐标轴标签和标题
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('三重积分在球面坐标系中的几何意义')

        # 设置坐标轴范围
        limit = self.r_max * 1.2
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.ax.set_zlim(-limit, limit)

        # 设置坐标轴比例相等
        self.ax.set_box_aspect([1, 1, 1])

    def setup_controls(self):
        # 为控制面板调整图形布局
        self.fig.subplots_adjust(bottom=0.3)

        # 创建滑块的坐标轴
        ax_r = plt.axes([0.25, 0.20, 0.65, 0.03])
        ax_n_r = plt.axes([0.25, 0.16, 0.65, 0.03])
        ax_n_theta = plt.axes([0.25, 0.12, 0.65, 0.03])
        ax_n_phi = plt.axes([0.25, 0.08, 0.65, 0.03])
        ax_speed = plt.axes([0.25, 0.04, 0.65, 0.03])

        # 创建滑块
        self.slider_r = Slider(ax_r, '最大半径 (r)', 0.5, 5.0, valinit=self.r_max)
        self.slider_n_r = Slider(ax_n_r, 'r分割数', 2, 10, valinit=self.n_r, valstep=1)
        self.slider_n_theta = Slider(ax_n_theta, 'θ分割数', 4, 20, valinit=self.n_theta, valstep=1)
        self.slider_n_phi = Slider(ax_n_phi, 'φ分割数', 4, 20, valinit=self.n_phi, valstep=1)
        self.slider_speed = Slider(ax_speed, '动画速度', 10, 200, valinit=self.animation_speed)

        # 创建按钮
        ax_reset = plt.axes([0.8, 0.25, 0.1, 0.04])
        self.button_reset = Button(ax_reset, '重置')

        ax_play = plt.axes([0.6, 0.25, 0.1, 0.04])
        self.button_play = Button(ax_play, '播放')

        ax_pause = plt.axes([0.7, 0.25, 0.1, 0.04])
        self.button_pause = Button(ax_pause, '暂停')

        # 创建单选按钮
        ax_radio = plt.axes([0.025, 0.05, 0.15, 0.15])
        self.radio = RadioButtons(ax_radio, ('径向积分', '角向积分', '完整积分'))

        # 注册回调函数
        self.slider_r.on_changed(self.update_params)
        self.slider_n_r.on_changed(self.update_params)
        self.slider_n_theta.on_changed(self.update_params)
        self.slider_n_phi.on_changed(self.update_params)
        self.slider_speed.on_changed(self.update_animation_speed)
        self.button_reset.on_clicked(self.reset)
        self.button_play.on_clicked(self.play_animation)
        self.button_pause.on_clicked(self.pause_animation)
        self.radio.on_clicked(self.set_integration_mode)

    def initialize_visualization(self):
        # 清除当前图形
        self.ax.clear()
        self.setup_axes()

        # 绘制坐标轴
        self.draw_coordinate_system()

        # 启动动画
        self.start_animation()

    def draw_coordinate_system(self):
        # 绘制坐标轴
        origin = np.zeros(3)
        x_axis = np.array([self.r_max, 0, 0])
        y_axis = np.array([0, self.r_max, 0])
        z_axis = np.array([0, 0, self.r_max])

        # 绘制坐标轴线
        self.ax.quiver(*origin, *x_axis, color='r', arrow_length_ratio=0.1, label='X轴')
        self.ax.quiver(*origin, *y_axis, color='g', arrow_length_ratio=0.1, label='Y轴')
        self.ax.quiver(*origin, *z_axis, color='b', arrow_length_ratio=0.1, label='Z轴')

        # 添加坐标轴标签
        self.ax.text(self.r_max * 1.1, 0, 0, "X", color='red')
        self.ax.text(0, self.r_max * 1.1, 0, "Y", color='green')
        self.ax.text(0, 0, self.r_max * 1.1, "Z", color='blue')

        # 绘制球坐标系说明
        self.ax.text(self.r_max * 0.7, self.r_max * 0.7, self.r_max * 0.7,
                     "球坐标系 (r,θ,φ)\n体积元素: dV = r²sinθ drdθdφ",
                     fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

        # 如果需要，绘制网格
        if self.show_grid:
            self.draw_spherical_grid()

    def draw_spherical_grid(self):
        # 绘制球坐标系网格
        # 1. r方向的网格（同心球面）
        r_values = np.linspace(0, self.r_max, self.n_r + 1)[1:]
        for r in r_values:
            u = np.linspace(0, 2 * np.pi, 30)
            v = np.linspace(0, np.pi, 30)
            x = r * np.outer(np.cos(u), np.sin(v))
            y = r * np.outer(np.sin(u), np.sin(v))
            z = r * np.outer(np.ones(np.size(u)), np.cos(v))
            self.ax.plot_surface(x, y, z, color='gray', alpha=0.1)

        # 2. θ方向的网格（经线）
        theta_values = np.linspace(0, np.pi, self.n_theta + 1)[:-1]
        for theta in theta_values:
            phi = np.linspace(0, 2 * np.pi, 50)
            r = self.r_max
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta) * np.ones_like(phi)
            self.ax.plot(x, y, z, color='gray', alpha=0.3, linestyle=':')

        # 3. φ方向的网格（纬线）
        phi_values = np.linspace(0, 2 * np.pi, self.n_phi + 1)[:-1]
        for phi in phi_values:
            theta = np.linspace(0, np.pi, 50)
            r = self.r_max
            x = r * np.sin(theta) * np.cos(phi) * np.ones_like(theta)
            y = r * np.sin(theta) * np.sin(phi) * np.ones_like(theta)
            z = r * np.cos(theta)
            self.ax.plot(x, y, z, color='gray', alpha=0.3, linestyle=':')

    def draw_volume_element(self, r, theta, phi, dr, dtheta, dphi, alpha=0.7):
        # 绘制体积元素 dV = r²sinθ drdθdφ
        # 计算体积元素的8个顶点
        points = []
        for r_val in [r, r + dr]:
            for theta_val in [theta, theta + dtheta]:
                for phi_val in [phi, phi + dphi]:
                    x = r_val * np.sin(theta_val) * np.cos(phi_val)
                    y = r_val * np.sin(theta_val) * np.sin(phi_val)
                    z = r_val * np.cos(theta_val)
                    points.append([x, y, z])

        # 将点转换为NumPy数组
        points = np.array(points)

        # 定义体积元素的面
        faces = [
            [0, 1, 3, 2],  # 内侧r面
            [4, 5, 7, 6],  # 外侧r面
            [0, 1, 5, 4],  # 下侧theta面
            [2, 3, 7, 6],  # 上侧theta面
            [0, 2, 6, 4],  # 左侧phi面
            [1, 3, 7, 5]  # 右侧phi面
        ]

        # 绘制体积元素的面
        for face in faces:
            x = [points[i][0] for i in face]
            y = [points[i][1] for i in face]
            z = [points[i][2] for i in face]
            # 添加第一个点以闭合多边形
            x.append(x[0])
            y.append(y[0])
            z.append(z[0])
            self.ax.plot(x, y, z, 'k-', alpha=0.3)

            # 填充面
            verts = [list(zip(x, y, z))]
            self.ax.add_collection3d(plt.matplotlib.collections.PolyCollection(verts,
                                                                               facecolors='cyan',
                                                                               alpha=alpha))

    def update(self, frame):
        # 清除当前图形
        self.ax.clear()
        self.setup_axes()

        # 绘制坐标系
        self.draw_coordinate_system()

        # 根据当前帧和积分模式更新可视化
        progress = frame / self.total_frames

        if self.integration_mode == 'radial':
            self.visualize_radial_integration(progress)
        elif self.integration_mode == 'angular':
            self.visualize_angular_integration(progress)
        else:  # 'full'
            self.visualize_full_integration(progress)

        return self.ax,

    def visualize_radial_integration(self, progress):
        # 可视化径向积分过程
        # 固定θ和φ的值，r从0增加到r_max*progress
        r_current = self.r_max * progress
        dr = r_current / max(1, self.n_r - 1)

        # 计算体积元素的大小
        dtheta = np.pi / self.n_theta
        dphi = 2 * np.pi / self.n_phi

        # 绘制已经积分的部分（从原点到当前r的扇形）
        if r_current > 0:
            theta_values = np.linspace(0, np.pi, self.n_theta + 1)
            phi_values = np.linspace(0, 2 * np.pi, self.n_phi + 1)

            for i in range(len(theta_values) - 1):
                for j in range(len(phi_values) - 1):
                    theta = theta_values[i]
                    phi = phi_values[j]

                    # 绘制当前体积元素
                    if self.show_volume_element:
                        for r in np.linspace(0, r_current, self.n_r)[:-1]:
                            self.draw_volume_element(r, theta, phi, dr, dtheta, dphi, alpha=0.3)

        # 添加说明文本
        self.ax.text2D(0.05, 0.95, f"径向积分: ∫(0→{r_current:.2f}) r² dr",
                       transform=self.ax.transAxes, fontsize=12,
                       bbox=dict(facecolor='white', alpha=0.7))

    def visualize_angular_integration(self, progress):
        # 可视化角向积分过程
        # 固定r，θ和φ从0增加到各自的最大值*progress
        theta_max = np.pi * progress
        phi_max = 2 * np.pi * progress

        # 计算体积元素的大小
        dr = self.r_max / self.n_r
        dtheta = theta_max / max(1, self.n_theta - 1)
        dphi = phi_max / max(1, self.n_phi - 1)

        # 绘制已经积分的部分
        if theta_max > 0 and phi_max > 0:
            r_values = np.linspace(0, self.r_max, self.n_r + 1)[1:]
            theta_values = np.linspace(0, theta_max, self.n_theta + 1)[:-1]
            phi_values = np.linspace(0, phi_max, self.n_phi + 1)[:-1]

            for r in r_values:
                for theta in theta_values:
                    for phi in phi_values:
                        # 绘制当前体积元素
                        if self.show_volume_element:
                            self.draw_volume_element(r, theta, phi, dr, dtheta, dphi, alpha=0.3)

        # 添加说明文本
        self.ax.text2D(0.05, 0.95, f"角向积分: ∫(0→{theta_max:.2f}) ∫(0→{phi_max:.2f}) sinθ dθdφ",
                       transform=self.ax.transAxes, fontsize=12,
                       bbox=dict(facecolor='white', alpha=0.7))

    def visualize_full_integration(self, progress):
        # 可视化完整的三重积分过程
        # 所有变量都随进度增加
        r_current = self.r_max * progress
        theta_max = np.pi * progress
        phi_max = 2 * np.pi * progress

        # 计算体积元素的大小
        dr = r_current / max(1, self.n_r - 1)
        dtheta = theta_max / max(1, self.n_theta - 1)
        dphi = phi_max / max(1, self.n_phi - 1)

        # 绘制已经积分的部分
        if r_current > 0 and theta_max > 0 and phi_max > 0:
            r_values = np.linspace(0, r_current, self.n_r + 1)[:-1]
            theta_values = np.linspace(0, theta_max, self.n_theta + 1)[:-1]
            phi_values = np.linspace(0, phi_max, self.n_phi + 1)[:-1]

            for r in r_values:
                for theta in theta_values:
                    for phi in phi_values:
                        # 绘制当前体积元素
                        if self.show_volume_element:
                            self.draw_volume_element(r, theta, phi, dr, dtheta, dphi, alpha=0.2)

        # 计算当前积分体积
        volume = (4 / 3) * np.pi * r_current ** 3 * (progress ** 2)  # 近似值

        # 添加说明文本
        self.ax.text2D(0.05, 0.95,
                       f"三重积分: ∫(0→{r_current:.2f}) ∫(0→{theta_max:.2f}) ∫(0→{phi_max:.2f}) r²sinθ drdθdφ\n当前体积: {volume:.2f}",
                       transform=self.ax.transAxes, fontsize=12,
                       bbox=dict(facecolor='white', alpha=0.7))

    def start_animation(self):
        # 启动动画
        self.current_frame = 0
        self.anim = FuncAnimation(self.fig, self.update, frames=self.total_frames,
                                  interval=self.animation_speed, blit=True)

    def update_params(self, val):
        # 更新参数
        self.r_max = self.slider_r.val
        self.n_r = int(self.slider_n_r.val)
        self.n_theta = int(self.slider_n_theta.val)
        self.n_phi = int(self.slider_n_phi.val)

        # 重新初始化可视化
        self.initialize_visualization()

    def update_animation_speed(self, val):
        # 更新动画速度
        self.animation_speed = self.slider_speed.val
        if self.anim is not None:
            self.anim.event_source.interval = self.animation_speed

    def reset(self, event):
        # 重置所有参数到初始值
        self.slider_r.set_val(2.0)
        self.slider_n_r.set_val(5)
        self.slider_n_theta.set_val(8)
        self.slider_n_phi.set_val(8)
        self.slider_speed.set_val(50)
        self.integration_mode = 'radial'
        self.radio.set_active(0)

        # 重新初始化可视化
        self.initialize_visualization()

    def play_animation(self, event):
        # 播放动画
        if self.anim is not None:
            self.anim.event_source.start()

    def pause_animation(self, event):
        # 暂停动画
        if self.anim is not None:
            self.anim.event_source.stop()

    def set_integration_mode(self, label):
        # 设置积分模式
        mode_map = {
            '径向积分': 'radial',
            '角向积分': 'angular',
            '完整积分': 'full'
        }
        self.integration_mode = mode_map[label]

        # 重新初始化可视化
        self.initialize_visualization()


# 主函数
def main():
    # 创建可视化器实例
    visualizer = SphericalIntegralVisualizer()

    # 显示图形
    plt.show()


if __name__ == "__main__":
    main()