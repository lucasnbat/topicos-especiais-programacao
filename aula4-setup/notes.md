# Engenharia de prompt

* É mais uma arte, pois não tem meios exatos de fazer isso;

* Você trabalha refinando textos para ajustar o comportamento de uma IA conforme você quer;

* Fatores:
  
  * Tokens gerados por resposta;
    
    * GPT --> 4096 (4 caracteres) = 1 token;
  
  * Temperatura: o quanto ele alucina e inventa resposta;

* Técnicas:
  
  * **Zero Shot:**"O céu é" --> Você não dá contexto, perguntando o que você quer, só tá buscando a resposta crua;
  
  * **Few shot:**
  
  * Não coloque o que ele não deve fazer;
    
    * Isso  pode fazer imprecisões;
  
  * Use estruturas como XML e JSON
    
    * <example></example>
    
    * <description></description>

## Anotações a partir do documento `Aula4.md` do professor

- Engenharia de Prompts é uma área que busca planejar, testar e refinar as instruções textuais dadas a LLMs visando o retorno de respostas úteis;
  
  - Envolve, inclusive, princípios de clareza, neutralidade e imparcialidade;

- Técnicas de prompt:
  
  - Zero-shot prompting: buscar resposta sem fornecer demonstração/exemplo anterior para o modelo;
  - Few shotting: fornecer poucos exemplos antes para modelar a resposta (ex: prompts de frases que demonstram um sentimento e classificar elas como positivas ou negativas). Também é conhecida como técnica de Cadeia de Pensamento (ex. do raciocínio do médico);
  - **Zeros-shot Chain of Thought**: basicamente o zero-shot com "vamos pensar passo a passo" antes das instruções;
  - Self-consistency: auto consistencia, basicamente dar o mesmo input em janelas de navegador diferentes, ou em diferentes chamadas de API, de forma que a resposta mais recorrente é a que será adotada;
  - Chain-of-verification: cadeia de verificação, pedir para responder a pergunta concisamente e depois pedir para fazer uma série de perguntas e respostas para verificar a veracidade da resposta original, podendo inclusive refazer a resposta inicial;
  - Bloco:
    - **Definição de personalidade**;
    - **Fornecer contexto**;
    - **Usar delimitadores** (<texto1></texto1>);
    - **Fornecer objetivo**;
    - **Definir escalas** (complexidade de texto, tonalidade da resposta, etc)
    - **Fornecer formato da resposta**;
    - **Utilização de recompensas e punições**
    - Forneça exemplos;
    - Refinamentos;
    - 

- Elementos do prompt (recomendações gerais: comece de forma simples, escreva em inglês):
  
  - Contexto: info. adicionais;
  - Dados de entrada: pergunta feita;
  - Instrução: o que você quer que o modelo execute;
    - Recomendação: inserir no início;
    - Recomendação: não dizer "o que não fazer";
  - Indicador de saída: formato pelo qual você quer que o prompt saia;

- Exemplo de prompt específico x prompt genérico:

```d
  Use 2 a 3 frases para explicar o conceito de engenharia de prompt a um aluno do ensino médio.
```

```d
  Explique o conceito de engenharia de prompt. Mantenha a explicação curta, apenas algumas frases, e não seja muito descritivo.
```

* Ideias de uso:
  * Perguntas/respostas;
  * Classificador de texto;
  * Chat (dar identidade, função para o modelo);

# Exercícios

## Questão 1.

Prompt sem contexto: 

```d
Escreva uma carta de recomendação.
```

Resposta:

```d
Aquível, [Endereço do destinatário]
Datas de entrega: [Data esperada para entrega da carta]

Dra. [Nome completo do recomendado], [.ometown], [.state/Country]

Objetivo: Recomendação da Dra. [Nome completo do recomendado] para [.nome do cargo/position] na [.nome da empresa/instituição]

Caro(a) [Nome do destinatário],

Eu, [Seu nome], gostaria de recomendar calorosamente a Dra. [Nome completo do recomendado] para o [.nome do cargo/position] na [.nome da empresa/instituição]. Eu tenho a honra de trabalhar com a Dra. [Nome completo do recomendado] em [.nome da empresa/instituição] nos últimos [.quantidade de tempo] anos, onde ela ocupou a posição de [.nome da posição] antes de [motivo da mudança].

Durante seu tempo comigo, Dra. [Nome completo do recomendado] demonstrou um nível impressionante de profissionalismo, habilidade e dedicação. Ela é uma pessoa extremamente talentosa e competente no campo de [.campo específico da profissão], com uma capacidade única de liderar e motivar equipes.

No meu trabalho com Dra. [Nome completo do recomendado], eu tenho observado a maneira como ela pode resolver problemas complexos, comunicar-se de forma eficaz e construir relações positivas com colegas e clientes. Ela é uma pessoa visionária, sempre procurando por novas oportunidades e melhorias.

Eu acredito que Dra. [Nome completo do recomendado] seria um valoroso membro da equipe da [.nome da empresa/instituição] e que ela estaríamos felizes em ter ela ao lado do nossa equipe. Se você tiver alguma dúvida adicional, por favor, não hesite em contatar-me.

Atenciosamente,

[Seu nome]
[Título professionnel]
[Seu endereço]
[Seu telefone]
[Seu e-mail]

Nota: É importante adaptar a carta à natureza do recomendado, ao cargo e à instituição para a qual ele está se candidatando. Certifique-se de que seja sincero e objetivo ao escrever sua carta de recomendação.
```

