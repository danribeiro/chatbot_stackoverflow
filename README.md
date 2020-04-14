# chatbot_stackoverflow
Stackoverflow chabot api

### Instalação de dependências

Para criar a virtualenv

`$ virtualenv -p python3 venv`

Após realizar o clone do repositório

`$ source venv/bin/activate`

`$ pip install -r chatbot_stackoverflow/requirements.txt`

### Parte 1

Como resolução da parte 1 do test

`$ python main.py <key_word1> <key_word2> <key_word3> ...`

### Parte 2 

Como resolução da parte 2 do test

`$ python chatbot_stackoverflow/src/core.py`

Com o [telegram](http://t.me/danrs_bot) aberto , comando `/start` para inicializar o chabot. 

Para realizar a pesquisa digitar `<key_word1> <key_word2> <key_word3>`


### Parte 3 (tests)

Pequeno cenário de teste foi implementado para cobrir a funcionalidade utilizando BDD(Behavior Driven Development) fazendo uso adaptado do exemplo presente no [link](https://github.com/mmdaz/feature_testing_chat_bots).

A biblioteca utilizada para criar os cenários é a [behave](https://behave.readthedocs.io/en/latest/tutorial.html). 

Para criar os links simbólicos:

`$ cd src`
`ln -s core.py tests/core.py`
`ln -s utils.py tests/utils.py`

Após criados os links pode-se executar o cenário de teste, para isso é necessário rodar o bot, em seguida executar na linha de comando:

`$ cd chatbot_stackoverflow/src/tests`
`$ behave`


Output:

> Feature: call stackoverflow api for questions  by tags 
  Scenario: enter tags for search        
    Given a bot and update from server   # steps/test.py:7 0.008s
    When user send /search django python # steps/test.py:17 0.828s
    Then return question list            # steps/test.py:24 0.627s
1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m1.463s



