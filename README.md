# 🔧 Proxy Auto-Config Tool

[![GitHub](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/MaiiNor/proxy-auto-config)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)

**智能代理自动检测和配置工具 - 专为开发者和网络受限环境设计**

## 🎯 为什么需要这个工具？

在网络受限的环境中，配置代理是一项繁琐且容易出错的任务。这个工具可以：

- ✅ **自动检测**现有的代理配置
- ✅ **智能配置**系统环境变量
- ✅ **无缝集成**各种开发工具
- ✅ **零配置**开箱即用

## ✨ 核心特性

### 🔍 智能检测
- **多协议支持**: SOCKS5, HTTP, HTTPS 代理
- **全方位扫描**: 环境变量、端口、进程、网络配置
- **自动识别**: v2ray, Clash, SS/SSR, Shadowsocks 等
- **零依赖**: 纯 Python 实现，无需额外安装

### ⚙️ 自动配置
- **环境变量**: 自动设置 `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`
- **工具集成**: 支持 curl, wget, git, pip, npm 等
- **开发环境**: 为 Python, Node.js, Go 等配置代理
- **系统范围**: 支持 Linux, macOS, WSL

### 🛠️ 开发友好
- **API 集成**: 提供 Python API 供其他工具调用
- **CLI 工具**: 简单的命令行界面
- **配置导出**: 生成可重复使用的配置脚本
- **日志记录**: 详细的运行日志和调试信息

## 🚀 快速开始

### 安装

#### 方法1: 直接下载
```bash
# 克隆仓库
git clone https://github.com/MaiiNor/proxy-auto-config.git
cd proxy-auto-config

# 运行检测
python3 scripts/simple_proxy_check.py
```

#### 方法2: 使用 pip (即将推出)
```bash
pip install proxy-auto-config
proxy-check
```

#### 方法3: 作为模块使用
```python
from proxy_auto_config import detect_proxy

# 自动检测代理
proxy_info = detect_proxy()
print(f"检测到代理: {proxy_info['url']}")
```

### 基本使用

#### 1. 快速检测
```bash
# 运行代理检测
python3 scripts/simple_proxy_check.py

# 输出示例:
# ✅ 环境变量 HTTP_PROXY: socks5://127.0.0.1:10808
# ✅ 端口 10808 正在监听
# ✅ 检测到 v2ray 进程
# 🔧 推荐配置: socks5://127.0.0.1:10808
```

#### 2. 自动配置
```bash
# 自动检测并配置
python3 scripts/proxy_detector.py --configure

# 应用配置
source ~/.proxy_config/configure.sh

# 验证配置
env | grep -i proxy
```

#### 3. 生成配置脚本
```bash
# 生成配置脚本
python3 scripts/proxy_detector.py --generate-script

# 脚本位置
ls -la ~/.proxy_config/
# configure.sh    - Shell 配置脚本
# proxy.json      - JSON 配置文件
# python_config.py - Python 配置模块
```

## 📖 详细指南

### 支持的代理类型

| 代理工具 | 默认端口 | 检测方法 | 支持程度 |
|---------|---------|---------|---------|
| **v2ray / Xray** | 10808 | 进程 + 端口 | ✅ 完整 |
| **Clash** | 7890, 7891 | 进程 + 端口 | ✅ 完整 |
| **Shadowsocks** | 1080, 1081 | 进程 + 端口 | ✅ 完整 |
| **HTTP 代理** | 8080, 8888 | 环境变量 | ✅ 完整 |
| **SOCKS5 代理** | 10808, 1080 | 端口扫描 | ✅ 完整 |
| **系统代理** | - | 系统设置 | ⚠️ 部分 |

### 配置示例

#### Shell 环境 (.bashrc / .zshrc)
```bash
# 自动代理配置
if [ -f ~/.proxy_config/configure.sh ]; then
    source ~/.proxy_config/configure.sh
fi

# 或者使用函数
function set-proxy() {
    python3 ~/proxy-auto-config/scripts/simple_proxy_check.py --configure
    source ~/.proxy_config/configure.sh
}
```

#### Python 项目
```python
# config.py
import os
from proxy_auto_config import get_proxy_config

# 自动获取代理配置
proxy_config = get_proxy_config()

# 设置 requests 代理
import requests
session = requests.Session()
if proxy_config['http']:
    session.proxies = {
        'http': proxy_config['http'],
        'https': proxy_config['https']
    }
```

#### Git 配置
```bash
# 设置 Git 代理
git config --global http.proxy socks5://127.0.0.1:10808
git config --global https.proxy socks5://127.0.0.1:10808

# 或使用自动配置
python3 scripts/proxy_detector.py --configure-git
```

### 高级功能

#### 定时检测
```bash
# 添加到 crontab (每小时检测一次)
0 * * * * cd /path/to/proxy-auto-config && python3 scripts/proxy_detector.py --configure >> ~/.proxy_log.log 2>&1
```

#### 网络切换时自动配置
```bash
# 网络变化时触发 (Linux)
#!/bin/bash
# /etc/network/if-up.d/proxy-auto-config
cd /path/to/proxy-auto-config
python3 scripts/simple_proxy_check.py --configure --quiet
```

