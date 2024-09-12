import markdown2

pseudocode = '''
Algoritmo "Insercao_RedBlack"

// Definicao da insercao na Arvore Red-Black
Procedimento InserirNo(arvore, valor)
    novoNo <- criarNovoNo(valor)
    
    // Se a arvore estiver vazia
    Se (arvore.raiz == sentinel) entao
        arvore.raiz <- novoNo
        novoNo.cor <- PRETA
    Senao
        pai <- sentinel
        atual <- arvore.raiz
        
        // Encontrar local para inserir
        Enquanto (atual != sentinel) faca
        ...     
    FimEnquanto
    arvore.raiz.cor <- PRETA
FimProcedimento

// Procedimento de rotacao a esquerda
Procedimento RotacionarEsquerda(arvore, no)
    temporario <- no.direita
    no.direita <- temporario.esquerda
    
    Se (temporario.esquerda != sentinel) entao
        temporario.esquerda.pai <- no
    FimSe
    
    temporario.pai <- no.pai
    
    Se (no.pai == sentinel) entao
        arvore.raiz <- temporario
    SenaoSe (no == no.pai.esquerda) entao
        no.pai.esquerda <- temporario
    Senao
        no.pai.direita <- temporario
    FimSe
    
    temporario.esquerda <- no
    no.pai <- temporario
FimProcedimento

// Procedimento de rotacao a direita
Procedimento RotacionarDireita(arvore, no)
    temporario <- no.esquerda
    no.esquerda <- temporario.direita
    
    Se (temporario.direita != sentinel) entao
        temporario.direita.pai <- no
    FimSe
    
    temporario.pai <- no.pai
    
    Se (no.pai == sentinel) entao
        arvore.raiz <- temporario
    SenaoSe (no == no.pai.direita) entao
        no.pai.direita <- temporario
    Senao
        no.pai.esquerda <- temporario
    FimSe
    
    temporario.direita <- no
    no.pai <- temporario
FimProcedimento

'''

html = markdown2.markdown(pseudocode)
print(html)
