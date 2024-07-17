# API-VnStock
API đơn giản cho VnStock

# Cài đặt virtual env
python -m venv env

# Kích hoạt virtual env
env/Scripts/activate
nếu không được thì thử env/Scripts/activate.bat
sau đấy reset lại vsc

# Cài đặt package
pip install -r requirements.txt

# Chạy server API
uvicorn API:app --reload

đổi host hoặc port khác thì thêm --host=8000 --port=...

uvicorn API:app --host=... port=... --reload