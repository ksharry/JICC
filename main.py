# -*- coding: utf-8 -*-
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn
from config_manager import config

# 從配置文件讀取設置
app_config = {
    'title': 'JICC',
    'version': '1.0.0',
    'debug': config.getboolean('development', 'debug', True)
}

app = FastAPI(**app_config)

@app.get('/', response_class=HTMLResponse)
async def login_page():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>JICC 登入</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>JICC 系統登入</h1>
    <form id="loginForm">
        <div>
            <label>用戶名:</label>
            <input type="text" id="username" required>
        </div>
        <div>
            <label>密碼:</label>
            <input type="password" id="password" required>
        </div>
        <button type="submit">登入</button>
    </form>
    <div id="error" style="color:red; display:none;"></div>
    <script>
        document.getElementById('loginForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: 'username=' + username + '&password=' + password
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('登入成功！');
                } else {
                    document.getElementById('error').textContent = result.message || '登入失敗';
                    document.getElementById('error').style.display = 'block';
                }
            } catch (error) {
                document.getElementById('error').textContent = '網路錯誤';
                document.getElementById('error').style.display = 'block';
            }
        });
    </script>
</body>
</html>'''

@app.post('/api/login')
async def login(username: str = Form(...), password: str = Form(...)):
    if username == 'admin' and password == 'admin123':
        return {'success': True, 'message': '登入成功', 'user': {'username': 'admin', 'role': 'admin'}}
    elif username == 'user1' and password == 'user123':
        return {'success': True, 'message': '登入成功', 'user': {'username': 'user1', 'role': 'user'}}
    else:
        raise HTTPException(status_code=401, detail='用戶名或密碼錯誤')

if __name__ == '__main__':
    # 從配置文件讀取服務器設置
    host = config.get('server', 'host', '0.0.0.0')
    port = config.getint('server', 'port', 8000)
    reload = config.getboolean('server', 'reload', True)
    
    print(' 啟動 JICC 服務器...')
    print(f' 訪問地址: http://{host}:{port}')
    print(' 測試帳號: admin/admin123 或 user1/user123')
    print('=' * 50)
    
    # 修復 reload 警告
    if reload:
        uvicorn.run("main:app", host=host, port=port, reload=True)
    else:
        uvicorn.run(app, host=host, port=port)
