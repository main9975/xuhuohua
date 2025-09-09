

# Douyin-Bond-Maintainer 🔥

自动帮你在抖音网页端续火花 💖，保持和心仪对象的「联系不断线」。

---

## 🛠️ How to Use

### 1️⃣ 获取抖音 Cookies

1. 打开 [抖音网页版](https://www.douyin.com/) 并登陆
2. 安装浏览器插件 [Cookie-Editor](https://cookie-editor.com/)
   👉 [Chrome 商店](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) | [Edge 商店](https://microsoftedge.microsoft.com/addons/detail/cookieeditor/neaplmfkghagebokkhpjpoebhdledlfi)
3. 使用插件导出 Cookies（JSON 格式）
4. 将 Cookies 以 Base64 编码（[在线编码](https://www.sojson.com/base64.html)）

![使用指南](https://github.com/user-attachments/assets/6216240b-c0af-4461-8894-f2c45c81fb25)

---

### 2️⃣ 配置仓库 Secret

进入仓库 `Settings → Secrets and variables → Actions → Repository secrets`，添加以下变量：

| 名称             | 说明                                                                           |
| -------------- |------------------------------------------------------------------------------|
| `COOKIES`      | 从 Cookie-Editor 获取的 Cookies（Base64 编码）                                       |
| `NICKNAME`     | 要续火花的对象昵称（如“某人”）                                                             |
| `MSG`          | 留言内容（可选，默认为“火花”）                                                             |
| `V2RAY_CONFIG` | **（可选）Base64 编码的 V2Ray 配置文件**，用于解决在 GitHub Actions 中访问抖音超时                   |
| `PROXY`        | **（可选）设置 Playwright 使用的代理地址**，如 `socks5://127.0.0.1:10808` |

> ⚠️ 若使用 `V2RAY_CONFIG`，**必须同时设置 `PROXY`**，否则无法生效。

> ⚠️ 若未设置 `COOKIES` 或 `NICKNAME`，将终止任务并提示用户配置。

---

## ✅ Todo

* [ ] 支持模板变量，例如 `$date$` 插入当前日期
* [ ] 更多自定义内容（如 emoji、随机话术）
* [ ] 多对象循环续火花
