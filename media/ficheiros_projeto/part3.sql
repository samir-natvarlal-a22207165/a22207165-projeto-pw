
-- Realizado por o grupo do turno da terça-feira 10h ao 12h
-- Membros do grupo:
-- Samir Natvarlal : a22207165
-- Ricardo Borges : a22203987
-- Manuel Afonso : a22207170


-- Funções de calculo ex: 1 finalizado
-- só houve um caso em que foi retirado valor de calculo que é o numeroInscricoes em TFC

DELIMITER //
CREATE FUNCTION ObterContagemInscricoesNaoFilt(idTFCProc INT) RETURNS INT
BEGIN
    DECLARE contagem INT;
    
    SELECT COUNT(*) INTO contagem
    FROM Inscricao
    WHERE idTFC = idTFCProc;

    RETURN contagem;
END //
DELIMITER ;

-- Candidaturas Ordenadas ex: 2

-- função de calculo da média
DELIMITER //
CREATE FUNCTION CalcularMediaAluno(idAlunoParam INT) RETURNS DECIMAL(5,2)
BEGIN
    DECLARE totalNotas DECIMAL(10,2);
    DECLARE totalDisciplinas INT;

    SELECT SUM(nota), COUNT(*) INTO totalNotas, totalDisciplinas
    FROM AvaliacaoDisciplinaAluno ad
    WHERE ad.idNumeroAluno = idAlunoParam;

    IF totalDisciplinas = 0 THEN
        RETURN 0;
    END IF;

    RETURN totalNotas / totalDisciplinas;
END //
DELIMITER ;

-- View que ordena os resultados : problema não faz os grupos
CREATE VIEW candidaturaOrdenada AS
SELECT
    i.idTFC AS TFC,
    i.numeroAluno AS Aluno,
    i.ordemEscolha AS OrdemEscolha,
    i.registoDeInscricao AS RegistoDeInscricao,
    CalcularMediaAluno(a.id) AS Media,
    t.orientador AS Orientador
FROM
    Inscricao i
    JOIN Aluno a ON i.numeroAluno = a.nome
    JOIN TFC t ON i.idTFC = t.idTFC
ORDER BY
    i.ordemEscolha, i.registoDeInscricao;

-- Query Lista temas atribuídos ex:3 finalizado
-- Procurar todos on temas em todos os anos
CREATE VIEW TodosTemasAtribuidos AS
SELECT
    t.idTFC AS TFC,
    COALESCE(i.numeroAluno, i.idNumeroGrupo) AS aluno,
    t.orientador AS orientadores,
    t.anoLetivo
FROM
    TFC t
    LEFT JOIN Inscricao i ON t.idTFC = i.idTFC;

-- filtragem para ver de um ano específico
-- apesar de no enunciado dizer para fazer um View somente foi decidido fazer um
-- view e procedure por ser necessário especificar o ano visto que é dito nas variáveis para limitar por um ano selecionado
DELIMITER //  
CREATE PROCEDURE GetTemasAtribuidosAnoLetivo(IN pAnoLetivo VARCHAR(255))
BEGIN
    SELECT *
    FROM TodosTemasAtribuidos tta
    WHERE tta.anoLetivo = pAnoLetivo;
END //
DELIMITER ;

-- Query Lista de orientações ex:4 finalizado

-- View que procura todas as referencias
CREATE VIEW TodosTemasComCoorientador AS
SELECT
    t.orientador AS Docente,
    t.id AS TFC,
    t.Titulo AS Titulo,
    i.numeroAluno AS Aluno
FROM
    TFC t
    LEFT JOIN Inscricao i ON t.idTFC = i.idTFC
WHERE
    t.orientador <> ''

UNION

SELECT
    t.coorientador AS Docente,
    t.id AS TFC,
    t.Titulo AS Titulo,
    i.numeroAluno AS Aluno
FROM
    TFC t
    LEFT JOIN Inscricao i ON t.idTFC = i.idTFC
WHERE
    t.coorientador <> '';
-- filtaragem para encontrar o Docente esperado
DELIMITER //   
CREATE PROCEDURE GetTemasAtribuidosPorOrientador(IN pNumeroDocente VARCHAR(15))
BEGIN
    SELECT *
    FROM TodosTemasComCoorientador tc
    WHERE tc.Docente = pNumeroDocente;
END //
DELIMITER ;

-- Alunos sem trabalho atribuido ex:5 finalizado

CREATE VIEW AlunosSemTrabalhoAtribuido AS
SELECT
    i.numeroAluno AS Aluno,
    i.idTFC AS TFC,
    i.ordemEscolha AS OrdemEscolha,
    t.estado AS estadoTFC,
    COALESCE(CONCAT(g.idNumeroAluno1, '/', g.idNumeroAluno2), 'Disponível') AS Atribuicao
