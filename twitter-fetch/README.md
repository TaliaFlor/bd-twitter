# Twitter Fetch
Busca dados reais do twitter para popular o banco de dados

# Compilação
Para buscar novos dados do Twitter, deve-se fazer as seguintes configurações:

- [Obrigatório] `twitter-fetch/resources/credentials.json`: credenciais de acesso a API do Twitter. Elas podem ser obtidas [aqui](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).
- [Opcional] `twitter-fetch/resources/query.json`: query de busca dos twitters. Mais informações sobre como montar uma query [aqui](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query). 

Um modelo de retorno da API pode ser encontrado em `twitter-fetch/resources/examples/sample_response.json`. Os modelos de representação utililizados estão em `twitter-fetch/src/models`.

## Dependências

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)

- [twitter](https://pypi.org/project/twitter/)
- [Faker](https://pypi.org/project/Faker/)
