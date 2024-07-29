# mov

### intstall
```bash
# main
$ pip install git+https://github.com/minju210/movie.git

# branch
$ pip install git+https://github.com/minju210/movie.git@<BRANCH_NAME>
$ pip install git+https://github.com/minju210/movie.git@0.2/api
```

### start dev
```
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install
$ pytest

# option
$ pdm venv create
```
### setting env
```
cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<KEY>"
```

### 트러블슈팅
- [ ] 영화진흥위원회 가입 및 키생성
```
{'faultInfo': {'message': '유효하지않은 키값입니다.', 'errorCode': '320010'}}
```