FROM
    Inscricao i
    JOIN TFC t ON i.idTFC = t.idTFC
    LEFT JOIN Grupo g ON t.idGrupo = g.id
WHERE
   t.estado <> 'Atribuído' AND t.estado <> 'Publicado';

-- Query Temas disponíveis ex:6 finalizado

CREATE VIEW TemasDisponiveis AS
SELECT
    t.idTFC AS TFC,
    i.numeroAluno AS aluno,
    i.ordemEscolha AS ordemEscolha,
    i.registoDeInscricao AS registoDeInscricao,
    t.orientador AS orientador
FROM
    Inscricao i
    JOIN TFC t ON i.idTFC = t.idTFC
WHERE
    i.estado = 'Não Atribuído'
    t.estado <> 'Atribuído' AND t.estado <> 'Publicado';

-- Query Lista de trabalhos atribuídos por alunos ex:7 finalizado

CREATE VIEW TrabalhosAtribuidos AS
SELECT
    COALESCE(i.numeroAluno, i.idNumeroGrupo) AS Aluno,
    t.idTFC AS TFC,
    t.Titulo AS titulo,
    t.orientador AS Orientador
FROM
    TFC t
    JOIN Inscricao i ON t.idTFC = i.idTFC
WHERE
    t.estado = 'Atribuído' OR t.estado = 'Publicado';

-- Query Histórico de tema ex:8 não concluido por conversão de data inválido
-- tentou-se o uso do case mas provocava mais erros mesmo abranjendo todos os casos
-- este formato foi o que apresentava mais valores e com menos erros

CREATE VIEW GetRegistosTFCNaoFiltrado AS
SELECT
    h.idTFC AS TFC,
    CASE
        WHEN COUNT(*) > 1 THEN 'Alterado'
        ELSE 'Não Alterado'
    END AS Alteracao,
    MAX(h.estado) AS Estado,
    MAX(STR_TO_DATE(h.dataMudancaEstado, '%d/%m/%Y')) AS DataMudancaEstado,
    MAX(h.utilizador) AS Utilizador
FROM
    HistoricoTFC h
GROUP BY h.idTFC
ORDER BY dataMudancaEstado DESC;
-- filtragem para o TFC esperado
DELIMITER //   
CREATE PROCEDURE GetRegistosTFCFiltrado(IN numeroTFCEsc VARCHAR(50))
BEGIN
    SELECT *
    FROM GetRegistosTFCNaoFiltrado gtf
    WHERE gtf.TFC = numeroTFCEsc;
END //
DELIMITER ;

-- Query Contagem de orientações ex:9 finalizado

CREATE VIEW ContagemOrientacoesDocentes AS
SELECT
    p.numeroProfessor AS docente,
    COUNT(DISTINCT t.id) AS contagem_orientacoes
FROM 
	ProfessorDEISI p
    LEFT JOIN TFC t ON p.numeroProfessor = t.orientador OR p.numeroProfessor = t.coorientador
GROUP BY p.numeroProfessor;

-- Query Melhores candidatos ex:10 finalizado

CREATE VIEW melhoresCandidatos AS
SELECT
    t.idTFC AS TFC,
    a.id AS identificacaoAluno,
    a.nome AS Aluno,
    CalcularMediaAluno(a.id) AS Media,
    a.ECTS AS ECTS,
    i.registoDeInscricao AS registoDeInscricao
FROM
    Aluno a
    JOIN Inscricao i ON i.numeroAluno = a.nome
    JOIN TFC t ON t.idTFC = i.idTFC
ORDER BY
    Media DESC, ECTS DESC, i.registoDeInscricao
LIMIT 2;


-- Query Alteração de estados com atribuição de temas ex:11 finalizado

