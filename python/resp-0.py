Teste de Python Salux - Solução Detalhada
Questões Teóricas
1- Programação Síncrona vs Assíncrona
A programação síncrona caracteriza-se pela execução sequencial de operações, onde cada tarefa bloqueia a execução até ser completamente finalizada. É especialmente adequada para tarefas simples e rápidas, como cálculos matemáticos ou leituras de arquivos locais. Em contrapartida, a programação assíncrona permite a execução não bloqueante de tarefas, sendo ideal para operações de entrada e saída como requisições de rede ou processamento de arquivos grandes.
Em Python, a programação assíncrona utiliza as palavras-chave async e await, proporcionando melhor performance em aplicações com múltiplas operações de espera. A escolha entre síncrona e assíncrona depende do contexto específico do projeto, considerando a natureza das tarefas a serem executadas e os requisitos de desempenho.
2-Metaclasses
Metaclasses são classes especiais que definem o comportamento de outras classes, permitindo modificar dinamicamente a criação e o comportamento de classes em Python. Elas são executadas quando uma nova classe é definida, oferecendo um poderoso mecanismo de metaprogramação.
As principais utilidades incluem adicionar métodos automaticamente, validar definições de classe, implementar padrões de design como singletons e criar frameworks avançados. São particularmente úteis em cenários que exigem transformação ou validação de classes durante sua definição, proporcionando um nível adicional de flexibilidade e controle no desenvolvimento de software.
3-Garbage Collector em Python
O garbage collector do Python é um mecanismo automático de gerenciamento de memória que utiliza duas estratégias principais: contagem de referências e coleta cíclica. Ele monitora os objetos criados durante a execução do programa e libera automaticamente aqueles que não possuem mais referências ativas.
Embora o gerenciamento seja majoritariamente automático, é possível realizar controle manual através do módulo gc, que oferece métodos como collect() para forçar coleta de lixo, disable() para desativar a coleta temporariamente, e outras funções para manipulação mais precisa da memória.
4-DeepCopy vs Copy
A diferença entre deepcopy e copy reside na profundidade da cópia criada. O método copy tradicional cria um novo objeto, mas mantém as referências internas dos objetos aninhados compartilhadas, sendo útil para estruturas simples.
Já o deepcopy, disponível no módulo copy, realiza uma cópia completamente independente, clonando recursivamente todos os objetos aninhados. É especialmente recomendado para estruturas de dados complexas onde é necessário garantir que nenhuma referência ao objeto original seja mantida.
5-Decorators
Decorators são funções que modificam o comportamento de outras funções sem alterar seu código original. Utilizando a sintaxe @, permitem adicionar funcionalidades como logging, medição de tempo, autenticação ou validação de maneira elegante e reutilizável.
Um decorator funciona envolvendo a função original com uma função wrapper, que pode executar código antes ou depois da função original, modificar seus argumentos ou resultados, ou até mesmo alterar completamente seu comportamento. São uma ferramenta poderosa para metaprogramação e separação de preocupações no código Python.
6-Global Interpreter Lock (GIL)
O Global Interpreter Lock é um mecanismo presente no interpretador CPython que permite apenas uma thread executar código Python simultaneamente. Essa característica simplifica o gerenciamento de memória, mas limita o verdadeiro paralelismo em aplicações multi-threaded, especialmente em tarefas intensivas de CPU.
Para contornar essas limitações, desenvolvedores podem utilizar alternativas como multiprocessing para processamento paralelo ou asyncio para tarefas de I/O, dependendo dos requisitos específicos da aplicação.
7-Tipagem Dinâmica e Forte
A tipagem em Python é simultaneamente dinâmica e forte. Dinâmica porque o tipo das variáveis é definido em tempo de execução, permitindo que uma variável mude de tipo durante a execução do programa. Forte porque não permite conversões implícitas entre tipos incompatíveis, prevenindo erros sutis de tipo.
Essa abordagem combina flexibilidade com segurança, exigindo que conversões entre tipos sejam explícitas e controladas, o que contribui para a robustez do código Python.
