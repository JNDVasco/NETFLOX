create table cliente_artigos
(
    cliente_pessoa_id_pessoa bigint not null
        constraint cliente_artigos_fk1
            references cliente,
    artigos_id_art           bigint not null
        constraint cliente_artigos_fk2
            references artigos,
    constraint cliente_artigos_pkey
        primary key (cliente_pessoa_id_pessoa, artigos_id_art)
);

alter table cliente_artigos
    owner to lbkoexwzuhsloo;

