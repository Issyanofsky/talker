# <p align="center">**Summarize**</p>

connecting to Gemini API. and pull summarize text with some instruction.

it relay on a secret made in k8s with the API_KEY in order to work.

    kubectl create secret generic my-secret \
      --from-literal=api_key=<your-api-key> \
      --from-literal=other_key=<your-other-key>


