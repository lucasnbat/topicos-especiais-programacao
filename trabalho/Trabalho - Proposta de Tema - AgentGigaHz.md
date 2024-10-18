# 🚀 Proposta de Tema para Trabalho de Tópicos Especiais em Programação 🚀

## 📝 Informações Básicas

- **Nome dos Alunos:** Lucas Nunes Batista, Winy Zanin.

## 🎯 Tema Proposto

### 📌 Título do Projeto

* ChatBot para atendimento de clientes de assistência técnica em Sinop MT - GigaHz.

### 📌 Descrição do Projeto

* Atualmente o proprietário não possui uma automação que:
  
  * Faça a recepção geral dos clientes no WhatsApp;
  
  * Exponha os serviços disponíveis com seus valores padrão;
  
  * Agende horários de atendimento;
  
  * Disponha de formas de aviso ao proprietário sobre os agendamentos (webhooks ou crons para alerta de horários dos atendimentos).

* Todos os processos são feitos manualmente, demandando tempo que poderia ser utilizado para decisões de negócio de alto nível (estratégico e tático).

### 📌 Objetivos

* Fornecer uma automação que:
  
  * Faça a recepção geral do cliente da assistência técnica;
  
  * Exponha os serviços disponíveis e seus valores assim que solicitado;
  
  * Agende horários de atendimento;
  
  * Comunique com uma ferramenta de calendário para organização do proprietário;
  
  * Forneça meios de avisar o proprietário sobre os atendimentos previstos em um dia.

### 📌 Ferramentas e Tecnologias Sugeridas

* Ferramentas pássiveis de uso:
  
  * Dify - Agente de Conhecimento;
  
  * EvolutionAPI;
  
  * N8N;
  
  * Cal.com;
  
  * Agenda Google;
  
  * APIs de IA (Groq ou Gemini).

### 📌 Funcionalidades Principais

* As funcionalidades inicialmente englobam:
  
  * Conjunto de mensagens de recepção do cliente;
  
  * Identificação de mensagens de voz;
  
  * Listagem de serviços disponíveis junto ao valor padrão destes;
    
    * Fluxos que identifiquem cada serviço conforme complexidade para identificar quando seguir com o atendimento e quando conduzir para que um humano prossiga com o atendimento;
  
  * Funcionalidade de agendamento com chamada à API da Cal.com para:
    
    * Expor horários disponíveis;
    
    * Agendar efetivamente o atendimento.
  
  * Webhook no N8N para aviso de atendimentos agendados para um determinado período de tempo.

### 📌 Atividades por Membro da Equipe

* Lucas Batista:
  
  * Análise de requisitos do projeto;
  
  * Estruturação e treinamento do modelo;
  
  * Configuração da conexão com a API (Groq, Gemini);
  
  * Configuração de conexão com API Cal.com;
  
  * Configuração de serviço de disparo de avisos com N8N;

* Winy Zanin:
  
  * Análise de requisitos do projeto;
  
  * Estruturação e treinamento do modelo;
  
  * Setup, integração, deploy e administração do EvolutionAPI;
  
  * Configuração de serviço de disparo de avisos com N8N;

### 📌 Cronograma Preliminar

[Proponha um cronograma preliminar para o desenvolvimento do projeto. Use uma tabela para listar as principais etapas e prazos.]

| **Etapa** | **Descrição**                                                        | **Prazo**  | **Responsáveis**          |
| --------- | -------------------------------------------------------------------- | ---------- | ------------------------- |
| 1         | Análise de requisitos do projeto                                     | 12/10/2024 | Lucas Batista, Winy Zanin |
| 2         | Estruturação e treinamento do modelo (IA para recepção e orçamentos) | 19/10/2024 | Lucas Batista, Winy Zanin |
| 3         | Configuração da conexão com a API Groq/GPT                           | 26/10/2024 | Lucas Batista             |
| 4         | Configuração de conexão com API Cal.com                              | 26/10/2024 | Lucas Batista             |
| 5         | Setup, integração e deploy do EvolutionAPI                           | 28/10/2024 | Winy Zanin                |
| 6         | Configuração de serviço de disparo de avisos com N8N                 | 07/11/2024 | Lucas Batista, Winy Zanin |
| 7         | Testes de funcionalidade e integração                                | 16/11/2024 | Lucas Batista, Winy Zanin |
| 8         | Ajustes e otimizações finais                                         | 23/11/2024 | Lucas Batista, Winy Zanin |
| 9         | Entrega final                                                        | 28/11/2024 | Lucas Batista, Winy Zanin |

### 📌 Referências

[Liste as principais referências que vocês utilizarão para desenvolver o projeto. Isso pode incluir artigos, documentações de APIs, tutoriais, etc.]

- Documentação EvolutionAPI - documentação oficial da ferramenta EvolutionAPI disponível em: [Introdução - Evolution API Documentation](https://doc.evolution-api.com/v2/pt/get-started/introduction)
- Documentação N8N - documentação oficial da ferramenta N8N disponível em: https://docs.n8n.io/
- Documentação Cal - documentação oficial da ferramenta Cal disponível em: [Introduction - Cal.com Docs](https://cal.com/docs/developing/introduction)
- Documentação Dify - documentação oficial da ferramenta Dify disponível em: https://docs.dify.ai/
- Documentação Groq - documentação oficial da ferramenta Groq disponível em: [GroqCloud](https://console.groq.com/docs/libraries?_gl=1*1ew13y7*_gcl_au*NTc0MDY4NjY3LjE3MjY3OTA2NDY.*_ga*MTY4MDgxMjAyMy4xNzI2NzkwNjQ1*_ga_4TD0X2GEZG*MTcyODY2NTQ3Ni4yLjEuMTcyODY2NTUxNi4yMC4wLjA.)
- Documentação Gemini - documentação oficial da ferramenta Gemini AI disponível em: [Documentos do desenvolvedor da API Gemini e referência da API &nbsp;|&nbsp; Gemini API &nbsp;|&nbsp; Google AI for Developers](https://ai.google.dev/gemini-api/docs?_gl=1*1sbefno*_ga*OTI0MjQxODE3LjE3MjczOTQzMzg.*_ga_P1DBVKWT6V*MTcyODY2NTY2Ni41LjAuMTcyODY2NTY3MS41NS4wLjQzODIwNzIwMw..&hl=pt-br)

## 📬 Envio da Proposta

Enviar através do SIGAA, na Tarefa correspondente. Caso tenha dúvidas, encaminhe via whatsapp professor antes de submeter a tarefa.

---

**Observação:** Certifique-se de que a proposta esteja clara, detalhada e coerente com os objetivos do trabalho de Tópicos Especiais em Programação. A equipe avaliará a viabilidade e a relevância do tema proposto.
