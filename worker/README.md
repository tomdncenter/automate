# เตรียม venv
mkdir prefect
cd prefect
python -m venv flow
source ./flow/bin/activate

# ติดตั้ง Prefect + dependency ของ flow
pip install prefect -r requirements.txt

# export ค่าให้ชี้ไปที่ Server A
export PREFECT_API_URL="https://automate.prod-5088.healthupgroup.com/api"

# (ถ้าใช้ Prefect Cloud ต้อง export PREFECT_API_KEY ด้วย)

# รัน worker ให้ join pool ที่ต้องการ
prefect worker start --pool my-pool