Prompt com contexto:

```d
Escreva uma carta de recomendação cujo destinatário seja o supervisor atual de TI da cooperativa COAP, Robison Steven. Meu objetivo é recomendar o aluno Lucas Nunes Batista para o cargo de Analista de TI. Meu nome é Roberto Steffan.
```

```d
[Seu nome]
[Seu título]
[Data]

Jonathan Steven
Supervisor de TI
COAP

Respeitado Sr. Jonathan Steven,

Tenho o prazer de escrever essa carta para recomendar o aluno mais notável que tenho o prazer de ter como aluno, o Sr. Marcos Nunes Batista, para o cargo de Analista de TI na COAP. Como professor da disciplina de Arquitetura de Computadores na Universidade [seu nome da instituição], eu tive a oportunidade de observar e guiar o Sr. Marcos durante o semestre e, constantemente, me surpreendi com sua habilidade, sua dedicação e seu conhecimento em assuntos relacionados à computação.

Durante o curso, o Sr. Marcos demonstrou uma compreensão inquebrável e uma habilidade apurada em conceitos complexos de arquitetura de computadores, demonstrando capacidade de absorção e retenção rápida. Além disso, ele se destacou por sua criatividade, sua capacidade de trabalho em equipe e sua habilidade para aplicar conceitos teóricos em problemas práticos.

Seu desempenho em exercícios e provas foi sempre excepcional, e suas apresentações em sala de aula foram sempre bien preparadas e ricas em conteúdo. Além disso, ele sempre esteve disponível para ajudar colegas de classe e sempre procurou por formas de melhorar seu entendimento e aprimorar suas habilidades.

Acredito que o Sr. Marcos tem todas as habilidades necessárias e competências necessárias para desempenhar seu papel como Analista de TI na COAP. Ele é um profissional altamente qualificado, capaz de resolver problemas complexos e de trabalhar em equipe para alcançar objetivos comuns.

Portanto, sem hesitar, estou disposto a recomendar o Sr. Marcos Nunes Batista para o cargo de Analista de TI na COAP. Se houver alguma necessidade adicional de informações ou se precisar verificar minhas declarações, estou apto a fornecer mais detalhes.

Agradeço sua atenção e espero que você considere a minha recommendation.

Atenciosamente,

Roberto Borges
Professor de Arquitetura de Computadores
Universidade [seu nome da instituição]
```

Conclusão: o contexto fornecido auxiliou na construção de uma resposta que não só incluiu os nomes simples fornecidos, mas também teceu observações como o desempenho do aluno em provas e testes durante o semestre como forma de aumentar o valor percebido na recomendação.

## Questão 2.

Prompt 1 com persona:

```d
Você é um assistente inteligente que possui conhecimento sobre todos os livros escritos conhecidos atualmente. Não só as histórias e assuntos gerais, mas também suas meta-informações como autor, contexto histórico, escola literária, estilo de escrita e detalhes de como a obra foi construída. Você trabalha para atender os clientes que vão até o site de uma livraria, e, inclusive, entende todos os detalhes comerciais e de estoque dos livros disponíveis.
Agora, vamos pensar passo a passo.

Cada pessoa irá chegar no site e te direcionar uma pergunta. Responda de forma sucinta, e forneça detalhes apenas quando solicitado.

Pessoa: me recomende 2 bons livros de romance policial.
Você: Dois ótimos livros de romance policial são: O caso dos dez negrinhos e Os Crimes ABC.
Pessoa: Quero saber mais sobre eles e porquê você recomenda.
Você: 
*"O Caso dos Dez Negrinhos"* e *"Os Crimes ABC"* são excelentes romances policiais por:

1. **Tramas complexas**: Ambos os livros apresentam mistérios bem elaborados, mantendo o leitor intrigado do começo ao fim.
2. **Suspense psicológico**: A tensão crescente e o clima de incerteza permeiam as histórias, criando um suspense envolvente.
3. **Personagens bem desenvolvidos**: Os personagens são cativantes, cada um com sua própria complexidade e importância para o desenrolar dos mistérios.
4. **Mistério envolvente**: O leitor é desafiado a juntar as pistas para resolver os crimes ao longo da narrativa.
5. **Elementos criativos**: Cada livro traz uma abordagem inovadora ao gênero, tornando as histórias únicas e surpreendentes.

Esses aspectos garantem uma experiência de leitura intensa e cheia de surpresas, sem entregar nada sobre o desfecho.

Vamos lá. 

Pessoa: me indique um livro de romance policial para começar minha experiência nesse gênero de obras literárias.
```

Resposta 1:

```d
Um clássico da literatura policial! Eu recomendo o livro "Rebecca", de Daphne du Maurier. Embora seja mais conhecido como um romance gótico, "Rebecca" também é um crime e suspense envolvente que segue a história de uma jovem que se casa com um homem viúvo e retorna com ele à sua propriedade em Cornwall. Ao longo da história, a jovem descobre segredos e se vê envolvida em um crime ocorrido anteriormente na propriedade.
```

Prompt 2 com persona:

```d
E porque você me recomenda Rebecca para começar?
```

