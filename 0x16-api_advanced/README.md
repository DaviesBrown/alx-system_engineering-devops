API-advanced
curl -X GET "https://api.datadoghq.com/api/v1/dashboard/lists/manual" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${d3c1293fc26640d2a39c956f04e4ad96}" \
-H "DD-APPLICATION-KEY: ${b189b9fa978a94486a118557257d5c1ef8b941b1}"
DD_SITE="datadoghq.com" DD_API_KEY="d3c1293fc26640d2a39c956f04e4ad96" DD_APP_KEY="b189b9fa978a94486a118557257d5c1ef8b941b1" python3 "example.py"
curl -X GET "https://api.datadoghq.com/api/v1/dashboard" -H "DD-API-KEY: 248835cf341d270a7c1a2723c42f9b7e"
d3c1293fc26640d2a39c956f04e4ad96