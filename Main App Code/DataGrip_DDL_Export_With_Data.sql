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


INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (1, 'Chris', 'Bender');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (2, 'Tarquin', 'Gotch');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (3, 'Joseph', 'Drake');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (4, 'Bill', 'Andrew');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (5, 'Marc', 'Bienstock ');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (6, 'William', 'M. Connor');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (7, 'Marty', 'Bowen');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (9, 'Mary', 'Viola');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (8, 'Emma', 'Thomas');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (11, 'Sara', 'Rodriguez');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (15, 'Larissa', 'Rhodes');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (14, 'Nathan', 'Fielder');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (13, 'Paul', 'Martin');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (12, 'Matt', 'Schrader');
INSERT INTO public.produtor (id_produtor, primeiro_nome, segundo_nome) VALUES (10, 'Lynn', 'Philpott');

INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 3, 'marta@netflox', 'Marta', '$5$rounds=535000$H1/3lCLSvJj1o5OT$w.FoF0VTz3uckKecKyG4tkYpwKaF3cXtJL0978bm7hA');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (200, 5, 'mario@netflox', 'Mário', '$5$rounds=535000$plsbpQOVcHDGpsu1$vCMFUDufGVN0bUFgER277E3ocB3VtJIKIufYss.bSu6');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 7, 'daninandes@', 'DaniMélia', '$5$rounds=535000$ipAqtkpqbIa4Yqdg$J2YtfvNhwslvkjfB/XDoNKnWJZSZv0hmxt3etMh6Gv5');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (2000, 8, 'teste@', 'Teste', '$5$rounds=535000$TwuvQojjPNdK1N6i$3MLH4qi3LYa338gdjzdzD7Za3c./BvuXbPu2CLc2WC8');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (34313, 1, '@', 'João', '$5$rounds=535000$d5on8ALzbWCbD1YY$bVPKOcmaixTs6kliordcMMJoKplWHtWDSoTq4k8CZo7');
INSERT INTO public.cliente (saldo, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (12100, 2, 'jv@netflox', 'João', '$5$rounds=535000$4jpn7TzNxlTZyF/F$Kw1vv3OyE0Ypy/TUf455aVz12xrDMNzB1/nvZ9s7kJ2');

INSERT INTO public.admin (codigo_seg, pessoa_id_pessoa, pessoa_email, pessoa_nome, pessoa_password) VALUES (20, 2, 'jv@netflox', 'João', '$5$rounds=535000$4jpn7TzNxlTZyF/F$Kw1vv3OyE0Ypy/TUf455aVz12xrDMNzB1/nvZ9s7kJ2');

INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (7, 550, 24, 1, 1607651672, 1608864872);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (8, 899, 4, 1, 1607652655, 1611889855);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (9, 1230, 26, 1, 1607675419, 1609493419);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (10, 1056, 2, 1, 1607677991, 1610705591);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (11, 599, 15, 1, 1607701951, 1608310351);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (12, 899, 9, 1, 1607701973, 1612543973);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (13, 1200, 10, 1, 1607702964, 1611335364);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (5, 899, 3, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (4, 899, 1, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (3, 899, 3, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (2, 899, 12, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (1, 899, 18, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (6, 899, 21, 1, 1607651272, 1607651672);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (14, 1023, 25, 1, 1607722443, 1608935643);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (15, 849, 20, 1, 1607724947, 1608333347);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (16, 799, 21, 1, 1607725270, 1608333670);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (17, 599, 12, 1, 1607786799, 1608999999);
INSERT INTO public.aluguer (id_aluguer, preco, artigos_id_art, cliente_pessoa_id_pessoa, data, data_validade) VALUES (18, 599, 19, 1, 1607790860, 1609004060);

INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (2, 'The quick brown fox jumps over the lazy dog 2 The quick brown fox jumps over the lazy dog 2 The quick brown fox jumps over the lazy dog 2', true, 2, 'NetFLOX 2');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (5, 'The quick brown fox jumps over the lazy dog 5 The quick brown fox jumps over the lazy dog 5 The quick brown fox jumps over the lazy dog 5', true, 2, 'Assunto?');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (4, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eu nisl vitae odio commodo viverra porta et ligula. Aliquam pharetra venenatis arcu vitae vestibulum. Proin congue nisl ac nunc consectetur rhoncus. Nulla fermentum vestibulum arcu at cursus. Phasellus feugiat lorem maximus felis tincidunt, in consequat ante varius. Sed nec elit cursus, facilisis sapien at, viverra tortor. Suspendisse felis lacus, pretium ullamcorper ultrices eu, fringilla in mi.', true, 2, 'Lorem ipsum');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (3, 'The quick brown fox jumps over the lazy dog 3 The quick brown fox jumps over the lazy dog 3 The quick brown fox jumps over the lazy dog 3', true, 2, 'Ganhou um vale!');
INSERT INTO public.mensagem (id_msg, corpo, mensagens_lida, admin_pessoa_id_pessoa, assunto) VALUES (1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eu nisl vitae odio commodo viverra porta et ligula. Aliquam pharetra venenatis arcu vitae vestibulum. Proin congue nisl ac nunc consectetur rhoncus. Nulla fermentum vestibulum arcu at cursus. Phasellus feugiat lorem maximus felis tincidunt, in consequat ante varius. Sed nec elit cursus, facilisis sapien at, viverra tortor. Suspendisse felis lacus, pretium ullamcorper ultrices eu, fringilla in mi.', true, 2, 'NetFLOX 1');