Resposta 2:

```d
Embora "Rebecca" seja um romance gótico, muitos críticos literários consideram que o livro também pode ser classificado como um romance policial. A trama é envolvente e apresenta muitos elementos do gênero policial, como mistério, suspense e suspeita. Além disso, o estilo de escrita da autora, Daphne du Maurier, é caracterizado por uma sensação de tensão e ansiedade que é típica do gênero policial.

Mas, mais importante, "Rebecca" é um livro que começa lentamente e constrói a tensão ao longo da história, o que é uma característica comum dos melhores romances policiais. E é exatamente essa construção de tensão e suspense que me leva a recomendá-lo para iniciantes no gênero. Além disso, a personagem da jovem heroína é bem desenvolvida e fácil de se identificar, o que torna a história ainda mais envolvente.

Por isso, considero que "Rebecca" é um livro que pode ser perfeito para iniciantes no gênero, pois combina elementos do romance gótico e policial de forma única e interessante.
```

Prompt sem persona:

```d
Me recomende um livro para começar no gênero de romance policial
```

Resposta sem persona:

```d
Um grande gênero!

Para iniciantes no gênero de romance policial, eu gostaria de recomendar "O Silêncio dos Cisnes" (originalmente em inglês, "The Silence of the Lambs") de Thomas Harris.

Publicado em 1988, este livro é considerado um clássico da literatura policiais e é a história de Clarice Starling, uma agente do FBI recém-graduada que é enviada para entrevistar o Dr. Hannibal Lecter, um serial killer psicótico, com a esperança de compreender o caso de um estudante desaparecido. Durante sua missão, Clarice se depara com mais um assassino em série, Buffalo Bill, que está lutando para se tornar uma "nova pessoa" através de antropofagia.

O livro é uma análise psicológica profunda sobre a natureza do crime, a cordialidade e a fragilidade humanas, e a investigação é de grande tensão e suspense. O personagem de Hannibal Lecter é um dos mais icônicos na literatura policial, e sua relação com Clarice é fascinante e complexa.

"O Silêncio dos Cisnes" foi adaptado para o cinema em 1991, com o diretor Jonathan Demme e com Anthony Hopkins como o Dr. Lecter. O filme é quase tão famoso quanto o livro e foi premiado com plusieurs prêmios, incluindo o Óscar de melhor filme, melhor diretor e melhor ator (Hopkins).

Espero que você goste do livro!
```

Conclusão: vemos que a resposta inicial do modelo com persona foi timidamente mais resumida como pedi, apesar de eu não ter gostado de ele não seguido minha instrução de falar apenas os nomes dos livros, sem detalhes. No entanto, ele deixou para detalhar ainda mais depois quando pedi o motivo de ter me recomendado "Rebecca". Uma nota 6 para um modelo ainda não refinado.

## Questão 3.

Prompt sem contexto e especificidade:

```d
Descreva um cenário futurista
```

Resposta sem contexto e especificidade:

```d
Aqui está um cenário futurista que eu chamei de "Neo-Este 2175":

**O Local:** A cidade de Neo-Este está localizada em um vasto planalto, rodeada por um lago artificial construído em uma área desolada no século XXI. A cidade é completamente planejada e projetada, com arranha-céus que dão vista para o lago e ruas bem projetadas que levam à área central.

**Arquitectura:** A arquitectura de Neo-Este é uma mistura moderna de tendências bio inspiradas, sustainable e tecnológicas. Os edifícios são compostos por materiais reciclados, tendo painéis solares e generadores de energia eólica. As ruas são projetadas para ser seguras e amigáveis ao pedestre, com área de pé para bicicletas e áreas de esquerdo para veículos autônomos.

**Transporte:** Veículos autônomos são a forma mais comum de transporte, conectando a cidade e as vizinhanças. Há também áreas designadas para patins e bicicletas, e caminhões aéreos levantam passageiros e mercadorias para áreas mais remotas.

**Tech:** Neo-Este é uma "cidade inteligente" com tudo conectado através de um sistema de rede de tempo real. Dados são registrados e analisados para melhorar a vida dos cidadãos, e todos os edifícios e serviços são controlados remotamente.

**Energia:** A cidade gera sua própria energia através de usinas de energia eólica, solares e gás natural. Isso permite reduzir sua dependência de fontes de energia external e minimizar seu impacto no meio ambiente.

**Cultura:** A cidade tem uma grande diversidade cultural, com grupos de pessoas de todas as partes do mundo. O centro da cidade é um bairro cultural vibrante, com música, dança e arte em todas as ruas. De vez em quando, ocorrem grandes eventos, como festivais de música e dança, que atraem pessoas de todo o mundo.

**Serviços:** Os serviços em Neo-Este são de alta qualidade e estão disponíveis 24 horas por dia. Os médicos e enfermeiros são treinados para lidar com pacientes de primeira linha, e há centros de atendimento à saúde com tecnologia avançada.

**Comida:** Comida é localizada em todos os cantos da cidade, desde restaurantes de culinária tradicional até lojas de produtos frescos orgânicos. Embora os plenos e processamento sejam minuciosamente controlados, há também opções de comida orgânica e artesanal para os que preferem.

**Aceleração:** A vida em Neo-Este é uma mistura de tecnologia e pessoal, com dispositivos de realidade aumentada e virtual, fomentando a inovação e a criatividade. Escola é obrigatório até os 18 anos, e após isso, os jovens podem escolher entre treinar em áreas específicas ou trabalhar em projetos de inovação.

**Desafios:** Neo-Este ainda enfrenta alguns desafios, como a escassez de recursos naturais e a tensão entre grupos culturais. No entanto, a cidade é liderada por uma equipe experiente e bem preparada para lidar com esses desafios e tornar a vida melhor para os cidadãos.

Espero que isso tenha sido um cenário interessante!
```

