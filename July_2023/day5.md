# Topic5. Data pipeline
### 1. 데이터 처리 기초
- Data Lake, Data Warehouse, Data Mart 개념을 이해하고 정리하세요.
- Parquet, ORC, Avro 포맷을 각각 찾아 정리하세요.
- ETL 개념을 찾아 정리하세요.

### 2. 스트림 처리
- FluentBit/FluentD를 활용하여 로그 데이터를 Kinesis Stream에 전송해보세요.
- Kinesis Firehose를 통해 스트림 데이터를 Parquet 포맷으로 변환하여 S3에 저장해 보세요.
- Kinesis Analytics Studio를 통해 Zeppelin을 생성하고, SQL 문법을 활용한 Flink 어플리케이션을 생성해 보세요.

### 3. 배치 처리
- RDBMS에 저장된 데이터를 일괄적으로 S3에 저장해보세요.
- DynamoDB에 저장된 데이터를 일괄적으로 S3에 저장해보세요.
- 간단한 스크립트를 작성하여 로그 데이터를 1시간 간격으로 백업할 수 있도록 구성해 보세요.

### 4. Athena (Deep Dive)
- Ad-hoc Query에 대해 이해하고 정리하세요.
- Redshift와 같은 Data Warehouse에서 쿼리를 수행하는 것과 Athena 쿼리의 차이점을 분석하여 정리하세요.
- Partitioning 에 대해 이해하고 정리하세요.
- AWS Glue 기반 Athena 테이블을 생성해보세요.
- CTAS (Create Table As Select) 를 실습해보세요.

### 5. Glue (Deep Dive)
- 메타데이터에 대한 개념을 이해하고 정리하세요.
- Glue Catalog 를 수동으로 생성해보세요.
- Crawler를 활용하여 S3에 저장된 로그데이터를 기반으로 자동으로 Catalog 를 생성해 보세요.
- 수동으로 생성한 Catalog와 자동으로 생성한 Catalog를 서로 비교하여 정리하세요.
- Glue Studio를 사용하여 시각적으로 ETL 작업을 생성해보세요.
- Glue Studio로 생성한 ETL 작업의 pyspark 스크립트를 확인해 보세요. (정리X)
