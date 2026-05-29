# -*- coding: utf-8 -*-
"""
AI Job Application Automation Script (AI Command Center Extension)
Author: AI Command Center Dev
Target: Automation of job application emails with attachment & customization support.
"""

import os
import smtplib
import json
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 初始化日志系统
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIJobAutomator:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.load_config()

    def load_config(self):
        """安全读取或初始化设定档（包含寄件信箱、回复信箱与 Gmail 应用程序密码）"""
        if not os.path.exists(self.config_path):
            # 自动生成安全隔离的设定模版
            default_config = {
                "sender_email": "Wshao777opscenter@gmail.com",
                "reply_to": "Wshao777opscenter@gmail.com",
                "gmail_app_password": "YOUR_GMAIL_APP_PASSWORD_HERE",  # 请在此处填入 Google 申请的 16 位金钥
                "github_links": [
                    "https://github.com/AnonymousTalent/ai-command-center/tree/main",
                    "https://github.com/Wshao777/wind-pricing"
                ]
            }
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=4, ensure_ascii=False)
            logging.info(f"已在当前目录生成安全配置模版 {self.config_path}，请更新您的 Gmail 应用程式金钥。")
            
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
            
        self.sender_email = self.config.get("sender_email", "Wshao777opscenter@gmail.com")
        self.reply_to = self.config.get("reply_to", "Wshao777opscenter@gmail.com")
        self.password = self.config.get("gmail_app_password", "")

    def generate_email_content(self, company_name="新亚洲仪器", contact_person="人力资源部 / 技术主管"):
        """动态组合针对不同企业的客制化自荐信内容"""
        subject = f"[求职] AI Systems Engineer / AI Automation Engineer – 徐志曆（12年机械/设备经验 + AI 系统整合）"
        
        body = f"""尊敬的贵公司{contact_person}您好：

我是 徐志曆，毕业于高职机械制图科，拥有正统且扎实的识图与绘图基本功。在机械与设备领域，我累积了 12 年贯穿内外场的实务经验，对于产线流程、设备结构、制程逻辑有深刻理解。同时，我对于公司的资讯安全与技术保密持有极高的职业道德标准。

收到贵公司（{company_name}）的联系信件让我非常期待。我相信，我的 “机械专业背景 + AI 系统整合能力” 正是贵公司目前最需要的即战力，能立刻为团队带来具体产出。

---

🔧 我的两大核心优势

1. 扎实的机械/设备现场经验
· 高职机械制图科毕业，熟悉 SolidWorks / AutoCAD / Inventor，三视图展开与识图能力扎实。
· 12 年内外场实务，清楚设备从设计、加工、组装到调试的完整流程。
· 能快速理解贵公司在光学检测、自动化设备、工业仪器领域的技术语言与工程痛点。

2. AI 系统工程与自动化整合能力
· 建立过 Multi-AI Command Center：整合 GPT、DeepSeek、Grok 等模型，通过 FastAPI 实现统一 AI Gateway 与 Workflow Router。
· 擅长 AI Orchestration、Agent Registry、AI Workflow 设计，并已完成 Docker 化部署与 JWT 认证。
· 明确朝向 AI Systems Engineer / AI Automation Engineer 发展，专注于 AI SaaS 产品化、工业 AI 整合、AI Agent 系统。
· GitHub 作品集：https://github.com/AnonymousTalent/ai-command-center/tree/main （展示多 AI 协作、API 编排、工业 AI 中介层原型）

---

🎯 我能为贵公司带来的具体价值
· 将 AOI / HALCON 检测输出 与 LLM 分析层 衔接，建立 工业 AI 中介层，让视觉结果自动转为制程决策与参数建议。
· 协助贵公司从 “设备/仪器供应商” 升级为 “AI 整合解决方案提供者”，抢占工业 AI 决策层的市场空白。
· 快速搭建 AI Command Center 原型，用于内部测试或客户展示，缩短 AI 应用的导入周期。

---

📄 附件 / 参考连结
· GitHub 主仓库：https://github.com/AnonymousTalent/ai-command-center/tree/main
· 更多专案（动态定价/决策系统）：https://github.com/Wshao777/wind-pricing

---

💼 期望职缺方向
· AI Systems Engineer
· AI Automation Engineer
· AI Integration Engineer
· AI Workflow Architect（进阶）

希望能在 AI SaaS、工业 AI、智慧工厂、多 Agent 系统 等领域贡献所长。

---

感谢您抽空阅读这封信。我期待能有机会与您进一步面谈，当面展示我的作品集与系统原型。

请随时以邮件或电话联系我。

徐志曆 敬上
📧 {self.reply_to}
📅 2026年5月
"""
        return subject, body

    def send_application(self, to_email, company_name="新亚洲仪器", contact_person="人力资源部 / 技术主管", resume_path=None):
        """执行高度保密的自动化投递，并强制将回复导流至指定的回复信箱"""
        if not self.password or "YOUR_GMAIL" in self.password:
            logging.error("错误：请先在 config.json 中设定正确的 Gmail 16位应用程式金钥！")
            return False

        subject, body = self.generate_email_content(company_name, contact_person)

        # 建立标准 MIME 邮件容器
        msg = MIMEMultipart()
        msg['From'] = f"徐志曆 <{self.sender_email}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        msg['Reply-To'] = self.reply_to  # 关键保密路由：强制让对方回复时，寄到此处

        # 挂载文本
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # 如果有实体 PDF 履历，执行自动挂载
        if resume_path and os.path.exists(resume_path):
            try:
                with open(resume_path, "rb") as fil:
                    part = MIMEApplication(fil.read(), Name=os.path.basename(resume_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_path)}"'
                msg.attach(part)
                logging.info(f"成功挂载实体履历附件: {resume_path}")
            except Exception as e:
                logging.error(f"挂载附件失败: {e}")

        # 连接加密 SMTP 安全网关并发送
        try:
            logging.info(f"正在建立安全连接，准备投递至 {company_name} ({to_email})...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # 启动 TLS 加密安全层
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, to_email, msg.as_string())
            server.close()
            logging.info(f"🚀 履历自动化投递成功！已成功送达 {company_name}。")
            return True
        except Exception as e:
            logging.error(f"SMTP 网关异常: {e}")
            return False

if __name__ == "__main__":
    # 初始化引擎
    automator = AIJobAutomator()
    print("\n[AI Command Center - 自动化发信引擎就绪]")
    
    # 实际测试或投递时，只需呼叫下行程式码（示例：寄送至新亚洲仪器 HR 信箱）
    # automator.send_application(to_email="hr@newasia.com.tw", company_name="新亚洲仪器", resume_path="徐志曆_AI系统工程师履历.pdf")
