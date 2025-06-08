# day4 - Test Project

## Overview

- REST API를 제공하는 웹 어플리케이션을 서비스하기 위한 클라우드 솔루션을 설계하고 구축합니다.
- 서비스를 제공하는 시스템 운영을 위한 모니터링 시스템을 구축합니다.
- AWS Well Architected Framework 6 fillar를 참고하여 최적의 클라우드 솔루션을 제공합니다.
- 글로벌 리소스를 제외한 모든 리소스는 ap-northeast2 에 생성합니다.
- 경기 시작 2시간 이후에 설정한 엔드포인트로 트래픽이 주입됩니다.
- 컴퓨팅 타입은 EC2 인스턴스만 사용하도록합니다. 어떠한 목적으로든 Fargate와 Lambda를 사용할 수 없습니다.
- 불필요한 리소스를 생성하는 경우, 비용이 발생하는 리소스가 아니더라도 감점의 요인이 될 수 있습니다.

## Description

### 1. Database

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
    - 저장되는 데이터의 형태는 다음과 같습니다.
        | key     | type   | description            |
        | ------- | ------ | ---------------------- |
        | id      | String | Primary key            |
        | color   | String | -                      |
    - 정상적인 동작을 위해 `color` 테이블에 아래 범위의 id 값을 가지는 데이터를 수동으로 생성합니다.
        - bee6ed6c-bbf3-4be0-99dd-000000000001  
          bee6ed6c-bbf3-4be0-99dd-000000000002  
          bee6ed6c-bbf3-4be0-99dd-000000000003  
          ... (생략) ...  
          bee6ed6c-bbf3-4be0-99dd-000000100000  
        - 수동으로 생성하는 모든 데이터의 color 값은 "Black"을 가지도록 하며 총 100,000 개의 데이터가 생성되어야 합니다.
        
        

### 2. Application

- token application
    - Golang Gin 기반 RDB에 데이터 생성 및 조회하는 REST API를 제공하는 token 앱을 배포하고 서비스합니다.
    - 해당 어플리케이션은 데이터의 생성을 제공하는 API만 존재 합니다.
    - 해당 어플리케이션은 생성하고자 하는 Token의 길이에 따라 CPU 연산량이 급증할 수 있습니다.
    - 최소한의 가용성을 위해 5초 이하의 응답시간을 보장하고자 하며, 3.5초 이하의 응답시간을 서비스 수준 목표로 설정하였습니다.
    - 변조 방지를 위해 Request 요청에 requestid, uuid 쿼리스트링/요청본문이 추가됩니다.
    - TCP/8080 포트로 사용자의 요청을 Listen 합니다.
    - API Spec
        | Path      | Verb  | Parameter              |
        | --------- | ----- | ---------------------- |
        | /v1/token | POST  | {"id":\<String\>,"length":\<Integer\>,"requestid":\<String\>,"uuid":\<String\>} |
        | /health   | GET   | -                      |

- color application
    - Golang Gin 기반 DynamoDB에 데이터 생성 및 조회하는 REST API를 제공하는 color 앱을 배포하고 서비스합니다.
    - 해당 어플리케이션은 데이터의 생성, 검색을 제공하는 API만 존재 합니다.
    - 최소한의 가용성을 위해 5초 이하의 응답시간을 보장하고자 하며, 0.5초 이하의 응답시간을 서비스 수준 목표로 설정하였습니다.
    - 변조 방지를 위해 Request 요청에 requestid, uuid 쿼리스트링/요청본문이 추가됩니다.
    - TCP/9090 포트로 사용자의 요청을 Listen 합니다.
    - API Spec
        | Path      | Verb  | Parameter            |
        | --------- | ----- | -------------------- |
        | /v1/color | GET   | ?id=\<String\>&requestid=\<String\>&uuid=\<String\>           |
        | /v1/color | POST  | {"color":\<String\>,"requestid":\<String\>,"uuid":\<String\>} |
        | /health   | GET   | -                    |


### 3. Traffic Handling

- 어플리케이션을 배포하고 외부 사용자들에게 서비스를 제공할 수 있도록 시스템을 구축합니다.
- 컴퓨팅 리소스는 EC2를 사용하며 인스턴스 타입은 t3.medium을 사용합니다. 다른 인스턴스 타입을 사용하는 경우 
- 어플리케이션을 배포하기 위한 컴퓨팅 리소스로 EC2를 사용합니다.
- 트래픽 처리를 위해 사용자에게 제공되는 엔드포인트를 하나로 단일화합니다.
- 경기 시작 1시간 뒤부터 트래픽이 발생하며 채점 플랫폼에 입력한 엔드포인트로 트래픽이 주입됩니다.
- 경기 중 발생하는 트래픽을 목표 서비스 수준에 만족하도록 처리하세요.
- 모니터링 환경과 로깅 솔루션을 구축하여 로그 분석, 트래픽 패턴 분석, 시스템 장애/오류 감지 및 대처를 수행해야 합니다.
- 본인의 엔드포인트를 타인에게 노출하여 불이익을 받는 일이 없도록 합니다.
- 채점 플래폼에 입력하는 형식은 프로토콜 및 주소(IP/DNS)이며 경로를 적어선 안됩니다.
    - 정상 예시: `https://example.org`
    - 잘못된 예시(프로토콜 누락): `example.org`
    - 잘못된 예시(경로 추가기입): `https://example.org/v1/color`
- 서비스 중단 없이 안정적으로 서비스를 제공할 수 있도록 가용성을 확보합니다.
- 사용자에게 제공하는 엔드포인트로의 비정상적인 요청은 Block하도록 하며 403 응답코드를 내려주도록 합니다.
- 단 제공하는 API외의 요청은 404응답코드를 내려주도록 합니다.
