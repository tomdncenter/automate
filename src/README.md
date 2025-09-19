# ติดตั้ง Prefect
pip install prefect

# export ให้ชี้ไปที่ Orion (Server A)
export PREFECT_API_URL="http://192.168.1.155:4200/api"

# clone โค้ด project
git clone https://github.com/your-org/your-repo.git
cd your-repo

# สร้างไฟล์ prefect.yaml ตามที่ออกแบบ
# (มี build/pull/git_clone, deployments, work_pool ฯลฯ)

# สร้าง/อัพเดท deployment
prefect deploy --all
