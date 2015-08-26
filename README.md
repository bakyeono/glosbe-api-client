glosbe-api-client
=================

문서 원본: http://bakyeono.net/post/2015-08-27-glosbe-api-client.html

## 다국어 사전 Glosbe API

Glosbe는 다국어 온라인 사전이다. 사용자들이 직접 데이터베이스를 보완해 만드는 사전이며 무료다. 아쉽게도 사전의 질은 상용 사전만큼 좋지는 못한 듯하다.

Glosbe는 무료로 웹 API도 제공하기 때문에 다국어 사전이 필요한 경우 이용할 수 있다.

* Glosbe: [https://glosbe.com](https://glosbe.com)
* Glosbe API 페이지: [https://glosbe.com/a-api](https://glosbe.com/a-api)

## Glosbe API 사용하기

Glosbe API 를 사용하려면 다음과 같이 요청을 보내면 된다.

    https://glosbe.com/gapi/translate?from=eng&dest=kor&format=json&pretty=true&phrase=phrase

요청을 보낼 프로토콜과 주소는 `https://glosbe.com/gapi/translate` 이다.

위 예에서 쓰인 매개변수는 다음과 같다.

* `from`: 번역해야 할 단어의 언어 (ISO 693-3 코드)
* `dest`: ~으로 번역되어야 할 언어 (ISO 693-3 코드)
* `format`: 응답 받은 데이터의 유형 (JSON 또는 XML)
* `pretty`: 응답을 사람이 보기 좋게 출력할 것인지 여부 (Boolean)
* `phrase`: 번역해야 할 단어 (대소문자 구분)

언어를 지정할 때는 ISO 693-3 코드로 지정해야 한다. [ISO 693-3 코드 문서](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes)에서 해당 언어를 찾아보면 된다.

문제는 응답인데 사전에 실린 여러 개의 번역어가 모두 담겨서 오기 때문에 처리하기 약간 복잡할 수 있다. (직접 뜯어보길 바라며, 자세한 설명은 생략한다.)

파이썬 사용자는 바로 아래에 내가 짠 스크립트가 있으니 이걸 사용하면 요청과 응답 모두 해결할 수 있다.

## glosbe-api-client

내가 Glosbe API 사용을 위해 만든 파이썬 스크립트다. 아래 주소에서 다운로드하거나 클론하면 된다.

GitHub: [https://github.com/bakyeono/glosbe-api-client](https://github.com/bakyeono/glosbe-api-client)

### 사용법

사용법은 아래와 같다.

    $ python glosbe.py 원래언어 목적언어 번역어

즉, 한->영 사전으로 '딸기'를 검색하고 싶다면 아래와 같이 실행한다.

    $ python glosbe.py kor eng 딸기
    딸기
    ========
    strawberry
    berry
    strawberries

