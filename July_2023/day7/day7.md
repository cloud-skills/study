# day7 - Test Project
## Overview
- 클라우드 환경에서 효율적인 데이터 분석을 위한 데이터 파이프라인을 구축합니다.
- 데이터 전처리, 파티셔닝 등 효율적인 데이터 분석을 위한 기법을 이해합니다.
- 모든 시간은 UTC+9 (KST) 타임존을 사용합니다.

## Description
### 1. VPC
- Network CIDR: 10.0.0.0/16
- Subnets: 단순한 개발/테스트 용으로 생산하며 가용성을 고려할 필요가 없습니다. 하나의 AZ에 서브넷을 생성합니다.
  - Public Subnet (Connected Internet Gateway)
  - Application Subnet (Conntected Nat Gateway)

### 2. Application
- 접근 로그를 생성하기 위한 Python/Flask 기반의 임시 REST API 어플리케이션입니다.
- 해당 어플리케이션은 flask 패키지 모듈에 의존성을 가집니다.
- 어플리케이션을 실행하기 위한 EC2 인스턴스를 하나 생성하고 실행합니다.
- 접근 로그는 어플리케이션을 실행한 위치에 app.log 이름의 파일에 저장됩니다.
- INFO 레벨의 로그를 전부 기록합니다.

### 3. Stream 데이터 수집
- FluentBit 를 활용해 접근 로그를 Cloudwatch logs에 저장합니다.
  - log group: wsi/app/accesslog
  - stream: ec2_<instance-id>
- FluentBit 를 활용해 접근 로그를 Kinesis에 전송합니다.
  - Stream Name: wsi-log

### 4. Stream 데이터 전처리 및 적재
- Kinesis Firehose 를 활용하여 Stream 데이터를 S3에 적재합니다.
- Ad-Hoc Query 를 참고하여 효율적인 데이터 분석을 수행할 수 있도록 파티셔닝을 수행하세요.
- 이벤트가 발생한 시점(접근 로그에 기록된 시간)을 기준으로 파티셔닝을 수행하세요.
- 효율적인 쿼리를 위해 Parquet 포맷으로 저장합니다.

### 5. Ad-Hoc Query
- S3 에 저장된 접근 로그를 기반으로 임시 쿼리를 작성하고 실행합니다.
  - 오늘 하루 발생한 요청량을 분석합니다.
  - 오늘 하루 시간대별로 발생한 요청량을 분석합니다.

### 6. Stream 데이터 실시간 분석
- Kinesis Analayitcs 를 사용하여 스트림 데이터에 대한 실시간 분석을 수행합니다.
- Kinesis Analytics Studio 를 활용하여 Zepplin NoteBook을 생성하고 Flink 어플리케이션을 작성합니다.
- SQL 문법을 활용하여 어플리케이션을 작성하며, 어플리켄이션에서는 다음과 같은 실시간 분석을 수행합니다.
  - 최근 10분 동안의 요청량을 분석합니다. (1 cell)
  - 최근 10분 동안 경로/메소드/상태코드 별 카운트를 분석합니다. (1 cell)

### 7. ETL, Data Warehouse
- 데이터 웨어하우징을 위한 Redshift Cluster 를 생성합니다.
- S3에 저장된 원본 데이터를 Redshift Cluster 에 적재하는 Glue ETL 작업을 생성합니다.
  - Glue Studio 를 사용하여 시각화된 ETL 작업을 생성합니다.
  - 데이터 분석에 사용하지 않는 필드는 삭제합니다.
  - 접근 로그의 시간(Timestamp)를 분석에 용이한 형태로 변환하여 저장합니다.
  - 접근 로그의 각 필드값을 적절한 자료형으로 변환합니다.
- 데이터 웨어하우스에 저장된 데이터에 대한 분석을 수행합니다.
  - 일자/시간대별 요청량을 분석합니다.
  - 일자/시간대별 에러 발생량에 대해서 분석합니다.