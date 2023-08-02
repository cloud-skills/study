# Topic4. CI/CD
### 1. CI/CD 기초 개념
- CI, CD 의 각 개념을 이해하고 정리하세요.

### 2. SCM 기초
- SCM(Software Configuration Management) 개념을 찾아 정리하세요.
- Git 기초적인 개념을 이해하고, 명령어를 숙지하세요. (https://git-scm.com/book/ko/v2)
- 개발 환경에 대해 정리하세요. (dev 환경, staging 환경, production 환경 등)
- 개발 환경과 연관지어 Git Branch 전략을 이해하고 정리하세요.

### 3. 빌드 및 테스트
- Golang/Gin으로 간단한 웹 어플리케이션을 개발하고 CodeBuild를 통한 빌드를 실습해보세요.
- AMI 이미지 빌드, 컨테이너 이미지 빌드를 각각 실습하여보세요.
- 간단한 Unit Test를 작성하고 CodeBuild의 Report를 생성해보세요.

### 4. 무중단 배포
- Rolling Update 개념을 찾아 정리하세요.
- 3가지 배포 전략(In-place, Blue/Green, Canary)을 이해하고 각각의 장/단점, 활용방안을 분석하여 정리하세요.
- 3가지 컴퓨팅 타입 별로 무중단 배포를 실습해보세요.
  EC2 - In-place, Blue/Green, Canary
  ECS - In-place, Blue/Green, Canary
  EKS - In-place, Blue/Green, Canary

### 5. CI/CD 파이프라인
- CodeCommit, CodeBuild, CodeDeploy, CodePipeline을 활용하여 CI/CD 파이프라인을 구축해보세요.
- main 브랜치에 새로운 Commit이 발생하면 자동으로 빌드, 배포 될 수 있도록 트리거를 구성해보세요.