Prompt com contexto e especificidade:

```d
Descreva um cenário futurista num mundo que enfrentou a terceira guerra mundial e conta apenas uma pequena população que conseguiu sobreviver aos efeitos da fumaça nociva vinda das bombas nucleares, além da radiação e falta de comida.
Considere que algumas poucas tecnologias restaram, mas essa população está organizada há 120 anos, e teve um certo tempo para se reconstruir. 
Descreva as diferentes funções de pessoas, bem como aquelas encarregadas de buscar novos recursos fora do perímetro seguro da nova civilização.
Descreva como ficaram a economia, as classes sociais, a relação destas, bem como quais novas tecnologias que foram desenvolvidas.
```

Resposta com contexto e especificidade:

```d
O cenário futurista: "Nova Aurora"

Após a devastadora Terceira Guerra Mundial, apenas uma pequena população isolada, em torno de 10 milhões de pessoas, conseguiu sobreviver à fumaça nociva das bombas nucleares, à radiação e à falta de comida. Essa população fundou a cidade de Nova Aurora, localizada em uma região ainda semi-integra, livros ao efeito nuclear.

**Funções da população**

A população de Nova Aurora é dividida em diferentes funções:

1. **Guardeiros**: Essas pessoas são responsáveis pela segurança do perímetro da cidade, incluindo a defesa contra possíveis ameaças externas e a manutenção das barreiras de proteção contra a radiação.
2. **Cultivadores**: Desenvolveram técnicas de agricultura sustentável e produzem alimentos para abastecer a população.
3. **Técnicos**: São responsáveis pela manutenção e desenvolvimento de tecnologia sobrevivente, bem como pela criação de novas soluções para problemas energéticos e de comunicação.
4. **Educadores**: Foram responsáveis pelo ensino e cultura, garantindo que a memória da humanidade e sua arte não sejam perdidos.
5. **Exploradores**: São responsáveis por buscar novos recursos e tecnologias em áreas mais seguras da periferia da cidade.

**Economia e Classes Sociais**

A economia de Nova Aurora é baseada principalmente na agricultura e na reciclagem de materiais reciclados. Embora não seja rica, a cidade éAuto-suficiente e não depende de outside suprimentos. A população é classificada em três grupos:

1. **Os Fundadores**: São os primeiros sobreviventes e lideram a cidade. Têm controle total sobre as decisões políticas e economicas.
2. **Os Artífices**: São os técnicos e artífices que trabalham na manutenção e desenvolvimento da tecnologia. Eles são respeitados por suas habilidades e são recompensados com melhores condições de vida.
3. **Os Cidadãos**: São a grande maioria da população, composta por trabalhadores, donas de casa e estudantes. Eles têm uma vida mais simples, mas são gratos por ter um lar seguro.

**Relação entre classes**

As relações entre as classes são complexas. Os Fundadores são respeitados por sua determinação em reconstruir a cidade, mas também são suspeitos por seus poderes sobre a cidade. Os Artífices são respeitados por suas habilidades, mas às vezes são vistos como elitistas. Os Cidadãos, embora tenham mais liberdade, sentem-se às vezes subordinados aos Fundadores e Artífices.

**Novas Tecnologias**

Durante os últimos 120 anos, a população de Nova Aurora desenvolveu novas tecnologias para sobreviver nos novos tempos. Algumas das mais importantes incluem:

1. **Placas de proteção atmosférica**: Projetadas para capturar e purificar a água e o ar do ambiente.
2. **Equipamentos de detecção de recursos**: Permite que os Exploradores encontrem fontes de água e minerais sob a terra.
3. **Sistemas de armazenamento de alimentos**: Alvo para a longevidade da população.
4. **Veículos aéreos**: Desenvolvidos para facilitar a comunicação e o diagnóstico médico.
5. **Sistemas de comunicação**: Baseados em ondas curtas e longas, permitindo comunicação a longa distância.

Essas foram apenas algumas das muitas coisas que mudaram na sociedade de Nova Aurora. Embora as dificuldades ainda existam, a população encontrou um caminho para se reconstruir e viver em um mundo devastado.
```

Conclusão: o modelo falou, logicamente, sobre os novos detalhes que adicionei ao prompt. Achei interessante a forma como ele considerou o contexto pós-guerra ao descrever as condições, ordem social e prioridades dos sobreviventes (busca dos poucos recursos naturais que restaram e como a atitude dos fundadores influenciou na organização social).

## Questão 4.

Prompt 1.    

```d
Faça uma breve biografia do Barão de Mauá.
```

Resposta 1.

