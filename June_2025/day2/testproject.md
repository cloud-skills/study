# day2 - Test Project

## Overview

- REST API를 제공하는 웹 어플리케이션을 서비스하기 위한 클라우드 솔루션을 설계하고 구축합니다.
- AWS Well Architected Framework 6 fillar를 참고하여 최적의 클라우드 솔루션을 제공합니다.
- 글로벌 리소스를 제외한 모든 리소스는 ap-northeast2 에 생성합니다.

## Description

### 1. VPC

- VPC CIDR: 10.0.0.0/16
- 아래 서브넷들을 각각 2개의 AZ를 가지도록 구성합니다.
    - Internet Gateway를 통해 통신하며 인터넷에서 직접 접근 가능한 Public subnet
    - NAT Gateway를 사용하는 Private subnet
    - 인터넷으로부터 격리된 Isolated subnet
- 아래의 S3와 DynamoDB 서비스에 AWS 내부 네트워크를 통해 접근하기 위한 VPC Endpoint를 생성합니다.

### 2. Database

- token 어플리케이션에서 사용하는 데이터를 효율적으로 저장하고 읽어오기 위해 RDBMS을 구축합니다.
    - MySQL 호환 엔진을 사용하고 Major Version은 8.0을 사용합니다.
    - 인스턴스 타입은 db.t3.medium 을 사용합니다.
    - 아래 명령어를 참고하여 과제에 필요한 테이블을 생성하세요.
        ```
        CREATE DATABASE dev;
        CREATE TABLE dev.token (
            id VARCHAR(255) PRIMARY KEY,
            token VARCHAR(255) NOT NULL
        );
        ```
- color 어플리케이션에서 사용하는 데이터를 효율적으로 저장하고 읽어오기 위해 DynamoDB를 구축합니다.
    - 테이블 이름은 `color`로 명명합니다.
    - WCU와 RCU를 각각 1로 설정합니다.

### 3. Application

- token application
    - Golang Gin 기반 RDB에 데이터 생성 및 조회하는 REST API를 제공하는 token 앱을 배포하고 서비스합니다.
    - 해당 어플리케이션은 평균적으로 40초의 응답 시간을 가집니다.
    - 해당 어플리케이션은 데이터의 생성을 제공하는 API만 존재 합니다.
    - 해당 어플리케이션은 생성하고자 하는 Token의 길이에 따라 CPU 연산량이 급증할 수 있습니다.
    - TCP/8080 포트로 사용자의 요청을 Listen 합니다.
    - API Spec
        | Path      | Verb  | Parameter              |
        | --------- | ----- | ---------------------- |
        | /v1/token | POST  | {"length":\<Integer\>} |
        | /health   | GET   | -                      |

- color application
    - Golang Gin 기반 DynamoDB에 데이터 생성 및 조회하는 REST API를 제공하는 color 앱을 배포하고 서비스합니다.
    - 데이터의 생성, 검색을 제공하는 API만 존재 합니다.
    - 해당 어플리케이션은 평균적으로 1초 미만의 응답 시간을 가집니다.
    - TCP/9090 포트로 사용자의 요청을 Listen 합니다.
    - API Spec
        | Path      | Verb  | Parameter            |
        | --------- | ----- | -------------------- |
        | /v1/color | GET   | ?id=\<String\>       |
        | /v1/color | POST  | {"color":\<String\>} |
        | /health   | GET   | -                    |


### 4. EC2 / AutoScalingGroup

- 어플리케이션을 배포하기 위한 컴퓨팅 리소스로 EC2를 사용합니다.
- EC2 인스턴스에서는 token, color 어플리케이션을 실행합니다.
- 트래픽 변화에 따라 자동으로 스케일링 될 수 있도록 Scaling Policy를 작성합니다.
- 인스턴스 타입은 `t3.micro`를 사용합니다.

### 5. Elastic Load Balancer

- 외부 사용자들이 분산 배포된 Application에 접근할 수 있도록 ALB를 구성합니다.
- CloudFront에서만 접근 가능하도록 보안을 구성합니다.
- 하나의 HTTP Listener 를 사용합니다.

### 6. S3

- 정적 컨텐츠를 제공하기 위해 Object Storage인 S3를 구성합니다.
- `wsc2025-s3-bucket-<4words>` 이름으로 버킷을 생성합니다.
- CloudFront에서만 접근 가능하도록 보안을 구성합니다.

### 7. CDN

- 사용자와 가까운 위치에서 캐시 데이터를 제공하기 위해 CloudFront를 구성합니다.
- 아래와 같이 경로에 따라 요청이 각각의 Origin 에 전달될 수 있도록 구성합니다.
    - /v1/* 경로로 접근 시 ALB로 라우팅되도록 합니다.
    - /images/* 경로로 접근 시 S3로 라우팅되도록 합니다.