DELIMITER //
CREATE TRIGGER AtribuirTemaPublicado
AFTER UPDATE
ON TFC
FOR EACH ROW
BEGIN
    DECLARE vIdTFC VARCHAR(255);
    DECLARE vNumeroAluno VARCHAR(255);
    DECLARE vIdNumeroGrupo BIGINT(20);
    DECLARE vIdNumeroAluno1 VARCHAR(255);
    DECLARE vIdNumeroAluno2 VARCHAR(255);

    -- Verifica se o estado anterior era 'Publicado' e o novo estado é 'Atribuído'
    IF OLD.estado = 'Publicado' AND NEW.estado = 'Atribuído' THEN
        -- Obtém o idTFC do TFC
        SET vIdTFC = NEW.idTFC;

        -- Obtém o número do aluno atribuído ao tema
        SET vNumeroAluno = (
            SELECT i.numeroAluno FROM Inscricao i WHERE i.idTFC = vIdTFC AND estado = 'Atribuído' LIMIT 1
        );

        -- Se o número do aluno não for NULL, atualiza o estado das restantes inscrições para 'Não Atribuído'
        IF vNumeroAluno IS NOT NULL THEN
            UPDATE Inscricao i
            SET i.estado = 'Não Atribuído'
            WHERE i.idTFC = vIdTFC AND i.numeroAluno <> vNumeroAluno;
        ELSE
            -- Se o número do aluno for NULL, obtém o idNumeroGrupo e atualiza o estado para 'Atribuído'
            SET vIdNumeroGrupo = (
                SELECT i.idNumeroGrupo FROM Inscricao i WHERE i.idTFC = vIdTFC AND i.numeroAluno IS NULL LIMIT 1
            );

            UPDATE Inscricao i
            SET i.estado = 'Atribuído'
            WHERE i.idTFC = vIdTFC AND i.idNumeroGrupo = vIdNumeroGrupo;

            -- Atualiza o estado das restantes inscrições para 'Não Atribuído'
            UPDATE Inscricao i
            SET i.estado = 'Não Atribuído'
            WHERE i.idTFC = vIdTFC AND idNumeroGrupo IS NOT NULL AND i.idNumeroGrupo <> vIdNumeroGrupo;
           
           -- Busca os valores idNumeroAluno1 e idNumeroAluno2 na tabela Grupo
            SELECT g.idNumeroAluno1, g.idNumeroAluno2
            INTO vIdNumeroAluno1, vIdNumeroAluno2
            FROM Grupo g
            WHERE g.id = vIdNumeroGrupo;

            -- Atualiza o estado nas inscrições com base em idNumeroAluno1 e idNumeroAluno2
            UPDATE Inscricao i
            SET i.estado = 'Não Atribuído'
            WHERE i.idTFC = vIdTFC AND (i.numeroAluno = vIdNumeroAluno1 OR i.numeroAluno = vIdNumeroAluno2);
        END IF;
    END IF;
END //
DELIMITER ;

-- Query Verificar elegibilidade de aluno para realização de TFC ex:12 finalizado

DELIMITER //
CREATE FUNCTION VerificarCriteriosInscricao(idInscricao BIGINT(20)) RETURNS VARCHAR(255)
BEGIN
    DECLARE vAlunoID BIGINT(20);
    DECLARE vTotalECTS INT;
    DECLARE vNotaDisciplina INT;
    DECLARE c_end INTEGER DEFAULT 0;

    -- Obtém o ID do aluno e o total de ECTS
    SELECT
        i.numeroAluno,
        a.ECTS AS TotalECTS
    INTO
        vAlunoID, vTotalECTS
    FROM
        Inscricao i
        JOIN Aluno a ON i.numeroAluno = a.nome
    WHERE
        i.id = idInscricao;

    -- Verificar critério de ECTS
    IF vTotalECTS < 160 THEN
        RETURN 'ECTS insuficientes para realização do tema';
    END IF;

    -- Verificar critério de notas nas disciplinas
    DECLARE cursorSearch CURSOR FOR
        SELECT
            ad.nota
        FROM
            AvaliacaoDisciplinaAluno ad
        WHERE
            ad.idNumeroAluno = vAlunoID;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET c_end := 1;

    OPEN cursorSearch;

    read_loop: LOOP
        FETCH cursorSearch INTO vNotaDisciplina;
        IF c_end = 1 THEN
            LEAVE read_loop;
        END IF;

        IF vNotaDisciplina < 10 THEN
            CLOSE cursorSearch;
            RETURN 'Nota insuficiente em uma ou mais disciplinas';
        END IF;
    END LOOP;

    CLOSE cursorSearch;

    RETURN 'Válida'; 
    -- Se todos os critérios foram atendidos
END //
DELIMITER ;


-- Query Composição de grupo ex:13 finalizado

DELIMITER //
CREATE FUNCTION ObterNomesElementosGrupo(idGrupoSearch INT) RETURNS VARCHAR(255)
BEGIN
    DECLARE nomes VARCHAR(255);

    SELECT 
        CONCAT('elementos do Grupo: ',g.idNumeroAluno1, ' e ', g.idNumeroAluno2) INTO nomes
    FROM
        Grupo g
    WHERE
        g.id = idGrupoSearch;
    RETURN nomes;
END //
DELIMITER ;

-- Query Verificar estado de TFC ex:14 finalizado