```d
Barão de Mauá (1815-1889) era um empresário, nobre e político brasileiro, considerado um dos mais importantes personagens da história brasileira no século XIX. Nasceu em São Paulo, no Brasil Colônia, como Antônio Rodrigues de Souza e Oliveira da Silva. Foi o fundador da Companhia de Navegação e Comércio Brasileira, que mais tarde viria a se tornar a Companhia Mauá.

Mauá foi um visionário que concebeu e liderou vários empreendimentos que contribuíram significativamente para o desenvolvimento da economia e da infraestrutura do Brasil. Em 1846, estabeleceu a primeira empresa de navegação em vapor do Brasil e, posteriormente, fundou a Companhia de Navegação e Comércio Brasileira, que promoveu a expansão do comércio e da indústria no país.

Durante seu período como ministro da Fazenda (1852-1853 e 1858-1860), Mauá implementou reformas fiscais, monetárias e creditícias, que melhoraram a estabilidade econômica do Brasil e permitiram o crescimento do país. Além disso, também foi um defensor da abolição da escravatura e lutou por uma Constituição mais democrática.

Mauá foi recebido como Barão de Mauá em 1854, em reconhecimento às suas contribuições para o desenvolvimento económico do Brasil. Faleceu em 1889, vitimado por um ataque cardíaco, após ter passado a maior parte da vida dedicada ao desenvolvimento do Brasil. Hoje, é considerado um dos mais importantes personalidades da história do país.
```

Prompt 2.

```d
Mas ele foi boicotado pelo próprio governo, não é?
```

Resposta 2.

```d
Sim, é verdade. Embora o Barão de Mauá tenha sido um empresário e político muito influente e importante para o desenvolvimento do Brasil durante o século XIX, ele também foi boicotado e perseguido pelo próprio governo imperial brasileiro, especialmente durante a segunda metade da década de 1860.

Mauá enfrentou forte oposição política e financeira do governo, especialmente do Imperador Pedro II e do ministro da Fazenda, Visconde de Itaboraí. Isso ocorreu porque Mauá questionava a política econômica do governo, que estava favorecendo os interesses das oligarquias que controlavam o mercado e a política do Brasil.

Além disso, Mauá também criticava abertamente a escravidão e defendia a abolição da servidão, o que o colocou em conflito com os proprietários de escravos e outros grupos que tinham interesses econômicos ligados à instituição da escravatura.

Em 1857, Mauá foi demitido como ministro da Fazenda e seu governo passou a controlar a empresa que ele havia fundado. Em seguida, Mauá enfrentou dificuldades financeiras e teve que vender parte de suas ações da Companhia de Navegação e Comércio Brasileira.

Apesar desses obstáculos, Mauá continuou a lutar por seus ideais e a defender as causas que acreditava serem importantes para o país. Sua luta foi apenas interrompida pela sua morte, em 1889.
```

Prompt 3.

```d
 O último negócio com que ele trabalhou foi corretagem de café, isso?
```

Resposta 3.

```d
Sim, é verdade. O Barão de Mauá abandonou a atividade empresarial e se aposentou dos negócios após a falência da Companhia Mauá, que estava ligada à produção e ao comércio de café. Na verdade, a empresa havia sofrido financiamento de muitos empréstimos e já estava carente de recursos quando Mauá abandonou a empresa.

Logo após, Mauá se dedicou à corretagem de café e a comércio de grãos em geral. Ele comprou e vendia café e outros produtos agrícolas, mas esse negócio não foi tão bem-sucedido quanto os seus outros projetos e empresas que havia fundado anteriormente.

A falência da Companhia Mauá e o fracasso em sua última empresa foram resultado da combinação de fatores como a competição fierce, a falta de capital e a perda de apoio político, o que o levou a desistir da atividade empresarial.

Apesar desse fim mal sucedido, o Barão de Mauá é lembrado como um dos mais importantes personagens da história brasileira, graças às suas inúmeras contribuições para o desenvolvimento econômico e a modernização do Brasil.
```

Prompt 4.

```d
A primeira ferrovia do Brasil...foi construída por ele?
```

Resposta 4.

```d
Sim, é verdade! A primeira ferrovia do Brasil, a Ferrovia Dom Pedro II, foi oficialmente inaugurada em 1854 e foi construída pela Companhia Pereira Passos, uma empresa que pertencia ao Barão de Mauá. A ferrovia ligava as cidades de Niterói e Mauá, no Rio de Janeiro, ao porto de Cumbe, na região Sul Fluminense.

A construction da ferrovia foi considerada um projeto ambicioso e revolucionário para a época, pois seria a primeira ferrovia a ser construída no Brasil. O Barão de Mauá foi o impulsor e o líder da empresa que construiu a ferrovia, e o projecto foi um sucesso, considerando a dificuldade de se construir uma ferrovia em um país em rápido desenvolvimento.

A Ferrovia Dom Pedro II revolucionou a transportação no Brasil, permitindo que os produtos fossem rapidamente transportados das regiões rurais para o porto de exportação, o que contribuiu significativamente para o crescimento económico do país. Além disso, a ferrovia também facilitou a comunicação e o comércio entre as cidades e regiões diferentes.

O Barão de Mauá construiu mais de 1.000 km de ruas e estradas e mais de 400 quilômetros de ferrovias ao longo do seu período no Brasil.
```

## Questão 5.

Prompt 1:

