# GOPNAS - Guia Ornitológico do PN Aparados da Serra

## Instalação

#### Windows

1. Clique no botão verde "Code" e depois em "Download ZIP"
2. Extraia a pasta "gopnas" do arquivo que foi baixado
3. Entre na pasta e execute o arquivo "GOPNAS.exe"

## Guia de contribuição

Esta aplicação é autonoma no que se refere à adição de novas espécies e grupos de aves.
Desde de que os arquivos tenham sido adicionados da forma correta, eles serão automaticamente dispostos na árvore dentro
 da aplicação em ordem alfabética.

#### Para adicionar grupos de aves:

Todos os grupos de aves devem ser pastas no diretório "cladi".
Os nomes de tais pastas não importam, podendo ser manipulados de forma a forçar certos grupos a aparecerem antes ou depois.
 Eles, no entanto **não** podem conter acentos agudos, sendo somente permitidos caracteres existentes na língua inglesa

As pastas dos grupos devem conter:

1. Um arquivo denominado "icon.png", que representará o ícone do grupo na barra de seleção. Esse arquivo deve seguir as 
seguintes especificações:
    1. Seu nome deve ser "icon.png"
    2. Seu nome já implica que a extensão do arquivo deve ser "**png**"
    3. Ter resolução de 250px X 250px
    4. Ter apenas a silhueta em preto do animal representante do grupo
    5. Ter um fundo opaco e colorido com o intuito de se destacar dos demais grupos de animais

2. Um arquivo denominado "silh.png", que servirá exclusivamente para propositos estéticos secundários, mais 
especificamente acompanhará o nome de todas as espécies do grupo em questão na tela de informações. Esse arquivo é 
**opcional**, podendo ser substituído pelo arquivo "silh.png" do grupo "passeriforme". Caso opte por criar o arquivo, ele deve seguir 
as seguintes especificações:
	1. Seu nome deve ser "silh.png"
	2. Seu nome já implica que a extensão do arquivo deve ser "**png**"
	3. Ter resolução de 800px X 430px
	4. Ter apenas a silhueta em **branco** do animal representante do grupo
	5. Ter um fundo transparente
	6. Para que a imagem se alinhe propriamente quando inserida no programa, o colaborador deve manipular digitalmente o
	 próprio arquivo, buscando redimensionar a silhueta dentro do mesmo de forma a nivelá-la dentro da aplicação

3. As pastas com as espécies de animais, as quais deverão seguir o modelo ditado pelo próximo bloco desse guia:

#### Para adicionar espécies de aves à grupos já existentes:
	
Todas espécies são representadas por pastas inseridas **obrigatoriamente** dentro de uma das pastas de grupos pré-existentes.
 Isso implica que **sob hipótese alguma espécies podem ser adicionadas fora de um grupo**. O nome da pasta da esécie deve corresponder ao nome científico da espécie, porém não em italico. Existe um arquivo no diretório "cladi" chamado "species_aliases.json". Nesse arquivo o nome da pasta deve ser 
 adicionado seguido por ":" e o nome que se deseja exibir no aplicativo. Ex.:

    {
	    "Nome científico": "Nome-formatado-da-espécie",
    }

O próprio colaborador define em qual grupo adicionará a espécie, seguindo dois critérios básicos:

- Acuidade biológica (ordem à qual pertence a espécie é um bom parâmetro, por exemplo)
- Bom senso, já que cabe ao colaborador determinar se é válida a criação de um novo grupo apenas em virtude da adição da
 espécie em questão, ou se esta pode ser encaixada em um grupo pré-existente por proximidade fenotípica

Por último, as pastas de espécies devem conter:

1. Um arquivo de texto denominado "info.txt" com todas as informações da espécie por escrito. Esse arquivo deve seguir 
as seguintes especificações:
	1. Seu nome deve ser "info.txt"
	2. Seu nome já implica que a extensão do arquivo deve ser "**txt**"
	3. **Não** deve conter nenhum símbolo gráfico que não seja reconhecido pelo padrão UTF-8 (apenas caracteres da língua portuguesa)
	4. **Não** deve conter "TABS", sendo a identação dos parágrafos feita **obrigatoriamente** por 4 espaços
	5. O programa tem capacidade limitada de formatar o texto. Caso seja insuficiente, a formatação pode ser feita 
	manualmente ao adicionar linhas e identar os blocos de texto
	6. As informações devem ser **extremamente** confiáveis, priorizando **sempre** a descrição física da espécie sobre outras 
	curiosidades, de forma a facilitar sua identificação em campo
	7. Posteriormente aos aspectos físicos do animal, qualquer outra informação considerada relevante pode ser adicionada,
	 desde que cumpram as demais condições citadas acima

2. Um arquivo denominado "icon.png" que representará o ícone da espécie. Esse arquivo deve seguir as seguintes especificações:
	1. Seu nome deve ser "icon.png"
	2. Seu nome já implica que a extensão do arquivo deve ser "**png**"
	4. Ter a imagem do animal **em cores** e em um fundo transparente
	
3. Uma pasta denominada "images", que deverá conter as fotos e representações gráficas da espécie em questão. 
Tais imagens devem seguir tais especificações:
	1. Seus nomes tecnicamente não importam
	2. Dito isso, o ideal é que sejam nomeadas sucessivamente como "1.jpg", "2.jpg", "3.jpg"
	3. A razão largura/altura ideal das imagens é 16/9, sendo que outros formatos podem ser usados, apesar de causarem 
	inconsistência estética
	4. A resolução deve obedecer um limite máximo de 1360px de largura e 765px de altura, sendo que, dentro desses limites,
	 resoluções maiores são preferíveis
	6. Autores podem ser adicionados aos metadados da imagem se creditação for desejada. Essa informação será mostrada ao clicar na foto em questão no aplicativo
	7. Comentários podem ser adicionados aos metadados da imagem caso sejam relevantes (por ex.: "Espécime fêmea").
	 Essa informação será mostrada ao clicar na foto em questão no aplicativo

	
