# Dashboards de Expedição — NDI

App Streamlit que hospeda os dois dashboards estáticos (HTML + Chart.js) em um único
lugar, com um seletor na barra lateral para trocar entre eles. Cada dashboard continua
funcionando exatamente como antes (leitura direto do Google Sheets, histórico de meses
sincronizado com a aba `HistoricoDash` via Apps Script).

```
ndi-dashboards/
├── app.py                       # app Streamlit (lê e embute os HTMLs)
├── requirements.txt
├── .streamlit/config.toml
└── dashboards/
    ├── dashprincipal.html       # Resultado Operacional
    └── dashcomparativo.html     # Comparativo 2025 x 2026
```

## 1. Subir para o GitHub

Crie um repositório novo (vazio, sem README) em https://github.com/new — por exemplo
`ndi-dashboards`. Depois, dentro desta pasta:

```bash
git init
git add .
git commit -m "Dashboards de expedição via Streamlit"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/ndi-dashboards.git
git push -u origin main
```

Troque `SEU-USUARIO` pelo seu usuário/organização do GitHub.

## 2. Publicar no Streamlit Community Cloud

1. Acesse https://share.streamlit.io e entre com sua conta do GitHub.
2. Clique em **New app**.
3. Selecione o repositório `ndi-dashboards`, branch `main` e o arquivo principal `app.py`.
4. Clique em **Deploy**. Em ~1 minuto o app estará no ar em uma URL do tipo
   `https://ndi-dashboards.streamlit.app` (o Streamlit escolhe o subdomínio, você pode
   ajustar no painel do app depois).

## 3. Corrigir o link cruzado entre os dois dashboards

Cada dashboard tem um botão que leva para o outro. Como agora os dois vivem no mesmo
app, esses botões apontam para `__APP_URL__/?dash=...` como placeholder. Depois do
deploy, troque `__APP_URL__` pela URL real do seu app (ex: `https://ndi-dashboards.streamlit.app`)
nos dois arquivos dentro de `dashboards/`:

```bash
sed -i 's#__APP_URL__#https://ndi-dashboards.streamlit.app#' dashboards/dashprincipal.html dashboards/dashcomparativo.html
git add dashboards
git commit -m "Ajusta links cruzados para a URL final do app"
git push
```

O Streamlit Cloud reimplanta automaticamente a cada push na branch `main`.

## Observações

- O app.py só lê os arquivos HTML e os exibe dentro de um iframe (`st.components.v1.html`),
  então JS, Chart.js, localStorage e a sincronização via Apps Script continuam funcionando
  normalmente — quem acessa o app vê o dashboard exatamente como no navegador local.
- O plano gratuito do Streamlit Community Cloud "dorme" o app depois de um tempo sem uso;
  o primeiro acesso do dia pode levar alguns segundos extra para acordar.
- Se preferir algo mais leve/instantâneo (sem essa "soneca"), hospedar os HTMLs direto no
  GitHub Pages também funciona bem para esse tipo de dashboard estático — mas como você
  pediu Streamlit, ficou assim, para manter o padrão dos seus outros projetos.