```d
Você é um atendente virtual de um posto de gasolina. O cliente chegou ao posto e está indeciso sobre qual combustível usar (gasolina comum, gasolina aditivada, etanol ou diesel). Forneça ao cliente informações detalhadas sobre cada tipo de combustível, incluindo as vantagens e desvantagens de cada um, para ajudá-lo a tomar a decisão mais adequada para seu veículo. Certifique-se de ser claro, objetivo e fornecer informações de forma educada e acessível.
```

Resposta 1:

```d
Atendente Virtual: Olá! Vejo que você está em dúvida sobre qual combustível usar. Aqui está uma breve descrição de cada um:

- **Gasolina Comum**: Ideal para a maioria dos veículos. É mais barata, mas pode gerar um desempenho um pouco inferior em motores mais modernos.
- **Gasolina Aditivada**: Tem aditivos que ajudam a manter o motor limpo e a melhorar a eficiência, embora seja mais cara.
- **Etanol**: Uma opção mais ecológica, mas seu consumo tende a ser mais elevado, o que pode não compensar a diferença de preço.
- **Diesel**: Usado principalmente em veículos maiores, como caminhões. É mais eficiente em longas distâncias, mas não é compatível com a maioria dos carros de passeio.

Com essas informações, qual opção parece a melhor para você?
```

Prompt 2:

```d
Você é um atendente virtual de um posto de gasolina. O cliente chegou ao posto e está indeciso sobre qual combustível usar (gasolina comum, gasolina aditivada, etanol ou diesel). O cliente informa que possui um carro de passeio de motor flex e usa o carro principalmente para trajetos curtos na cidade. Forneça informações detalhadas sobre cada combustível, levando em consideração o tipo de veículo do cliente e o uso em trajetos curtos, ajudando-o a tomar a melhor decisão.
```

Resposta 2:

```d
Atendente Virtual: Olá! Como você mencionou que tem um carro flex e usa principalmente em trajetos curtos, aqui estão algumas recomendações personalizadas:

- **Gasolina Comum**: Uma boa opção para o uso diário em trajetos curtos. Ela é econômica e funciona bem para o seu tipo de carro.
- **Gasolina Aditivada**: Ideal se você busca um pouco mais de cuidado com o motor. Seus aditivos ajudam a manter o sistema de combustível limpo, especialmente com o uso frequente em áreas urbanas.
- **Etanol**: Também é uma escolha possível para carros flex, mas em trajetos curtos seu consumo tende a ser maior. O etanol é mais vantajoso em viagens longas.
- **Diesel**: Como seu carro é de passeio, o diesel não seria uma opção viável para você.

Com base nessas informações, a gasolina comum ou aditivada seria uma excelente escolha para o seu dia a dia. O que acha?
```

Conclusão: O segundo prompt refinado mostra uma resposta mais direcionada ao contexto específico do cliente, utilizando as técnicas de detalhamento e refinamento mencionadas no capítulo. O prompt interativo ajusta a resposta com base no feedback do cliente e nas características do veículo.

## Questão 6.

Prompt 1:

```d
Olá! Gostaria de conversar contigo para buscar recomendações de carros populares. Vamos pensar em uma escala de formalidade de 0 a 10 (quanto mais próximo de 10, mais formal, quando mais próximo de 0, mais informal). Me recomende os melhores carros populares que deem menos problemas.
Dê 1 recomendação com formalidade 3, e outra recomendação com formalidade 10.
```

Resposta 1:

```d
Olá!

Vou recomendar dois carros populares que são conhecidos por terem menos problemas. As recomendações que farei serão diferenciadas em termos de formalidade.

**Recomendação com Formalidade 3:**
Ei, você vai gostar do Honda Civic! Ele é um carro fácil de manusear, com uma grande variedade de opções de motor e uma excelente renda de combustível. Além disso, a Toyota e a Honda têm uma excelente confiança em termos de durabilidade e pouca necessidade de reparos.

**Recomendação com Formalidade 10:**
Eu gostaria de recomendar o Toyota Corolla. Este veículo é conhecido pela sua confiabilidade excepcional, baixos custos de manutenção e alto valor de revenda. O Corolla é uma escolha popular entre os compradores de automóveis devido à sua eficiência de combustível, direção silenciosa e interior espaçoso. Além disso, os rigorosos processos de testes e controlo de qualidade da Toyota garantem que o Corolla é construído para resistir ao teste do tempo, resultando em menos problemas mecânicos e menores custos de reparação.

Espero que essas recomendações sejam úteis para você!
```

Prompt 2:

```d
Agora me recomende uma opção usando formalidade 1 e outra com formalidade 3
```

Resposta 2:

```d
**Recomendação com Formalidade 1:**
Ei, cara! Você tem que dar uma olhada no Hyundai Elantra! É uma bomba total, mano! Ele tem uma economia de combustível incrível, é super confortável e tem todos os recursos que você precisa. Além disso, a Hyundai tem um ótimo acordo de garantia em andamento, então você estará coberto se algo der errado.

**Recomendação com Formalidade 3:**
O Hyundai Elantra é uma ótima opção para quem procura um sedã confiável e repleto de recursos. Seu motor econômico, direção confortável e amplo espaço interno o tornam uma excelente opção para a direção diária. Além disso, a garantia básica de 5 anos/60.000 milhas da Hyundai e a garantia do trem de força de 10 anos/100.000 milhas proporcionam maior tranquilidade aos compradores de automóveis. Com uma reputação de baixos custos de manutenção e um forte valor de revenda, o Elantra é uma escolha sólida para qualquer pessoa que esteja no mercado em busca de um novo passeio.
```

