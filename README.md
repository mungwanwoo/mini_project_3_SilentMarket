# mini_project_3_SilentMarket
이 문서는 번개장터와 비슷한 고요장터를 장고를 사용해서 만든 것이다
- 구매하기 판매정보 개인프로필등 추후 추가예정
---

# 📋 요구 사항 (Requirements)
Django 프로젝트를 시작하기 전에 아래 소프트웨어와 라이브러리가 필요합니다:

- Python 3.10
- Django 최신 버전
- pip (Python 패키지 관리자)
- miniconda
- dotenv
---

# 🛠️ Django 프로젝트를 로컬에서 http://127.0.0.1:8000/를 열어 확인하기
## 1. Python 설치

### 파이썬 미니콘다 설치하기
- https://github.com/conda-forge/miniforge
- OS 환경에 맞는 버전을 다운로드하고 설치

## 2. Python 가상환경 생성
가상환경은 프로젝트 의존성을 관리하기 위해 권장됩니다.


### 가상환경 생성
conda create --name myenv python=3.10
- myenv: 가상환경 이름
- python=3.10: 파이썬 버전

### 가상환경 활성화 (OS에 따라 명령어 다름)
- conda activate myenv

## 3. Django 설치
가상환경이 활성화된 상태에서 장고 설치
- pip install django

## 4. 필요한 패키지 설치
가상환경이 활성화된 상태에서 장고 설치
- pip install python-dotenv
- pip install django-debug-toolbar

