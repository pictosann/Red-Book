# AIGC 自动化内容生成系统

这是一个基于 Streamlit 的 AIGC 内容生成演示项目，支持文本生成、图像生成和 Word 文档导出。

## 安装

```powershell
pip install -r requirements.txt
```

## 配置

不要把真实 API Key 写入源码或提交到 Git。可以复制 `.env.example` 作为本地配置参考，或在运行前通过环境变量设置：

```powershell
$env:DEEPSEEK_API_KEY="你的 DeepSeek API Key"
$env:SILICONFLOW_API_KEY="你的 SiliconFlow API Key"
$env:GITEE_AI_TOKEN="你的 Gitee AI Token"
```

应用侧边栏也支持手动输入 API Key，输入内容只用于当前运行会话。

## 运行

```powershell
streamlit run app.py
```

## 安全说明

仓库已忽略 `.env`、`key.txt`、IDE 配置目录和常见密钥文件。公开仓库前请确认不要提交真实凭据、个人路径、联系方式或生成的私有文档。