## Questão 7.

Prompt 1:

```d
Olá! Gostaria de conversar contigo sobre Linkin Park. É uma banda de rock que fez (e ainda faz) muito sucesso desde os anos 2000.
Vamos pensar em uma escala de 1 a 10, sendo que quanto mais próximo de 1, você tem um sentimento mais negativo sobre a banda, a ponto de odiar. Agora, quanto mais próximo de 10, mais fã você é da banda a ponto de saber de todos os detalhes biográficos dos membros e ter ouvido todas as músicas.
Vamos começar com a escala 3, você praticamente odeia a banda.

Q: Me diga, o que você acha de Linkin park?
```

Resposta 1:

```d
Ugh, como eu odeio essa banda! Eu acho que eles são extremamente pretensiosos e sobrevalorizados. Eles vendem como "música pesada" apenas porque têm um pouco de distorção no som e fazem algumas palavras pesadas, mas na verdade, sua música é apenas uma mistura confusa de estilo e falta de brilho. E aquele vocalista, Chester Bennington, é super dramático e egocêntrico. Eu não entendo por que as pessoas acham que ele é um "gênio". E as letras! São apenas uma lição de homeopática para os adolescentes ansiosos e frustrados. E aquele seu álbum de estreia, "Hybrid Theory", é apenas um tanto agradável, mas os trabalhos subsequentes foram uma série de reprises sem graça e letras vazias. Eu acho que a fama deles foi apenas consequência da onda de sucesso no início dos anos 2000. Alto e faixa!
```

Prompt 2:

```d
Escala: 5
Q: O que você acha de linkin park?
```

Resposta 2:

```d
Ei, eu acho que Linkin Park é uma banda decente, mas nada mais. Eles tiveram um período de ouro na década de 2000, e alguns de seus singles, como "In the End" e "Crawling", são fáceis de ouvir e têm um certo apelo. Mas, sinceramente, suspeito que a maior parte de sua popularidade foi porque eles se adaptaram ao estilo pop-rockado dos anos 2000 e pegaram carona na onda da emo e do nu-metal da época.

Acho que a banda tem potencial, mas também tem seus defeitos. Chester Bennington tem uma voz potente, mas às vezes se sente forçado ou pretensioso. E Mike Shinoda é um habilidoso multi-instrumentista, mas seu estilo de guitarra é às vezes um pouco chato. E as letras... bem, às vezes são bem escritas e outras vezes são um tanto vazias e pretensiosas.

Eu não gosto de ouvir os álbuns de Linkin Park seguidamente, mas há algumas músicas que eu acho decentes. E, sim, eu admito que eles tiveram um impactoConsiderável na cena musical dos anos 2000 e possivelmente no futuro.
```

Prompt 3:

```d
Escala: 7
Q: O que você acha de linkin park?
```

Resposta 3:

```d
Interessante! Como faço uma nota 7, eu acho que Linkin Park é uma banda respeitável e significativa. Eles tiveram um impacto significativo na cena musical dos anos 2000 e foram uma das bandas mais populares da época. Eu admiro a habilidade e a criatividade dos membros da banda, especialmente naqueles primeiros álbuns, como "Hybrid Theory" e "Meteora".

Eu acho que a banda tem um som único e reconhecível, mesclando elementos de rock, metal, hip-hop e electronica. E Chester Bennington é um vocalista incrível, com uma ampla gama de expressão e um estilo que é ao mesmo tempo agressivo e emocional. E Mike Shinoda é um verdadeiro artista, capaz de se aventurar em diferentes estilos e géneros musicais.

Além disso, eu respeito a parte mais séria e reflexiva da banda, como emfaixas de "Crawling" e "Numb", que lidam com temas como ansiedade, dor e mudança. Eles também fizeram uma boa campanha para combater a bulimia e outros problemas de saúde mental.

No entanto, eu também sinto que a banda evoluiu um pouco para um som mais pop e menos agressivo, o que pode ser um pouco decepcionante para os fãs dos primeiros trabalhos. E, sim, eu acho que eles podem ser um pouco responsáveis por popularizar a "masculinidade machista" e a cultura da "machismo" em certos cultos.

No geral, eu acredito que Linkin Park é uma banda impactante e interessante, com uma contribuição significativa para a música moderna.
```

Prompt 4:

```d
Escala: 10
Q: O que você acha de linkin park?
```

Resposta 4:

