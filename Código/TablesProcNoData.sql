create table cliente
(
    saldo            bigint default 2000,
    pessoa_id_pessoa serial not null,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text,
    constraint cliente_pkey
        primary key (pessoa_id_pessoa)
);

create unique index cliente_pessoa_email_uindex
    on cliente (pessoa_email);

create table artigos
(
    id_art         serial not null,
    tipo           text,
    titulo         text,
    preco          bigint,
    tempo_para_ver bigint,
    detalhes       text,
    constraint artigos_pkey
        primary key (id_art)
);

create table admin
(
    codigo_seg       bigint,
    pessoa_id_pessoa serial not null,
    pessoa_email     text,
    pessoa_nome      text,
    pessoa_password  text,
    constraint admin_pkey
        primary key (pessoa_id_pessoa)
);

create table mensagem
(
    id_msg                 serial not null,
    corpo                  text,
    mensagens_lida         boolean,
    admin_pessoa_id_pessoa bigint,
    assunto                text,
    constraint mensagem_pkey
        primary key (id_msg),
    constraint mensagem_fk1
        foreign key (admin_pessoa_id_pessoa) references admin
);

create table estatistica
(
    id_estatistica        serial not null,
    total_clientes        bigint,
    total_artigos         bigint,
    valor_total_alugados  bigint,
    valor_total_alugueres boolean,
    total_art_por_tipo    bigint,
    tempo_total_alugado   bigint,
    tipo_mais_alugado     text,
    constraint estatistica_pkey
        primary key (id_estatistica)
);

create table historico_artigos
(
    id_art         serial not null,
    preco_anterior bigint,
    data_mudanca   date,
    artigos_id_art bigint,
    constraint historico_artigos_pkey
        primary key (id_art),
    constraint historico_artigos_fk1
        foreign key (artigos_id_art) references artigos
);

create table atores
(
    id_ator       serial not null,
    primeiro_nome text,
    segundo_nome  text,
    constraint atores_pkey
        primary key (id_ator)
);

create table realizador
(
    id_realizador serial not null,
    primeiro_nome text,
    segundo_nome  text,
    constraint realizador_pkey
        primary key (id_realizador)
);

create table produtor
(
    id_produtor   serial not null,
    primeiro_nome text,
    segundo_nome  text,
    constraint produtor_pkey
        primary key (id_produtor)
);

create table aluguer
(
    id_aluguer               serial not null,
    preco                    bigint,
    artigos_id_art           bigint not null,
    cliente_pessoa_id_pessoa bigint not null,
    data                     bigint,
    data_validade            bigint,
    constraint aluguer_pkey
        primary key (id_aluguer),
    constraint aluguer_fk1
        foreign key (artigos_id_art) references artigos,
    constraint aluguer_fk2
        foreign key (cliente_pessoa_id_pessoa) references cliente
);

create table registo_mensagem
(
    id_registo      serial not null,
    mensagens_lidas bigint,
    mensagem_id_msg bigint,
    constraint registo_mensagem_pkey
        primary key (id_registo),
    constraint registo_mensagem_fk1
        foreign key (mensagem_id_msg) references mensagem
);

create table artigos_produtor
(
    artigos_id_art       bigint not null,
    produtor_id_produtor bigint not null,
    constraint artigos_produtor_pkey
        primary key (artigos_id_art, produtor_id_produtor),
    constraint artigos_produtor_fk1
        foreign key (artigos_id_art) references artigos,
    constraint artigos_produtor_fk2
        foreign key (produtor_id_produtor) references produtor
);

create table artigos_realizador
(
    artigos_id_art           bigint not null,
    realizador_id_realizador bigint not null,
    constraint artigos_realizador_pkey
        primary key (artigos_id_art, realizador_id_realizador),
    constraint artigos_realizador_fk1
        foreign key (artigos_id_art) references artigos,
    constraint artigos_realizador_fk2
        foreign key (realizador_id_realizador) references realizador
);

create table artigos_atores
(
    artigos_id_art bigint not null,
    atores_id_ator bigint not null,
    constraint artigos_atores_pkey
        primary key (artigos_id_art, atores_id_ator),
    constraint artigos_atores_fk1
        foreign key (artigos_id_art) references artigos,
    constraint artigos_atores_fk2
        foreign key (atores_id_ator) references atores
);

create table cliente_mensagem
(
    cliente_pessoa_id_pessoa bigint not null,
    mensagem_id_msg          bigint not null,
    constraint cliente_mensagem_pkey
        primary key (cliente_pessoa_id_pessoa, mensagem_id_msg),
    constraint cliente_mensagem_fk1
        foreign key (cliente_pessoa_id_pessoa) references cliente,
    constraint cliente_mensagem_fk2
        foreign key (mensagem_id_msg) references mensagem
);

create table cliente_artigos
(
    cliente_pessoa_id_pessoa bigint not null,
    artigos_id_art           bigint not null,
    constraint cliente_artigos_pkey
        primary key (cliente_pessoa_id_pessoa, artigos_id_art),
    constraint cliente_artigos_fk1
        foreign key (cliente_pessoa_id_pessoa) references cliente,
    constraint cliente_artigos_fk2
        foreign key (artigos_id_art) references artigos
);

create table admin_artigos
(
    admin_pessoa_id_pessoa bigint not null,
    artigos_id_art         bigint not null,
    constraint admin_artigos_pkey
        primary key (admin_pessoa_id_pessoa, artigos_id_art),
    constraint admin_artigos_fk1
        foreign key (admin_pessoa_id_pessoa) references admin,
    constraint admin_artigos_fk2
        foreign key (artigos_id_art) references artigos
);

create procedure aluguer(dataaluguer integer, datafimaluguer integer, precoaluguercents integer, idartigo integer,
                         idpessoa integer)
    language plpgsql
as
$$
declare
    saldoCliente int;

BEGIN
    SELECT saldo
    INTO saldoCliente
    FROM cliente
    WHERE pessoa_id_pessoa = idPessoa;

    IF saldoCliente >= precoAluguerCents THEN
        INSERT INTO aluguer(preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade)
        VALUES (precoAluguerCents, idArtigo, idPessoa, dataAluguer, dataFimAluguer);
        UPDATE cliente SET saldo = saldoCliente - precoaluguercents WHERE pessoa_id_pessoa = idpessoa;
    ELSE
        RAISE EXCEPTION 'Saldo insuficiente';
        RETURN;
    END IF;
END;
$$;

