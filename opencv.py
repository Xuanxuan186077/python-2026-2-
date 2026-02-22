import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# 1. 复杂的数据预处理 (Data Augmentation)
# 在机器视觉中，我们不仅要加载数据，还要通过切片、旋转、归一化来增强模型的泛化能力
transform = transforms.Compose([
    transforms.RandomRotation(10),      # 随机旋转，增加模型鲁棒性
    transforms.RandomAffine(0, translate=(0.1, 0.1)), # 随机平移
    transforms.ToTensor(),              # 转为 Tensor 格式
    transforms.Normalize((0.5,), (0.5,)) # 归一化到 [-1, 1]
])

# 加载 MNIST 数据集
train_set = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_set = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
test_loader = DataLoader(test_set, batch_size=1000, shuffle=False)

# 2. 定义复杂的 CNN 模型
class ComplexCNN(nn.Module):
    def __init__(self):
        super(ComplexCNN, self).__init__()
        # 第一层卷积：提取基础纹理
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32) # 批归一化，加速收敛
        
        # 第二层卷积：提取复杂形状
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        
        self.pool = nn.MaxPool2d(2, 2) # 池化层：压缩空间，保留关键特征
        self.dropout = nn.Dropout(0.25) # 防止过拟合
        
        # 全连接层：将提取的视觉特征映射到 0-9 的分类上
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        # x 的维度变化: (Batch, 1, 28, 28)
        x = self.pool(torch.relu(self.bn1(self.conv1(x)))) # -> (Batch, 32, 14, 14)
        x = self.pool(torch.relu(self.bn2(self.conv2(x)))) # -> (Batch, 64, 7, 7)
        
        # 展平特征图（Flatten）
        x = x.view(-1, 64 * 7 * 7) 
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# 3. 训练与优化配置
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ComplexCNN().to(device)
criterion = nn.CrossEntropyLoss() # 交叉熵损失函数
optimizer = optim.Adam(model.parameters(), lr=0.001) # Adam 优化器

# 4. 完整的训练循环
def train(epochs):
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for i, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            
            optimizer.zero_grad()      # 梯度清零
            outputs = model(images)    # 前向传播
            loss = criterion(outputs, labels) # 计算损失
            loss.backward()            # 反向传播（计算梯度）
            optimizer.step()           # 更新参数
            
            running_loss += loss.item()
            if i % 100 == 99:
                print(f'[Epoch {epoch + 1}, Batch {i + 1}] Loss: {running_loss / 100:.3f}')
                running_loss = 0.0

# 5. 模型评估逻辑
def test():
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad(): # 测试时不计算梯度
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f'准确率: {100 * correct / total}%')

# 执行
if __name__ == "__main__":
    train(3) # 训练3轮
    test()