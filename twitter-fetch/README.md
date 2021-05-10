# Twitter Fetch

Busca dados reais do twitter para popular o banco de dados

# Compilação

Para buscar novos dados do Twitter, deve-se fazer as seguintes configurações no
arquivo `twitter-fetch/resources/config.json`:

- [Obrigatório] `twitter`: credenciais de acesso a API do Twitter. Elas podem ser
  obtidas [aqui](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).
- [Opcional] `application > query`: query de busca dos twitters. Mais informações sobre como montar uma
  query [aqui](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query).

Um modelo de retorno da API pode ser encontrado em `twitter-fetch/resources/examples/sample_response.json`.

## Dependências

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
  <br/><br/>
- [tweepy](https://docs.tweepy.org/en/latest/)
- [Faker](https://faker.readthedocs.io/en/master/index.html)
