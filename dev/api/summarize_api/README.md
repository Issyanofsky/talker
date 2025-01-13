# <p align="center">**Summarize**</p>

connecting to Gemini API. and pull summarize text with some instruction.

it relay on a secret made in k8s with the API_KEY in order to work.

    kubectl create secret generic summarize-secret \
      --from-literal=api_key="HkLK32HK54KAKAJJA3KJhhha7HH9lA8" \
      --namespace=talker-dev


