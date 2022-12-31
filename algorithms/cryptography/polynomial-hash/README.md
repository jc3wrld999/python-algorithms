## Polynomial Hash

### 해시함수
해시 함수는 임의 크기의 모든 종류의 데이터를 고정 크기 값으로 매핑하는 함수이다. 해시 함수는 두 문자열이 같으면 해시 값도 같아야 한다. 그러나 그 반대가 참일 필요는 없습니다. 함수가 반환하는 값을 해시 값 또는 다이제스트라고 한다. DJBX33A, MD5 및 SHA-256과 같은 인기 있는 해시 함수가 많이 있다.

### Polynomial Hash
다항 롤링 해시 함수는 곱셈과 덧셈만 사용하는 해시 함수이다. 

![image](https://user-images.githubusercontent.com/61821641/210150330-20eb41a7-2acb-47ec-b52d-fac6408e9a31.png)

![image](https://user-images.githubusercontent.com/61821641/210150336-379d738b-dd9c-4dc4-b15a-ada73762ca1a.png)

### Collisions

해시 함수의 출력은 정수 범위이므로 두 문자열이 동일한 해시 값을 생성할 가능성이 높다.

## Reference
- [다항 롤링 해시 함수를 사용한 문자열 해싱](https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/)