DELIMITER //
CREATE FUNCTION VerificarAtribuicaoTFCTeste(idTFCSearch VARCHAR(200)) RETURNS VARCHAR(255)
BEGIN
    DECLARE nomes VARCHAR(255);
    DECLARE estado VARCHAR(255);

    -- Verifica se o TFC foi atribuído através do idGrupo
    SELECT 
        CONCAT(g.idNumeroAluno1, ' e ', g.idNumeroAluno2), t.estado
    INTO
        nomes, estado
    FROM
        TFC t
    	JOIN Grupo g ON t.idGrupo = g.id
    WHERE
        t.idTFC = idTFCSearch AND t.idGrupo IS NOT NULL AND (t.estado = 'Atribuído' OR t.estado = 'Publicado')
    LIMIT 1;

    -- Se não foi atribuído através do idGrupo, verifica na tabela de Inscricoes
    IF nomes IS NULL THEN
        SELECT 
            CONCAT(g.idNumeroAluno1, ' e ', g.idNumeroAluno2), t.estado
        INTO
            nomes, estado
        FROM
            TFC t
        	JOIN Inscricao i ON t.idTFC = i.idTFC
        	JOIN Grupo g ON i.idNumeroGrupo = g.id
        WHERE
            t.idTFC = idTFCSearch AND i.idNumeroGrupo IS NOT NULL AND (t.estado = 'Atribuído' OR t.estado = 'Publicado')
        LIMIT 1;

        -- Se não foi atribuído através do idGrupo na tabela de Inscricoes, verifica pelo idNumeroAluno
        IF nomes IS NULL THEN
            SELECT 
                i.numeroAluno, t.estado
            INTO
                nomes, estado
            FROM
                TFC t
            	JOIN Inscricao i ON t.idTFC = i.idTFC
            WHERE
                t.idTFC = idTFCSearch AND i.idNumeroGrupo IS NULL AND (t.estado = 'Atribuído' OR t.estado = 'Publicado')
            LIMIT 1;
        END IF;
    END IF;
    RETURN CONCAT(nomes, ', Estado: ', estado);
END //
DELIMITER ;

-- Query Alterar atribuição de tema ex:15 finalizado

DELIMITER //
CREATE PROCEDURE AlterarAtribuicaoTema(
    IN pIdTFC VARCHAR(255),
    IN pNovoNumeroAluno VARCHAR(255)
)
BEGIN
    DECLARE vDataAtual VARCHAR(10);

    -- Obtém a data atual no formato 'dia/mes/ano'
    SET vDataAtual = DATE_FORMAT(NOW(), '%d/%m/%Y');

    -- Inicia a transação
    START TRANSACTION;

    -- Atualiza a tabela Inscricao para alterar o número do aluno associado ao TFC
    UPDATE Inscricao i
    SET i.numeroAluno = pNovoNumeroAluno
    WHERE i.idTFC = pIdTFC;

    -- Atualiza o estado do novo aluno para 'Atribuído' na tabela Inscricao
    UPDATE Inscricao i
    SET i.estado = 'Atribuído'
    WHERE i.idTFC = pIdTFC AND i.numeroAluno = pNovoNumeroAluno;

    -- Registra a alteração no históricoTFC
    UPDATE HistoricoTFC h
    SET h.dataMudancaEstado = vDataAtual
    WHERE h.idTFC = pIdTFC;

    -- Confirma a transação
    COMMIT;
END //
DELIMITER ;

-- Query Tema atribuído não pode ser apagado ex:16 finalizado

DELIMITER //
CREATE TRIGGER VerificarEstadoAntesDeExcluir
BEFORE DELETE
ON TFC
FOR EACH ROW
BEGIN
    DECLARE vEstadoAtual VARCHAR(255);

    -- Obtém o estado atual do tema
    SELECT estado 
    INTO vEstadoAtual 
    FROM TFC t
    WHERE t.idTFC = OLD.idTFC;

    -- Verifica se o estado é um estado em que a exclusão não é permitida
    IF vEstadoAtual IN ('Atribuído', 'Publicado') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Não é permitido excluir um tema Atribuído ou Publicado.';
    END IF;
END //
DELIMITER ;

-- Query Anular Atribuição de tema ex 17:finalizado

DELIMITER //
CREATE PROCEDURE AnularAtribuicaoTema(IN pIdTFC VARCHAR(255))
BEGIN
    DECLARE vDataAtual VARCHAR(10);

    -- Obtém a data atual no formato 'dia/mes/ano'
    SET vDataAtual = DATE_FORMAT(NOW(), '%d/%m/%Y');

    -- Inicia a transação
    START TRANSACTION;

    -- Atualiza o estado da inscrição
    UPDATE Inscricao i
    SET i.estado = 'Anulado'
    WHERE i.idTFC = pIdTFC;

    -- Atualiza o estado do TFC
    UPDATE TFC t
    SET t.estado = 'Indisponível'
    WHERE t.idTFC = pIdTFC;

    -- Registra a anulação no históricoTFC
    UPDATE HistoricoTFC h
    SET h.dataMudancaEstado = vDataAtual , h.estado = 'Indisponível'
    WHERE h.idTFC = pIdTFC;

    -- Confirma a transação
    COMMIT;
END //
DELIMITER ;



