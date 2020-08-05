# GOPNAS - Guia de Contribuição

Esta aplicação é autonoma no que se refere à adição de novas espécies e grupos de aves.
Desde de que os arquivos tenham sido adicionados da forma correta, eles serão automaticamente dispostos na árvore dentro
 da aplicação em ordem alfabética.

## Para adicionar grupos de aves:

Todos os grupos de aves devem ser pastas no diretório principal.
Os nomes de tais pastas não importam, podendo ser manipulados de forma a forçar certos grupos a aparecerem antes ou depois.
 Eles, no entanto NÃO podem conter acentos agudos, sendo somente permitidos caracteres existentes na língua inglesa

As pastas dos grupos devem conter:

1. Um arquivo denominado "icon.png", que representará o ícone do grupo na barra de seleção. Esse arquivo deve seguir as 
seguintes especificações:
    1. Seu nome deve ser "icon.png"
    2. Seu nome já implica que a extensão do arquivo deve ser "PNG"
    3. Ter resolução de 600px X 600px
    4. Ter apenas a silhueta em preto do animal representante do grupo
    5. Ter um fundo opaco e colorido com o intúito de se destacar dos demais grupos de animais

2. Um arquivo denominado "silh.png", que servirá exclusivamente para propositos estéticos secundários, mais 
especificamente acompanhará o nome de todas as espécies do grupo em questão na tela de informações. Esse arquivo é 
OPCIONAL, podendo ser substituído pelo arquivo do grupo "passeriforme". Caso opte por criar o arquivo, ele deve seguir 
as seguintes especificações:
	1. Seu nome deve ser "silh.png"
	2. Seu nome já implica que a extensão do arquivo deve ser "PNG"
	3. Ter resolução de 500px X 720px
	4. Ter apenas a silhueta em BRANCO do animal representante do grupo
	5. Ter um fundo transparente (recurso possibilitado pelas propriedades da extensão "PNG")
	6. Para que a imagem se alinhe propriamente quando inserida no programa, o colaborador deve manipular digitalmente o
	 próprio arquivo, buscando redimensionar a silhueta dentro do mesmo de forma a nivelá-la dentro da aplicação

3. As pastas com as espécies de animais, as quais deverão seguir o modelo ditado pelo próximo bloco desse tutorial:

## Para adicionar espécies de aves à grupos já existentes:
	
Todas espécies são representadas por pastas inseridas OBRIGATORIAMENTE dentro de uma das pastas de grupos pré-existentes.
 Isso implica que SOB HIPÓTESE ALGUMA ESPÉCIES PODEM SER ADICIONADAS FORA DE UM GRUPO. O nome da pasta da esécie deve corresponder ao nome científico da espécie, porém não em italico. Existe um arquivo no diretório "cladi" chamado "species_aliases.json". Nesse arquivo o nome da pasta deve ser 
 adicionado seguido por ":" e o nome que se deseja exibir no aplicativo. Ex.:

    {
	    "Nome científico": "Nome-formatado-da-espécie",
    }

O próprio colaborador define em qual grupo adicionará a espécie, seguindo dois critérios básicos:

- Acuidade biológica
- Bom senso, já que cabe ao colaborador determinar se é válida a criação de um novo grupo apenas em virtude da adição da
 espécie em questão, ou se esta pode ser encaixada em um grupo pré-existente por proximidade fenotípica

Por último, as pastas de espécies devem conter:

1. Um arquivo de texto denominado "info.txt" com todas as informações da espécie por escrito. Esse arquivo deve seguir 
as seguintes especificações:
	1. Seu nome deve ser "info.txt"
	2. Seu nome já implica que a extensão do arquivo deve ser "TXT"
	3. NÃO deve conter nenhum símbolo gráfico que não seja reconhecido pelo padrão UTF-8
	4. NÃO deve conter "TABS", sendo a identação dos parágrafos feita OBRIGATORIAMENTE por 4 espaços
	5. O programa tem capacidade limitada de formatar o texto. Caso seja insuficiente, a formatação pode ser feita 
	manualmente ao adicionar linhas e identar os blocos de texto
	6. As informações devem ser EXTREMAMENTE confiáveis, priorizando SEMPRE a descrição física da espécie sobre outras 
	curiosidades, de forma a facilitar sua identificação em campo
	7. Posteriormente aos aspectos físicos do animal, qualquer outra informação considerada relevante pode ser adicionada,
	 desde que cumpram as demais condições citadas acima

2. Um arquivo denominado "icon.png" que representará o ícone da espécie. Esse arquivo deve seguir as seguintes especificações:
	1. Seu nome deve ser "icon.png"
	2. Seu nome já implica que a extensão do arquivo deve ser "PNG"
	3. Ter resolução de 600px X 600px
	4. Ter a silhueta do animal EM CORES e em um fundo de outra cor opaca que o destaque das demais espécies
	5. Permitir a fácil identificação da espécie
	
3. Uma pasta denominada "images", que deverá conter as fotos e representações gráficas da espécie em questão. 
Tais imagens devem seguir tais especificações:
	1. Seus nomes tecnicamente não importam
	2. Dito isso, o ideal é que sejam nomeadas sucessivamente como "image.png", "image_1.png", "image_2.png"
	3. A razão largura/altura ideal das imagens é 16/9, sendo que outros formatos podem ser usados, apesar de causarem 
	inconsistência estética
	4. A resolução deve obedecer um limite máximo de 1360px de largura e 765px de altura, sendo que, dentro desses limites,
	 resoluções maiores são preferíveis
	5. As imagens devem preferencialmente conter uma etiqueta adicionada digitalmente com o intúito de informar a 
	localização em que foi tirada a foto em questão
	6. QUALQUER OUTRA INFORMAÇÃO DE TEXTO ESTÁ PROIBIDA, sendo o arquivo "info.txt" o lugar onde informações por texto 
	devem estar contidas

	
