import os

from openai import OpenAI


def main():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("请先设置 DEEPSEEK_API_KEY 环境变量。")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )

    messages = [
        {"role": "system", "content": "你是一个幽默、专业的 AI 编程导师。"},
        {"role": "user", "content": "请用一句简短的话鼓励我继续学习 AIGC 调用代码。"},
    ]

    print("正在调用大模型，请稍候...")
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
        )
        print(response.choices[0].message.content)
    except Exception as exc:
        print(f"调用失败: {exc}")


if __name__ == "__main__":
    main()