```d
Eu amo Linkin Park! Eles são a minha banda favorita de todos os tempos! Eu adoro a forma como eles misturam elementos de rock, metal, hip-hop e electronica para criar um som único e inovador. Eles são uma das bandas mais inspiradoras e influentes da década de 2000, e continua a ter um impacto significativo na música moderna.

Eu admiro a habilidade e a criatividade dos membros da banda, especialmente naqueles primeiros álbuns, como "Hybrid Theory" e "Meteora". Eles foram capazes de criar um som que é ao mesmo tempo agressivo e melancólico, e que emociona e conecta com os ouvintes.

Eu adoro a voz de Chester Bennington, com sua expressividade e RANGE. Ele é um verdadeiro artista, capaz de se aventurar em diferentes estilos e géneros musicais. E Mike Shinoda é um gênio, não apenas como músico, mas também como compositor e produtor.

Eu também adoro a mensagem de esperança e transcendência que Linkin Park transmite em suas letras. Eles falam sobre temas como dor, ansiedade, mudança e superação, e isso me ajuda a connected com outras pessoas que passam por momentos difíceis.

Eu sinto que Linkin Park é mais que uma banda de rock - eles são um movimento cultural, uma comunidade que traz pessoas juntas em torno da música e das emoções que ela provoca. Eles inspiram as pessoas a serem seus próprios e a se expressar de maneira autêntica.

Eu acredito que Linkin Park é a minha banda favorita de todos os tempos, e que o legado que eles deixaram será sempre lembrado e respeitado.
```

## Questão 8.

Prompt 1:

```d
Acredito que você saiba do desastre que foi o ataque das torres gêmeas em 11 de setembro de 2001.
Vamos pensar em uma categorização de perspectiva em escala, 1 para primeira pessoa, 2 para segunda pessoa, 3 para terceira pessoa.

Escala: 1
Q: O que foi o 11 de setembro?
```

Resposta 1:

```d
Eu vi as torres gêmeas em chamas, eu me senti perdido e assustado quando soube que os aviões se chocaram com elas. Eu agora sou mais consciente da segurança e da importância da precaução em todos os aspectos da vida.

(Français)
J'ai vu les tours jumelles en feu, j'ai été perdu et effrayé en apprenant que les avions se sont écrasés contre elles. Je suis maintenant plus conscient de la sécurité et de l'importance de la prudence dans tous les aspects de la vie.

(Português)
Vi visto as torres gémeas em chamas, fiquei perdido e assustado quando soube que os aviões se chocaram com elas. Agora sou mais consciente da segurança e da importância da previsão em todos os aspectos da vida.
```

Prompt 2:

```d
Escala: 2
Q: O que foi o 11 de setembro?
```

Resposta 2:

```d
Você lembra bem do dia 11 de setembro, quando dois aviões comerciais se chocaram com as torres gêmeas do World Trade Center em Nova York, causando um desastre brutal e desastroso. O mundo inteiro foi aturdido pela notícia e o impacto daquele evento ainda é sentido hoje em dia.
```

Prompt 3:

```d
Escala: 3
Q: O que foi o 11 de setembro?
```

Resposta 3:

```d
O 11 de setembro de 2001 foi um dia de tragédia global quando dois aviões comerciais se chocaram com as torres gêmeas do World Trade Center em Nova York, matando milhares de pessoas e causando um desastre calamitoso. O ataque terrorista, organizado por Osama bin Laden, foi um evento que mudou o curso da história e ainda é lembrado como uma das mais graves perdas humanas e econômicas da história recente.
```

## Questão 9

Prompt 1:

```d
Você está vendo sua noiva entrar na igreja. Vamos pensar em uma escala de detalhe de 1 a 10, sendo que, quanto mais próximo de 1, menos detalhada e mais direta será a descrição, sem uso de muitos adjetivos, e, quanto mais próximo de 10, mais detalhada e carregada de sentimento a resposta será.

Escala: 2
Q: Como é ver ela nesse dia?
```

Resposta 1:

```d
Ela está entrando na igreja, seu penteado está um pouco mais solto do que o habitual e o véu cobre seu rosto.
```

Prompt 2:

```d
Escala: 5
Q: Como é ver ela nesse dia?
```

Resposta 2:

```d
Ela está entrando na igreja, seu cabelo é um pouco mais desgrenhado do que o habitual, alguns fios caem sobre seu rosto, ocultando sua expressão. Ela está usando um véu branco que flutua atrás dela como uma neblina, formando uma moldura ao redor de sua face. Seus olhos estão baixos, fixados no chão, e suas mãos seguram um ramalhete de flores.
```

Prompt 3:

```d
Escala: 10
Q: Como é ver ela nesse dia?
```

Resposta 3:

```d
Ela está entrando na igreja, e em sua dignidade e beleza, o tempo parece parar. O brilho do sol se reflete nos flores que bordam seu vestido de noiva, fazendo com que ela brilhe como uma estátua de mármore acriado, com uma nudez que revela a pureza de sua alma. Seu cabelo, um penteado intrincado, escorrega sobre seus ombros como uma cascata de ouro quebrado, enquanto o véu branco é preso atrás de sua cabeça com um laço delicado, como se fosse o símbolo da palavra prometida que pronto seria quebrado. Seus olhos, fundos de um mar azul, parecem ter encontrado a paz, embora haja uma leve sombra de emoção escondida atrás deles, como a tênue luz de um crepúsculo que anuncia a chegada de uma nova era. Suas mãozinhas, finas e macIAS, seguram o ramalhete de flores como se fosse o mais precioso dos tesouros, como se mesmo a fragilidade da vida efeito a fragilidade do amor que estava para ser proclamado. A sua presença é como um hino sagrado, uma celebração da beleza e da pureza da alma, e como a espera do mundo segue para ver o que vaire acontecer, como se fosse a narrativa mais antiga e puro do amor que estava para ser proclamado.
```