#### Docker 集成
```dockerfile
# Dockerfile
FROM python:3.9

# 复制代理配置工具
COPY proxy-auto-config /app/proxy-auto-config

# 设置入口点
ENTRYPOINT ["python3", "/app/proxy-auto-config/scripts/proxy_detector.py", "--configure"]
```

## 🔧 开发集成

### Python API
```python
from proxy_auto_config import (
    detect_proxy,
    configure_environment,
    get_proxy_for_url,
    ProxyConfig
)

# 1. 检测代理
config = detect_proxy()
print(f"代理地址: {config.url}")
print(f"代理类型: {config.type}")

# 2. 配置环境
configure_environment(config)

# 3. 为特定 URL 获取代理
proxy = get_proxy_for_url("https://api.github.com")
print(f"GitHub API 代理: {proxy}")

# 4. 验证代理
if config.validate():
    print("✅ 代理可用")
else:
    print("❌ 代理不可用")
```

### 命令行工具
```bash
# 检测代理
proxy-check detect

# 配置环境
proxy-check configure

# 测试代理
proxy-check test https://api.github.com

# 生成配置
proxy-check generate --format bash
proxy-check generate --format python
proxy-check generate --format json

# 查看状态
proxy-check status
```

### 与其他工具集成

#### 与 curl/wget 集成
```bash
# 自动设置 curl 代理
alias curl='curl --proxy $(python3 -c "from proxy_auto_config import detect_proxy; print(detect_proxy().url)")'

# 自动设置 wget 代理
alias wget='wget -e use_proxy=yes -e http_proxy=$(python3 -c "from proxy_auto_config import detect_proxy; print(detect_proxy().url)")'
```

#### 与 pip/npm 集成
```bash
# 自动配置 pip 代理
python3 -m proxy_auto_config.configure_pip

# 自动配置 npm 代理
python3 -m proxy_auto_config.configure_npm
```

## 🐛 故障排除

### 常见问题

#### Q1: 检测不到代理
```bash
# 检查代理是否运行
ps aux | grep -E "v2ray|clash|ss-"

# 检查端口
netstat -tlnp | grep :10808

# 详细检测
python3 scripts/proxy_detector.py --verbose
```

#### Q2: 代理配置不生效
```bash
# 检查环境变量
env | grep -i proxy

# 重新加载配置
source ~/.proxy_config/configure.sh

# 测试代理
curl --socks5 127.0.0.1:10808 https://ipinfo.io
```

#### Q3: 某些工具不使用代理
```bash
# 检查工具特定配置
git config --get http.proxy
npm config get proxy

# 手动配置
python3 scripts/proxy_detector.py --configure-tool git
python3 scripts/proxy_detector.py --configure-tool npm
```

### 调试模式
```bash
# 启用调试输出
python3 scripts/proxy_detector.py --debug

# 查看日志
tail -f ~/.proxy_log.log

# 测试特定功能
python3 scripts/proxy_detector.py --test-all
```

## 📊 性能与兼容性

### 系统要求
- **操作系统**: Linux, macOS, Windows (WSL)
- **Python**: 3.8 或更高版本
- **内存**: 最少 50MB RAM
- **磁盘空间**: 最少 10MB

### 性能指标
- **检测时间**: < 2秒 (快速模式)
- **内存占用**: < 50MB
- **CPU 使用**: < 5% (检测时)
- **网络请求**: 0 (本地检测)

### 兼容性测试
| 工具/环境 | 兼容性 | 备注 |
|----------|--------|------|
| **Linux** | ✅ 优秀 | 所有主流发行版 |
| **macOS** | ✅ 优秀 | 10.15+ |
| **WSL** | ✅ 优秀 | WSL1/WSL2 |
| **Docker** | ✅ 优秀 | 需要主机网络 |
| **CI/CD** | ✅ 良好 | GitHub Actions, GitLab CI |

## 🤝 贡献指南

### 开发设置
```bash
# 1. 克隆仓库
git clone https://github.com/MaiiNor/proxy-auto-config.git
cd proxy-auto-config

# 2. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 3. 安装开发依赖
pip install -r requirements-dev.txt

# 4. 运行测试
pytest tests/
```

### 代码规范
- 遵循 PEP 8 代码风格
- 使用类型注解
- 编写单元测试
- 更新文档

### 提交更改
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢以下项目和工具：
- **v2ray/Xray** - 优秀的代理工具
- **Clash** - 功能丰富的代理客户端
- **Python 社区** - 提供了强大的工具生态
- **所有贡献者** - 感谢你们的反馈和改进

## 📞 支持与联系

### 获取帮助
- **GitHub Issues**: [报告问题](https://github.com/MaiiNor/proxy-auto-config/issues)
- **文档**: 查看本 README 和代码注释
- **讨论**: 在 Issues 中发起讨论

### 保持更新
```bash
# 关注仓库
git pull origin main

# 检查新版本
python3 scripts/proxy_detector.py --version
```

## ⭐ 支持项目

如果这个工具对你有帮助，请：
1. 给仓库点个 ⭐ Star
2. 分享给其他开发者
3. 提交改进建议
4. 报告遇到的问题

---

**最后更新**: 2026-03-29  
**版本**: 1.0.0  
**作者**: MaiiNor  
**状态**: ✅ 生产就绪

**Happy coding with proxy!** 🚀